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


class TestBusinessDetailsEndpoint:
    @pytest.mark.parametrize(
        "business_id",
        [
            "WavvLdfdP6g8aZTtbBQHTw",
            "gary-danko-san-francisco",
        ],
    )
    def test_url(self, business_id: str) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(business_id=business_id)

        assert business_details_endpoint.url == f"https://api.yelp.com/v3/businesses/{business_id}"

    def test_url_build_with_locale(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw", locale="en_US"
        )

        assert business_details_endpoint.url == "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw?locale=en_US"

    @pytest.mark.parametrize(
        "business_id",
        [
            "W vvLdfdP6g8aZTtbBQHTw",
            "W@vvLdfdP6g8aZTtbBQHTw",
            "gary danko-san-francisco",
            "gary_danko-san-francisco",
        ],
    )
    def test_url_build_fails_on_malformed_id(self, business_id: str) -> None:
        with pytest.raises(ValueError):
            BusinessDetailsEndpoint(business_id=business_id)

    def test_locale_init_validation(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw", locale="en_US"
        )

        assert business_details_endpoint.locale == "en_US"

    def test_locale_validation(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        business_details_endpoint.locale = "en_US"

        assert business_details_endpoint.locale == "en_US"

    def test_locale_fails_validation(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        with pytest.raises(ValueError):
            business_details_endpoint.locale = "zz_ZZ"


class TestBusinessMatchesEndpoint:
    def test_url(self) -> None:
        business_matches_endpoint: BusinessMatchesEndpoint = BusinessMatchesEndpoint(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        assert (
            business_matches_endpoint.url
            == "https://api.yelp.com/v3/businesses/matches?name=Gary%20Danko&address1=800%20N%20Point%20St&city=San%20Francisco&state=CA&country=US"
        )

    def test_country_init_fails_validation(self) -> None:
        with pytest.raises(ValueError):
            BusinessMatchesEndpoint(
                name="Gary Danko",
                address1="800 N Point St",
                city="San Francisco",
                state="CA",
                country="ZZ",
            )

    def test_country_fails_validation(self) -> None:
        business_match_endpoint: BusinessMatchesEndpoint = BusinessMatchesEndpoint(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        with pytest.raises(ValueError):
            business_match_endpoint.country = "ZZ"


class TestBusinessSearchEndpoint:
    def test_url(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint(
            term="coffee",
            location="san francisco",
            radius=25,
            limit=20,
            price="1,2",
        )

        assert (
            business_search_endpoint.url
            == "https://api.yelp.com/v3/businesses/search?term=coffee&location=san%20francisco&radius=25&limit=20&price=1%2C2"
        )

    def test_unsupported_fields_ignored(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint(
            term="coffee",
            location="san francisco",
            radius=25,
            limit=20,
            price="1,2",
            unsupported="an unsupported field",
        )

        assert "unsupported" not in [key for key, value in dict(business_search_endpoint).items()]
        assert (
            business_search_endpoint.url
            == "https://api.yelp.com/v3/businesses/search?term=coffee&location=san%20francisco&radius=25&limit=20&price=1%2C2"
        )

    @pytest.mark.parametrize("latitude", [-90, 0, 90])
    def test_latitude_validation(self, latitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.latitude = latitude

    @pytest.mark.parametrize("latitude", [-91, 91])
    def test_latitude_fails_validation(self, latitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.latitude = latitude

    @pytest.mark.parametrize("longitude", [-180, 0, 180])
    def test_longitude_validation(self, longitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.longitude = longitude

    @pytest.mark.parametrize("longitude", [-181, 181])
    def test_longitude_fails_validation(self, longitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.longitude = longitude

    @pytest.mark.parametrize(
        "locale",
        [
            "es_ES",
            "en_US",
            "fr_FR",
        ],
    )
    def test_locale_validation(self, locale: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.locale = locale

    def test_locale_fails_validation(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.locale = "xx_XX"

    @pytest.mark.parametrize(
        "price, expected",
        [
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("2,3", "2,3"),
            ("2, 3", "2,3"),
            ("  2  , 3    ", "2,3"),
        ],
    )
    def test_price_validation(self, price: str, expected: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.price = price

        assert business_search_endpoint.price == expected

    @pytest.mark.parametrize("price", ["0", "5", "4,5", "0,1", "invalid", "", " ", None])
    def test_price_fails_validation(self, price: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.price = price

    @pytest.mark.parametrize(
        "attributes, expected",
        [
            ("hot_and_new", "hot_and_new"),
            ("request_a_quote", "request_a_quote"),
            ("reservation", "reservation"),
            ("waitlist_reservation", "waitlist_reservation"),
            ("deals", "deals"),
            ("gender_neutral_restrooms", "gender_neutral_restrooms"),
            ("open_to_all", "open_to_all"),
            ("wheelchair_accessible", "wheelchair_accessible"),
            (
                "hot_and_new,reservation,open_to_all",
                "hot_and_new,reservation,open_to_all",
            ),
            (
                " hot_and_new , reservation , open_to_all  ",
                "hot_and_new,reservation,open_to_all",
            ),
        ],
    )
    def test_attributes_validation(self, attributes: str, expected: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.attributes = attributes

        assert business_search_endpoint.attributes == expected

    @pytest.mark.parametrize("attributes", ["unsupported_attribute", "", " ", None])
    def test_attributes_fails_validation(self, attributes: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.attributes = attributes


class TestPhoneSearchEndpoint:
    def test_url(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(phone="+14159083801")

        assert phone_search_endpoint.url == "https://api.yelp.com/v3/businesses/search/phone?phone=%2B14159083801"

    def test_locale_init_validation(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(phone="+14159083801", locale="en_US")

        assert phone_search_endpoint.locale == "en_US"

    def test_locale_validation(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(phone="+14159083801")

        phone_search_endpoint.locale = "en_US"

        assert phone_search_endpoint.locale == "en_US"

    def test_locale_fails_validation(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(phone="+14159083801")

        with pytest.raises(ValueError):
            phone_search_endpoint.locale = "zz_ZZ"


class TestReviewsEndpoint:
    def test_url(self) -> None:
        reviews_endpoint: ReviewsEndpoint = ReviewsEndpoint(business_id="WavvLdfdP6g8aZTtbBQHTw")

        assert reviews_endpoint.url == "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw/reviews"

    def test_url_build_with_locale(self) -> None:
        reviews_endpoint: ReviewsEndpoint = ReviewsEndpoint(business_id="WavvLdfdP6g8aZTtbBQHTw")
        reviews_endpoint.locale = "fr_FR"

        assert reviews_endpoint.url == "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw/reviews?locale=fr_FR"

    def test_locale_fails_validation(self) -> None:
        reviews_endpoint: ReviewsEndpoint = ReviewsEndpoint(business_id="WavvLdfdP6g8aZTtbBQHTw")

        with pytest.raises(ValueError):
            reviews_endpoint.locale = "zz_ZZ"


class TestTransactionSearchEndpoint:
    def test_url_location(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = TransactionSearchEndpoint(
            location="800 N Point St San Francisco CA"
        )

        assert (
            transaction_search_endpoint.url
            == "https://api.yelp.com/v3/transactions/delivery/search?location=800%20N%20Point%20St%20San%20Francisco%20CA"
        )

    def test_url_latitude_longitude(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = TransactionSearchEndpoint(
            latitude=37.80587, longitude=-122.42058
        )

        assert (
            transaction_search_endpoint.url
            == "https://api.yelp.com/v3/transactions/delivery/search?latitude=37.80587&longitude=-122.42058"
        )

    @pytest.mark.parametrize("latitude", [-91.0, 92.0])
    def test_latitude_fails_validation(self, latitude: float) -> None:
        with pytest.raises(ValueError):
            TransactionSearchEndpoint(latitude=latitude, longitude=-122.42058)

    @pytest.mark.parametrize("longitude", [-181.0, 182.0])
    def test_longitude_fails_validation(self, longitude: float) -> None:
        with pytest.raises(ValueError):
            TransactionSearchEndpoint(latitude=37.80587, longitude=longitude)


class TestAutocompleteEndpoint:
    def test_url(self) -> None:
        autocomplete_endpoint: AutocompleteEndpoint = AutocompleteEndpoint(text="coffee")

        assert autocomplete_endpoint.url == "https://api.yelp.com/v3/autocomplete?text=coffee"

    def test_url_locale(self) -> None:
        autocomplete_endpoint: AutocompleteEndpoint = AutocompleteEndpoint(text="coffee", locale="fr_FR")

        assert autocomplete_endpoint.url == "https://api.yelp.com/v3/autocomplete?text=coffee&locale=fr_FR"

    def test_url_latitude_longitude(self) -> None:
        autocomplete_endpoint: AutocompleteEndpoint = AutocompleteEndpoint(
            text="coffee", latitude=37.80587, longitude=-122.42058
        )

        assert (
            autocomplete_endpoint.url
            == "https://api.yelp.com/v3/autocomplete?text=coffee&latitude=37.80587&longitude=-122.42058"
        )

    def test_url_latitude_longitude_locale(self) -> None:
        autocomplete_endpoint: AutocompleteEndpoint = AutocompleteEndpoint(
            text="coffee", latitude=37.80587, longitude=-122.42058, locale="fr_FR"
        )

        assert (
            autocomplete_endpoint.url
            == "https://api.yelp.com/v3/autocomplete?text=coffee&latitude=37.80587&longitude=-122.42058&locale=fr_FR"
        )

    def test_locale_fails_validation(self) -> None:
        autocomplete_endpoint: AutocompleteEndpoint = AutocompleteEndpoint(
            text="coffee", latitude=37.80587, longitude=-122.42058
        )

        with pytest.raises(ValueError):
            autocomplete_endpoint.locale = "zz_ZZ"

    @pytest.mark.parametrize("latitude", [-91.0, 92.0])
    def test_latitude_fails_validation(self, latitude: float) -> None:
        with pytest.raises(ValueError):
            AutocompleteEndpoint(latitude=latitude, longitude=-122.42058)

    @pytest.mark.parametrize("longitude", [-181.0, 182.0])
    def test_longitude_fails_validation(self, longitude: float) -> None:
        with pytest.raises(ValueError):
            AutocompleteEndpoint(latitude=37.80587, longitude=longitude)
