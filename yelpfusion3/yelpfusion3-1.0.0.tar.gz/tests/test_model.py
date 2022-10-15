import pytest

from yelpfusion3.model import Location


class TestLocation:
    @pytest.mark.parametrize(
        "actual, expected",
        [
            ("CA", "CA"),
            ("ca", "CA"),
            ("cA", "CA"),
            ("Ca", "CA"),
        ],
    )
    def test_state(self, actual: str, expected: str) -> None:
        location: Location = Location(
            city="San Francisco",
            state=actual,
            zip_code="94109",
            country="US",
            display_address=["800 N Point St", "San Francisco, CA 94109"],
        )

        assert location.state == expected

    @pytest.mark.parametrize(
        "actual, expected",
        [
            ("US", "US"),
            ("us", "US"),
            ("uS", "US"),
            ("Us", "US"),
        ],
    )
    def test_country(self, actual: str, expected: str) -> None:
        location: Location = Location(
            city="San Francisco",
            state="CA",
            zip_code="94109",
            country=actual,
            display_address=["800 N Point St", "San Francisco, CA 94109"],
        )

        assert location.country == expected

    def test_country_fails(self) -> None:
        with pytest.raises(ValueError):
            Location(
                city="San Francisco",
                state="CA",
                zip_code="94109",
                country="zz",
                display_address=["800 N Point St", "San Francisco, CA 94109"],
            )
