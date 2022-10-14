"""EUMETSAT Data Access Client"""
from __future__ import annotations

import argparse
import itertools
import os
import pathlib
import re
import shlex
import signal
import stat
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

import requests
import yaml
from requests.exceptions import HTTPError

import eumdac
from eumdac import DataStore, DataTailor
from eumdac.collection import SearchResults
from eumdac.config import get_config_dir, get_credentials_path
from eumdac.download_app import DownloadApp
from eumdac.errors import EumdacError
from eumdac.fake import FakeDataStore, FakeDataTailor  # type: ignore
from eumdac.logging import gen_table_printer, init_logger, logger
from eumdac.order import Order, all_order_filenames, resolve_order
from eumdac.product import Product
from eumdac.tailor_app import TailorApp
from eumdac.tailor_models import Chain
from eumdac.token import AccessToken, AnonymousAccessToken

from .__version__ import __documentation__, __title__, __version__  # noqa

if TYPE_CHECKING:  # pragma: no cover
    from typing import Any, Callable, Collection, Dict, Iterator, Optional, Tuple, Union

    if sys.version_info < (3, 9):
        from typing import Iterable, Sequence
    else:
        from collections.abc import Iterable, Sequence


class SetCredentials(argparse.Action):
    """eumdac --set-credntials entry point"""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[str, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        token = eumdac.AccessToken(values)  # type: ignore[arg-type]
        config_dir = get_config_dir()
        config_dir.mkdir(exist_ok=True)
        credentials_path = get_credentials_path()
        credentials_path.touch(mode=(stat.S_IRUSR | stat.S_IWUSR))

        try:
            logger.info(f"Credentials are correct. Token was generated: {token}")
            try:
                with credentials_path.open(mode="w") as file:
                    file.write(",".join(values))  # type: ignore[arg-type]
                namespace.credentials = values
                logger.info(f"Credentials are written to file {credentials_path}")
            except OSError:
                logger.error(
                    "Credentials could not be written to {credentials_path}. Please review your configuration."
                )
        except HTTPError as e:
            if e.response.status_code == 401:
                token_url = token.urls.get("token", "token")
                logger.error(
                    "The provided credentials are not valid. "
                    f"Get your personal credentials at {token_url}",
                )
            else:
                report_request_error(e.response)

        parser.exit()


def describe(args: argparse.Namespace) -> None:
    """eumdac describe entrypoint"""
    datastore = get_datastore(args, anonymous_allowed=True)
    if args.collection is None and args.product is None:
        for collection in datastore.collections:
            logger.info(f"{collection} - {collection.title}")
    elif args.collection is not None and args.product is None:
        collection = datastore.get_collection(args.collection)
        date = collection.metadata["properties"].get("date", "/")
        match = re.match(r"([^/]*)/([^/]*)", date)
        start_date, end_date = match.groups()  # type: ignore[union-attr]
        start_date = start_date or "-"
        end_date = end_date or "now"
        logger.info(f"{collection} - {collection.title}")
        logger.info(f"Date: {start_date} - {end_date}")
        logger.info(collection.abstract)
        logger.info(f'Licence: {"; ".join(collection.metadata["properties"].get("rights", "-"))}')
    elif args.collection is None and args.product is not None:
        raise ValueError("Product ID requires a Collection ID!")
    else:
        product = datastore.get_product(args.collection, args.product)
        attributes = {
            "Mission": product.satellite,
            "Instrument": product.instrument,
            "Sensing Start": "none"
            if (product.sensing_start is False)
            else f"{product.sensing_start.isoformat(timespec='milliseconds')}Z",
            "Sensing End": "none"
            if (product.sensing_end is False)
            else f"{product.sensing_end.isoformat(timespec='milliseconds')}Z",
            "Size": f"{product.size} KB",
        }
        lines = [f"{product.collection} - {product}"] + [
            f"{key}: {value}" for key, value in attributes.items()
        ]
        logger.info("\n".join(lines))


class ProductIterables:
    """Helper class to manage the length of one or more SearchResults which are iterators"""

    def __init__(
        self,
        query_results: list[SearchResults],
        limit: Optional[int],
        search_query: Dict[str, str],
    ) -> None:
        self.query_results = query_results
        self.search_query = search_query
        self.limit = limit

    def __len__(self) -> int:
        result_lengths = sum(len(pq) for pq in self.query_results)
        if self.limit:
            return min(self.limit, result_lengths)
        return result_lengths

    def __iter__(self) -> Iterator[Product]:
        chained_it = itertools.chain(*self.query_results)
        if self.limit:
            return itertools.islice(chained_it, self.limit)
        return chained_it

    def __contains__(self, item: object) -> bool:
        raise NotImplementedError()


def _search(args: argparse.Namespace) -> Collection[Product]:
    """given search query arguments will return the list of matching products"""
    datastore = get_datastore(args, anonymous_allowed=True)
    query_results = []
    start = args.dtstart
    end = args.dtend
    if args.dtend:
        if not (end.hour or end.minute or end.second):
            end = end + timedelta(hours=23, minutes=59, seconds=59)
            logger.warning("As no time was given in -e/--end, it was set to 23:59:59.")
    if args.time_range:
        start, end = args.time_range

    sort_query = None
    if args.sort:
        if args.sort == "ingestion":
            sort_prefix = "publicationDate,,"
        elif args.sort == "sensing":
            sort_prefix = "start,time,"
        else:
            raise EumdacError("Unexpected sorting argument: {args.sort}")
        direction = 1
        if args.desc:
            direction = 0
        if args.asc:
            direction = 1
        sort_query = f"{sort_prefix}{direction}"

    _query = {
        "dtstart": start,
        "dtend": end,
        "bbox": args.bbox,
        "geo": args.geo,
        "sat": args.sat,
        "sort": sort_query,
        "cycle": args.cycle,
        "orbit": args.orbit,
        "relorbit": args.relorbit,
        "title": args.filename,
        "timeliness": args.timeliness,
    }

    query = {key: value for key, value in _query.items() if value is not None}
    bbox = query.pop("bbox", None)
    if bbox is not None:
        query["bbox"] = ",".join(map(str, bbox))

    for collection_id in args.collection:
        collection = datastore.get_collection(collection_id)
        query_results.append(collection.search(**query))

    return ProductIterables(query_results, args.limit, query)


def search(args: argparse.Namespace) -> None:
    """eumdac search entrypoint"""
    if args.time_range and (args.dtstart or args.dtend):
        raise ValueError("You can't combine --time-range and --start/--end.")

    products_query = _search(args)
    products_count = len(products_query)

    limit = args.limit or 10
    products = itertools.islice(products_query, limit)
    if products_count < 1:
        logger.error(f"No products were found for the given search parameters")
        return

    if products_count > limit:
        # show a warning through stderr only when more than 10
        # products would be shown and limit keyword is not used.
        logger.warning(f"By default, only 10 of {products_count} products are displayed.")
        logger.warning("Please use --limit to increase the number of products if necessary.")

    if products_count > 10000:
        logger.error(
            "Notice: EUMETSATs DataStore APIs allow a maximum of 10.000 items in a single request. If more than 10.000 items are needed, please split your requests."
        )

    for product in products:
        CRLF = "\r\n"
        logger.info(str(product).replace(CRLF, "-"))


class AngrySigIntHandler:
    """class that will block a SigInt `max_block` times before exiting the program"""

    def __init__(self, max_block: int = 3) -> None:
        self.max_block = max_block
        self.ints_received = 0

    def __call__(self, *args: Any) -> None:
        self.ints_received += 1
        if self.ints_received > self.max_block:
            logger.warning("Forced shut down.")
            sys.exit(1)
        logger.warning(
            "Currently shutting down. "
            f"Interrupt {self.max_block - self.ints_received + 1} "
            "more times to forcefully shutdown."
        )


def safe_run(app: Any, force: bool = False) -> None:
    """wrapper around app.run() for exception handling and logging"""

    num_products = len(list(app.order.iter_product_info()))
    plural = "" if num_products == 1 else "s"
    logger.info(f"Processing {num_products} product{plural}.")
    (chain,) = app.order.get_dict_entries("chain")

    if chain:
        plural = "It" if num_products == 1 else "They"
        logger.info(f"{plural} will be customized with the following parameters:")
        for line in yaml.dump(chain).splitlines():
            logger.info(f"   {line}")
    if num_products >= 10 and not force:
        user_in = input("Do you want to continue (Y/n)?")
        if user_in.lower() == "n":
            return
    logger.info(f"Using order: {app.order}")
    try:
        return app.run()
    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, AngrySigIntHandler())
        logger.info("Received request to shut down.")
        logger.info("Finishing Threads..")
        app.shutdown()
        logger.info("Resume this order with the following command:")
        logger.info(f"$ eumdac order resume {app.order}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected exception: {str(e)}")
        raise


