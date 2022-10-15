from datetime import datetime
from typing import List, Literal, Optional

from pydantic import HttpUrl, NonNegativeInt, confloat, constr, validator

from yelpfusion3.model import Location, Model


class Category(Model):
    """
    Category title and alias pairs associated with this business.
    """

    alias: str
    """
    Alias of a category, when searching for business in certain categories, use alias rather than the title.
    """

    title: str
    """
    Title of a category for display purpose.
    """


class Coordinates(Model):
    """
    The coordinates of this business.
    """

    latitude: confloat(ge=-90.0, le=90.0)
    """
    The latitude of this business.
    """

    longitude: confloat(ge=-180.0, le=180.0)
    """
    The longitude of this business.
    """


class Business(Model):
    """
    Details for a business found with a business search.
    """

    categories: List[Category]
    """
    A list of category title and alias pairs associated with this business.
    """

    coordinates: Optional[Coordinates] = None
    """
    The coordinates of this business.
    """

    display_phone: str
    """
    Phone number of the business formatted nicely to be displayed to users. The format is the standard phone number
    format for the business's country.
    """

    distance: Optional[float] = None
    """
    Distance in meters from the search location. This returns meters regardless of the locale.
    """

    id: constr(min_length=1)
    """
    Unique Yelp ID of this business. Example: ``4kMBvIEWPxWkWKFN__8SxQ``
    """

    alias: str
    """
    Unique Yelp alias of this business. Can contain unicode characters. Example: ``yelp-san-francisco``.
    """

    image_url: Optional[HttpUrl] = None
    """
    URL of photo for this business.
    """

    is_closed: bool
    """
    Whether business has been (permanently) closed
    """

    location: Location
    """
    The location of this business, including address, city, state, zip code and country.
    """

    name: str
    """
    Name of this business.
    """

    phone: Optional[str] = None
    """
    Phone number of the business.
    """

    price: Optional[Literal["$", "$$", "$$$", "$$$$"]] = None
    """
    Price level of the business. Value is one of ``$``, ``$$``, ``$$$`` and ``$$$$``.
    """

    rating: confloat(ge=0.0, le=5.0)
    """
    Rating for this business (value ranges from 1, 1.5, ... 4.5, 5).
    """

    review_count: NonNegativeInt
    """
    Number of reviews for this business.
    """

    url: HttpUrl
    """
    URL for business page on Yelp.
    """

    transactions: List[Literal["pickup", "delivery", "restaurant_reservation"]]
    """
    A list of Yelp transactions that the business is registered for. Current supported values are ``pickup``,
    ``delivery``, and ``restaurant_reservation``.
    """

    @validator("distance")
    def _check_distance(cls, v: float) -> float:
        """
        Checks that ``distance`` is non-negative.

        :param v: Distance in meters from the search location.
        :type v: float
        :raise ValueError: If ``v`` is a negative float.
        :return: ``v`` if it's non-negative.
        :rtype: float
        """
        if v <= 0.0:
            raise ValueError("Cannot have a negative distance.")
        return v

    @validator("rating")
    def _check_rating(cls, v: float) -> float:
        """
        Checks that the ``rating`` value is within the range of 1, 1.5, ... 4.5, 5.

        :param v: Rating for the business.
        :type v: float
        :raise ValueError: If ``v`` not in the range of 1, 1.5, ... 4.5, 5.
        :return: ``v`` if it's in the range of 1, 1.5, ... 4.5, 5.
        :rtype: float
        """
        # Avoid using NumPy for this. It's probably overkill here.
        if v in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]:
            return v
        raise ValueError("Invalid rating value.")


class DetailedHours(Model):
    """
    Opening hours of the business for a given day of the week.
    """

    is_overnight: bool = False
    """
    Whether the business opens overnight or not. When this is ``True``, the end time will be lower than the start time.
    """

    start: str
    """
    Start of the opening hours in a day, in 24-hour clock notation, like ``1000`` means 10 AM.
    """

    end: str
    """
    End of the opening hours in a day, in 24-hour clock notation, like ``2130`` means 9:30 PM.
    """

    day: Literal[0, 1, 2, 3, 4, 5, 6]
    """
    From 0 to 6, representing day of the week from Monday to Sunday. Notice that you may get the same day of the week
    more than once if the business has more than one opening time slots.
    """

    @validator("start")
    def _check_start(cls, v: str) -> str:
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid start time.")

    @validator("end")
    def _check_end(cls, v: str) -> str:
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid end time.")


