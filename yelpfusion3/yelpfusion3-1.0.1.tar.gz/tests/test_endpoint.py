import pytest

from yelpfusion3.endpoint import SupportedLocales


class TestSupportedLocales:
    @pytest.mark.parametrize(
        "code, country, language",
        [
            ("cs_CZ", "Czech Republic", "Czech"),
            ("de_DE", "Germany", "German"),
            ("en_GB", "United Kingdom", "English"),
            ("en_US", "United States", "English"),
            ("it_IT", "Italy", "Italian"),
            ("zh_TW", "Taiwan", "Chinese"),
        ],
    )
    def test_supported_locales(self, code: str, country: str, language: str) -> None:
        for locale in SupportedLocales.locales:
            if locale["code"] == code:
                assert locale["country"] == country
                assert locale["language"] == language
                return

        assert False

    @pytest.mark.parametrize(
        "code",
        [
            "cs_CZ",
            "de_DE",
            "en_GB",
            "en_US",
            "it_IT",
            "zh_TW",
        ],
    )
    def test_codes(self, code: str) -> None:
        assert code in SupportedLocales.codes()