def download(args: argparse.Namespace) -> None:
    """eumdac download entrypoint"""
    order = Order()
    datastore = get_datastore(args)

    if not args.collection or len(args.collection) > 1:
        raise ValueError("Please provide a (single) collection")

    if args.time_range and (args.dtstart or args.dtend):
        raise ValueError("You can't combine --time-range and --start/--end.")

    if args.time_range:
        args.dtstart = args.time_range[0]
        args.dtend = args.time_range[1]

    _collection = args.collection[0]
    if args.product and (args.dtstart or args.dtend):
        raise ValueError("Please provide either products or a time-range!")

    if args.product:
        products: Collection[Product] = [
            datastore.get_product(_collection, pid) for pid in args.product
        ]
    else:
        products = _search(args)

    try:
        query = products.search_query  # type: ignore
    except AttributeError:
        query = None

    if args.tailor and args.chain:
        raise ValueError("Please provide either a tailor file or chain yaml string!")
    elif args.tailor or args.chain:
        if args.tailor:
            chain_config = args.tailor
        elif args.chain:
            chain_config = args.chain
        if chain_config.endswith(".yml") or chain_config.endswith(".yaml"):
            with open(chain_config, "r") as file:
                try:
                    chain = yaml.safe_load(file)
                except:
                    logger.error("YAML file is corrupted. Please, check the YAML syntax.")
                    exit()
        else:
            chain_config = chain_config.strip()
            if not chain_config.startswith("{"):
                chain_config = "{" + chain_config + "}"
            try:
                chain = yaml.safe_load(chain_config)
            except:
                logger.error("YAML string is corrupted. Please, check the YAML syntax.")
                exit()
        chain = Chain(**chain)
        order.initialize(chain, products, Path(args.output_dir), args.entry, query)
        app: Any = TailorApp(order, datastore, get_datatailor(args))
    else:
        order.initialize(None, products, Path(args.output_dir), args.entry, query)
        app = DownloadApp(order, datastore)
    safe_run(app, args.yes)


