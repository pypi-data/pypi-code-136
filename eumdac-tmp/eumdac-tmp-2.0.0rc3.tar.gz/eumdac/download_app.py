"""module containing the DownloadApp which will be used when using 
eumdac download **without** the --tailor argument."""
import fnmatch
import shutil
from pathlib import Path
from typing import *

from eumdac.job_id import JobIdentifactor
from eumdac.logging import logger
from eumdac.order import Order
from eumdac.product import Product


class DownloadApp:
    def __init__(
        self,
        order: Order,
        datastore: Any,
    ) -> None:
        self.order = order
        self.datastore = datastore
        num_jobs = len(list(self.order.iter_product_info()))
        self.job_identificator = JobIdentifactor(num_jobs)

    def run(self) -> None:
        logger.debug("Starting download(s)")
        return self._run_app()

    def shutdown(self) -> None:
        with self.order._lock:
            return

    def _run_app(self) -> None:
        with self.order.dict_from_file() as order_d:
            output_dir = order_d["output_dir"]
            output_dir = Path(output_dir)
            output_dir.mkdir(exist_ok=True, parents=True)

        (file_patterns,) = self.order.get_dict_entries("file_patterns")
        logger.info(f"Output directory: {Path(output_dir).resolve()}")

        for product in self.order.get_products(self.datastore):
            self.job_identificator.register(product)
            with self.order.dict_from_file() as order_d:
                state = order_d["products_to_process"][product._id]["server_state"]
            if state == "DONE":
                continue
            if file_patterns:
                entries = product.entries
                filtered_entries = []
                for pattern in file_patterns:
                    matches = fnmatch.filter(entries, pattern)
                    filtered_entries.extend(matches)
                entries = filtered_entries
                for entry in entries:
                    self.download_product(product, entry, output_dir)
            else:
                self.download_product(product, None, output_dir)
            self.order.update(None, product._id, "DONE")

    def download_product(self, product: Product, entry: Optional[str], output_dir: Path) -> None:
        job_id = self.job_identificator.job_id_str(product)

        with product.open(entry=entry) as fsrc:
            output = output_dir / fsrc.name
            if entry:
                # when entry is used we create a subdirectory
                # to avoid overwriting common files
                output_subdir = output_dir / f"{product}"
                output_subdir.mkdir(exist_ok=True)
                output = output_subdir / fsrc.name

            if output.is_file():
                logger.info(f"{job_id} Skip {output} it already exists")
            else:
                logger.info(f"{job_id} Downloading {output}")
                tmp = Path(output.stem + ".tmp")
                with tmp.open(mode="wb") as fdst:
                    # note: currently, there is no content-length header
                    # in the data store http response, so it is not simple to
                    # build a progress bar. In case it is added in future,
                    # just check fsrc.getheader("Content-Length")
                    shutil.copyfileobj(fsrc, fdst)
                tmp.rename(output)
