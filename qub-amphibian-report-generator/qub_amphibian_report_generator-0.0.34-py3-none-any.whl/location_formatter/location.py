"""# Module for location class."""


class Location:
    """Location Class.

    Class representing location data.

    """

    def __init__(
        self,
        continent: str = "NoContinent",
        country: str = "NoCountry",
        region: str = "NoRegion",
        latitude: float = None,
        longitude: float = None,
        country_code="",
        country_full_name: str = "",
    ) -> None:
        """Class init.

        Init method for Location class

        Args:
            continent: continent name string
            country: country name string
            region: region name string
            latitiude: latitude float
            longitude: longitude float
            country_code: 2 letter country code string
            country_full_name: official full name of country string

        """
        self.country = country
        self.continent = continent
        self.region = region
        self.latitude = latitude
        self.longitude = longitude
        self.country_code = country_code
        self.country_full_name = country_full_name

    def get_location_obj(self) -> dict:
        """Get location object.

        Creates a python object based on location data.

        Returns:
            location_obj: python object representing location information.

        """
        return {
            "region": self.region,
            "country": self.country,
            "country_code": self.country_code,
            "continent": self.continent,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "country_full_name": self.country_full_name,
        }

    def __str__(self):
        """Get string magic method."""
        data = [
            self.continent.title(),
            self.country.title(),
            self.region.title(),
            str(self.latitude),
            str(self.longitude),
            self.country_code.upper(),
        ]
        return "_".join(data)
