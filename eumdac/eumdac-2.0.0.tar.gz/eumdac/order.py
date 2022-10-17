"""module that enables order management in eumdac"""
import os
import re
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import *

import yaml

from eumdac.config import get_config_dir
from eumdac.datatailor import DataTailor
from eumdac.errors import EumdacError
from eumdac.logging import gen_table_printer
from eumdac.product import Product
from eumdac.tailor_models import Chain


@dataclass
class ProductInfo:
    p_id: str
    p_dict: Dict[str, Any]


class Order:
    def __init__(self, order_file: Optional[Path] = None):
        self._order_file = order_file or new_order_filename()
        self._lock = threading.Lock()

    def initialize(
        self,
        chain: Optional[Chain],
        products: Iterable[Product],
        output_dir: Path,
        file_pattern: Optional[Iterable[str]],
        query: Optional[Dict[str, str]],
    ) -> None:
        self._chain = chain
        self._products = products
        self._output_dir = output_dir
        self._file_patterns = file_pattern

        order_info: Dict[str, Any] = {
            "file_patterns": file_pattern,
            "output_dir": str(output_dir.resolve()),
            "query": query,
        }

        if chain:
            order_info["type"] = "tailor"
            order_info["chain"] = chain.asdict()
            order_info["max_workers"] = 3
            order_info["products_to_process"] = {
                p._id: {
                    "col_id": p.collection._id,
                    "server_state": "UNSUBMITTED",
                    "customisation": None,
                }
                for p in products
            }
        else:
            order_info["type"] = "download"
            order_info["products_to_process"] = {
                p._id: {
                    "col_id": p.collection._id,
                    "server_state": "UNSUBMITTED",
                }
                for p in products
            }

        with self._lock:
            with self._order_file.open("w") as orf:
                yaml.dump(
                    order_info,
                    orf,
                )

    def __str__(self) -> str:
        return Path(self._order_file).stem

    def get_dict_entries(self, *args: str) -> Tuple[Optional[str], ...]:
        ret: List[Optional[str]] = []
        with self.dict_from_file() as order_d:
            for name in args:
                try:
                    ret.append(order_d[name])
                except KeyError:
                    ret.append(None)
        return tuple(ret)

    def status(self) -> str:
        if self.all_done():
            return "DONE"
        for p_info in self.iter_product_info():
            if p_info.p_dict["server_state"] in ("FAILED", "INACTIVE"):
                return "FAILED"
        return "NOT COMPLETED"

    def delete(self) -> None:
        os.remove(self._order_file)

    def collections(self) -> List[str]:
        ret = []
        for p_info in self.iter_product_info():
            ret.append(p_info.p_dict["col_id"])
        return list(set(ret))

    def pretty_string(self, print_products: bool = False) -> str:
        ret_lines: List[str] = []
        (typ, query, chain, output_dir) = self.get_dict_entries(
            "type", "query", "chain", "output_dir"
        )
        ret = [
            f"Order {str(self)}",
            f"Status: {self.status()}",
            f"Collection: {self.collections()}",
            "Query:",
        ]
        query_dump = yaml.dump(query).strip()
        for line in query_dump.split("\n"):
            ret.append(f"    {line.rstrip()}")
        if chain:
            ret.append("Chain:")
            chain_dump = yaml.dump(chain).strip()
            for line in chain_dump.split("\n"):
                ret.append(f"    {line.rstrip()}")
        ret.append(f"Output directory: {output_dir}")
        if print_products:
            print_func = ret.append
            if typ == "tailor":
                printer = gen_table_printer(
                    print_func, [("Product", 60), ("Job Id", 10), ("Status", 12)]
                )
                for p_info in self.iter_product_info():
                    state = _compute_state(p_info.p_dict)
                    printer([p_info.p_id, p_info.p_dict["customisation"], state])
            elif typ == "download":
                printer = gen_table_printer(print_func, [("Product", 60), ("Status", 12)])
                for p_info in self.iter_product_info():
                    printer([p_info.p_id, p_info.p_dict["server_state"]])
            else:
                raise NotImplementedError(typ)
        return "\n".join(ret)

    def _locked_serialize(self, order_dict: Dict[str, Any]) -> None:
        with self._lock:
            with self._order_file.open("w") as orf:
                yaml.dump(order_dict, orf)

    @contextmanager
    def dict_from_file(self) -> Generator[Dict[str, Any], None, None]:
        with self._lock:
            ret_dict = self._deserialize()
        yield ret_dict

    def _deserialize(self) -> Dict[str, Any]:
        with self._order_file.open("r") as orf:
            ret_val = yaml.safe_load(orf)
        if ret_val is None:
            raise EumdacError(f"{self._order_file.resolve()} is corrupted.")
        return ret_val

    def remote_delete_failed(self, datatailor: DataTailor) -> None:
        for p_info in self.iter_product_info():
            if p_info.p_dict["server_state"] == "FAILED":
                customisation_id = p_info.p_dict["customisation"]
                if customisation_id:
                    try:
                        customisation = datatailor.get_customisation(customisation_id)
                        customisation.delete()
                    except EumdacError:
                        continue

    def resolve_product_num(self, product_id: str) -> Tuple[int, int]:
        num_products = len(list(self.iter_product_info()))
        for num, p_info in enumerate(self.iter_product_info(), 1):
            if p_info.p_id == product_id:
                return num_products, num
        raise KeyError(product_id)

    def update(
        self,
        customisation_id: Optional[str],
        product_id: str,
        status: Optional[str] = None,
        download_states: Optional[Dict[str, str]] = None,
        max_workers: Optional[int] = 3,
    ) -> None:
        with self.dict_from_file() as order:
            if max_workers:
                order["max_workers"] = max_workers
            if status:
                order["products_to_process"][product_id]["server_state"] = status
            if download_states:
                order["products_to_process"][product_id]["download_states"] = download_states
            if customisation_id:
                order["products_to_process"][product_id]["customisation"] = customisation_id
        self._locked_serialize(order)

    def set_num_workers(self, number: int) -> None:
        with self.dict_from_file() as order_d:
            order_d["max_workers"] = number
        self._locked_serialize(order_d)

    def reset_states(self) -> None:
        with self.dict_from_file() as order:
            products = order["products_to_process"]
        for prod_id, prod_info in products.items():
            if "download_states" in prod_info:
                del prod_info["download_states"]
            prod_info["server_state"] = "UNSUBMITTED"
            if order["type"] == "tailor":
                prod_info["customisation"] = None
        self._locked_serialize(order)

    def iter_product_info(self) -> Iterable[ProductInfo]:
        with self.dict_from_file() as order:
            orders = order["products_to_process"].items()
        for p_id, p_dict in orders:
            yield ProductInfo(p_id, p_dict)

    def get_products(self, datastore: Any) -> Iterable[Product]:
        for p_info in self.iter_product_info():
            yield datastore.get_product(p_info.p_dict["col_id"], p_info.p_id)

    def all_done(self) -> bool:
        (typ,) = self.get_dict_entries("type")
        if typ == "tailor":
            return self._all_done_tailor()
        elif typ == "download":
            return self._all_done_download()
        else:
            raise NotImplementedError(typ)

    def _all_done_tailor(self) -> bool:
        for p_info in self.iter_product_info():
            if not "download_states" in p_info.p_dict:
                return False
            for _fname, state in p_info.p_dict["download_states"].items():
                if state != "DOWNLOADED":
                    return False
        return True

    def _all_done_download(self) -> bool:
        return all([pi.p_dict["server_state"] == "DONE" for pi in self.iter_product_info()])


