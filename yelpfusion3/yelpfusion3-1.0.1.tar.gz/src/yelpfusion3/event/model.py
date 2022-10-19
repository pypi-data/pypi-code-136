from typing import Dict, List, Literal, Optional, Union

from pydantic import HttpUrl, NonNegativeInt, confloat, constr, validator

from yelpfusion3.model import Location, Model


class SupportedCategories:
    """
    A collection of categories supported by the Yelp Fusion API's Event Search endpoint.
    See `Supported Categories <https://www.yelp.com/developers/documentation/v3/event_categories_list>`_
    """

    categories: Dict = {
        "Music": "music",
        "Visual Arts": "visual-arts",
        "Performing Arts": "performing-arts",
        "Film": "film",
        "Lectures & Books": "lectures-books",
        "Fashion": "fashion",
        "Food & Drink": "food-and-drink",
        "Festivals & Fairs": "festivals-fairs",
        "Charities": "charities",
        "Sports & Active Life": "sports-active-life",
        "Nightlife": "nightlife",
        "Kids & Family": "kids-family",
        "Other": "other",
    }

    @staticmethod
    def contains(value: constr(strip_whitespace=True, to_lower=True, min_length=1)) -> bool:
        return value in SupportedCategories.categories.values()


class Event(Model):
    """
    Detailed information for a specific Yelp event.
    """

    attending_count: NonNegativeInt
    """
    Number of Yelp users attending this event.
    """

    category: str
    """
    The category of this event.
    """

    cost: Optional[confloat(ge=0.0)] = None
    """
    Cost of attending this event.
    """

    cost_max: Optional[confloat(ge=0.0)] = None
    """
    Maximum cost of attending this event.
    """

    description: str
    """
    Detailed description of this event.
    """

    event_site_url: HttpUrl
    """
    Yelp page of this event.
    """

    id: constr(min_length=1)
    """
    Event id.
    """

    image_url: HttpUrl
    """
    Yelp image URL of this event.
    """

    interested_count: NonNegativeInt
    """
    Number of Yelp users interested in attending this event.
    """

    is_canceled: bool
    """
    Whether this event is canceled.
    """

    is_free: bool
    """
    Whether this event is free.
    """

    is_official: bool
    """
    Whether this event is created by a Yelp community manager.
    """

    latitude: confloat(ge=-90.0, le=90.0)
    """
    Latitude of this event.
    """

    longitude: confloat(ge=-180.0, le=180.0)
    """
    Longitude of this event.
    """

    name: constr(min_length=1)
    """
    Name of this event.
    """

    tickets_url: Optional[Union[HttpUrl, Literal[""]]] = None
    """
    URL to buy tickets for this event.
    """

    time_end: Optional[str]
    """
    Time this event ends. Returns date and time in ISO 8601 format: ``YYYY-MM-DDTHH:MM:SS+HH:MM``.
    """

    time_start: str
    """
    Time this event starts. Returns date and time in ISO 8601 format: ``YYYY-MM-DDTHH:MM:SS+HH:MM``.
    """

    location: Location
    """
    Location object of the event. Includes address, city, state, zip code and country.
    """

    business_id: Optional[constr(min_length=1)] = None
    """
    Yelp Business ID of this event. No ID is returned if a business is not associated with an event.
    """

    @validator("category")
    def _check_category(cls, v: str) -> str:
        """
        Checks that ``v`` is a supported category.

        :param v: Category alias.
        :type v: str
        :raise ValueError: If the category is unsupported.
        :return: The category alias.
        :rtype: str
        """

        # We could have done the validation in the "regex" argument to constr(), but it would be a lot more complicated
        # and not very readable.
        if SupportedCategories.contains(v):
            return v

        raise ValueError("'category' is set to an unsupported category.")


class EventSearch(Model):
    """
    Events returned by :py:class:`~yelpfusion3.event.endpoint.EventSearchEndpoint`.
    """

    total: int
    """
    Total number of events returned based on search criteria.
    """

    events: List[Event]
    """
    List of events found matching search criteria.
    """
