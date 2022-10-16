import re
from dataclasses import dataclass
from datetime import datetime
from typing import IO, List, Optional

from boatrace.models import RaceLaps, RacerRank, StadiumTelCode
from boatrace.official.exceptions import ScrapingError
from boatrace.official.v1707.decorators import no_content_handleable
from boatrace.official.v1707.factories import RaceLapsFactory
from boatrace.official.v1707.pages.race.utils import parse_race_key_attributes
from bs4 import BeautifulSoup


@dataclass(frozen=True)
class RaceInformation:
    race_holding_date: datetime.date
    stadium_tel_code: StadiumTelCode
    race_number: int
    title: str
    race_laps: RaceLaps
    deadline_at: datetime
    is_course_fixed: bool
    use_stabilizer: bool


@dataclass(frozen=True)
class RaceEntry:
    race_holding_date: datetime.date
    stadium_tel_code: StadiumTelCode
    race_number: int
    racer_registration_number: int
    racer_first_name: str
    racer_last_name: str
    current_racer_rating: RacerRank
    pit_number: int  # todo: enum で持つべき？
    is_absent: bool
    motor_number: int
    boat_number: int


@dataclass(frozen=True)
class BoatPerformance:
    recorded_date: datetime.date
    number: int
    quinella_rate: Optional[float]
    trio_rate: Optional[float]


@dataclass(frozen=True)
class MotorPerformance:
    recorded_date: datetime.date
    number: int
    quinella_rate: Optional[float]
    trio_rate: Optional[float]


@no_content_handleable
def extract_race_information(file: IO) -> RaceInformation:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)
    race_holding_date = race_key_attributes["race_holding_date"]
    stadium_tel_code = race_key_attributes["stadium_tel_code"]
    race_number = race_key_attributes["race_number"]

    deadline_table = soup.select_one(".table1")
    deadline_text = (
        deadline_table.select("tbody tr")[-1].select("td")[race_number].get_text()
    )
    hour, minute = [int(t) for t in deadline_text.split(":")]
    deadline_at = datetime(
        race_holding_date.year,
        race_holding_date.month,
        race_holding_date.day,
        hour,
        minute,
    )

    if m := re.match(
        r"(\w+)\s*(1200|1800)m",
        soup.select_one("h3.title16_titleDetail__add2020").get_text().strip(),
    ):
        title = m.group(1)
        metre = int(m.group(2))
    else:
        raise ScrapingError

    return RaceInformation(
        race_holding_date=race_holding_date,
        stadium_tel_code=stadium_tel_code,
        race_number=race_number,
        title=title,
        race_laps=RaceLapsFactory.create(metre),
        deadline_at=deadline_at,
        is_course_fixed="進入固定" in soup.body.get_text(),
        use_stabilizer="安定板使用" in soup.body.get_text(),
    )


@no_content_handleable
def extract_race_entries(file: IO) -> List[RaceEntry]:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)

    data = []
    for pit_number, row in enumerate(soup.select(".table1")[-1].select("tbody"), 1):
        racer_photo_path = row.select_one("tr").select("td")[1].select_one("img")["src"]
        if m := re.search(r"(\d+)\.jpe?g$", racer_photo_path):
            racer_registration_number = int(m.group(1))
        else:
            raise ScrapingError

        racer_full_name = (
            row.select_one("tr").select("td")[2].select_one("a").text.strip()
        )
        racer_last_name, racer_first_name = re.split(r"[　 ]+", racer_full_name)

        racer_rank = RacerRank(
            row.select_one("tr").select("td")[2].select_one("span").text.strip()
        )

        motor_number = int(row.select_one("tr").select("td")[6].text.strip().split()[0])
        boat_number = int(row.select_one("tr").select("td")[7].text.strip().split()[0])

        is_absent = "is-miss" in row["class"]

        data.append(
            RaceEntry(
                **race_key_attributes,
                racer_registration_number=racer_registration_number,
                racer_last_name=racer_last_name,
                racer_first_name=racer_first_name,
                pit_number=pit_number,
                current_racer_rating=racer_rank,
                is_absent=is_absent,
                motor_number=motor_number,
                boat_number=boat_number,
            )
        )

    return data


@no_content_handleable
def extract_boat_performances(file: IO) -> List[BoatPerformance]:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)

    PLACE_HOLDER_OF_UNRECORDED_DATA = "-"

    data = []
    for _, row in enumerate(soup.select(".table1")[-1].select("tbody"), 1):
        data_strings = row.select_one("tr").select("td")[7].text.strip().split()
        number = int(data_strings[0])
        quinella_rate = (
            float(data_strings[1])
            if data_strings[1] != PLACE_HOLDER_OF_UNRECORDED_DATA
            else None
        )
        trio_rate = (
            float(data_strings[2])
            if data_strings[2] != PLACE_HOLDER_OF_UNRECORDED_DATA
            else None
        )

        data.append(
            BoatPerformance(
                recorded_date=race_key_attributes["race_holding_date"],
                number=number,
                quinella_rate=quinella_rate,
                trio_rate=trio_rate,
            )
        )

    return data


@no_content_handleable
def extract_motor_performances(file: IO) -> List[MotorPerformance]:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)

    PLACE_HOLDER_OF_UNRECORDED_DATA = "-"

    data = []
    for _, row in enumerate(soup.select(".table1")[-1].select("tbody"), 1):
        motor_data_strings = row.select_one("tr").select("td")[6].text.strip().split()
        number = int(motor_data_strings[0])
        quinella_rate = (
            float(motor_data_strings[1])
            if motor_data_strings[1] != PLACE_HOLDER_OF_UNRECORDED_DATA
            else None
        )
        trio_rate = (
            float(motor_data_strings[2])
            if motor_data_strings[2] != PLACE_HOLDER_OF_UNRECORDED_DATA
            else None
        )

        data.append(
            MotorPerformance(
                recorded_date=race_key_attributes["race_holding_date"],
                number=number,
                quinella_rate=quinella_rate,
                trio_rate=trio_rate,
            )
        )

    return data