class Hours(Model):
    """
    Opening hours of the business.
    """

    open: List[DetailedHours] = []
    """
    Opening hours of the business.
    """

    hours_type: Literal["REGULAR"]
    """
    The type of the opening hours information. Right now, this is always ``REGULAR``.
    """

    is_open_now: bool
    """
    Whether the business is currently open or not.
    """


class SpecialHours(Model):
    """
    Out of the ordinary hours for the business that apply on certain dates. Whenever these are set, they will override
    the regular business hours found in the ``hours`` field.
    """

    date: str
    """
    An ISO8601 date string representing the date for which these special hours apply.
    """

    is_closed: Optional[bool] = None
    """
    Whether this particular special hour represents a date where the business is closed.
    """

    start: str
    """
    Start of the opening hours in a day, in 24-hour clock notation, like ``1000`` means 10 AM.
    """

    end: str
    """
    End of the opening hours in a day, in 24-hour clock notation, like ``2130`` means 9:30 PM.
    """

    is_overnight: bool
    """
    Whether the special hours time range spans across midnight or not. When this is ``True``, the end time will be lower
    than the start time.
    """

    @validator("date")
    def _check_date(cls, v: str) -> str:
        """
        Validates the date field for proper format. (YY-MM-DD)

        :param v: String representation of a calendar day. ("YY-MM-DD")
        :type v: str
        :raise ValueError: If ``v`` is a malformed string.
        :return: ``v`` if it's a valid date string.
        :rtype: str
        """
        # If the date string is malformed, an exception will be raised so we don't need to.
        datetime.strptime(v, "%Y-%m-%d")
        return v

    @validator("start")
    def _check_start(cls, v: str) -> str:
        """
        Validates the start field for proper format and checks that it properly represents a time. (HHMM)

        :param v: 4-digit string representing the time. (HHMM)
        :type v: str
        :raise ValueError: If ``v`` is outside of the 0000-2400 value range.
        :return: ``v`` if it's a valid time string.
        :rtype: str
        """
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid start time.")

    @validator("end")
    def _check_end(cls, v: str) -> str:
        """
        Validates the end field for proper format and checks that it properly represents a time. (HHMM)

        :param v: 4-digit string representing the time. (HHMM)
        :type v: str
        :raise ValueError: If ``v`` is outside of the 0000-2400 value range.
        :return: ``v`` if it's a valid time string.
        :rtype: str
        """
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid end time.")


class BusinessDetails(Model):
    """
    Detailed information about a business.
    """

    id: constr(min_length=1)
    """
    Unique Yelp ID of this business. Example: ``4kMBvIEWPxWkWKFN__8SxQ``
    """

    alias: str
    """
    Unique Yelp alias of this business. Can contain unicode characters. Example: ``yelp-san-francisco``.
    """

    name: str
    """
    Name of this business.
    """

    image_url: Optional[HttpUrl] = None
    """
    URL of photo for this business.
    """

    is_claimed: bool
    """
    Whether business has been claimed by a business owner.
    """

    is_closed: bool
    """
    Whether business has been (permanently) closed.
    """

    url: HttpUrl
    """
    URL for business page on Yelp.
    """

    phone: str
    """
    Phone number of the business.
    """

    display_phone: str
    """
    Phone number of the business formatted nicely to be displayed to users. The format is the standard phone number
    format for the business's country.
    """

    review_count: NonNegativeInt
    """
    Number of reviews for this business.
    """

    categories: List[Category]
    """
    A list of category title and alias pairs associated with this business.
    """

    rating: confloat(ge=0.0, le=5.0)
    """
    Rating for this business (value ranges from 1, 1.5, ... 4.5, 5).
    """

    location: Location
    """
    The location of this business, including address, city, state, zip code and country.
    """

    coordinates: Optional[Coordinates] = None
    """
    The coordinates of this business.
    """

    photos: Optional[List[HttpUrl]]
    """
    URLs of up to three photos of the business.
    """

    price: Literal["$", "$$", "$$$", "$$$$"]
    """
    Price level of the business. Value is one of ``$``, ``$$``, ``$$$`` and ``$$$$``.
    """

    hours: Optional[List[Hours]] = None
    """
    Opening hours of the business.
    """

    transactions: List[Literal["pickup", "delivery", "restaurant_reservation"]]
    """
    A list of Yelp transactions that the business is registered for. Current supported values are ``pickup``,
    ``delivery``, and ``restaurant_reservation``.
    """

    special_hours: Optional[List[SpecialHours]] = None
    """
    Out of the ordinary hours for the business that apply on certain dates. Whenever these are set, they will override
    the regular business hours found in the ``hours`` field.
    """

    @validator("rating")
    def _check_rating(cls, v: float) -> float:
        """
        Checks that the ``rating`` value is within the range of 1, 1.5, ... 4.5, 5.

        :param v: Rating for the business.
        :type v: float
        :raise ValueError: If ``v`` not in the range of 1, 1.5, ... 4.5, 5.
        :return: ``v`` if it's in the range of 1, 1.5, ... 4.5, 5.
        :rtype: float
        """
        # Avoid using NumPy for this. It's probably overkill here.
        if v in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]:
            return v
        raise ValueError("Invalid rating value.")


