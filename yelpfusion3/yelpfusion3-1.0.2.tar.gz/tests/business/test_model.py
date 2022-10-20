from datetime import datetime
from typing import Dict, List, Union

import pytest

from yelpfusion3.business.model import (
    Autocomplete,
    Business,
    BusinessDetails,
    BusinessSearch,
    DetailedHours,
    PhoneSearch,
    Review,
    Reviews,
    SpecialHours,
)


class TestBusiness:
    test_data: dict = {
        "id": "E8RJkjfdcwgtyoPMjQ_Olg",
        "alias": "four-barrel-coffee-san-francisco",
        "name": "Four Barrel Coffee",
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/e_urruIKpneV8yAXkAK9RA/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
        "review_count": 2154,
        "categories": [{"alias": "coffee", "title": "Coffee & Tea"}],
        "rating": 4.0,
        "coordinates": {"latitude": 37.7670169511878, "longitude": -122.42184275},
        "transactions": ["delivery"],
        "price": "$$",
        "location": {
            "address1": "375 Valencia St",
            "address2": "",
            "address3": "",
            "city": "San Francisco",
            "zip_code": "94103",
            "country": "US",
            "state": "CA",
            "display_address": ["375 Valencia St", "San Francisco, CA 94103"],
        },
        "phone": "+14158964289",
        "display_phone": "(415) 896-4289",
        "distance": 1452.8696502343696,
    }

    def test_deserialization(self) -> None:
        business: Business = Business(**self.test_data)

        assert business.id == "E8RJkjfdcwgtyoPMjQ_Olg"
        assert business.alias == "four-barrel-coffee-san-francisco"
        assert business.name == "Four Barrel Coffee"
        assert business.image_url == "https://s3-media1.fl.yelpcdn.com/bphoto/e_urruIKpneV8yAXkAK9RA/o.jpg"
        assert not business.is_closed
        assert (
            business.url
            == "https://www.yelp.com/biz/four-barrel-coffee-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA"
        )
        assert business.review_count == 2154
        assert business.categories[0].alias == "coffee"
        assert business.categories[0].title == "Coffee & Tea"
        assert business.rating == 4.0
        assert business.coordinates.latitude == 37.7670169511878
        assert business.coordinates.longitude == -122.42184275
        assert business.transactions == ["delivery"]
        assert business.price == "$$"
        assert business.location.address1 == "375 Valencia St"
        assert not business.location.address2
        assert not business.location.address3
        assert business.location.city == "San Francisco"
        assert business.location.zip_code == "94103"
        assert business.location.country == "US"
        assert business.location.state == "CA"
        assert business.location.display_address[0] == "375 Valencia St"
        assert business.location.display_address[1] == "San Francisco, CA 94103"
        assert business.phone == "+14158964289"
        assert business.display_phone == "(415) 896-4289"
        assert business.distance == 1452.8696502343696

    def test_distance_fails_validation(self) -> None:
        invalid_test_data: dict = self.test_data.copy()
        invalid_test_data["distance"] = -1.0

        with pytest.raises(ValueError):
            Business(**invalid_test_data)

    @pytest.mark.parametrize("rating", [-1.0, 0.1, 5.1, 6.0])
    def test_rating_fails_validation(self, rating: float) -> None:
        invalid_test_data: dict = self.test_data.copy()
        invalid_test_data["rating"] = rating

        with pytest.raises(ValueError):
            Business(**invalid_test_data)

    def test_location_country_fails_validation(self) -> None:
        invalid_test_data: dict = self.test_data.copy()
        invalid_test_data["location"]["country"] = "ZZ"

        with pytest.raises(ValueError):
            Business(**invalid_test_data)


