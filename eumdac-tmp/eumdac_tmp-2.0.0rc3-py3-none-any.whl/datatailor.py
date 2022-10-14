"""Module contianing the data tailor class"""
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import requests

from eumdac.customisation import Customisation
from eumdac.errors import EumdacError, eumdac_raise_for_status
from eumdac.tailor_models import Chain, DataTailorCRUD, Filter, Quicklook, RegionOfInterest

from .__version__ import __documentation__, __title__, __version__  # noqa

if TYPE_CHECKING:  # pragma: no cover
    import sys
    from typing import Any, Optional

    from eumdac.product import Product
    from eumdac.token import AccessToken, URLs

    if sys.version_info < (3, 9):
        from typing import Iterable, Mapping, Sequence
    else:
        from collections.abc import Iterable, Mapping, Sequence


class DataTailor:
    token: AccessToken
    urls: URLs
    chains: DataTailorCRUD
    filters: DataTailorCRUD
    rois: DataTailorCRUD
    quicklooks: DataTailorCRUD
    _info: Optional[Mapping[str, Any]] = None
    _user_info: Optional[Mapping[str, Any]] = None

    def __init__(self, token: AccessToken) -> None:
        self.token = token
        self.urls = token.urls
        self.chains = DataTailorCRUD(self, Chain)
        self.filters = DataTailorCRUD(self, Filter)
        self.rois = DataTailorCRUD(self, RegionOfInterest)
        self.quicklooks = DataTailorCRUD(self, Quicklook)

    @property
    def customisations(self) -> Sequence[Customisation]:
        url = self.urls.get("tailor", "customisations")
        response = requests.get(
            url,
            auth=self.token.auth,
            headers={
                "referer": __documentation__,
                "User-Agent": str(__title__ + "/" + __version__),
            },
        )
        eumdac_raise_for_status("Could not get customisations", response, DataTailorError)
        customisations = response.json()["data"]
        return [Customisation.from_properties(properties, self) for properties in customisations]

    @property
    def info(self) -> Mapping[str, Any]:
        if self._info is None:
            url = self.urls.get("tailor", "info")
            auth = self.token.auth
            response = requests.get(
                url,
                auth=auth,
                headers={
                    "referer": __documentation__,
                    "User-Agent": str(__title__ + "/" + __version__),
                },
            )
            eumdac_raise_for_status("Could not get info", response, DataTailorError)
            self._info = response.json()
        return self._info

    @property
    def user_info(self) -> Mapping[str, Any]:
        if self._user_info is None:
            url = self.urls.get("tailor", "user info")
            auth = self.token.auth
            response = requests.get(
                url,
                auth=auth,
                headers={
                    "referer": __documentation__,
                    "User-Agent": str(__title__ + "/" + __version__),
                },
            )
            eumdac_raise_for_status("Could not get user_info", response, DataTailorError)
            self._user_info = response.json()
        return self._user_info

    @property
    def quota(self) -> Mapping[str, Any]:
        url = self.urls.get("tailor", "report quota")
        auth = self.token.auth
        response = requests.get(
            url,
            auth=auth,
            headers={
                "referer": __documentation__,
                "User-Agent": str(__title__ + "/" + __version__),
            },
        )
        eumdac_raise_for_status("Could not get quota", response, DataTailorError)
        return response.json()

    def get_customisation(self, cutomisation_id: str) -> Customisation:
        return Customisation(cutomisation_id, self)

    def new_customisation(self, product: Product, chain: Chain) -> Customisation:
        (customisation,) = self.new_customisations([product], chain)
        return customisation

    def new_customisations(
        self, products: Iterable[Product], chain: Chain
    ) -> Sequence[Customisation]:
        product_paths = "|||".join(
            self.urls.get(
                "datastore",
                "download product",
                vars={
                    "product_id": product._id,
                    "collection_id": product.collection._id,
                },
            )
            for product in products
        )
        params = {"product_paths": product_paths, "access_token": str(self.token)}
        if isinstance(chain, str):
            params["chain_name"] = chain
        else:
            params["chain_config"] = json.dumps(chain.asdict())
        response = requests.post(
            self.urls.get("tailor", "customisations"),
            auth=self.token.auth,
            params=params,
        )
        eumdac_raise_for_status("Could not add customizations", response, DataTailorError)

        customisation_ids = response.json()["data"]
        return [self.get_customisation(customisation_id) for customisation_id in customisation_ids]


class DataTailorError(EumdacError):
    """Errors related to DataTailor operations"""
