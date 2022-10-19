from __future__ import annotations

from typing import Optional

from pydantic import confloat, constr

from yelpfusion3.business.endpoint import (
    AutocompleteEndpoint,
    BusinessDetailsEndpoint,
    BusinessMatchesEndpoint,
    BusinessSearchEndpoint,
    PhoneSearchEndpoint,
    ReviewsEndpoint,
    TransactionSearchEndpoint,
)
from yelpfusion3.category.endpoint import AllCategoriesEndpoint, CategoryDetailsEndpoint
from yelpfusion3.category.model import Categories
from yelpfusion3.event.endpoint import EventLookupEndpoint, EventSearchEndpoint, FeaturedEventEndpoint


class Client:
    """
    Client is a collection of factory methods that create :py:class:`~yelpfusion3.endpoint.Endpoint` objects used to
    interact with Yelp Fusion endpoints. Function parameters provide guidance on which endpoint parameters are required.
    Optional parameters can be added to the instantiated object by setting their respective fields.
    """

    @staticmethod
    def business_details(
        business_id: constr(strip_whitespace=True, min_length=1, regex=r"^[A-Za-z0-9\-]+$")
    ) -> BusinessDetailsEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.BusinessDetailsEndpoint` object used to interact with
        the Yelp Business Details REST endpoint.

        :param business_id: Unique Yelp ID of the business to query for.
        :type business_id: str
        :return: An endpoint wrapper for the Yelp Business Details REST endpoint.
        :rtype: BusinessDetailsEndpoint
        """

        return BusinessDetailsEndpoint(business_id=business_id)

    @staticmethod
    def business_matches(
        name: constr(strip_whitespace=True, min_length=1, max_length=64, regex=r"^[\da-zA-Z\s\!#$%&+,./:?@']+$"),
        address1: constr(strip_whitespace=True, min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'/#&,.:]+$"),
        city: constr(strip_whitespace=True, min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'.()]+$"),
        state: constr(strip_whitespace=True, min_length=2, max_length=3, to_upper=True),
        country: constr(strip_whitespace=True, min_length=2, max_length=2, to_upper=True),
    ) -> BusinessMatchesEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.BusinessMatchesEndpoint` object used to interact with
        the Yelp Business Matches REST endpoint.

        :param name: The name of the business. Maximum length is 64; only digits, letters, spaces, and
            ``!#$%&+,­./:?@'`` are allowed.
        :type name: str
        :param address1: The first line of the business’s address. Maximum length is 64; only digits, letters, spaces,
            and ``­’/#&,.:`` are allowed. The empty string "" is allowed; this will specifically match certain service
            businesses that have no street address.
        :type address1: str
        :param city: The city of the business. Maximum length is 64; only digits, letters, spaces, and ``­’.()`` are
            allowed.
        :type city: str
        :param state: The ISO 3166-2 (with a few exceptions) state code of this business.
        :type state: str
        :param country: The ISO 3166-1 alpha-2 country code of this business.
        :type country: str
        :return: An endpoint wrapper for the Yelp Business Match REST endpoint.
        :rtype: BusinessMatchEndpoint
        """

        return BusinessMatchesEndpoint(
            name=name,
            address1=address1,
            city=city,
            state=state,
            country=country,
        )

    @staticmethod
    def business_search(
        location: Optional[constr(strip_whitespace=True, min_length=1)] = None,
        latitude: Optional[confloat(ge=-90.0, le=90.0)] = None,
        longitude: Optional[confloat(ge=-180.0, le=180.0)] = None,
    ) -> BusinessSearchEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.BusinessSearchEndpoint` object used to interact with the
        Yelp Business Search REST endpoint.

        :param location: This string indicates the geographic area to be used when searching for businesses.
            Examples: ``New York City``, ``NYC``, ``350 5th Ave, New York, NY 10118``. (Required if either ``latitude``
            or ``longitude`` is not provided.)
        :type location: str
        :param latitude: Latitude of the location you want to search nearby. (Required if ``location`` is not provided.)
        :type latitude: float
        :param longitude: Longitude of the location you want to search nearby. (Required if ``location`` is not
            provided.)
        :type longitude: float
        :return: An endpoint wrapper for the Yelp Business Search REST endpoint.
        :rtype: BusinessSearchEndpoint
        """

        if location:
            return BusinessSearchEndpoint(location=location)
        elif latitude and longitude:
            return BusinessSearchEndpoint(latitude=latitude, longitude=longitude)
        else:
            raise ValueError("Missing required argument(s).")

    @staticmethod
    def phone_search(phone: constr(strip_whitespace=True, min_length=12, regex=r"^\+\d+")) -> PhoneSearchEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.PhoneSearchEndpoint` object used to interact with the
        Yelp Phone Search REST endpoint.

        :param phone: Phone number of the business you want to search for. It must start with + and include the country
            code, like ``+14159083801``.
        :type phone: str
        :return: An endpoint wrapper for the Yelp Phone Search REST endpoint.
        :rtype: PhoneSearchEndpoint
        """

        return PhoneSearchEndpoint(phone=phone)

    @staticmethod
    def reviews(business_id: constr(strip_whitespace=True, min_length=1, regex=r"^[A-Za-z0-9\-]+$")) -> ReviewsEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.ReviewsEndpoint` object used to interact with the Yelp
        Reviews REST endpoint.

        :param business_id: Unique Yelp ID of the business to query for.
        :type business_id: str
        :return: An endpoint wrapper for the Yelp Reviews REST endpoint.
        :rtype: ReviewsEndpoint
        """
        return ReviewsEndpoint(business_id=business_id)

    @staticmethod
    def transaction_search(
        location: Optional[constr(min_length=1, strip_whitespace=True)] = None,
        latitude: Optional[confloat(ge=-90.0, le=90.0)] = None,
        longitude: Optional[confloat(ge=-180.0, le=180.0)] = None,
    ) -> TransactionSearchEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.TransactionSearchEndpoint` object used to interact with
        the Yelp Transaction Search REST endpoint.

        :param location: This string indicates the geographic area to be used when searching for businesses.
            Examples: ``New York City``, ``NYC``, ``350 5th Ave, New York, NY 10118``. (Required if either ``latitude``
            or ``longitude`` is not provided.)
        :type location: str
        :param latitude: Latitude of the location you want to search nearby. (Required if ``location`` is not provided.)
        :type latitude: float
        :param longitude: Longitude of the location you want to search nearby. (Required if ``location`` is not
            provided.)
        :type longitude: float
        :return: An endpoint wrapper for the Yelp Transaction Search REST endpoint.
        :rtype: TransactionSearchEndpoint
        """

        if location:
            return TransactionSearchEndpoint(location=location)
        elif latitude and longitude:
            return TransactionSearchEndpoint(latitude=latitude, longitude=longitude)
        else:
            raise ValueError("Missing required argument(s).")

    @staticmethod
    def autocomplete(
        text: constr(strip_whitespace=True, min_length=1),
        latitude: Optional[confloat(ge=-90.0, le=90.0)] = None,
        longitude: Optional[confloat(ge=-180.0, le=180.0)] = None,
    ) -> AutocompleteEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.AutocompleteEndpoint` object used to interact with the
        Yelp Autocomplete REST endpoint.

        :param text: Required. Text to return autocomplete suggestions for.
        :type text: str
        :param latitude: Required if want to get autocomplete suggestions for businesses. Latitude of the location to
            look for business autocomplete suggestions.
        :type latitude: float
        :param longitude: Required if want to get autocomplete suggestions for businesses. Longitude of the location to
            look for business autocomplete suggestions.
        :type longitude: float
        :return: An endpoint wrapper for the Yelp Autocomplete REST endpoint.
        :rtype: AutocompleteEndpoint
        """

        if latitude and longitude:
            return AutocompleteEndpoint(text=text, latitude=latitude, longitude=longitude)
        else:
            return AutocompleteEndpoint(text=text)

    @staticmethod
    def event_search() -> EventSearchEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.event.endpoint.EventSearchEndpoint` object used to interact with the Yelp
        Event Search REST endpoint.

        :return: An endpoint wrapper for the Yelp Event Search REST endpoint.
        :rtype: EventSearchEndpoint
        """

        return EventSearchEndpoint()

    @staticmethod
    def event_lookup(event_id: str) -> EventLookupEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.event.endpoint.EventLookupEndpoint` object used to interact with the Yelp
        Event Lookup REST endpoint.

        :param event_id: ID of the Yelp event to query for.
        :type event_id: str
        :return: An endpoint wrapper for the Yelp Event Lookup REST endpoint.
        :rtype: EventLookupEndpoint
        """

        return EventLookupEndpoint(id=event_id)

    @staticmethod
    def featured_event(
        location: Optional[constr(strip_whitespace=True, min_length=1)] = None,
        latitude: Optional[confloat(ge=-90.0, le=90.0)] = None,
        longitude: Optional[confloat(ge=-180.0, le=180.0)] = None,
    ) -> FeaturedEventEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.event.endpoint.FeaturedEventEndpoint` object used to interact with the
        Yelp Featured Event REST endpoint.

        :param location: Required, if latitude and longitude not provided. Specifies the combination of "address,
            neighborhood, city, state or zip, optional country" to be used while searching for events.
        :type location: str
        :param latitude: Required, if location not provided. Latitude of the location to search from.
        :type latitude: float
        :param longitude: Required, if location not provided. Longitude of the location to search from.
        :type longitude: float
        :return: An endpoint wrapper for the Yelp Featured Event REST endpoint.
        :rtype: FeaturedEventEndpoint
        """

        if location:
            return FeaturedEventEndpoint(location=location)
        elif latitude and longitude:
            return FeaturedEventEndpoint(latitude=latitude, longitude=longitude)
        else:
            raise ValueError("Missing required argument(s).")

    @staticmethod
    def category_details(alias: constr(strip_whitespace=True, min_length=1)) -> CategoryDetailsEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.category.endpoint.CategoryDetailsEndpoint` object used to interact with
        the Yelp Category Details REST endpoint.

        :param alias: The alias of the category.
        :type alias: str
        :return: An endpoint wrapper for the Yelp Category Details REST endpoint.
        :rtype: CategoryDetailsEndpoint
        """

        return CategoryDetailsEndpoint(alias=alias)

    @staticmethod
    def all_categories() -> AllCategoriesEndpoint:
        """
        This endpoint returns all Yelp business categories across all locales by default.

        :return: An endpoint wrapper for the Yelp All Categories REST endpoint.
        :rtype: Categories
        """

        return AllCategoriesEndpoint()