def order(args: argparse.Namespace) -> None:
    """eumdac order entrypoint"""
    if args.order_command == "list":
        filenames = list(all_order_filenames())
        logger.info(f"Found {len(filenames)} order(s):")
        table_printer = gen_table_printer(
            logger.info,
            [
                ("Order ID", 15),
                ("Created on", 10),
                ("Products", 8),
                ("Tailor", 6),
                ("Status", 15),
                ("Collection", 28),
            ],
            column_sep="  ",
        )
        for filename in filenames:
            try:
                order = Order(filename)
                with order.dict_from_file() as order_d:
                    table_printer(
                        [
                            filename.stem,  # order_id
                            filename.stem.split("#")[0],  # created
                            str(len(order_d["products_to_process"])),  # products
                            "Yes" if order_d["type"] == "tailor" else "No",  # tailor
                            order.status(),  # status
                            ", ".join(order.collections()),  # collection
                        ]
                    )
            except EumdacError:
                logger.error(f"{filename} is corrupted.")
        return

    order_name = args.order_id
    order = resolve_order(order_name)

    if args.order_command == "status":
        logger.info(order.pretty_string(print_products=args.verbose))
        if not args.verbose:
            logger.info("")
            logger.info("Use the -v flag to see more details")
        return

    if args.order_command == "restart":
        order.reset_states()

    if args.order_command == "delete":
        if order._order_file.is_file():
            order_id = str(order)
            user_in = input(f"Are you sure to delete order {order_name} (Y/n)?")
            if user_in.lower() == "y":
                try:
                    order.delete()
                    logger.info(f"Order {order_name} successfully deleted.")
                except:
                    logger.warning(f"Order {order_name} can't be deleted.")
                exit()
            else:
                logger.info(f"Order {order_name} wasn't deleted.")
                exit()
        else:
            logger.info(f"Order {order_name} doesn't exist.")
            exit()

    if not order._order_file.is_file():
        logger.info(f"Order {order_name} doesn't exist.")
        exit()

    (typ,) = order.get_dict_entries("type")
    if typ == "download":
        app: Any = DownloadApp(order, get_datastore(args))

    elif typ == "tailor":
        if order.all_done():
            logger.info("Order already completed")
            return
        app = TailorApp(order, get_datastore(args), get_datatailor(args))

    else:
        raise Exception(f"Unknown Order Type: {typ}")
    safe_run(app, True)


def get_datastore(args: argparse.Namespace, anonymous_allowed: bool = False) -> Any:
    """get an instance of DataStore"""
    if args.test:
        return FakeDataStore()
    try:
        creds = load_credentials()
    except CredentialsFileNotFoundError as exc:
        if anonymous_allowed:
            creds = None
        else:
            raise EumdacError("No credentials found! Please set credentials!") from exc

    if creds is None:
        token: Any = AnonymousAccessToken()
    else:
        token = AccessToken(creds)
    return DataStore(token)


def get_datatailor(args: argparse.Namespace) -> Any:
    """get an instance of DataTailor"""
    if args.test:
        return FakeDataTailor()
    try:
        creds = load_credentials()
    except CredentialsFileNotFoundError as exc:
        raise EumdacError("No credentials found! Please set credentials!") from exc
    token = AccessToken(creds)
    return DataTailor(token)


def load_credentials() -> Iterable[str]:
    """load the credentials and do error handling"""
    credentials_path = get_credentials_path()
    try:
        content = credentials_path.read_text()
    except FileNotFoundError as exc:
        raise CredentialsFileNotFoundError(str(credentials_path)) from exc
    match = re.match(r"(\w+),(\w+)$", content)
    if match is None:
        raise EumdacError(f'Corrupted file "{credentials_path}"! Please reset credentials!')
    return match.groups()


def subscribe_list_subscriptions(args: argparse.Namespace) -> None:
    """eumdac subscribe list entrypoint"""
    datastore = get_datastore(args)
    subscriptions = datastore.subscriptions
    if not subscriptions:
        logger.error("No subscriptions registered")
    else:
        table_printer = gen_table_printer(
            logger.info,
            [
                ("Subscription ID", 40),
                ("Status", 8),
                ("Collection", 25),
                ("Area of interest", 20),
                ("Listener URL", 20),
            ],
        )
        for subscription in datastore.subscriptions:
            line = [
                str(subscription),
                str(subscription.status),
                str(subscription.collection),
                str(subscription.area_of_interest),
                str(subscription.url),
            ]
            table_printer(line)


