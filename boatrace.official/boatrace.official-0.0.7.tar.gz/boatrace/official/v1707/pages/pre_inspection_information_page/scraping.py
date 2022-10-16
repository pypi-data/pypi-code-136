import re
from dataclasses import dataclass
from typing import IO, List

from boatrace.models import Gender, RacerRank
from boatrace.official.v1707.decorators import no_content_handleable
from bs4 import BeautifulSoup


@dataclass(frozen=True)
class EventEntry:
    racer_registration_number: int
    racer_last_name: str
    racer_first_name: str
    racer_rank: RacerRank
    motor_number: int
    quinella_rate_of_motor: float
    boat_number: int
    quinella_rate_of_boat: float
    anterior_time: float
    racer_gender: Gender


@no_content_handleable
def extract_event_entries(file: IO) -> List[EventEntry]:
    soup = BeautifulSoup(file, "html.parser")

    data = []
    series_entry_rows = soup.select(".table1 table tbody tr")
    pattern_of_name_delimiter = re.compile(r"[　]+")

    for row in series_entry_rows:
        cells = row.select("td")
        try:
            racer_last_name, racer_first_name = pattern_of_name_delimiter.split(
                cells[2].get_text().strip()
            )
        except ValueError:
            racer_last_name = cells[2].get_text()
            racer_first_name = ""

        data.append(
            EventEntry(
                racer_registration_number=int(cells[1].get_text()),
                racer_last_name=racer_last_name,
                racer_first_name=racer_first_name,
                racer_rank=RacerRank(cells[3].get_text().strip()),
                motor_number=int(cells[4].get_text()),
                quinella_rate_of_motor=float(cells[5].get_text().replace("%", "")),
                boat_number=int(cells[6].get_text()),
                quinella_rate_of_boat=float(cells[7].get_text().replace("%", "")),
                anterior_time=float(cells[8].get_text().replace("%", "")),
                racer_gender=Gender.FEMALE
                if row.select_one("i.is-lady")
                else Gender.MALE,
            )
        )

    return data
