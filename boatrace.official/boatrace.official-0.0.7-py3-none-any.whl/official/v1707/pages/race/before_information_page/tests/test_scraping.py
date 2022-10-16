import os
from datetime import date

import pytest
from boatrace.models import MotorParts, StadiumTelCode, Weather
from boatrace.official.exceptions import DataNotFound
from boatrace.official.v1707.pages.race.before_information_page.scraping import (
    BoatSetting,
    CircumferenceExhibitionRecord,
    RacerCondition,
    StartExhibitionRecord,
    WeatherCondition,
    extract_boat_settings,
    extract_circumference_exhibition_records,
    extract_racer_conditions,
    extract_start_exhibition_records,
    extract_weather_condition,
)

base_path = os.path.dirname(os.path.abspath(__file__))


def test_extract_start_exhibition_records():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_23#_1R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_start_exhibition_records(file)

    assert data == [
        StartExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=1,
            start_course=1,
            start_time=0.23,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=2,
            start_course=2,
            start_time=0.28,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=3,
            start_course=3,
            start_time=0.21,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=4,
            start_course=4,
            start_time=0.21,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=5,
            start_course=5,
            start_time=0.11,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=6,
            start_course=6,
            start_time=-0.04,
        ),
    ]


# レース欠場者とスタ展欠場者で場合分けした方がいいかと思ったがどちらも出力されるtableは同じなのでこれで網羅できたと見做す
def test_extract_start_exhibition_records_from_a_page_including_absent_racer():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20170625_06#_10R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_start_exhibition_records(file)

    assert data == [
        StartExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=1,
            start_course=1,
            start_time=0.02,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=2,
            start_course=2,
            start_time=0.32,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=3,
            start_course=3,
            start_time=0.05,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=4,
            start_course=4,
            start_time=0.19,
        ),
        StartExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=6,
            start_course=5,
            start_time=0.16,
        ),
    ]


def test_extract_circumference_exhibition_records():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_23#_1R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_circumference_exhibition_records(file)

    assert data == [
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=1,
            exhibition_time=6.7,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=2,
            exhibition_time=6.81,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=3,
            exhibition_time=6.84,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=4,
            exhibition_time=6.86,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=5,
            exhibition_time=6.83,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=6,
            exhibition_time=6.81,
        ),
    ]


def test_extarct_circumference_exhibition_records_including_st_absent_racer():
    file_path = os.path.normpath(
        # 5号艇がスタ展出てない
        os.path.join(
            base_path,
            "./fixtures/20170625_06#_10R.html",
        )
    )

    with open(file_path, mode="r") as file:
        data = extract_circumference_exhibition_records(file)

    assert data == [
        CircumferenceExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=1,
            exhibition_time=6.66,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=2,
            exhibition_time=6.76,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=3,
            exhibition_time=6.71,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=4,
            exhibition_time=6.77,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=5,
            exhibition_time=6.73,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2017, 6, 25),
            stadium_tel_code=StadiumTelCode.HAMANAKO,
            race_number=10,
            pit_number=6,
            exhibition_time=6.73,
        ),
    ]


def test_extract_circumference_exhibition_records_including_race_absent_racer():
    file_path = os.path.normpath(
        # 1号艇が欠場
        os.path.join(
            base_path,
            "./fixtures/20151116_03#_11R.html",
        )
    )

    with open(file_path, mode="r") as file:
        data = extract_circumference_exhibition_records(file)

    assert data == [
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=2,
            exhibition_time=6.91,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=3,
            exhibition_time=7.04,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=4,
            exhibition_time=7,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=5,
            exhibition_time=7.16,
        ),
        CircumferenceExhibitionRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=6,
            exhibition_time=6.78,
        ),
    ]


def test_extract_racer_conditions():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_23#_1R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_racer_conditions(file)

    assert data == [
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=4096,
            weight=52.5,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=4693,
            weight=51.0,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=2505,
            weight=50.0,
            adjust=1.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=4803,
            weight=54.4,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=3138,
            weight=51.9,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=4221,
            weight=50.0,
            adjust=1.0,
        ),
    ]