def subscribe_create_subscriptions(args: argparse.Namespace) -> None:
    """eumdac subscribe create entrypoint"""
    datastore = get_datastore(args)
    collection = datastore.get_collection(args.collection)
    try:
        table_printer = gen_table_printer(
            logger.info,
            [
                ("Subscription ID", 40),
                ("Status", 8),
                ("Collection", 25),
                ("Area of interest", 20),
                ("Listener URL", 20),
            ],
        )

        subscription = datastore.new_subscription(
            collection, args.url, area_of_interest=args.area_of_interest
        )
        table_printer(
            [
                str(subscription),
                str(subscription.status),
                str(subscription.collection),
                str(subscription.area_of_interest),
                str(subscription.url),
            ]
        )
    except requests.exceptions.HTTPError as exception:
        messages = {
            400: "Please provide a correct collection and URL. See below:",
            500: "There was an issue on server side. See below:",
            0: "An error occurred. See below:",
            -1: "An unexpected error has occurred.",
        }
        report_request_error(exception.response, None, messages=messages)


def subscribe_delete_subscriptions(args: argparse.Namespace) -> None:
    """eumdac subscribe delete entrypoint"""
    datastore = get_datastore(args)
    for subscription_id in args.sub_ids:
        try:
            subscription = datastore.get_subscription(subscription_id)
            subscription.delete()
            logger.info(f"Deleted subscription {subscription_id}")
        except requests.exceptions.HTTPError as exception:
            messages = {
                400: "Subscription ID does not seem to be a valid. See below:",
                500: "There was an issue on server side. See below:",
                0: "An error occurred. See below:",
                -1: "An unexpected error has occurred.",
            }
            report_request_error(exception.response, None, messages=messages)


def tailor_post_job(args: argparse.Namespace) -> None:
    """eumdac tailor post entrypoint"""
    from eumdac.tailor_models import Chain

    datastore = get_datastore(args)
    datatailor = get_datatailor(args)
    collection_id = args.collection
    product_ids = args.product
    chain_config = args.chain

    if not args.collection or not args.product or not args.chain:
        raise ValueError("Please provide collection ID, product ID and a chain file!")
    if chain_config.endswith(".yml") or chain_config.endswith(".yaml"):
        with open(chain_config, "r") as file:
            try:
                chain = yaml.safe_load(file)
            except:
                logger.error("YAML file is corrupted. Please, check the YAML syntax.")
                exit()
    else:
        chain_config = chain_config.strip()
        if not chain_config.startswith("{"):
            chain_config = "{" + chain_config + "}"
        try:
            chain = yaml.safe_load(chain_config)
        except:
            logger.error("YAML string is corrupted. Please, check the YAML syntax.")
            exit()
    chain = Chain(**chain)
    products = [datastore.get_product(collection_id, product_id) for product_id in product_ids]
    try:
        customisation = datatailor.new_customisations(products, chain=chain)
        jobidsToStr = "\n".join([str(jobid) for jobid in customisation])
        logger.info("Customisation(s) has been started.")
        logger.info(jobidsToStr)
    except requests.exceptions.HTTPError as exception:
        messages = {
            400: "Collection ID and/or Product ID does not seem to be a valid. See below:",
            500: "There was an issue on server side. See below:",
            0: "An error occurred. See below:",
            -1: "An unexpected error has occurred.",
        }
        report_request_error(exception.response, None, messages=messages)


def tailor_list_customisations(args: argparse.Namespace) -> None:
    """eumdac tailor list entrypoint"""
    datatailor = get_datatailor(args)
    try:
        customisations = datatailor.customisations
        if not customisations:
            logger.error("No customisations available")
        else:
            table_printer = gen_table_printer(
                logger.info,
                [("Job ID", 10), ("Status", 8), ("Product", 10), ("Creation Time", 20)],
            )
            for customisation in datatailor.customisations:
                line = [
                    str(customisation),
                    customisation.status,
                    customisation.product_type,
                    str(customisation.creation_time),
                ]
                table_printer(line)
    except requests.exceptions.HTTPError as exception:
        report_request_error(exception.response)


def tailor_show_status(args: argparse.Namespace) -> None:
    """eumdac tailor status entrypoint"""
    datatailor = get_datatailor(args)
    if args.verbose:
        table_printer = gen_table_printer(
            logger.info,
            [("Job ID", 10), ("Status", 8), ("Product", 10), ("Creation Time", 20)],
        )
        for customisation_id in args.job_ids:
            try:
                customisation = datatailor.get_customisation(customisation_id)
                line = [
                    str(customisation),
                    customisation.status,
                    customisation.product_type,
                    str(customisation.creation_time),
                ]
                table_printer(line)
            except requests.exceptions.HTTPError as exception:
                report_request_error(exception.response, customisation_id)
    else:
        for customisation_id in args.job_ids:
            try:
                customisation = datatailor.get_customisation(customisation_id)
                logger.info(customisation.status)
            except requests.exceptions.HTTPError as exception:
                report_request_error(exception.response, customisation_id)


def tailor_get_log(args: argparse.Namespace) -> None:
    """eumdac tailor log entrypoint"""
    datatailor = get_datatailor(args)
    try:
        customisation = datatailor.get_customisation(args.job_id)
        logger.info(customisation.logfile)
    except requests.exceptions.HTTPError as exception:
        report_request_error(exception.response, args.job_id)