class BusinessMatch(Model):
    """
    A Yelp business matching the inputs.
    """

    id: constr(min_length=1)
    """
    Unique Yelp ID of this business. Example: ``4kMBvIEWPxWkWKFN__8SxQ``
    """

    alias: str
    """
    Unique Yelp alias of this business. Can contain unicode characters.
    """

    name: str
    """
    Name of this business.
    """

    location: Location
    """
    Street, city, state, country, etc. Same as the ``location`` in search.
    """

    coordinates: Optional[Coordinates] = None
    """
    Latitude and longitude, if available. Same as the ``coordinates`` in search.
    """

    phone: str
    """
    The business's phone number.
    """


class BusinessMatches(Model):
    """
    List of Yelp business matches.
    """

    businesses: List[BusinessMatch]
    """
    List of Yelp business matches.
    """


class Region(Model):
    """
    Suggested area in a map to display results in.
    """

    center: Coordinates
    """
    Center position of map area.
    """


class BusinessSearch(Model):
    """
    A list of businesses based on a location search.
    """

    total: int
    """
    Total number of business Yelp finds based on the search criteria. Sometimes, the value may exceed 1000. In such
    case, you still can only get up to 1000 businesses using multiple queries and combinations of the "limit" and
    "offset" parameters.
    """

    businesses: List[Business]
    """
    List of business Yelp finds based on the search criteria.
    """

    region: Region
    """
    Suggested area in a map to display results in.
    """


class PhoneSearch(Model):
    """
    A list of businesses based on the provided phone number.
    """

    total: NonNegativeInt
    """
    The total number of business Yelp finds based on the search criteria. Sometimes, the value may exceed 1000. In such
    case, you still can only get up to 1000 businesses.
    """

    businesses: List[Business]
    """
    A list of business Yelp finds based on the search criteria.
    """


class User(Model):
    """
    A user who wrote a review.
    """

    id: constr(min_length=1)
    """
    ID of the user.
    """

    profile_url: HttpUrl
    """
    URL of the user's profile.
    """

    name: constr(min_length=1)
    """
    User screen name (first name and first initial of last name).
    """

    image_url: Optional[HttpUrl] = None
    """
    URL of the user's profile photo.
    """


class Review(Model):
    """
    A review excerpt for a given business.
    """

    id: constr(min_length=1)
    """
    A unique identifier for this review.
    """

    text: str
    """
    Text excerpt of this review.
    """

    url: HttpUrl
    """
    URL of this review.
    """

    rating: Literal[1, 2, 3, 4, 5]
    """
    Rating of this review.
    """

    time_created: datetime
    """
    The time that the review was created in PST.
    """

    user: User
    """
    The user who wrote the review.
    """


class Reviews(Model):
    """
    Review excerpts for a given business.
    """

    total: NonNegativeInt
    """
    The total number of reviews that the business has.
    """

    possible_languages: List[str]
    """
    A list of languages for which the business has at least one review.
    """

    reviews: List[Review]
    """
    A list of up to three reviews of this business.
    """


class TransactionSearch(Model):
    """
    A list of businesses which support food delivery transactions.
    """

    total: NonNegativeInt
    """
    The total number of business Yelp finds based on the search criteria. Sometimes, the value may exceed 1000. In such
    case, you still can only get up to 1000 businesses.
    """

    businesses: List[Business]
    """
    A list of business Yelp finds based on the search criteria.
    """


class Term(Model):
    """
    A term autocomplete suggestion.
    """

    text: constr(min_length=1)
    """
    The text content of the term autocomplete suggestion.
    """


class BusinessSuggestion(Model):
    """
    An autocomplete suggestion for a business.
    """

    name: constr(min_length=1)
    """
    Name of the business.
    """

    id: constr(min_length=1)
    """
    Yelp ID of the business.
    """


class Autocomplete(Model):
    """
    Autocomplete suggestions based on input text.
    """

    terms: List[Term]
    """
    A list of term autocomplete suggestions based on the input text.
    """

    businesses: List[BusinessSuggestion]
    """
    A list of business autocomplete suggestions based on the input text.
    """

    categories: List[Category]
    """
    A list of category autocomplete suggestions based on the input text.
    """
