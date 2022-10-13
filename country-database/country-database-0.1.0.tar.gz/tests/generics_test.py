import pytest

from country_database import DataLoader
from country_database import FullCountryIndex
from country_database import Property
from country_database import load_countries_generic
from country_database import load_country
from country_database import load_country_generic

from .helper import CUSTOM_DATA_DIR
from .helper import TOTAL_COUNTRIES
from .helper import CustomCountry
from .helper import CustomCountryIndex


class InvalidCountryProperties:
    color: Property


class InvalidCountryIndex:
    USA: CustomCountry


def test_load_country_generic():
    loader = DataLoader()
    loader.merge_database(CUSTOM_DATA_DIR)
    v = load_country_generic(CustomCountry, "US", loader=loader)
    assert v.flag == "🇺🇸"


def test_load_country_generic_with_invalid_type():
    with pytest.raises(ValueError, match=r".+must be a frozen dataclass") as ex:
        load_country_generic(InvalidCountryProperties, "US")


def test_load_country_with_unknown_country_code():
    with pytest.raises(KeyError, match=r".+not found"):
        load_country("ZZZ")


def test_load_countries_generic_with_custom_index_cls():
    country_index = load_countries_generic(CustomCountryIndex)
    assert hasattr(country_index, "CHN") is False, "CHN should be missing"
    assert country_index.USA.flag == ""


def test_load_countries_generic_with_generic_index_cls():
    country_index = load_countries_generic(
        FullCountryIndex[CustomCountry], loader=DataLoader(CUSTOM_DATA_DIR)
    )
    assert len(country_index.asdict()) == TOTAL_COUNTRIES
    assert country_index.CHN.flag == "🇨🇳"
    # The `lookup` method is useful when the field is not a defined property.
    assert country_index.CHN.lookup("flag") == "🇨🇳"
    assert country_index.USA.national_flower == "Rose"
    assert country_index.USA.lookup("national_flower") == "Rose"

    assert country_index.USA.lookup("404") == ""


def test_load_countries_generic_with_invalid_type():
    with pytest.raises(ValueError, match=r".+must be a dataclass"):
        load_countries_generic(InvalidCountryIndex)