class TestBusinessDetails:
    test_data = {
        "id": "WavvLdfdP6g8aZTtbBQHTw",
        "alias": "gary-danko-san-francisco",
        "name": "Gary Danko",
        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/CPc91bGzKBe95aM5edjhhQ/o.jpg",
        "is_claimed": True,
        "is_closed": False,
        "url": "https://www.yelp.com/biz/gary-danko-san-francisco?adjust_creative=wpr6gw4FnptTrk1CeT8POg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=wpr6gw4FnptTrk1CeT8POg",  # NOQA
        "phone": "+14157492060",
        "display_phone": "(415) 749-2060",
        "review_count": 5296,
        "categories": [
            {"alias": "newamerican", "title": "American (New)"},
            {"alias": "french", "title": "French"},
            {"alias": "wine_bars", "title": "Wine Bars"},
        ],
        "rating": 4.5,
        "location": {
            "address1": "800 N Point St",
            "address2": "",
            "address3": "",
            "city": "San Francisco",
            "zip_code": "94109",
            "country": "US",
            "state": "CA",
            "display_address": ["800 N Point St", "San Francisco, CA 94109"],
            "cross_streets": "",
        },
        "coordinates": {"latitude": 37.80587, "longitude": -122.42058},
        "photos": [
            "https://s3-media2.fl.yelpcdn.com/bphoto/CPc91bGzKBe95aM5edjhhQ/o.jpg",
            "https://s3-media4.fl.yelpcdn.com/bphoto/FmXn6cYO1Mm03UNO5cbOqw/o.jpg",
            "https://s3-media4.fl.yelpcdn.com/bphoto/HZVDyYaghwPl2kVbvHuHjA/o.jpg",
        ],
        "price": "$$$$",
        "hours": [
            {
                "open": [
                    {"is_overnight": False, "start": "1730", "end": "2200", "day": 0},
                    {"is_overnight": False, "start": "1731", "end": "2200", "day": 1},
                    {"is_overnight": False, "start": "1732", "end": "2200", "day": 2},
                    {"is_overnight": False, "start": "1733", "end": "2200", "day": 3},
                    {"is_overnight": False, "start": "1734", "end": "2200", "day": 4},
                    {"is_overnight": False, "start": "1735", "end": "2200", "day": 5},
                    {"is_overnight": False, "start": "1736", "end": "2200", "day": 6},
                ],
                "hours_type": "REGULAR",
                "is_open_now": False,
            }
        ],
        "transactions": [],
        "special_hours": [
            {
                "date": "2019-02-07",
                "is_closed": None,
                "start": "1600",
                "end": "2000",
                "is_overnight": False,
            }
        ],
    }

    def test_deserialization(self) -> None:
        business_details: BusinessDetails = BusinessDetails(**self.test_data)

        assert business_details.hours[0].open[0].start == "1730"

    @pytest.mark.parametrize("rating", [-1.0, 0.1, 5.1, 6.0])
    def test_rating_fails_validation(self, rating: float) -> None:
        invalid_test_data: Dict[str, object] = self.test_data.copy()
        invalid_test_data["rating"] = rating

        with pytest.raises(ValueError):
            BusinessDetails(**invalid_test_data)


