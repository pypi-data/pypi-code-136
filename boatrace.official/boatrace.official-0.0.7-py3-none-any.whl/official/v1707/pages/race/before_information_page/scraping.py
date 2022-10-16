import re
from dataclasses import dataclass
from datetime import date
from typing import IO, List

from boatrace.models import MotorParts, StadiumTelCode
from boatrace.official.exceptions import DataNotFound
from boatrace.official.v1707.decorators import (
    no_content_handleable,
    race_cancellation_handleable,
)
from boatrace.official.v1707.factories import MotorPartsFactory
from boatrace.official.v1707.pages.race.common import (
    WeatherCondition,
    extract_weather_condition_base_data,
)
from boatrace.official.v1707.pages.race.utils import parse_race_key_attributes
from bs4 import BeautifulSoup


@dataclass(frozen=True)
class StartExhibitionRecord:
    race_holding_date: date
    stadium_tel_code: StadiumTelCode
    race_number: int
    pit_number: int
    start_course: int
    start_time: float


@dataclass(frozen=True)
class CircumferenceExhibitionRecord:
    race_holding_date: date
    stadium_tel_code: StadiumTelCode
    race_number: int
    pit_number: int
    exhibition_time: float


@dataclass(frozen=True)
class RacerCondition:
    recorded_on: date
    racer_registration_number: int
    weight: int
    adjust: float


@dataclass(frozen=True)
class BoatSetting:
    race_holding_date: date
    stadium_tel_code: StadiumTelCode
    race_number: int
    pit_number: int
    tilt: float
    is_new_propeller: bool
    motor_parts_exchanges: List[tuple[MotorParts, int]]


@no_content_handleable
@race_cancellation_handleable
def extract_start_exhibition_records(file: IO) -> List[StartExhibitionRecord]:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)

    data = []
    for start_course, row in enumerate(soup.select(".table1")[2].select("tbody tr"), 1):
        if row.select_one("img") is None:
            # 画像がない場合は出遅れか展示不出走
            #
            # 出遅れが発生した展示
            # http://boatrace.jp/owpc/pc/race/beforeinfo?rno=2&jcd=17&hd=20170511
            continue

        m = re.search(r"_([1-6]{1}).png$", row.select_one("img")["src"])
        pit_number = int(m.group(1))

        start_time_element = row.select("span")[-1]
        if m := re.search(r"F?\.(\d{2})$", start_time_element.text):
            start_time = float(f"0.{m.group(1)}")
        else:
            raise ValueError

        if "is-fBold" in start_time_element["class"]:
            # この場合はフライング
            start_time = start_time * -1

        data.append(
            StartExhibitionRecord(
                **race_key_attributes,
                pit_number=pit_number,
                start_course=start_course,
                start_time=start_time,
            )
        )

    return data


@no_content_handleable
@race_cancellation_handleable
def extract_circumference_exhibition_records(
    file: IO,
) -> List[CircumferenceExhibitionRecord]:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)

    data = []
    for pit_number, row in enumerate(soup.select(".table1")[1].select("tbody"), 1):
        if "is-miss" in row["class"]:
            # 欠場
            continue

        try:
            exhibition_time = float(row.select("td")[4].text)
        except TypeError:
            # 欠場じゃなくても展示だけ不参加とか展示中に転覆とかだとNoneをfloatで評価した結果ここに来るかも？
            continue

        data.append(
            CircumferenceExhibitionRecord(
                **race_key_attributes,
                pit_number=pit_number,
                exhibition_time=exhibition_time,
            )
        )

    return data


@no_content_handleable
@race_cancellation_handleable
def extract_racer_conditions(file: IO) -> List[RacerCondition]:
    soup = BeautifulSoup(file, "html.parser")

    # hack: 欲しいのは日付だけで場コードと何レース目かは不要なんだけどいったんこれで
    race_key_attributes = parse_race_key_attributes(soup)

    data = []
    for row in soup.select(".table1")[1].select("tbody"):
        if "is-miss" in row["class"]:
            # 欠場
            continue

        if m := re.search(
            r"toban=(\d{4})$", row.select("td")[2].select_one("a")["href"]
        ):
            racer_registration_number = int(m.group(1))
        else:
            raise ValueError

        weight = float(row.select("td")[3].text[:-2])
        adjust = float(row.select("td")[12].text)

        data.append(
            RacerCondition(
                recorded_on=race_key_attributes["race_holding_date"],
                racer_registration_number=racer_registration_number,
                weight=weight,
                adjust=adjust,
            )
        )

    return data


@no_content_handleable
@race_cancellation_handleable
def extract_boat_settings(file: IO) -> BoatSetting:
    NEW_PROPELLER_MARK = "新"
    MOTOR_PARTS_QUANTITY_DELIMITER = "×"

    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)
    race_holding_date = race_key_attributes["race_holding_date"]
    stadium_tel_code = race_key_attributes["stadium_tel_code"]
    race_number = race_key_attributes["race_number"]

    data = []

    for pit_number, row in enumerate(soup.select(".table1")[1].select("tbody"), 1):
        if "is-miss" in row["class"]:
            continue

        try:
            tilt = float(row.select("td")[5].text)
            is_new_propeller = row.select("td")[6].text.strip() == NEW_PROPELLER_MARK
        except ValueError:
            raise DataNotFound

        numbers = dict(zip(["１", "２", "３", "４", "５", "６", "７", "８", "９"], range(1, 10)))
        motor_parts_exchanges = []
        for li in row.select("td")[7].select("li"):
            if MOTOR_PARTS_QUANTITY_DELIMITER in li.get_text():
                parts_name, quantity_text = li.get_text().split(
                    MOTOR_PARTS_QUANTITY_DELIMITER
                )
            else:
                parts_name = li.get_text()
                quantity_text = None

            motor_parts_exchanges.append(
                (MotorPartsFactory.create(parts_name), numbers.get(quantity_text, 1))
            )

        data.append(
            BoatSetting(
                race_holding_date=race_holding_date,
                stadium_tel_code=stadium_tel_code,
                race_number=race_number,
                pit_number=pit_number,
                tilt=tilt,
                is_new_propeller=is_new_propeller,
                motor_parts_exchanges=motor_parts_exchanges,
            )
        )

    return data


@no_content_handleable
@race_cancellation_handleable
def extract_weather_condition(file: IO) -> WeatherCondition:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)

    file.seek(0)
    weather_condition_base_attributes = extract_weather_condition_base_data(file)

    return WeatherCondition(
        **race_key_attributes,
        **weather_condition_base_attributes,
        in_performance=False,
    )
