"""
The Service module.

This module provides the following classes:
- CardTrader
"""
__all__ = ["CardTrader"]

import platform
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

from pydantic import ValidationError, parse_obj_as
from ratelimit import limits, sleep_and_retry
from requests import get
from requests.exceptions import ConnectionError, HTTPError, JSONDecodeError, ReadTimeout

from cardtrader import __version__
from cardtrader.exceptions import AuthenticationError, ServiceError
from cardtrader.schemas.blueprint import Blueprint
from cardtrader.schemas.category import Category
from cardtrader.schemas.expansion import Expansion
from cardtrader.schemas.game import Game
from cardtrader.schemas.info import Info
from cardtrader.schemas.product import Product
from cardtrader.sqlite_cache import SQLiteCache

MINUTE = 60


class CardTrader:
    """
    Wrapper to allow calling CardTrader API endpoints.

    Args:
        access_token: User's access token to access CardTrader.
        timeout: Set how long requests will wait for a response (in seconds).
        cache: SQLiteCache to use if set.

    Attributes:
        headers (Dict[str, str]): Header used when requesting from CardTrader.
        timeout (int): How long requests will wait for a response (in seconds).
        cache (Optional[SQLiteCache]): SQLiteCache to use if set.
    """

    API_URL = "https://api.cardtrader.com/api/v2"

    def __init__(self, access_token: str, timeout: int = 30, cache: Optional[SQLiteCache] = None):
        self.headers = {
            "Accept": "application/json",
            "User-Agent": f"CardTrader-Wrapper/{__version__}"
            f"/{platform.system()}: {platform.release()}",
            "Authorization": f"Bearer {access_token}",
        }
        self.timeout = timeout
        self.cache = cache

    @sleep_and_retry
    @limits(calls=20, period=MINUTE)
    def _perform_get_request(self, url: str, params: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Make GET request to CardTrader.

        Args:
            url: The url to request information from.
            params: Parameters to add to the request.
        Returns:
            Json response from CardTrader.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with the request or response.
        """
        if params is None:
            params = {}

        try:
            response = get(url, params=params, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except ConnectionError:
            raise ServiceError(f"Unable to connect to '{url}'")
        except HTTPError as err:
            if err.response.status_code == 401:
                raise AuthenticationError(err.response.text)
            raise ServiceError(err.response.text)
        except JSONDecodeError:
            raise ServiceError(f"Unable to parse response from '{url}' as Json")
        except ReadTimeout:
            raise ServiceError("Server took too long to respond")

    def _get_request(
        self, endpoint: str, params: Dict[str, str] = None, skip_cache: bool = False
    ) -> Dict[str, Any]:
        """
        Check cache or make GET request to CardTrader.

        Args:
            endpoint: The endpoint to request information from.
            params: Parameters to add to the request.
        Returns:
            Json response from CardTrader.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with the request or response.
        """
        if params is None:
            params = {}

        url = self.API_URL + endpoint
        cache_params = f"?{urlencode(params)}" if params else ""
        cache_key = f"{url}{cache_params}"

        if self.cache and not skip_cache:
            if cached_response := self.cache.select(cache_key):
                return cached_response

        response = self._perform_get_request(url=url, params=params)

        if self.cache and not skip_cache:
            self.cache.insert(cache_key, response)

        return response

    def info(self) -> Info:
        """
        Request information on your CardTrader account.

        Returns:
            An Info object.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with validating the response.
        """
        try:
            result = self._get_request(endpoint="/info", skip_cache=True)
            return Info(**result)
        except ValidationError as err:
            raise ServiceError(err)

    def games(self) -> List[Game]:
        """
        Request a list of Games.

        Returns:
            A list of games.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with validating the response.
        """
        try:
            results = self._get_request(endpoint="/games")["array"]
            return parse_obj_as(List[Game], results)
        except ValidationError as err:
            raise ServiceError(err)

    def categories(self, game_id: Optional[int] = None) -> List[Category]:
        """
        Request a list of Categories optionally filtered by Game.

        Args:
            game_id: Optional filter by game_id.
        Returns:
            A list of categories.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with validating the response.
        """
        try:
            results = self._get_request(
                endpoint="/categories", params={"game_id": str(game_id)} if game_id else {}
            )
            return parse_obj_as(List[Category], results)
        except ValidationError as err:
            raise ServiceError(err)

    def expansions(self) -> List[Expansion]:
        """
        Request a list of Expansions.

        Returns:
            A list of expansions.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with validating the response.
        """
        try:
            results = self._get_request(endpoint="/expansions")
            return parse_obj_as(List[Expansion], results)
        except ValidationError as err:
            raise ServiceError(err)

    def blueprints(self, expansion_id: int) -> List[Blueprint]:
        """
        Request a list of Blueprints in an Expansion.

        Args:
            expansion_id: The expansion id.
        Returns:
            A list of blueprints.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with validating the response.
        """
        try:
            results = self._get_request(
                endpoint="/blueprints/export", params={"expansion_id": str(expansion_id)}
            )
            return parse_obj_as(List[Blueprint], results)
        except ValidationError as err:
            raise ServiceError(err)

    def products_by_expansion(self, expansion_id: int) -> List[Product]:
        """
        Request a list of Products by expansion.

        Args:
            expansion_id: The expansion id.
        Returns:
            A list of products.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with validating the response.
        """
        try:
            results = self._get_request(
                endpoint="/marketplace/products", params={"expansion_id": str(expansion_id)}
            ).values()
            return parse_obj_as(List[Product], list(results)[0])
        except ValidationError as err:
            raise ServiceError(err)

    def products_by_blueprint(self, blueprint_id: int) -> List[Product]:
        """
        Request a list of Products by blueprint.

        Args:
            blueprint_id: The blueprint id.
        Returns:
            A list of products.
        Raises:
            AuthenticationError: If CardTrader returns with an invalid access token response.
            ServiceError: If there is an issue with validating the response.
        """
        try:
            results = self._get_request(
                endpoint="/marketplace/products", params={"blueprint_id": str(blueprint_id)}
            ).values()
            return parse_obj_as(List[Product], list(results)[0])
        except ValidationError as err:
            raise ServiceError(err)