class TestBusinessSearch:
    test_data = {
        "businesses": [
            {
                "id": "DaOQgNk4LjN2gbvYrLQGvA",
                "alias": "rise-and-grind-coffee-and-tea-san-francisco-6",
                "name": "Rise & Grind Coffee and Tea",
                "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/P3nSiVthgTWO4zZJjMsdkg/o.jpg",
                "is_closed": False,
                "url": "https://www.yelp.com/biz/rise-and-grind-coffee-and-tea-san-francisco-6?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
                "review_count": 373,
                "categories": [{"alias": "coffee", "title": "Coffee & Tea"}],
                "rating": 4.5,
                "coordinates": {"latitude": 37.7737156, "longitude": -122.4660674},
                "transactions": ["delivery", "pickup"],
                "price": "$$",
                "location": {
                    "address1": "785 8th Ave",
                    "address2": None,
                    "address3": "",
                    "city": "San Francisco",
                    "zip_code": "94118",
                    "country": "US",
                    "state": "CA",
                    "display_address": ["785 8th Ave", "San Francisco, CA 94118"],
                },
                "phone": "+14157801579",
                "display_phone": "(415) 780-1579",
                "distance": 2974.448388088878,
            },
            {
                "id": "-NbDKVqG170J19MqSQ5q_A",
                "alias": "the-mill-san-francisco",
                "name": "The Mill",
                "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/3mYaiweH3tRKTLSLj24hVA/o.jpg",
                "is_closed": False,
                "url": "https://www.yelp.com/biz/the-mill-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
                "review_count": 1283,
                "categories": [
                    {"alias": "coffee", "title": "Coffee & Tea"},
                    {"alias": "bakeries", "title": "Bakeries"},
                    {"alias": "desserts", "title": "Desserts"},
                ],
                "rating": 4.0,
                "coordinates": {
                    "latitude": 37.7764801534107,
                    "longitude": -122.437750024358,
                },
                "transactions": ["delivery"],
                "price": "$$",
                "location": {
                    "address1": "736 Divisadero St",
                    "address2": "",
                    "address3": "",
                    "city": "San Francisco",
                    "zip_code": "94117",
                    "country": "US",
                    "state": "CA",
                    "display_address": ["736 Divisadero St", "San Francisco, CA 94117"],
                },
                "phone": "+14153451953",
                "display_phone": "(415) 345-1953",
                "distance": 1736.2808394903705,
            },
            {
                "id": "lL-3T2fZIP_oCYC-uc074w",
                "alias": "flywheel-coffee-roasters-san-francisco",
                "name": "Flywheel Coffee Roasters",
                "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/hNFgdE_XYbZdH_ZcesWurg/o.jpg",
                "is_closed": False,
                "url": "https://www.yelp.com/biz/flywheel-coffee-roasters-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
                "review_count": 539,
                "categories": [
                    {"alias": "coffee", "title": "Coffee & Tea"},
                    {"alias": "coffeeroasteries", "title": "Coffee Roasteries"},
                ],
                "rating": 4.0,
                "coordinates": {
                    "latitude": 37.769681598837636,
                    "longitude": -122.45350500151754,
                },
                "transactions": ["delivery"],
                "price": "$$",
                "location": {
                    "address1": "672 Stanyan St",
                    "address2": "",
                    "address3": "",
                    "city": "San Francisco",
                    "zip_code": "94117",
                    "country": "US",
                    "state": "CA",
                    "display_address": ["672 Stanyan St", "San Francisco, CA 94117"],
                },
                "phone": "+14156824023",
                "display_phone": "(415) 682-4023",
                "distance": 1789.386184315149,
            },
        ],
        "total": 5900,
        "region": {"center": {"longitude": -122.43644714355469, "latitude": 37.76089938976322}},
    }

    def test_deserialization(self) -> None:
        business_search: BusinessSearch = BusinessSearch(**self.test_data)

        assert business_search.total == 5900
        assert business_search.region.center.longitude == -122.43644714355469
        assert business_search.region.center.latitude == 37.76089938976322

        assert business_search.businesses[0].id == "DaOQgNk4LjN2gbvYrLQGvA"
        assert business_search.businesses[0].alias == "rise-and-grind-coffee-and-tea-san-francisco-6"
        assert business_search.businesses[0].review_count == 373
        assert business_search.businesses[0].display_phone == "(415) 780-1579"
        assert business_search.businesses[0].distance == 2974.448388088878


class TestDetailedHours:
    test_data: List[dict] = [
        {
            "open": [
                {"is_overnight": False, "start": "1730", "end": "2200", "day": 0},
                {"is_overnight": False, "start": "1731", "end": "2200", "day": 1},
                {"is_overnight": False, "start": "1732", "end": "2200", "day": 2},
                {"is_overnight": False, "start": "1733", "end": "2200", "day": 3},
                {"is_overnight": False, "start": "1734", "end": "2200", "day": 4},
                {"is_overnight": False, "start": "1735", "end": "2200", "day": 5},
                {"is_overnight": False, "start": "1736", "end": "2200", "day": 6},
            ],
            "hours_type": "REGULAR",
            "is_open_now": False,
        }
    ]

    def test_deserialization(self) -> None:
        test_detailed_hours: Dict[str, Union[bool, int, str]] = self.test_data[0]["open"][0].copy()
        detailed_hours: DetailedHours = DetailedHours(**test_detailed_hours)

        assert not detailed_hours.is_overnight
        assert detailed_hours.start == "1730"
        assert detailed_hours.end == "2200"
        assert detailed_hours.day == 0

    @pytest.mark.parametrize("start", ["-1", "2401"])
    def test_start_fails_validation(self, start: str) -> None:
        test_detailed_hours: Dict[str, Union[bool, int, str]] = self.test_data[0]["open"][0].copy()
        test_detailed_hours["start"] = start

        with pytest.raises(ValueError):
            DetailedHours(**test_detailed_hours)

    @pytest.mark.parametrize("end", ["-1", "2401"])
    def test_end_fails_validation(self, end: str) -> None:
        test_detailed_hours: Dict[str, Union[bool, int, str]] = self.test_data[0]["open"][0].copy()
        test_detailed_hours["end"] = end

        with pytest.raises(ValueError):
            DetailedHours(**test_detailed_hours)


