import os

from yelpfusion3.settings import Settings


class TestSettings:
    def test_headers_from_environment_variable(self) -> None:
        os.environ["YELP_API_KEY"] = "TESTAPIKEY"
        settings: Settings = Settings()

        assert settings.headers == {"Authorization": "Bearer TESTAPIKEY"}
