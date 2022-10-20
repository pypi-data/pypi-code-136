from typing import Optional
from urllib.parse import urlencode

from pydantic import constr
from requests import Response

from yelpfusion3.category.model import Categories, CategoryDetails
from yelpfusion3.endpoint import Endpoint
from yelpfusion3.model import Model
from yelpfusion3.settings import Settings


class CategoryDetailsEndpoint(Endpoint):
    """
    This endpoint returns detailed information about the Yelp category specified by a Yelp category alias.
    """

    _path: str = "/categories/{alias}"

    locale: Optional[str]
    """
    Optional. Specify the locale to return the autocomplete suggestions in. See
    :py:class:`~yelpfusion3.endpoint.SupportedLocales`. Defaults to ``en_US``.
    """

    alias: constr(min_length=1)
    """
    Required. Specify the alias of the category.
    """

    @property
    def url(self) -> str:
        """
        Constructs a URL to the category details endpoint with the given query parameters.

        :return: Yelp Fusion API 3 endpoint URL.
        :rtype: str
        """
        non_none_fields = {key: value for key, value in self.dict().items() if value is not None and key != "alias"}
        parameters = urlencode(query=non_none_fields)
        settings: Settings = Settings()
        path: str = self._path.format(alias=self.alias)

        if parameters:
            return f"{settings.base_url}{path}?{parameters}"
        else:
            return f"{settings.base_url}{path}"

    def get(self) -> CategoryDetails:
        response: Response = self._get()
        return CategoryDetails(**response.json())


class AllCategoriesEndpoint(Endpoint):
    """
    This endpoint returns all Yelp business categories across all locales by default. Include the "locale" parameter to
    filter to only those categories available for a particular locale, and translate/localize the names of those
    categories.
    """

    _path: str = "/categories"

    locale: Optional[str]
    """
    Optional. Specify the locale to filter the categories returned to only those available in that locale, and to
    translate the names of the categories appropriately. See
    :py:class:`~yelpfusion3.endpoint.SupportedLocales`. If not included, all categories across all locales will be
    returned and the category names will be in English.
    """

    def get(self) -> Categories:
        response: Response = self._get()
        return Categories(**response.json())
