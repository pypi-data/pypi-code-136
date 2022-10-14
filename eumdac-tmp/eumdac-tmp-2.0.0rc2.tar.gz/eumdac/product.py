"""Module containing the Data Store Product class."""
from __future__ import annotations

import re
from contextlib import contextmanager
from datetime import datetime
from functools import total_ordering
from typing import TYPE_CHECKING

import requests

from .__version__ import __documentation__, __title__, __version__  # noqa

if TYPE_CHECKING:  # pragma: no cover
    import sys
    from typing import IO, Any, Optional

    if sys.version_info < (3, 9):
        from typing import Generator, Mapping, MutableMapping, Pattern, Sequence
    else:
        from collections.abc import Mapping, MutableMapping, Generator, Sequence
        from re import Pattern
    from eumdac.datastore import DataStore
    from eumdac.collection import Collection

from eumdac.errors import EumdacError, eumdac_raise_for_status


@total_ordering
class Product:
    """Product of a Collection in the Data Store

    Attributes:
        datastore: Reference to the Data Store
        download_url: URL to the download endpoint of the Data Store

    Arguments:
        collection_id: Data Store ID of the collection
        product_id: Data Store ID of the product
        datastore: Reference to the Data Store
    """

    _id: str
    datastore: DataStore
    collection: Collection
    _properties: Optional[Mapping[str, Any]] = None
    _geometry: Optional[Mapping[str, Any]] = None
    _entries: Optional[Sequence[str]] = None
    _extract_filename: Pattern[str] = re.compile(r'filename="(.*?)"')
    _extract_sensing_time: Pattern[str] = re.compile(
        r"(?P<start>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3,6})?)?"
        r"\d*Z?[\\/]+"
        r"(?P<end>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3,6})?)?"
    )

    def __init__(self, collection_id: str, product_id: str, datastore: DataStore) -> None:
        self._id = product_id
        self.datastore = datastore
        self.collection = self.datastore.get_collection(collection_id)

    def __str__(self) -> str:
        return str(self._id)

    def __repr__(self) -> str:
        return f"{self.__class__}({self.collection._id}, {self._id})"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and (self.collection._id, self._id) == (
            other.collection._id,
            other._id,
        )

    def __lt__(self, other: Product) -> bool:
        return (self.collection._id, self._id) < (other.collection._id, other._id)

    def __hash__(self) -> int:
        return hash(repr(self))

    def _ensure_properties(self) -> None:
        if self._properties is not None:
            return
        url = self.datastore.urls.get(
            "datastore",
            "download product metadata",
            vars={"collection_id": self.collection._id, "product_id": self._id},
        )
        auth = self.datastore.token.auth
        response = requests.get(
            url,
            params={"format": "json"},
            auth=auth,
            headers={
                "referer": __documentation__,
                "User-Agent": str(__title__ + "/" + __version__),
            },
        )
        eumdac_raise_for_status(
            f"Product {self._id} not found in {self.collection._id}", response, ProductError
        )
        geometry = response.json()["geometry"]
        properties = response.json()["properties"]
        properties.pop("parentIdentifier")
        properties.pop("links", None)

        self._geometry = geometry
        self._properties = properties

    def _load_sip_entries(self) -> None:
        url = self.datastore.urls.get(
            "datastore",
            "browse product",
            vars={"collection_id": self.collection._id, "product_id": self._id},
        )
        auth = self.datastore.token.auth
        response = requests.get(
            url,
            params={"format": "json"},
            auth=auth,
            headers={
                "referer": __documentation__,
                "User-Agent": str(__title__ + "/" + __version__),
            },
        )
        eumdac_raise_for_status(
            f"Product {self._id} not found in {self.collection._id}", response, ProductError
        )
        properties = response.json()["properties"]
        links = properties.pop("links")
        self._entries = [link["title"] for link in links["sip-entries"]]

    @property
    def sensing_start(self) -> datetime or bool:  # type: ignore[valid-type]
        """Sensing start date"""
        self._ensure_properties()
        sensing_time = self._extract_sensing_time.search(  # type: ignore[union-attr]
            self._properties["date"]  # type: ignore[index]
        ).groupdict()
        sensing_start = sensing_time["start"]
        if sensing_start is None:
            return False
        else:
            return datetime.fromisoformat(sensing_start)

    @property
    def sensing_end(self) -> datetime or bool:  # type: ignore[valid-type]
        """Sensing end date"""
        self._ensure_properties()
        sensing_time = self._extract_sensing_time.search(  # type: ignore[union-attr]
            self._properties["date"]  # type: ignore[index]
        ).groupdict()
        sensing_end = sensing_time["end"]
        if sensing_end is None:
            return False
        else:
            return datetime.fromisoformat(sensing_end)

    @property
    def satellite(self) -> str:
        """Platform or Mission related to the product"""
        self._ensure_properties()
        satellites = [
            acquisition["platform"]["platformShortName"]
            for acquisition in self._properties["acquisitionInformation"]  # type: ignore[index]
        ]
        return ", ".join(satellites)

    @property
    def instrument(self) -> str:
        """Instrument related to the product"""
        self._ensure_properties()
        instruments = [
            acquisition["instrument"]["instrumentShortName"]
            for acquisition in self._properties["acquisitionInformation"]  # type: ignore[index]
        ]
        return ", ".join(instruments)

    @property
    def size(self) -> int:
        """Size of the product"""
        self._ensure_properties()
        return self._properties["productInformation"]["size"]  # type: ignore[index]

    @property
    def timeliness(self) -> int:
        """Timeliness of the product"""
        self._ensure_properties()
        return self._properties["productInformation"]["timeliness"]  # type: ignore[index]

    @property
    def metadata(self) -> MutableMapping[str, Any]:
        """Product metadata"""
        self._ensure_properties()
        return {
            "geometry": self._geometry.copy(),  # type: ignore[union-attr]
            "properties": self._properties.copy(),  # type: ignore[union-attr]
        }

    @property
    def entries(self) -> Sequence[str]:
        """Files inside the product"""
        if self._entries is None:
            self._load_sip_entries()
        return tuple(self._entries)  # type: ignore[arg-type]

    @property
    def url(self) -> str:
        """URL of the product"""
        auth = str(self.datastore.token.access_token)
        url = self.datastore.urls.get(
            "datastore",
            "download product",
            vars={"collection_id": self.collection._id, "product_id": self._id},
        )
        download_url = str(url) + "?access_token=" + auth
        return download_url

    @contextmanager
    def open(self, entry: Optional[str] = None) -> Generator[IO[bytes], None, None]:
        """Opens a stream to download the product content.

        Note:
            A Data Store product refers to a zip archive containing the data.

        Arguments:
            entry (optional): specific file inside the product
        """
        url = self.datastore.urls.get(
            "datastore",
            "download product",
            vars={"collection_id": self.collection._id, "product_id": self._id},
        )
        auth = self.datastore.token.auth
        params = None
        if entry is not None:
            url += "/entry"
            params = {"name": entry}
        with requests.get(
            url,
            auth=auth,
            params=params,
            stream=True,
            headers={
                "referer": __documentation__,
                "User-Agent": str(__title__ + "/" + __version__),
            },
        ) as response:
            eumdac_raise_for_status(
                f"Could not download Product {self._id} of Collection {self.collection._id}",
                response,
                ProductError,
            )
            match = self._extract_filename.search(response.headers["Content-Disposition"])
            filename = match.group(1)  # type: ignore[union-attr]
            response.raw.name = filename
            response.raw.decode_content = True
            yield response.raw


class ProductError(EumdacError):
    """Errors related to products"""
