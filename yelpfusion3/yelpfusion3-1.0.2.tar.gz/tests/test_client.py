import os

import pytest

from yelpfusion3.business.endpoint import (
    AutocompleteEndpoint,
    BusinessDetailsEndpoint,
    BusinessMatchesEndpoint,
    BusinessSearchEndpoint,
    PhoneSearchEndpoint,
    ReviewsEndpoint,
    TransactionSearchEndpoint,
)
from yelpfusion3.business.model import (
    Autocomplete,
    BusinessDetails,
    BusinessMatches,
    BusinessSearch,
    PhoneSearch,
    Reviews,
    TransactionSearch,
)
from yelpfusion3.category.endpoint import AllCategoriesEndpoint, CategoryDetailsEndpoint
from yelpfusion3.category.model import Categories, CategoryDetails
from yelpfusion3.client import Client
from yelpfusion3.event.endpoint import EventLookupEndpoint, EventSearchEndpoint, FeaturedEventEndpoint
from yelpfusion3.event.model import Event, EventSearch


@pytest.mark.skipif(condition=not os.getenv("YELP_API_KEY"), reason="API key not configured")
class TestClient:
    def test_business_details(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = Client.business_details(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        business_details: BusinessDetails = business_details_endpoint.get()

        assert business_details.id == "WavvLdfdP6g8aZTtbBQHTw"
        assert business_details.alias == "gary-danko-san-francisco"
        assert business_details.name == "Gary Danko"
        assert business_details.phone == "+14157492060"
        assert business_details.location.address1 == "800 N Point St"
        assert business_details.location.address2 == ""
        assert business_details.location.address3 == ""
        assert business_details.location.city == "San Francisco"
        assert business_details.location.zip_code == "94109"
        assert business_details.location.country == "US"
        assert business_details.location.state == "CA"

    def test_business_matches(self) -> None:
        business_matches_endpoint: BusinessMatchesEndpoint = Client.business_matches(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        business_matches: BusinessMatches = business_matches_endpoint.get()

        assert business_matches.businesses[0].id == "WavvLdfdP6g8aZTtbBQHTw"
        assert business_matches.businesses[0].alias == "gary-danko-san-francisco"
        assert business_matches.businesses[0].name == "Gary Danko"
        assert business_matches.businesses[0].phone == "+14157492060"
        assert business_matches.businesses[0].location.address1 == "800 N Point St"
        assert business_matches.businesses[0].location.address2 == ""
        assert business_matches.businesses[0].location.address3 == ""
        assert business_matches.businesses[0].location.city == "San Francisco"
        assert business_matches.businesses[0].location.zip_code == "94109"
        assert business_matches.businesses[0].location.country == "US"
        assert business_matches.businesses[0].location.state == "CA"

    def test_business_search_by_location(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = Client.business_search(
            location="20488 Stevens Creek Blvd, Cupertino, CA 95014"
        )
        business_search_endpoint.radius = 1609

        business_search: BusinessSearch = business_search_endpoint.get()

        assert business_search.total > 0
        assert all(business.location.city == "Cupertino" for business in business_search.businesses)

    def test_business_search_by_latitude_longitude(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = Client.business_search(
            latitude=37.32238222393683, longitude=-122.0306396484375
        )
        business_search_endpoint.radius = 1609

        business_search: BusinessSearch = business_search_endpoint.get()

        assert business_search.total > 0
        assert all(business.location.city == "Cupertino" for business in business_search.businesses)

    def test_business_search_missing_arguments_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.business_search()

    def test_business_search_missing_longitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.business_search(latitude=37.32238222393683)

    def test_business_search_missing_latitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.business_search(longitude=-122.0306396484375)

    def test_phone_search(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = Client.phone_search(phone="+14157492060")

        phone_search: PhoneSearch = phone_search_endpoint.get()

        assert phone_search.total > 0
        assert phone_search.businesses[0].phone == "+14157492060"
        assert phone_search.businesses[0].id == "WavvLdfdP6g8aZTtbBQHTw"
        assert phone_search.businesses[0].alias == "gary-danko-san-francisco"
        assert phone_search.businesses[0].name == "Gary Danko"

    def test_phone_search_no_matches(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = Client.phone_search(phone="+10000000000")

        phone_search: PhoneSearch = phone_search_endpoint.get()

        assert phone_search.total == 0
        assert not phone_search.businesses

    def test_reviews(self) -> None:
        reviews_endpoint: ReviewsEndpoint = Client.reviews(business_id="WavvLdfdP6g8aZTtbBQHTw")

        reviews: Reviews = reviews_endpoint.get()

        # "total" returns the total number of reviews that a business has.
        assert reviews.total > 3
        # The "reviews" list returns a maximum of 3 reviews.
        assert len(reviews.reviews) == 3
        assert "en" in reviews.possible_languages

    def test_transaction_search_by_location(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = Client.transaction_search(
            location="20488 Stevens Creek Blvd, Cupertino, CA 95014"
        )

        transaction_search: TransactionSearch = transaction_search_endpoint.get()

        assert transaction_search.total > 0
        assert all("delivery" in business.transactions for business in transaction_search.businesses)

    def test_transaction_search_by_latitude_longitude(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = Client.transaction_search(
            latitude=37.32238222393683, longitude=-122.0306396484375
        )

        transaction_search: TransactionSearch = transaction_search_endpoint.get()

        assert transaction_search.total > 0
        assert all("delivery" in business.transactions for business in transaction_search.businesses)

    def test_transaction_search_missing_arguments_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.transaction_search()

    def test_transaction_search_missing_longitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.transaction_search(latitude=37.32238222393683)

    def test_transaction_search_missing_latitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.transaction_search(longitude=-122.0306396484375)

    def test_autocomplete_text(self) -> None:
        autocomplete_endpoint: AutocompleteEndpoint = Client.autocomplete(text="del")

        autocomplete: Autocomplete = autocomplete_endpoint.get()

        assert len(autocomplete.categories) > 0
        assert not autocomplete.businesses
        assert len(autocomplete.terms) > 0
        assert all("del" in category.alias.lower() for category in autocomplete.categories)
        assert all("del" in category.title.lower() for category in autocomplete.categories)
        assert all("del" in term.text.lower() for term in autocomplete.terms)

    def test_autocomplete_text_latitude_longitude(self) -> None:
        autocomplete_endpoint: AutocompleteEndpoint = Client.autocomplete(
            text="del", latitude=37.786942, longitude=-122.399643
        )

        autocomplete: Autocomplete = autocomplete_endpoint.get()

        assert len(autocomplete.categories) > 0
        assert len(autocomplete.businesses) > 0
        assert len(autocomplete.terms) > 0
        assert all("del" in category.alias.lower() for category in autocomplete.categories)
        assert all("del" in category.title.lower() for category in autocomplete.categories)
        assert all("del" in business.name.lower() for business in autocomplete.businesses)
        assert all("del" in term.text.lower() for term in autocomplete.terms)

    def test_event_search(self) -> None:
        event_search_endpoint: EventSearchEndpoint = Client.event_search()
        event_search_endpoint.limit = 50
        event_search_endpoint.radius = 40000
        event_search_endpoint.location = "san francisco, ca"
        event_search_endpoint.categories = "food-and-drink,nightlife"

        event_search: EventSearch = event_search_endpoint.get()

        assert event_search.total > 0
        assert all(event.category in ["food-and-drink", "nightlife"] for event in event_search.events)

    def test_event_lookup(self) -> None:
        event_lookup_endpoint: EventLookupEndpoint = Client.event_lookup(
            event_id="oakland-saucy-oakland-restaurant-pop-up"
        )

        event: Event = event_lookup_endpoint.get()

        assert event.id == "oakland-saucy-oakland-restaurant-pop-up"
        assert event.category == "food-and-drink"
        assert event.location.city == "Oakland"
        assert event.location.state == "CA"
        assert event.location.zip_code == "94612"
        assert event.location.country == "US"
        assert event.business_id == "anfilo-oakland-2"

    def test_featured_event_location(self) -> None:
        featured_event_endpoint: FeaturedEventEndpoint = Client.featured_event(location="San Francisco, CA")

        event: Event = featured_event_endpoint.get()

        assert event.id
        assert event.location.city == "San Francisco"
        assert event.location.state == "CA"
        assert event.location.country == "US"

    def test_featured_event_latitude_longitude(self) -> None:
        featured_event_endpoint: FeaturedEventEndpoint = Client.featured_event(
            latitude=37.7726402, longitude=-122.4099154
        )

        event: Event = featured_event_endpoint.get()

        assert event.id
        assert event.location.city == "San Francisco"
        assert event.location.state == "CA"
        assert event.location.country == "US"

    def test_featured_event_missing_required_arguments(self) -> None:
        with pytest.raises(ValueError):
            Client.featured_event()

    def test_featured_event_missing_latitude(self) -> None:
        with pytest.raises(ValueError):
            Client.featured_event(longitude=-122.4099154)

    def test_featured_event_missing_longitude(self) -> None:
        with pytest.raises(ValueError):
            Client.featured_event(latitude=37.7726402)

    def test_category_details(self) -> None:
        category_details_endpoint: CategoryDetailsEndpoint = Client.category_details(alias="archery")

        category_details: CategoryDetails = category_details_endpoint.get()

        assert category_details.category.alias == "archery"
        assert category_details.category.title == "Archery"
        assert len(category_details.category.parent_aliases) == 1
        assert category_details.category.parent_aliases[0] == "active"
        assert not category_details.category.country_whitelist
        assert not category_details.category.country_blacklist

    def test_all_categories(self) -> None:
        all_categories_endpoint: AllCategoriesEndpoint = Client.all_categories()

        categories: Categories = all_categories_endpoint.get()

        assert len(categories.categories) > 0
        # Not much else can viably do here since the collection of categories is massive.
