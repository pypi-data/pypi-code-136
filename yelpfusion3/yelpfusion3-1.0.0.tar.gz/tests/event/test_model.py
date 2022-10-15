from typing import Dict

import pytest

from yelpfusion3.event.model import Event, EventSearch, SupportedCategories


class TestSupportedCategories:
    @pytest.mark.parametrize(
        "category",
        [
            "music",
            "visual-arts",
            "performing-arts",
            "film",
            "lectures-books",
            "fashion",
            "food-and-drink",
            "festivals-fairs",
            "charities",
            "sports-active-life",
            "nightlife",
            "kids-family",
            "other",
        ],
    )
    def test_contains(self, category: str) -> None:
        assert SupportedCategories.contains(category)

    def test_contains_fails(self) -> None:
        assert not SupportedCategories.contains("not-supported")


class TestEvent:
    test_data: Dict = {
        "attending_count": 926,
        "category": "nightlife",
        "cost": None,
        "cost_max": None,
        "description": 'Come join the Yelp Team and all of Yelpland in celebrating our 3rd Annual Yelp Holiday Party! Just some of the "funny, useful and cool" thrills will include...',
        "event_site_url": "https://www.yelp.com/events/san-francisco-peace-love-and-yelp-our-3rd-annual-holiday-party?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_event_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
        "id": "san-francisco-peace-love-and-yelp-our-3rd-annual-holiday-party",
        "image_url": "https://s3-media2.fl.yelpcdn.com/ephoto/5Y1VFZBPHF9IIOO_IIpnhQ/o.jpg",
        "interested_count": 73,
        "is_canceled": False,
        "is_free": True,
        "is_official": False,
        "latitude": 37.78574,
        "longitude": -122.40255,
        "name": "Peace, Love & Yelp: Our 3rd Annual Holiday Party!",
        "tickets_url": "",
        "time_end": "2007-12-05T23:00:00-08:00",
        "time_start": "2007-12-05T20:30:00-08:00",
        "location": {
            "address1": "701 Mission St",
            "address2": "",
            "address3": "",
            "city": "San Francisco",
            "zip_code": "94103",
            "country": "US",
            "state": "CA",
            "display_address": ["701 Mission St", "San Francisco, CA 94103"],
            "cross_streets": "Opera Aly & 3rd St",
        },
        "business_id": "yerba-buena-center-for-the-arts-san-francisco",
    }

    def test_deserialization(self) -> None:
        event: Event = Event(**self.test_data)

        assert event.attending_count == 926
        assert event.category == "nightlife"
        assert not event.cost
        assert not event.cost_max
        assert (
            event.description
            == 'Come join the Yelp Team and all of Yelpland in celebrating our 3rd Annual Yelp Holiday Party! Just some of the "funny, useful and cool" thrills will include...'
        )
        assert event.id == "san-francisco-peace-love-and-yelp-our-3rd-annual-holiday-party"
        assert event.interested_count == 73
        assert not event.is_canceled
        assert event.is_free
        assert not event.is_official
        assert event.latitude == 37.78574
        assert event.longitude == -122.40255
        assert event.name == "Peace, Love & Yelp: Our 3rd Annual Holiday Party!"
        assert event.location.address1 == "701 Mission St"
        assert event.location.city == "San Francisco"
        assert event.location.zip_code == "94103"
        assert event.location.country == "US"
        assert event.location.state == "CA"
        assert event.location.cross_streets == "Opera Aly & 3rd St"
        assert event.business_id == "yerba-buena-center-for-the-arts-san-francisco"


class TestEventSearch:
    test_data: Dict = {
        "total": 1,
        "events": [
            {
                "attending_count": 926,
                "category": "nightlife",
                "cost": None,
                "cost_max": None,
                "description": 'Come join the Yelp Team and all of Yelpland in celebrating our 3rd Annual Yelp Holiday Party! Just some of the "funny, useful and cool" thrills will include...',
                "event_site_url": "https://www.yelp.com/events/san-francisco-peace-love-and-yelp-our-3rd-annual-holiday-party?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_event_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
                "id": "san-francisco-peace-love-and-yelp-our-3rd-annual-holiday-party",
                "image_url": "https://s3-media2.fl.yelpcdn.com/ephoto/5Y1VFZBPHF9IIOO_IIpnhQ/o.jpg",
                "interested_count": 73,
                "is_canceled": False,
                "is_free": True,
                "is_official": False,
                "latitude": 37.78574,
                "longitude": -122.40255,
                "name": "Peace, Love & Yelp: Our 3rd Annual Holiday Party!",
                "tickets_url": "",
                "time_end": "2007-12-05T23:00:00-08:00",
                "time_start": "2007-12-05T20:30:00-08:00",
                "location": {
                    "address1": "701 Mission St",
                    "address2": "",
                    "address3": "",
                    "city": "San Francisco",
                    "zip_code": "94103",
                    "country": "US",
                    "state": "CA",
                    "display_address": ["701 Mission St", "San Francisco, CA 94103"],
                    "cross_streets": "Opera Aly & 3rd St",
                },
                "business_id": "yerba-buena-center-for-the-arts-san-francisco",
            }
        ],
    }

    def test_deserialization(self) -> None:
        event_search: EventSearch = EventSearch(**self.test_data)

        assert event_search.total == 1
        assert len(event_search.events) == 1
        assert event_search.events[0].attending_count == 926
        assert event_search.events[0].category == "nightlife"
        assert not event_search.events[0].cost
        assert not event_search.events[0].cost_max
        assert (
            event_search.events[0].description
            == 'Come join the Yelp Team and all of Yelpland in celebrating our 3rd Annual Yelp Holiday Party! Just some of the "funny, useful and cool" thrills will include...'
        )
        assert event_search.events[0].id == "san-francisco-peace-love-and-yelp-our-3rd-annual-holiday-party"
        assert event_search.events[0].interested_count == 73
        assert not event_search.events[0].is_canceled
        assert event_search.events[0].is_free
        assert not event_search.events[0].is_official
        assert event_search.events[0].latitude == 37.78574
        assert event_search.events[0].longitude == -122.40255
        assert event_search.events[0].name == "Peace, Love & Yelp: Our 3rd Annual Holiday Party!"
        assert event_search.events[0].location.address1 == "701 Mission St"
        assert event_search.events[0].location.city == "San Francisco"
        assert event_search.events[0].location.zip_code == "94103"
        assert event_search.events[0].location.country == "US"
        assert event_search.events[0].location.state == "CA"
        assert event_search.events[0].location.cross_streets == "Opera Aly & 3rd St"
        assert event_search.events[0].business_id == "yerba-buena-center-for-the-arts-san-francisco"
