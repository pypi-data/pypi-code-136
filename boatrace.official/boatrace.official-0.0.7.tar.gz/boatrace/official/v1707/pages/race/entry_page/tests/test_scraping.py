import os
from datetime import date, datetime

from boatrace.models import RaceLaps, RacerRank, StadiumTelCode
from boatrace.official.v1707.pages.race.entry_page.scraping import (
    BoatPerformance,
    MotorPerformance,
    RaceEntry,
    RaceInformation,
    extract_boat_performances,
    extract_motor_performances,
    extract_race_entries,
    extract_race_information,
)

base_path = os.path.dirname(os.path.abspath(__file__))


def test_extract_race_information_from_an_entry_page():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151016_08#_2R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_information(file)

    assert data == RaceInformation(
        race_holding_date=date(2015, 10, 16),
        stadium_tel_code=StadiumTelCode.TOKONAME,
        race_number=2,
        title="予選",
        race_laps=RaceLaps.THREE,
        deadline_at=datetime(2015, 10, 16, 11, 13),
        is_course_fixed=False,
        use_stabilizer=False,
    )


def test_extract_race_information_using_stabilizers_from_an_entry_page():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20180301_07#_8R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_information(file)

    assert data == RaceInformation(
        race_holding_date=date(2018, 3, 1),
        stadium_tel_code=StadiumTelCode.GAMAGORI,
        race_number=8,
        title="一般戦",
        race_laps=RaceLaps.THREE,
        deadline_at=datetime(2018, 3, 1, 18, 26),
        is_course_fixed=False,
        use_stabilizer=True,
    )


def test_extract_course_fixed_race_information_from_an_entry_page():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20180301_07#_7R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_information(file)

    assert data == RaceInformation(
        race_holding_date=date(2018, 3, 1),
        stadium_tel_code=StadiumTelCode.GAMAGORI,
        race_number=7,
        title="一般戦",
        race_laps=RaceLaps.THREE,
        deadline_at=datetime(2018, 3, 1, 17, 57),
        is_course_fixed=True,
        use_stabilizer=True,
    )


def test_extract_two_laps_race_information_from_an_entry_page():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20180301_15#_12R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_information(file)

    assert data == RaceInformation(
        race_holding_date=date(2018, 3, 1),
        stadium_tel_code=StadiumTelCode.MARUGAME,
        race_number=12,
        title="一般選抜",
        race_laps=RaceLaps.TWO,
        deadline_at=datetime(2018, 3, 1, 20, 42),
        is_course_fixed=False,
        use_stabilizer=True,
    )


def test_extract_race_entries_from_an_entry_page():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20180301_07#_8R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_race_entries(file)

    assert data == [
        RaceEntry(
            race_holding_date=date(2018, 3, 1),
            stadium_tel_code=StadiumTelCode.GAMAGORI,
            race_number=8,
            racer_registration_number=4190,
            racer_first_name="万記",
            racer_last_name="長嶋",
            current_racer_rating=RacerRank.A1,
            pit_number=1,
            is_absent=False,
            motor_number=66,
            boat_number=40,
        ),
        RaceEntry(
            race_holding_date=date(2018, 3, 1),
            stadium_tel_code=StadiumTelCode.GAMAGORI,
            race_number=8,
            racer_registration_number=4240,
            racer_first_name="裕梨",
            racer_last_name="今井",
            current_racer_rating=RacerRank.B1,
            pit_number=2,
            is_absent=False,
            motor_number=41,
            boat_number=43,
        ),
        RaceEntry(
            race_holding_date=date(2018, 3, 1),
            stadium_tel_code=StadiumTelCode.GAMAGORI,
            race_number=8,
            racer_registration_number=4419,
            racer_first_name="加央理",
            racer_last_name="原",
            current_racer_rating=RacerRank.B1,
            pit_number=3,
            is_absent=False,
            motor_number=58,
            boat_number=74,
        ),
        RaceEntry(
            race_holding_date=date(2018, 3, 1),
            stadium_tel_code=StadiumTelCode.GAMAGORI,
            race_number=8,
            racer_registration_number=3175,
            racer_first_name="千草",
            racer_last_name="渡辺",
            current_racer_rating=RacerRank.A2,
            pit_number=4,
            is_absent=False,
            motor_number=33,
            boat_number=13,
        ),
        RaceEntry(
            race_holding_date=date(2018, 3, 1),
            stadium_tel_code=StadiumTelCode.GAMAGORI,
            race_number=8,
            racer_registration_number=3254,
            racer_first_name="千春",
            racer_last_name="柳澤",
            current_racer_rating=RacerRank.B1,
            pit_number=5,
            is_absent=False,
            motor_number=71,
            boat_number=65,
        ),
        RaceEntry(
            race_holding_date=date(2018, 3, 1),
            stadium_tel_code=StadiumTelCode.GAMAGORI,
            race_number=8,
            racer_registration_number=4843,
            racer_first_name="巴恵",
            racer_last_name="深尾",
            current_racer_rating=RacerRank.B1,
            pit_number=6,
            is_absent=False,
            motor_number=40,
            boat_number=68,
        ),
    ]


