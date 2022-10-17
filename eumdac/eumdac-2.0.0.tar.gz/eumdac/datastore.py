from __future__ import annotations

from typing import TYPE_CHECKING

import requests

from eumdac.collection import Collection
from eumdac.errors import EumdacError, eumdac_raise_for_status
from eumdac.product import Product
from eumdac.subscription import Subscription
from eumdac.token import AccessToken, URLs

from .__version__ import __documentation__, __title__, __version__  # noqa

if TYPE_CHECKING:  # pragma: no cover
    import sys
    from typing import Optional

    if sys.version_info < (3, 9):
        from typing import Iterable, Mapping
    else:
        from collections.abc import Iterable, Mapping


class DataStore:
    token: AccessToken
    urls: URLs
    _collections: Mapping[str, Collection]

    def __init__(self, token: AccessToken) -> None:
        self.token = token
        self.urls = token.urls
        self._collections = {}

    def _load_collections(self) -> None:
        if self._collections:
            return
        url = self.urls.get("datastore", "browse collections")
        response = requests.get(
            url,
            params={"format": "json"},
            auth=self.token.auth,
            headers={
                "referer": __documentation__,
                "User-Agent": str(__title__ + "/" + __version__),
            },
        )
        eumdac_raise_for_status("Load collections failed", response, DataStoreError)
        collection_ids = [item["title"] for item in response.json()["links"]]
        self._collections = {
            collection_id: Collection(collection_id, self) for collection_id in collection_ids
        }

    @property
    def collections(self) -> Iterable[Collection]:
        self._load_collections()
        return list(self._collections.values())

    @property
    def subscriptions(self) -> Iterable[Subscription]:
        url = self.urls.get("datastore", "subscriptions")
        response = requests.get(
            url,
            auth=self.token.auth,
            headers={
                "referer": __documentation__,
                "User-Agent": str(__title__ + "/" + __version__),
            },
        )
        eumdac_raise_for_status("Get subscriptions failed", response, DataStoreError)
        return [Subscription(properties["uuid"], self) for properties in response.json()]

    def get_collection(self, collection_id: str) -> Collection:
        """collection factory"""
        self._load_collections()
        try:
            return self._collections[collection_id]
        except KeyError as error:
            raise DataStoreError(f"unknown collection {collection_id}") from error

    def get_product(self, collection_id: str, product_id: str) -> Product:
        """product factory"""
        return Product(collection_id, product_id, self)

    def get_subscription(self, subscription_id: str) -> Subscription:
        """subscription factory"""
        return Subscription(subscription_id, self)

    def new_subscription(
        self, collection: Collection, url: str, area_of_interest: Optional[str] = None
    ) -> Subscription:
        """create new subscription"""
        parameters = {"collectionId": collection._id, "url": url}
        if area_of_interest is not None:
            parameters["aoi"] = area_of_interest
        subscriptions_url = self.urls.get("datastore", "subscriptions")
        response = requests.post(subscriptions_url, json=parameters, auth=self.token.auth)
        eumdac_raise_for_status("Creation of new subscription failed", response, DataStoreError)
        subscription_id = response.json()
        return Subscription(subscription_id, self)


class DataStoreError(EumdacError):
    "Errors related to the DataStore"