class TestPhoneSearch:
    test_data = {
        "businesses": [
            {
                "id": "WavvLdfdP6g8aZTtbBQHTw",
                "alias": "gary-danko-san-francisco",
                "name": "Gary Danko",
                "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/eyYUz3Xl7NtcJeN7x7SQwg/o.jpg",
                "is_closed": False,
                "url": "https://www.yelp.com/biz/gary-danko-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_phone_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
                "review_count": 5733,
                "categories": [
                    {"alias": "newamerican", "title": "American (New)"},
                    {"alias": "french", "title": "French"},
                    {"alias": "wine_bars", "title": "Wine Bars"},
                ],
                "rating": 4.5,
                "coordinates": {"latitude": 37.80587, "longitude": -122.42058},
                "transactions": [],
                "price": "$$$$",
                "location": {
                    "address1": "800 N Point St",
                    "address2": "",
                    "address3": "",
                    "city": "San Francisco",
                    "zip_code": "94109",
                    "country": "US",
                    "state": "CA",
                    "display_address": ["800 N Point St", "San Francisco, CA 94109"],
                },
                "phone": "+14157492060",
                "display_phone": "(415) 749-2060",
            }
        ],
        "total": 1,
    }

    def test_deserialization(self) -> None:
        phone_search: PhoneSearch = PhoneSearch(**self.test_data)

        assert phone_search.total == 1

        assert phone_search.businesses[0].id == "WavvLdfdP6g8aZTtbBQHTw"
        assert phone_search.businesses[0].alias == "gary-danko-san-francisco"
        assert phone_search.businesses[0].name == "Gary Danko"
        assert phone_search.businesses[0].review_count == 5733
        assert phone_search.businesses[0].rating == 4.5
        assert phone_search.businesses[0].coordinates.latitude == 37.80587
        assert phone_search.businesses[0].coordinates.longitude == -122.42058


class TestReview:
    test_data = {
        "id": "xAG4O7l-t1ubbwVAlPnDKg",
        "rating": 5,
        "user": {
            "id": "W8UK02IDdRS2GL_66fuq6w",
            "profile_url": "https://www.yelp.com/user_details?userid=W8UK02IDdRS2GL_66fuq6w",
            "image_url": "https://s3-media3.fl.yelpcdn.com/photo/iwoAD12zkONZxJ94ChAaMg/o.jpg",
            "name": "Ella A.",
        },
        "text": "Went back again to this place since the last time i visited the bay area 5 months ago, and nothing has changed. Still the sketchy Mission, Still the cashier...",
        "time_created": "2016-08-29 00:41:13",
        "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=hp8hAJ-AnlpqxCCu7kyCWA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
    }

    def test_deserialization(self) -> None:
        review: Review = Review(**self.test_data)

        assert review.id == "xAG4O7l-t1ubbwVAlPnDKg"
        assert review.rating == 5
        assert (
            review.text
            == "Went back again to this place since the last time i visited the bay area 5 months ago, and nothing has changed. Still the sketchy Mission, Still the cashier..."
        )
        assert review.time_created == datetime(2016, 8, 29, 0, 41, 13)
        assert (
            review.url
            == "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=hp8hAJ-AnlpqxCCu7kyCWA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w"
        )
        assert review.user.id == "W8UK02IDdRS2GL_66fuq6w"
        assert review.user.profile_url == "https://www.yelp.com/user_details?userid=W8UK02IDdRS2GL_66fuq6w"
        assert review.user.image_url == "https://s3-media3.fl.yelpcdn.com/photo/iwoAD12zkONZxJ94ChAaMg/o.jpg"
        assert review.user.name == "Ella A."