def tailor_quota(args: argparse.Namespace) -> None:
    """eumdac tailor quota entrypoint"""
    datatailor = get_datatailor(args)
    user_name = datatailor.user_info["username"]
    quota_info = datatailor.quota["data"][user_name]
    if args.verbose:
        logger.info(f"Usage: {round(quota_info['space_usage'] / 1024, 1)} Gb")
        logger.info(f"Percentage: {round(quota_info['space_usage_percentage'], 1)}%")
        logger.info(f"Available: {round(quota_info['user_quota'] / 1024, 1)} Gb")
        logger.info(f"Workspace usage: {round(quota_info['workspace_dir_size'] / 1024, 1)} Gb")
        logger.info(f"Logs space usage: {round(quota_info['log_dir_size'], 3)} Mb")
        logger.info(f"Output usage: {round(quota_info['output_dir_size'], 1)} Mb")
        logger.info(f"Jobs: {quota_info['nr_customisations']}")
    else:
        logger.info(f"Usage: {round(quota_info['space_usage'] / 1024, 1)} Gb")
        logger.info(f"Percentage: {round(quota_info['space_usage_percentage'], 1)}%")


def tailor_delete_jobs(args: argparse.Namespace) -> None:
    """eumdac tailor delete entrypoint"""
    datatailor = get_datatailor(args)
    for customisation_id in args.job_ids:
        customisation = datatailor.get_customisation(customisation_id)
        try:
            customisation.delete()
            logger.info(f"Customisation {customisation_id} has been deleted.")
        except requests.exceptions.HTTPError as exception:
            if exception.response.status_code >= 400:
                report_request_error(exception.response, customisation_id)


def tailor_cancel_jobs(args: argparse.Namespace) -> None:
    """eumdac tailor cancel entrypoint"""
    datatailor = get_datatailor(args)

    for customisation_id in args.job_ids:
        customisation = datatailor.get_customisation(customisation_id)
        try:
            customisation.kill()
            logger.info(f"Customisation {customisation_id} has been cancelled.")
        except requests.exceptions.HTTPError as exception:
            messages = {
                400: f"{customisation_id} is already cancelled or job id is invalid. See below:",
                500: "There was an issue on server side. See below:",
                0: "An error occurred. See below:",
                -1: "An unexpected error has occurred.",
            }
            report_request_error(exception.response, None, messages=messages)


def tailor_clear_jobs(args: argparse.Namespace) -> None:
    """eumdac tailor clear entrypoint"""
    datatailor = get_datatailor(args)

    jobs_to_clean = args.job_ids

    if args.all and len(args.job_ids) > 0:
        logger.info(
            "All flag provided. Ignoring the provided customization IDs and clearing all jobs"
        )

    if args.all:
        # Fetch all job ids
        jobs_to_clean = datatailor.customisations

    for customisation in jobs_to_clean:
        # If we are provided a job id, get the customisation
        if isinstance(customisation, str):
            customisation_id = customisation
            customisation = datatailor.get_customisation(customisation)
        else:
            customisation_id = customisation._id

        try:
            if (
                customisation.status == "QUEUED"
                or customisation.status == "RUNNING"
                or customisation.status == "INACTIVE"
            ):
                customisation.kill()
                logger.info(f"Customisation {customisation_id} has been cancelled.")
        except requests.exceptions.HTTPError as exception:
            messages = {
                400: f"{customisation_id} is already cancelled or job id is invalid. See below:",
                500: "There was an issue on server side. See below:",
                0: "An error occurred. See below:",
                -1: "An unexpected error has occurred.",
            }
            report_request_error(exception.response, None, messages=messages)

        try:
            customisation.delete()
            logger.info(f"Customisation {customisation_id} has been deleted.")
        except requests.exceptions.HTTPError as exception:
            report_request_error(exception.response, customisation_id)


def tailor_download(args: argparse.Namespace) -> None:
    """eumdac tailor download entrypoint"""
    creds = load_credentials()
    token = AccessToken(creds)
    # for customisation_id in customisation_ids:  # type: ignore[union-attr]
    customisation_id = args.job_id
    url = token.urls.get("tailor", "customisations") + f"/{customisation_id}"
    response = requests.get(
        url,
        headers={
            "Authorization": "Bearer {}".format(token),
            "referer": __documentation__,
            "User-Agent": str(__title__ + "/" + __version__),
        },
    )
    if response.status_code == 200:
        results = response.json()[customisation_id]["output_products"]

        # Create output path if it does not exist
        logger.info(f"Output directory: {os.path.abspath(args.output_dir)}")
        if not os.path.exists(args.output_dir):
            logger.info(f"Output directory {args.output_dir} does not exist. It will be created.")
            os.makedirs(args.output_dir)

        # Download all the output files into the output path
        logger.info(f"Downloading {len(results)} output products")
        for result in results:
            logger.info("Downloading " + os.path.basename(result))
            url = token.urls.get("tailor", "download") + f"?path={result}"
            response = requests.get(
                url,
                headers={
                    "Authorization": "Bearer {}".format(token),
                    "referer": __documentation__,
                    "User-Agent": str(__title__ + "/" + __version__),
                },
            )
            output = args.output_dir
            if response.status_code == 200:
                product_path = os.path.join(output, os.path.basename(result))
                open(product_path, "wb").write(response.content)
                logger.info(f"{os.path.basename(result)} has been downloaded.")
            else:
                messages = {
                    400: f"{os.path.basename(result)} couldn't be downloaded:",
                    500: f"{os.path.basename(result)} couldn't be downloaded:",
                    0: f"{os.path.basename(result)} couldn't be downloaded:",
                    -1: f"{os.path.basename(result)} couldn't be downloaded:",
                }
                report_request_error(response, None, messages=messages)

    else:
        report_request_error(response, customisation_id)


