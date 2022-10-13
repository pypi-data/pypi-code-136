from pathlib import Path

import pytest

from country_database import DataLoader

from .helper import CUSTOM_DATA_DIR


def test_DataLoader():
    dl = DataLoader()
    assert dl.lookup("CAN", "name") == "Canada"
    assert dl.lookup("CHN", "name", locale="zh") == "中国"

    assert dl.lookup("Invalid-Code", "name") is None
    assert dl.lookup("Invalid-Code", "name", locale="de") is None

    assert dl.lookup("USA", "UnknownField") is None
    assert dl.lookup("USA", "UnknownField", locale="fr") is None


def test_DataLoader_merge_database():
    dl = DataLoader()
    dl.merge_database(Path(__file__).parent / "custom")
    assert len(dl.databases) == 2

    assert dl.lookup("CAN", "flag") == "🇨🇦"
    assert dl.lookup("CHN", "flag") == "🇨🇳"
    assert dl.lookup("USA", "flag") == "🇺🇸"
    assert dl.lookup("GBR", "flag") is None
    assert dl.lookup("CAN", "flag", locale="de") is None

    assert dl.lookup("USA", "name", locale="fr") == "États-Unis d'Amérique (les)"
    assert dl.lookup("CHN", "name", locale="fr") == "Chine"

    assert dl.lookup("USA", "name") == "United States"
    assert dl.lookup("GBR", "name") == "United Kingdom"
    assert dl.lookup("CHN", "name") == "China"


def test_DataLoader_merge_database_OverrideLevel_LOCALE():
    dl = DataLoader()
    dl.merge_database(CUSTOM_DATA_DIR, override_level=DataLoader.OverrideLevel.LOCALE)
    assert dl.lookup("USA", "name") == "United States"
    assert dl.lookup("GBR", "name") == "United Kingdom"
    assert dl.lookup("CHN", "name") is None


def test_DataLoader_merge_database_reload():
    called = False

    def mock_reload_callback():
        nonlocal called
        called = True

    dl = DataLoader()
    dl.register_reload_callback(mock_reload_callback)
    dl.merge_database(Path(__file__).parent / "custom")
    assert called, "reload callback should be called"


def test_DataLoader_merge_database_duplicate_path():
    dl = DataLoader()
    dl.merge_database(CUSTOM_DATA_DIR)

    with pytest.raises(ValueError, match=r".+already loaded"):
        dl.merge_database(CUSTOM_DATA_DIR)