class TestReviews:
    test_data = {
        "reviews": [
            {
                "id": "xAG4O7l-t1ubbwVAlPnDKg",
                "rating": 5,
                "user": {
                    "id": "W8UK02IDdRS2GL_66fuq6w",
                    "profile_url": "https://www.yelp.com/user_details?userid=W8UK02IDdRS2GL_66fuq6w",
                    "image_url": "https://s3-media3.fl.yelpcdn.com/photo/iwoAD12zkONZxJ94ChAaMg/o.jpg",
                    "name": "Ella A.",
                },
                "text": "Went back again to this place since the last time i visited the bay area 5 months ago, and nothing has changed. Still the sketchy Mission, Still the cashier...",
                "time_created": "2016-08-29 00:41:13",
                "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=hp8hAJ-AnlpqxCCu7kyCWA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
            },
            {
                "id": "1JNmYjJXr9ZbsfZUAgkeXQ",
                "rating": 4,
                "user": {
                    "id": "rk-MwIUejOj6LWFkBwZ98Q",
                    "profile_url": "https://www.yelp.com/user_details?userid=rk-MwIUejOj6LWFkBwZ98Q",
                    "image_url": None,
                    "name": "Yanni L.",
                },
                "text": 'The "restaurant" is inside a small deli so there is no sit down area. Just grab and go.\n\nInside, they sell individually packaged ingredients so that you can...',
                "time_created": "2016-09-28 08:55:29",
                "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=fj87uymFDJbq0Cy5hXTHIA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
            },
            {
                "id": "SIoiwwVRH6R2s2ipFfs4Ww",
                "rating": 4,
                "user": {
                    "id": "rpOyqD_893cqmDAtJLbdog",
                    "profile_url": "https://www.yelp.com/user_details?userid=rpOyqD_893cqmDAtJLbdog",
                    "image_url": None,
                    "name": "Suavecito M.",
                },
                "text": "Dear Mission District,\n\nI miss you and your many delicious late night food establishments and vibrant atmosphere.  I miss the way you sound and smell on a...",
                "time_created": "2016-08-10 07:56:44",
                "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=m_tnQox9jqWeIrU87sN-IQ&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
            },
        ],
        "total": 3,
        "possible_languages": ["en"],
    }

    def test_deserialization(self) -> None:
        reviews: Reviews = Reviews(**self.test_data)

        assert reviews.total == 3
        assert reviews.possible_languages == ["en"]
        assert reviews.reviews[1].id == "1JNmYjJXr9ZbsfZUAgkeXQ"
        assert reviews.reviews[1].rating == 4
        assert (
            reviews.reviews[1].text
            == 'The "restaurant" is inside a small deli so there is no sit down area. Just grab and go.\n\nInside, they sell individually packaged ingredients so that you can...'
        )
        assert reviews.reviews[1].time_created == datetime(2016, 9, 28, 8, 55, 29)
        assert (
            reviews.reviews[1].url
            == "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=fj87uymFDJbq0Cy5hXTHIA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w"
        )


class TestSpecialHours:
    test_data: Dict[str, Union[bool, None, str]] = {
        "date": "2019-02-07",
        "is_closed": None,
        "start": "1600",
        "end": "2000",
        "is_overnight": False,
    }

    def test_deserialize(self) -> None:
        special_hours = SpecialHours(**self.test_data)

        assert special_hours.date == "2019-02-07"
        assert not special_hours.is_closed
        assert special_hours.start == "1600"
        assert special_hours.end == "2000"
        assert not special_hours.is_overnight

    @pytest.mark.parametrize("start", ["-1", "2401"])
    def test_start_fails_validation(self, start: str) -> None:
        test_special_hours: Dict[str, Union[bool, None, str]] = self.test_data.copy()
        test_special_hours["start"] = start

        with pytest.raises(ValueError):
            SpecialHours(**test_special_hours)

    @pytest.mark.parametrize("end", ["-1", "2401"])
    def test_end_fails_validation(self, end: str) -> None:
        test_special_hours: Dict[str, Union[bool, None, str]] = self.test_data.copy()
        test_special_hours["end"] = end

        with pytest.raises(ValueError):
            SpecialHours(**test_special_hours)


class TestAutocomplete:
    test_data: Dict = {
        "terms": [{"text": "Delivery"}],
        "businesses": [
            {"name": "Delfina", "id": "YqvoyaNvtoC8N5dA8pD2JA"},
            {"name": "Pizzeria Delfina", "id": "bai6umLcCNy9cXql0Js2RQ"},
        ],
        "categories": [
            {"alias": "delis", "title": "Delis"},
            {"alias": "fooddeliveryservices", "title": "Food Delivery Services"},
            {"alias": "couriers", "title": "Couriers & Delivery Services"},
        ],
    }

    def test_deserialize(self) -> None:
        autocomplete = Autocomplete(**self.test_data)

        assert len(autocomplete.terms) == 1
        assert autocomplete.terms[0].text == "Delivery"
        assert len(autocomplete.businesses) == 2
        assert autocomplete.businesses[0].name == "Delfina"
        assert autocomplete.businesses[0].id == "YqvoyaNvtoC8N5dA8pD2JA"
        assert autocomplete.businesses[1].name == "Pizzeria Delfina"
        assert autocomplete.businesses[1].id == "bai6umLcCNy9cXql0Js2RQ"
        assert len(autocomplete.categories) == 3
        assert autocomplete.categories[0].alias == "delis"
        assert autocomplete.categories[0].title == "Delis"
        assert autocomplete.categories[1].alias == "fooddeliveryservices"
        assert autocomplete.categories[1].title == "Food Delivery Services"
        assert autocomplete.categories[2].alias == "couriers"
        assert autocomplete.categories[2].title == "Couriers & Delivery Services"
