import os
from datetime import date

import pytest
from boatrace.models import RaceGrade, RaceKind
from boatrace.official.exceptions import DataNotFound, ScrapingError
from boatrace.official.v1707.pages.monthly_schedule_page.scraping import (
    Event,
    extract_events,
)

base_path = os.path.dirname(os.path.abspath(__file__))


def test_extract_events_from_a_monthly_schedule_page():
    file_path = os.path.normpath(os.path.join(base_path, "./fixtures/2015_11.html"))
    with open(file_path, mode="r") as file:
        data = extract_events(file)

    assert len(data) == 59
    assert len(list(filter(lambda x: x.stadium_tel_code == 1, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 2, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 3, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 4, data))) == 2
    assert len(list(filter(lambda x: x.stadium_tel_code == 5, data))) == 2
    assert len(list(filter(lambda x: x.stadium_tel_code == 6, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 7, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 8, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 9, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 10, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 11, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 12, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 13, data))) == 2
    assert len(list(filter(lambda x: x.stadium_tel_code == 14, data))) == 0
    assert len(list(filter(lambda x: x.stadium_tel_code == 15, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 16, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 17, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 18, data))) == 1
    assert len(list(filter(lambda x: x.stadium_tel_code == 19, data))) == 2
    assert len(list(filter(lambda x: x.stadium_tel_code == 20, data))) == 0
    assert len(list(filter(lambda x: x.stadium_tel_code == 21, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 22, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 23, data))) == 3
    assert len(list(filter(lambda x: x.stadium_tel_code == 24, data))) == 2

    # 代表値（月を跨ぐ開催の次節）
    assert data[3] == Event(
        stadium_tel_code=2,
        title="戸田ルーキーシリーズ第７戦",
        starts_on=date(2015, 11, 7),
        days=6,
        grade=RaceGrade.NO_GRADE,
        kind=RaceKind.ROOKIE,
    )

    # 代表値（1日が初日）
    assert data[6] == Event(
        stadium_tel_code=3,
        title="ヴィーナスシリーズ第７戦\u3000江戸川ＪＩＮＲＯ\u3000ＣＵＰ",
        starts_on=date(2015, 11, 1),
        days=6,
        grade=RaceGrade.NO_GRADE,
        kind=RaceKind.VENUS,
    )

    # 代表値（下旬初日で月を跨ぐ節）
    assert data[15] == Event(
        stadium_tel_code=6,
        title="公営レーシングプレスアタック",
        starts_on=date(2015, 11, 28),
        days=5,
        grade=RaceGrade.NO_GRADE,
        kind=RaceKind.UNCATEGORIZED,
    )

    # 代表値（SG）
    assert data[50] == Event(
        stadium_tel_code=21,
        title="ＳＧ１８回チャレンジカップ／ＧⅡ２回レディースＣＣ",
        starts_on=date(2015, 11, 24),
        days=6,
        grade=RaceGrade.SG,
        kind=RaceKind.UNCATEGORIZED,
    )

    # 代表値（グレードとカテゴリの取得）
    assert data[54] == Event(
        stadium_tel_code=23,
        title="ＧⅢオールレディース\u3000ＲＫＢラジオ杯",
        starts_on=date(2015, 11, 7),
        days=6,
        grade=RaceGrade.G3,
        kind=RaceKind.ALL_LADIES,
    )


def test_extract_events_from_a_monthly_schedule_page_for_specified_stadium():
    file_path = os.path.normpath(os.path.join(base_path, "./fixtures/2016_03_14#.html"))

    with open(file_path, mode="r") as file:
        with pytest.raises(ScrapingError):
            extract_events(file)


def test_extract_events_from_a_no_contents_page():
    file_path = os.path.normpath(
        os.path.join(os.path.join(base_path, "./fixtures/data_not_found.html"))
    )

    with open(file_path, mode="r") as file:
        with pytest.raises(DataNotFound):
            extract_events(file)