def test_extract_racer_conditions_including_race_absent_racer():
    file_path = os.path.normpath(
        # 1号艇が欠場
        os.path.join(
            base_path,
            "./fixtures/20151116_03#_11R.html",
        )
    )

    with open(file_path, mode="r") as file:
        data = extract_racer_conditions(file)

    assert data == [
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=3880,
            weight=55.8,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=3793,
            weight=56.5,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=4357,
            weight=52.8,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=4037,
            weight=51.2,
            adjust=0.0,
        ),
        RacerCondition(
            recorded_on=date(2015, 11, 16),
            racer_registration_number=3797,
            weight=58.3,
            adjust=0.0,
        ),
    ]


def test_extract_boat_settings():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_23#_1R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_boat_settings(file)

    assert data == [
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=1,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=2,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=3,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=4,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=5,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=1,
            pit_number=6,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
    ]


def test_extract_boat_settings_including_propeller_exchanges():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20180619_04#_4R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_boat_settings(file)

    assert data == [
        BoatSetting(
            race_holding_date=date(2018, 6, 19),
            stadium_tel_code=StadiumTelCode.HEIWAJIMA,
            race_number=4,
            pit_number=1,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2018, 6, 19),
            stadium_tel_code=StadiumTelCode.HEIWAJIMA,
            race_number=4,
            pit_number=2,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2018, 6, 19),
            stadium_tel_code=StadiumTelCode.HEIWAJIMA,
            race_number=4,
            pit_number=3,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2018, 6, 19),
            stadium_tel_code=StadiumTelCode.HEIWAJIMA,
            race_number=4,
            pit_number=4,
            tilt=-0.5,
            is_new_propeller=True,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2018, 6, 19),
            stadium_tel_code=StadiumTelCode.HEIWAJIMA,
            race_number=4,
            pit_number=5,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2018, 6, 19),
            stadium_tel_code=StadiumTelCode.HEIWAJIMA,
            race_number=4,
            pit_number=6,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
    ]


def test_extract_boat_settings_including_absent_racers():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_03#_11R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_boat_settings(file)

    assert data == [
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=2,
            tilt=0,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=3,
            tilt=0,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=4,
            tilt=0,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=5,
            tilt=0,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            pit_number=6,
            tilt=0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
    ]


def test_extract_boat_settings():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20200630_12#_12R.html")
    )

    with open(file_path, mode="r") as file:
        with pytest.raises(DataNotFound):
            extract_boat_settings(file)


def test_scrape_boat_settings_including_motor_parts_exchanges():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_23#_12R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_boat_settings(file)

    assert data == [
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=12,
            pit_number=1,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=12,
            pit_number=2,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=12,
            pit_number=3,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=12,
            pit_number=4,
            tilt=0,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=12,
            pit_number=5,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[
                (MotorParts.PISTON, 2),
                (MotorParts.PISTON_RING, 3),
                (MotorParts.ELECTRICAL_SYSTEM, 1),
                (MotorParts.GEAR_CASE, 1),
            ],
        ),
        BoatSetting(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.KARATSU,
            race_number=12,
            pit_number=6,
            tilt=-0.5,
            is_new_propeller=False,
            motor_parts_exchanges=[],
        ),
    ]


def test_extract_weather_condition():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151115_07#_12R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_weather_condition(file)

    assert data == WeatherCondition(
        race_holding_date=date(2015, 11, 15),
        stadium_tel_code=StadiumTelCode.GAMAGORI,
        race_number=12,
        in_performance=False,
        weather=Weather.FINE,
        wavelength=2.0,
        wind_angle=315.0,
        wind_velocity=4.0,
        air_temperature=17.0,
        water_temperature=17.0,
    )


def test_extract_weather_condition_from_incomplete_information():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20171030_03#_1R.html")
    )

    with open(file_path, mode="r") as file:
        with pytest.raises(ValueError):
            # 0:00現在表示があったら欠損値があるはずなのでこの例外になる
            extract_weather_condition(file)