def test_extract_race_entries_from_an_entry_page_of_a_race_including_absent():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_03#_11R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_race_entries(file)

    assert data == [
        RaceEntry(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            racer_registration_number=3872,
            racer_first_name="憲行",
            racer_last_name="岡田",
            current_racer_rating=RacerRank.A1,
            pit_number=1,
            is_absent=True,
            motor_number=62,
            boat_number=25,
        ),
        RaceEntry(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            racer_registration_number=3880,
            racer_first_name="宗孝",
            racer_last_name="浅見",
            current_racer_rating=RacerRank.B1,
            pit_number=2,
            is_absent=False,
            motor_number=61,
            boat_number=31,
        ),
        RaceEntry(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            racer_registration_number=3793,
            racer_first_name="真吾",
            racer_last_name="高橋",
            current_racer_rating=RacerRank.B1,
            pit_number=3,
            is_absent=False,
            motor_number=56,
            boat_number=60,
        ),
        RaceEntry(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            racer_registration_number=4357,
            racer_first_name="和也",
            racer_last_name="田中",
            current_racer_rating=RacerRank.A1,
            pit_number=4,
            is_absent=False,
            motor_number=68,
            boat_number=43,
        ),
        RaceEntry(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            racer_registration_number=4037,
            racer_first_name="正幸",
            racer_last_name="別府",
            current_racer_rating=RacerRank.A2,
            pit_number=5,
            is_absent=False,
            motor_number=26,
            boat_number=46,
        ),
        RaceEntry(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            racer_registration_number=3797,
            racer_first_name="繁",
            racer_last_name="岩井",
            current_racer_rating=RacerRank.A2,
            pit_number=6,
            is_absent=False,
            motor_number=20,
            boat_number=69,
        ),
    ]


def test_extract_boat_performances():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20180301_07#_8R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_boat_performances(file)

    assert data == [
        BoatPerformance(
            recorded_date=date(2018, 3, 1),
            number=40,
            quinella_rate=39.18,
            trio_rate=57.22,
        ),
        BoatPerformance(
            recorded_date=date(2018, 3, 1),
            number=43,
            quinella_rate=37.65,
            trio_rate=55.29,
        ),
        BoatPerformance(
            recorded_date=date(2018, 3, 1),
            number=74,
            quinella_rate=35.62,
            trio_rate=54.79,
        ),
        BoatPerformance(
            recorded_date=date(2018, 3, 1),
            number=13,
            quinella_rate=29.78,
            trio_rate=45.51,
        ),
        BoatPerformance(
            recorded_date=date(2018, 3, 1),
            number=65,
            quinella_rate=27.43,
            trio_rate=50.86,
        ),
        BoatPerformance(
            recorded_date=date(2018, 3, 1),
            number=68,
            quinella_rate=28.49,
            trio_rate=45.35,
        ),
    ]


def test_extract_boat_performances_including_missing_values():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_03#_11R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_boat_performances(file)

    assert data == [
        BoatPerformance(
            recorded_date=date(2015, 11, 16),
            number=25,
            quinella_rate=30.3,
            trio_rate=None,
        ),
        BoatPerformance(
            recorded_date=date(2015, 11, 16),
            number=31,
            quinella_rate=31.9,
            trio_rate=None,
        ),
        BoatPerformance(
            recorded_date=date(2015, 11, 16),
            number=60,
            quinella_rate=30.4,
            trio_rate=None,
        ),
        BoatPerformance(
            recorded_date=date(2015, 11, 16),
            number=43,
            quinella_rate=33.5,
            trio_rate=None,
        ),
        BoatPerformance(
            recorded_date=date(2015, 11, 16),
            number=46,
            quinella_rate=31.3,
            trio_rate=None,
        ),
        BoatPerformance(
            recorded_date=date(2015, 11, 16),
            number=69,
            quinella_rate=29,
            trio_rate=None,
        ),
    ]


def test_extract_motor_performances():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20180301_07#_8R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_motor_performances(file)

    assert data == [
        MotorPerformance(
            recorded_date=date(2018, 3, 1),
            number=66,
            quinella_rate=38.1,
            trio_rate=51.9,
        ),
        MotorPerformance(
            recorded_date=date(2018, 3, 1),
            number=41,
            quinella_rate=36.5,
            trio_rate=51,
        ),
        MotorPerformance(
            recorded_date=date(2018, 3, 1),
            number=58,
            quinella_rate=33.17,
            trio_rate=51.49,
        ),
        MotorPerformance(
            recorded_date=date(2018, 3, 1),
            number=33,
            quinella_rate=39.72,
            trio_rate=55.61,
        ),
        MotorPerformance(
            recorded_date=date(2018, 3, 1),
            number=71,
            quinella_rate=29.51,
            trio_rate=46.72,
        ),
        MotorPerformance(
            recorded_date=date(2018, 3, 1),
            number=40,
            quinella_rate=33.16,
            trio_rate=49.49,
        ),
    ]


def test_extract_motor_performances_including_missing_values():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_03#_11R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_motor_performances(file)

    assert data == [
        MotorPerformance(
            recorded_date=date(2015, 11, 16),
            number=62,
            quinella_rate=31.5,
            trio_rate=None,
        ),
        MotorPerformance(
            recorded_date=date(2015, 11, 16),
            number=61,
            quinella_rate=34.4,
            trio_rate=None,
        ),
        MotorPerformance(
            recorded_date=date(2015, 11, 16),
            number=56,
            quinella_rate=27.8,
            trio_rate=None,
        ),
        MotorPerformance(
            recorded_date=date(2015, 11, 16),
            number=68,
            quinella_rate=48.3,
            trio_rate=None,
        ),
        MotorPerformance(
            recorded_date=date(2015, 11, 16),
            number=26,
            quinella_rate=30.2,
            trio_rate=None,
        ),
        MotorPerformance(
            recorded_date=date(2015, 11, 16),
            number=20,
            quinella_rate=40.1,
            trio_rate=None,
        ),
    ]