def _compute_state(p_dict: Dict[str, Any]) -> str:
    server_state = p_dict["server_state"]
    if server_state != "DONE":
        return server_state
    if not "download_states" in p_dict:
        return "DONE (NOT DOWNLOADED)"
    for _fname, state in p_dict["download_states"].items():
        if state != "DOWNLOADED":
            return "DONE (NOT DOWNLOADED)"
    return "DONE"


def get_order_dir() -> Path:
    order_dir = get_config_dir() / "orders"
    order_dir.mkdir(exist_ok=True, parents=True)
    return order_dir


def highest_number_in_order_filenames(file_paths: Iterable[Path]) -> int:
    number_pattern = re.compile(r".*#([\d]+).yml")
    order_numbers = [int(number_pattern.findall(fname.name)[0]) for fname in file_paths]
    return max(order_numbers)


def highest_prefix_in_order_filenames(file_paths: Iterable[Path]) -> str:
    return max([fpath.stem.split("#")[0] for fpath in file_paths])


def all_order_filenames(prefix: str = "") -> Iterable[Path]:
    order_dir = get_order_dir()
    glob = f"*.yml"
    if len(prefix) > 0:
        glob = f"{prefix}#*.yml"
    return sorted(order_dir.glob(glob), key=_dt_from_order_filename)


def _dt_from_order_filename(fn: Path) -> datetime:
    date, number = fn.stem.split("#")
    return datetime.fromisoformat(date) + timedelta(milliseconds=int(number))


def latest_order_file() -> Path:
    filepaths = all_order_filenames()
    prefix = highest_prefix_in_order_filenames(filepaths)
    filepaths = all_order_filenames(prefix)
    number = highest_number_in_order_filenames(filepaths)
    return get_order_dir() / Path(f"{prefix}#{number:04d}.yml")


def new_order_filename() -> Path:
    order_prefix = f"{datetime.now().strftime('%Y-%m-%d')}"

    all_filenames = list(all_order_filenames(order_prefix))

    if len(all_filenames) < 1:
        return get_order_dir() / Path(f"{order_prefix}#{1:04d}.yml")

    highest_existing_number = highest_number_in_order_filenames(all_filenames)

    return get_order_dir() / Path(f"{order_prefix}#{int(highest_existing_number)+1:04d}.yml")


def resolve_order(order_name: str) -> Order:
    if order_name == "latest":
        filenames = list(all_order_filenames())
        if len(filenames) == 0:
            raise EumdacError("No order files found. Cannot use 'latest'")
        return Order(latest_order_file())
    return Order(get_order_dir() / Path(f"{order_name}.yml"))
