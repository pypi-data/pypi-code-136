import os
from datetime import date

import pytest
from boatrace.models import (
    BettingMethod,
    Disqualification,
    StadiumTelCode,
    Weather,
    WinningTrick,
)
from boatrace.official.exceptions import DataNotFound, RaceCanceled
from boatrace.official.v1707.pages.race.result_page.scraping import (
    Payoff,
    RaceRecord,
    WeatherCondition,
    extract_race_payoffs,
    extract_race_records,
    extract_weather_condition,
)

base_path = os.path.dirname(os.path.abspath(__file__))


def test_extract_race_payoffs():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151115_07#_12R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_payoffs(file)

    assert data == [
        Payoff(
            race_holding_date=date(2015, 11, 15),
            stadium_tel_code=StadiumTelCode.GAMAGORI,
            race_number=12,
            betting_method=BettingMethod.TRIFECTA,
            betting_number=435,
            amount=56670,
        )
    ]


def test_extract_payoffs_from_a_race_which_has_an_absent():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_03#_11R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_payoffs(file)

    assert data == [
        Payoff(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.EDOGAWA,
            race_number=11,
            betting_method=BettingMethod.TRIFECTA,
            betting_number=234,
            amount=3100,
        )
    ]


def test_extract_payoffs_from_a_race_which_has_a_tie():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20181116_18#_7R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_race_payoffs(file)

    assert data == [
        Payoff(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            betting_method=BettingMethod.TRIFECTA,
            betting_number=142,
            amount=2230,
        ),
        Payoff(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            betting_method=BettingMethod.TRIFECTA,
            betting_number=412,
            amount=15500,
        ),
    ]


def test_extract_payoffs_from_a_race_which_has_four_disqualified_racers():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151114_02#_2R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_payoffs(file)

    assert data == []


def test_extract_payoffs_from_a_no_contents_page():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/data_not_found.html")
    )

    with open(file_path, mode="r") as file:
        with pytest.raises(DataNotFound):
            extract_race_payoffs(file)


def test_extract_payoffs_from_a_canceled_race():
    file_path = os.path.normpath(os.path.join(base_path, "./fixtures/canceled.html"))

    with open(file_path, mode="r") as file:
        with pytest.raises(RaceCanceled):
            extract_race_payoffs(file)


def test_extract_weather_condition():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20181116_18#_7R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_weather_condition(file)

    assert data == WeatherCondition(
        race_holding_date=date(2018, 11, 16),
        stadium_tel_code=StadiumTelCode.TOKUYAMA,
        race_number=7,
        in_performance=True,
        weather=Weather.CLOUDY,
        wavelength=1.0,
        wind_angle=135.0,
        wind_velocity=1.0,
        air_temperature=15.0,
        water_temperature=18.0,
    )


def test_extract_race_record_from_a_race_includes_lateness_entry():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151116_09#_7R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_race_records(file)

    assert data == [
        RaceRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.TSU,
            race_number=7,
            pit_number=1,
            start_course=1,
            arrival=2,
            total_time=110.9,
            start_time=0.06,
            winning_trick=None,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.TSU,
            race_number=7,
            pit_number=2,
            start_course=None,
            arrival=None,
            total_time=None,
            start_time=None,
            winning_trick=None,
            disqualification=Disqualification.LATENESS,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.TSU,
            race_number=7,
            pit_number=3,
            start_course=3,
            arrival=3,
            total_time=112.5,
            start_time=0.22,
            winning_trick=None,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.TSU,
            race_number=7,
            pit_number=4,
            start_course=4,
            arrival=1,
            total_time=109.9,
            start_time=0.21,
            winning_trick=WinningTrick.SASHI,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.TSU,
            race_number=7,
            pit_number=5,
            start_course=5,
            arrival=4,
            total_time=113.5,
            start_time=0.23,
            winning_trick=None,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 16),
            stadium_tel_code=StadiumTelCode.TSU,
            race_number=7,
            pit_number=6,
            start_course=2,
            arrival=5,
            total_time=None,
            start_time=0.1,
            winning_trick=None,
            disqualification=None,
        ),
    ]