def report_request_error(
    response: requests.Response,
    cust_id: Optional[str] = None,
    messages: Optional[Dict[int, str]] = None,
) -> None:
    """helper function report requests errors to the user"""
    if messages is not None:
        _messages = messages
    else:
        _messages = {
            400: "There was an issue on client side. See below:",
            500: "There was an issue on server side. See below:",
            0: "An error occurred. See below:",
            -1: "An unexpected error has occurred.",
        }
        if cust_id is not None:
            _messages[400] = f"{cust_id} does not seem to be a valid job id. See below:"

    def _message_func(status_code: Optional[int] = None) -> str:
        try:
            if not status_code:
                return _messages[-1]

            if 400 <= status_code < 500:
                return _messages[400]

            elif status_code >= 500:
                return _messages[500]
            return _messages[0]
        except KeyError:
            return "Error description not found"
        return "Unexpected error"

    message = _message_func(response.status_code)

    logger.error(message)
    logger.error(f"{response.status_code} - {response.text}")


class TailorHelpAction(argparse.Action):
    """eumdac tailor -h entrypoint"""

    def __call__(self, parser: argparse.ArgumentParser, *args: Any, **kwargs: Any) -> None:
        # Print the help if the command has 2 args,
        # meaning it's just $ eumdac tailor
        if len(sys.argv) == 2:
            parser.print_help()
            parser.exit()


def parse_isoformat(input_string: str) -> datetime:
    """helper function to provide a user readable message when argparse encounters
    a wrongly formatted date"""
    try:
        return datetime.fromisoformat(input_string)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "The format of the provided date was not recognized. "
            "Expecting YYYY-MM-DD[THH[:MM[:SS]]]"
        )


