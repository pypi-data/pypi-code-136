import pytest

from yelpfusion3.event.endpoint import EventLookupEndpoint, EventSearchEndpoint, FeaturedEventEndpoint


class TestEventSearchEndpoint:
    def test_url(self) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        assert event_search_endpoint.url == "https://api.yelp.com/v3/events"

    @pytest.mark.parametrize(
        "categories",
        [
            "music",
            "food-and-drink",
            "visual-arts,food-and-drink,festivals-fairs,kids-family",
            "sports-active-life,nightlife",
        ],
    )
    def test_valid_categories(self, categories: str) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        #  Model validation will raise an error if "categories" is malformed or contains invalid categories.
        event_search_endpoint.categories = categories

    @pytest.mark.parametrize(
        "categories",
        [
            "not-supported",
            "music,not-supported",
            "visual-arts,food-and-drink,not-supported,festivals-fairs,kids-family",
        ],
    )
    def test_invalid_categories(self, categories: str) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        with pytest.raises(ValueError):
            event_search_endpoint.categories = categories

    def test_radius_too_large(self) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        with pytest.raises(ValueError):
            event_search_endpoint.radius = 40001


class TestEventLookupEndpoint:
    def test_url(self) -> None:
        event_lookup_endpoint: EventLookupEndpoint = EventLookupEndpoint(id="oakland-saucy-oakland-restaurant-pop-up")

        assert event_lookup_endpoint.url == "https://api.yelp.com/v3/events/oakland-saucy-oakland-restaurant-pop-up"

    def test_url_locale(self) -> None:
        event_lookup_endpoint: EventLookupEndpoint = EventLookupEndpoint(
            id="oakland-saucy-oakland-restaurant-pop-up", locale="fr_FR"
        )

        assert (
            event_lookup_endpoint.url
            == "https://api.yelp.com/v3/events/oakland-saucy-oakland-restaurant-pop-up?locale=fr_FR"
        )


class TestFeaturedEventEndpoint:
    def test_url_location(self) -> None:
        featured_event_endpoint: FeaturedEventEndpoint = FeaturedEventEndpoint(location="San Francisco, CA")

        assert featured_event_endpoint.url == "https://api.yelp.com/v3/events/featured?location=San%20Francisco%2C%20CA"

    def test_url_locale(self) -> None:
        featured_event_endpoint: FeaturedEventEndpoint = FeaturedEventEndpoint(
            location="San Francisco, CA", locale="fr_FR"
        )

        assert (
            featured_event_endpoint.url
            == "https://api.yelp.com/v3/events/featured?locale=fr_FR&location=San%20Francisco%2C%20CA"
        )

    def test_url_latitude_longitude(self) -> None:
        featured_event_endpoint: FeaturedEventEndpoint = FeaturedEventEndpoint(
            latitude="37.7726402", longitude="-122.4099154"
        )

        assert (
            featured_event_endpoint.url
            == "https://api.yelp.com/v3/events/featured?latitude=37.7726402&longitude=-122.4099154"
        )