def test_extract_race_records_from_a_race_which_has_a_tie():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20181116_18#_7R.html")
    )

    with open(file_path, mode="r") as file:
        data = extract_race_records(file)

    assert data == [
        RaceRecord(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            pit_number=1,
            start_course=1,
            arrival=1,
            total_time=111.4,
            start_time=0.1,
            winning_trick=WinningTrick.NUKI,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            pit_number=2,
            start_course=2,
            arrival=3,
            total_time=114.3,
            start_time=0.16,
            winning_trick=None,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            pit_number=3,
            start_course=3,
            arrival=4,
            total_time=114.6,
            start_time=0.15,
            winning_trick=None,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            pit_number=4,
            start_course=4,
            arrival=1,
            total_time=111.4,
            start_time=0.17,
            winning_trick=WinningTrick.NUKI,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            pit_number=5,
            start_course=5,
            arrival=6,
            total_time=None,
            start_time=0.19,
            winning_trick=None,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2018, 11, 16),
            stadium_tel_code=StadiumTelCode.TOKUYAMA,
            race_number=7,
            pit_number=6,
            start_course=6,
            arrival=5,
            total_time=None,
            start_time=0.19,
            winning_trick=None,
            disqualification=None,
        ),
    ]


def test_extract_race_records_from_a_race_which_has_four_disqualified_racers():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/20151114_02#_2R.html")
    )
    with open(file_path, mode="r") as file:
        data = extract_race_records(file)

    assert [
        RaceRecord(
            race_holding_date=date(2015, 11, 14),
            stadium_tel_code=StadiumTelCode.TODA,
            race_number=2,
            pit_number=1,
            start_course=1,
            arrival=2,
            total_time=112.7,
            start_time=0.35,
            winning_trick=None,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 14),
            stadium_tel_code=StadiumTelCode.TODA,
            race_number=2,
            pit_number=2,
            start_course=2,
            arrival=1,
            total_time=111.8,
            start_time=0.11,
            winning_trick=WinningTrick.MEGUMARE,
            disqualification=None,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 14),
            stadium_tel_code=StadiumTelCode.TODA,
            race_number=2,
            pit_number=3,
            start_course=3,
            arrival=None,
            total_time=None,
            start_time=-0.01,
            winning_trick=None,
            disqualification=Disqualification.FLYING,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 14),
            stadium_tel_code=StadiumTelCode.TODA,
            race_number=2,
            pit_number=4,
            start_course=4,
            arrival=None,
            total_time=None,
            start_time=-0.01,
            winning_trick=None,
            disqualification=Disqualification.FLYING,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 14),
            stadium_tel_code=StadiumTelCode.TODA,
            race_number=2,
            pit_number=5,
            start_course=5,
            arrival=None,
            total_time=None,
            start_time=-0.01,
            winning_trick=None,
            disqualification=Disqualification.FLYING,
        ),
        RaceRecord(
            race_holding_date=date(2015, 11, 14),
            stadium_tel_code=StadiumTelCode.TODA,
            race_number=2,
            pit_number=6,
            start_course=6,
            arrival=None,
            total_time=None,
            start_time=-0.01,
            winning_trick=None,
            disqualification=Disqualification.FLYING,
        ),
    ]


def test_extract_race_records_from_a_no_contents_page():
    file_path = os.path.normpath(
        os.path.join(base_path, "./fixtures/data_not_found.html")
    )

    with open(file_path, mode="r") as file:
        with pytest.raises(DataNotFound):
            extract_race_records(file)


def test_extract_race_records_from_a_canceled_race():
    file_path = os.path.normpath(os.path.join(base_path, "./fixtures/canceled.html"))

    with open(file_path, mode="r") as file:
        with pytest.raises(RaceCanceled):
            extract_race_records(file)
