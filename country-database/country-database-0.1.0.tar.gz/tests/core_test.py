from country_database import load_countries
from country_database import load_country


def test_load_country():
    can = load_country("CAN")
    assert can.locale == "en"
    assert can.alpha2_code == "CA"
    assert can.alpha3_code == "CAN"
    assert can.numeric_code == "124"
    assert can.name == "Canada"


def test_load_country_by_using_alpha2_code():
    can = load_country("CA")
    assert can.locale == "en"
    assert can.alpha2_code == "CA"
    assert can.alpha3_code == "CAN"
    assert can.numeric_code == "124"
    assert can.name == "Canada"


def test_load_country_with_locale():
    can_zh = load_country("CAN", locale="zh")
    assert can_zh.locale == "zh"
    assert can_zh.alpha2_code == "CA"
    assert can_zh.alpha3_code == "CAN"
    assert can_zh.numeric_code == "124"
    assert can_zh.name == "加拿大"


def test_country_to_locale():
    can = load_country("CAN")
    assert can.locale == "en"
    assert can.name == "Canada"

    can_zh = can.to_locale("zh")
    assert can_zh.locale == "zh"
    assert can_zh.name == "加拿大"


def test_load_countries():
    country_index = load_countries()

    assert country_index.CHN.locale == "en"
    assert country_index.CHN.name == "China"
    assert country_index.CHN.name.to_locale("zh") == "中国"

    assert country_index.CAN.locale == "en"
    assert country_index.CAN.name == "Canada"
    assert country_index.CAN.name.to_locale("zh") == "加拿大"
    assert country_index.CAN.name.to_locale("invalid-translation") == ""


def test_load_countries_with_locale():
    country_index = load_countries(locale="zh")

    assert country_index.CHN.locale == "zh"
    assert country_index.CHN.name == "中国"
    assert country_index.CHN.name.to_locale("en") == "China"

    assert country_index.CAN.locale == "zh"
    assert country_index.CAN.name == "加拿大"
    assert country_index.CAN.name.to_locale("en") == "Canada"