def cli(command_line: Optional[Sequence[str]] = None) -> None:
    """eumdac entrypoint"""
    # append piped args
    if not sys.stdin.isatty():
        sys.argv.extend(shlex.split(sys.stdin.read()))

    init_logger("INFO")

    # main parser
    parser = argparse.ArgumentParser(description=__doc__, fromfile_prefix_chars="@")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--version", action="version", version=f"%(prog)s {eumdac.__version__}")
    parser.add_argument(
        "--set-credentials",
        nargs=2,
        action=SetCredentials,
        help=(
            "permanently set consumer key and secret and exit, "
            "see https://api.eumetsat.int/api-key"
        ),
        metavar=("ConsumerKey", "ConsumerSecret"),
        dest="credentials",
    )
    parser.add_argument("--debug", help="show backtrace for errors", action="store_true")

    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument("--test", action="store_true", help=argparse.SUPPRESS)
    common_parser.add_argument("-v", "--verbose", action="store_true")
    common_parser.add_argument("--debug", help="show backtrace for errors", action="store_true")

    subparsers = parser.add_subparsers(dest="command")

    # describe parser
    parser_describe = subparsers.add_parser(
        "describe",
        help="describe a collection or product",
        epilog="example: %(prog)s -c EO:EUM:DAT:MSG:HRSEVIRI",
        parents=[common_parser],
    )
    parser_describe.add_argument(
        "-c", "--collection", help="collection to describe", metavar="CollectionId"
    )
    parser_describe.add_argument("-p", "--product", help="product to describe", metavar="ProductId")
    parser_describe.add_argument(
        "--credentials",
        nargs=2,
        default=argparse.SUPPRESS,
        help="consumer key and secret, see https://api.eumetsat.int/api-key",
        metavar=("ConsumerKey", "ConsumerSecret"),
    )
    parser_describe.set_defaults(func=describe)

    # search parser
    search_argument_parser = argparse.ArgumentParser(add_help=False)
    search_argument_parser.add_argument(
        "-c", "--collection", nargs="+", help="collection ID(s)", required=True
    )
    search_argument_parser.add_argument(
        "-s",
        "--start",
        type=parse_isoformat,
        help="UTC start date e.g. 2002-12-21T12:30:15",
        metavar="YYYY-MM-DD[THH[:MM[:SS]]]",
        dest="dtstart",
    )
    search_argument_parser.add_argument(
        "-e",
        "--end",
        type=parse_isoformat,
        help="UTC end date e.g. 2002-12-21T12:30:15",
        metavar="YYYY-MM-DD[THH[:MM[:SS]]]",
        dest="dtend",
    )
    search_argument_parser.add_argument(
        "--bbox",
        nargs=4,
        type=float,
        metavar=("W", "S", "E", "N"),
        help="filter by bounding box, the box is defined in EPSG:4326 decimal degrees",
    )
    search_argument_parser.add_argument(
        "--time-range",
        nargs=2,
        type=parse_isoformat,
        help="convenience search on UTC time range",
        metavar="YYYY-MM-DD[THH[:MM[:SS]]]",
    )
    search_argument_parser.add_argument(
        "--geometry",
        help="filter by geometry, a custom geomtery in a EPSG:4326 decimal degrees.",
        dest="geo",
    )
    search_argument_parser.add_argument(
        "--cycle",
        help="filter by cycle number, must be a positive integer.",
        dest="cycle",
        type=int,
    )
    search_argument_parser.add_argument(
        "--orbit",
        help="filter by orbit number, must be a positive integer.",
        dest="orbit",
        type=int,
    )
    search_argument_parser.add_argument(
        "--relorbit",
        help="filter by relative orbit number, must be a positive integer.",
        dest="relorbit",
        type=int,
    )
    search_argument_parser.add_argument(
        "--filename",
        help="Can be used to define a wildcard search on the product title (product identifier), use set notation as OR and space as AND operator between multiple search terms.",
        dest="filename",
        type=str,
    )
    search_argument_parser.add_argument(
        "--timeliness",
        help="filter by timeliness",
        dest="timeliness",
        choices=["NT", "NR", "ST"],
    )
    search_argument_parser.add_argument("--satellite", help="filter by satellite", dest="sat")
    search_argument_parser.add_argument(
        "--sort", choices=("ingestion", "sensing"), help="sort results accordingly"
    )
    sorting_direction = search_argument_parser.add_mutually_exclusive_group(required=False)
    sorting_direction.add_argument("--asc", action="store_true", help="sort ascending")
    sorting_direction.add_argument("--desc", action="store_true", help="sort descending")
    search_argument_parser.add_argument(
        "--limit", type=int, help="Max Items to return, default = %(default)s"
    )
    search_argument_parser.add_argument(
        "--credentials",
        nargs=2,
        default=argparse.SUPPRESS,
        help="consumer key and secret, see https://api.eumetsat.int/api-key",
        metavar=("ConsumerKey", "ConsumerSecret"),
    )
    parser_search = subparsers.add_parser(
        "search",
        help="search for products at the collection level",
        epilog="example: %(prog)s -s 2020-03-01 -e 2020-03-15T12:15 -c EO:EUM:DAT:MSG:CLM",
        parents=[common_parser, search_argument_parser],
    )
    parser_search.set_defaults(func=search)

    parser_download = subparsers.add_parser(
        "download",
        help="download product(s) from a collection",
        parents=[common_parser, search_argument_parser],  # this inherits collection lists
    )
    parser_download.add_argument("-p", "--product", nargs="*", help="product ID(s)")
    parser_download.add_argument(
        "-o",
        "--output-dir",
        type=pathlib.Path,
        help="path to output directory, default CWD",
        metavar="DIR",
        default=pathlib.Path.cwd(),
    )
    parser_download.add_argument(
        "--entry",
        nargs="+",
        help="shell-style wildcard pattern(s) to filter product files",
    )
    parser_download.add_argument(
        "--tailor",
        help="Chain file for tailoring prior to downloading",
        metavar="CHAINYML",
    )
    parser_download.add_argument(
        "-y", "--yes", help="Skip interactive user input", action="store_true"
    )
    parser_download.add_argument(
        "--chain",
        help="Chain YAML string for tailoring prior to downloading",
        metavar="CHAINYMLSTR",
    )
    parser_download.set_defaults(func=download)

    # subscribe parser
    parser_subscribe = subparsers.add_parser(
        "subscribe",
        help="subscribe a server for a collection",
        parents=[common_parser],
    )
    parser_subscribe.add_argument(
        dest="print_help", nargs=0, action=TailorHelpAction, help=argparse.SUPPRESS
    )

    subscribe_subparsers = parser_subscribe.add_subparsers(dest="subscribe-command")

    subscribe_list_parser = subscribe_subparsers.add_parser(
        "list",
        description="List subscriptions from Data Store",
        help="List subscriptions from Data Store",
        parents=[common_parser],
    )
    subscribe_list_parser.set_defaults(func=subscribe_list_subscriptions)

    subscribe_create_parser = subscribe_subparsers.add_parser(
        "create",
        description="Create a new subscription for Data Store",
        help="Create a new subscription for Data Store",
        parents=[common_parser],
    )
    subscribe_create_parser.add_argument("-c", "--collection", help="collection ID", required=True)
    subscribe_create_parser.add_argument(
        "-u", "--url", help="public URL of the listener server", required=True
    )
    subscribe_create_parser.add_argument(
        "--area-of-interest",
        help="area of interest, a custom geomtery in a EPSG:4326 decimal degrees.",
    )
    subscribe_create_parser.set_defaults(func=subscribe_create_subscriptions)

    subscribe_delete_parser = subscribe_subparsers.add_parser(
        "delete",
        description="Delete subscriptions from Data Store",
        help="Delete subscriptions from Data Store",
        parents=[common_parser],
    )
    subscribe_delete_parser.add_argument("sub_ids", help="Subscription ID", type=str, nargs="+")
    subscribe_delete_parser.set_defaults(func=subscribe_delete_subscriptions)

    parser_subscribe.add_argument(
        "--credentials",
        nargs=2,
        default=argparse.SUPPRESS,
        help="consumer key and secret, see https://api.eumetsat.int/api-key",
        metavar=("ConsumerKey", "ConsumerSecret"),
    )

    # tailor parser
    parser_tailor = subparsers.add_parser(
        "tailor",
        description="Manage Data Tailor customisations",
        help="tailoring product(s) from collection",
        parents=[common_parser],
    )
    parser_tailor.add_argument(
        dest="print_help", nargs=0, action=TailorHelpAction, help=argparse.SUPPRESS
    )
    tailor_subparsers = parser_tailor.add_subparsers(dest="tailor-command")

    tailor_post_parser = tailor_subparsers.add_parser(
        "post",
        description="Posts a new customisation job into Data Tailor",
        help="Posts a new customisation job into Data Tailor",
        parents=[common_parser],
    )
    tailor_post_parser.add_argument("-c", "--collection", help="collection ID")
    tailor_post_parser.add_argument("-p", "--product", nargs="+", help="product ID(s)")
    tailor_post_parser.add_argument(
        "--chain",
        help="define a chain for customisation",
        metavar="chain",
    )
    tailor_post_parser.set_defaults(func=tailor_post_job)

    tailor_list_parser = tailor_subparsers.add_parser(
        "list",
        help="list customisations",
        parents=[common_parser],
    )
    tailor_list_parser.set_defaults(func=tailor_list_customisations)

    tailor_status_parser = tailor_subparsers.add_parser(
        "status",
        description="(DESC) Gets the status of one (or more) customisations",
        help="Get status of customisation",
        parents=[common_parser],
    )
    tailor_status_parser.add_argument("job_ids", metavar="Customisation ID", type=str, nargs="+")
    tailor_status_parser.set_defaults(func=tailor_show_status)

    tailor_log_parser = tailor_subparsers.add_parser(
        "log",
        help="Get the log of a customisation",
        parents=[common_parser],
    )
    tailor_log_parser.add_argument(
        "job_id", metavar="Customisation ID", type=str, help="Customisation ID"
    )
    tailor_log_parser.set_defaults(func=tailor_get_log)

    tailor_quota_parser = tailor_subparsers.add_parser(
        "quota", help="Get the quota of user", parents=[common_parser]
    )
    tailor_quota_parser.set_defaults(func=tailor_quota)

    tailor_delete_parser = tailor_subparsers.add_parser(
        "delete",
        description="Delete finished customisations",
        help="Delete finished customisations",
        parents=[common_parser],
    )
    tailor_delete_parser.add_argument("job_ids", metavar="Customisation ID", type=str, nargs="+")
    tailor_delete_parser.set_defaults(func=tailor_delete_jobs)

    tailor_cancel_parser = tailor_subparsers.add_parser(
        "cancel",
        description="Cancel QUEUED, RUNNING or INACTIVE customisations",
        help="Cancel QUEUED, RUNNING or INACTIVE customisations",
        parents=[common_parser],
    )
    tailor_cancel_parser.add_argument("job_ids", metavar="Customisation ID", type=str, nargs="+")
    tailor_cancel_parser.set_defaults(func=tailor_cancel_jobs)

    tailor_clean_parser = tailor_subparsers.add_parser(
        "clean",
        description="Remove customisations in any state",
        help="Remove customisations in any state",
        parents=[common_parser],
    )
    tailor_clean_parser.add_argument("job_ids", metavar="Customisation ID", type=str, nargs="*")
    tailor_clean_parser.add_argument("--all", help="Clean all customisations", action="store_true")
    tailor_clean_parser.set_defaults(func=tailor_clear_jobs)

    tailor_download_parser = tailor_subparsers.add_parser(
        "download",
        help="Download the output of a customisation",
        parents=[common_parser],
    )
    tailor_download_parser.add_argument(
        "job_id", metavar="Customisation ID", type=str, help="Customisation ID"
    )
    tailor_download_parser.add_argument(
        "-o",
        "--output-dir",
        type=pathlib.Path,
        help="path to output directory, default CWD",
        metavar="DIR",
        default=pathlib.Path.cwd(),
    )
    tailor_download_parser.set_defaults(func=tailor_download)

    parser_tailor.add_argument(
        "--credentials",
        nargs=2,
        default=argparse.SUPPRESS,
        help="consumer key and secret, see https://api.eumetsat.int/api-key",
        metavar=("ConsumerKey", "ConsumerSecret"),
    )

    #  Order parser
    parser_order = subparsers.add_parser(
        "order",
        description="Manage Data Store and Data Tailor orders",
        help="manage orders",
        parents=[common_parser],
    )
    parser_order.add_argument(
        dest="print_help", nargs=0, action=TailorHelpAction, help=argparse.SUPPRESS
    )
    order_subparsers = parser_order.add_subparsers(dest="order_command")
    order_parsers = {}
    for action in ["restart", "status", "resume", "delete"]:
        subparser = order_subparsers.add_parser(
            action,
            description=f"Order {action}",
            parents=[common_parser],
        )
        subparser.add_argument("order_id", metavar="ORDERID", nargs="?", default="latest")
        subparser.set_defaults(func=order)
        order_parsers[action] = subparser

    order_parsers["list"] = order_subparsers.add_parser(
        "list",
        description="Order list",
        parents=[common_parser],
    )
    order_parsers["list"].set_defaults(func=order)

    args = parser.parse_args(command_line)
    if args.debug:
        init_logger("DEBUG")

    if args.command:
        if args.test:
            return args.func(args)

        try:
            args.func(args)
        except KeyboardInterrupt:
            # Ignoring KeyboardInterrupts to allow for clean CTRL+C-ing
            pass
        except Exception as error:
            if args.debug:
                raise
            logger.error(str(error))
    else:
        parser.print_help()


class CredentialsFileNotFoundError(EumdacError):
    """Error that will be raised when no credentials file is found"""
