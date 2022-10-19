#      A python library for getting Load Shedding schedules.
#      Copyright (C) 2021  Werner Pieterson
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
from datetime import timezone, timedelta, datetime
from typing import List, Tuple

from load_shedding.libs import sepush, citypower
from load_shedding.providers import dict_list_to_obj_list, ProviderError, to_utc, Province
from load_shedding.providers import Area, Stage, Provider


class Area(Area):
    def __init__(self, /, **kwargs) -> object:
        self.id: str = kwargs.get("id", "")
        self.name: str = kwargs.get("name", "")
        self.municipality: str = kwargs.get("region", "")
        self.province: Province = Province.from_name(kwargs.get("ProvinceName", ""))


class SePush(Provider):
    name = "SePush"

    def __init__(self, token: str = "") -> object:
        if not token:
            raise ProviderError(f"Invalid Provider Token.")
        else:
            self.api = sepush.SePush(token)

    def get_areas(self, search_text: str = None, max_results: int = None) -> List[Area]:
        try:
            areas = self.api.areas_search(search_text)
        except Exception as e:
            raise ProviderError(e)
        else:
            areas = dict_list_to_obj_list(areas.get("areas"), Area)
            return filter_empty_areas(areas)

    def get_area_schedule(self, area: Area, stage: Stage) -> List[Tuple]:
        try:
            area_schedule = self.api.area(area_id=area.id)
        except Exception as e:
            raise ProviderError(e)
        else:
            schedule = []
            events = area_schedule.get("events", {})
            if not events:
                return schedule

            note = events[0].get("note")
            parts = str(note).split(" ")
            stage = Stage(int(parts[1]))

            sast = timezone(timedelta(hours=+2), 'SAST')
            for day in area_schedule.get("schedule", {}).get("days", []):
                date = datetime.strptime(day.get("date"), "%Y-%m-%d")
                stages = day.get("stages", [])
                if len(stages) < stage.value:
                    continue
                for slot in stages[stage.value]:
                    start_str, end_str = slot.strip().split("-")
                    start = datetime.strptime(start_str, "%H:%M").replace(
                        year=date.year, month=date.month, day=date.day, second=0, microsecond=0, tzinfo=sast
                    )
                    end = datetime.strptime(end_str, "%H:%M").replace(
                        year=date.year, month=date.month, day=date.day, second=0, microsecond=0, tzinfo=sast
                    )
                    if end < start:
                        end = end + timedelta(days=1)
                    schedule.append((start, end))

            schedule = to_utc(schedule)
            return schedule

    def get_stage(self, coct_stage: bool = False) -> Stage:
        try:
            data = self.get_stages()
            stage = data.get(Provider.ESKOM)
            if coct_stage:
                stage = data.get(Provider.COCT)
        except Exception as e:
            raise ProviderError(e)
        else:
            return stage

    def get_stages(self) -> dict:
        stages = {
            Provider.COCT: Stage.UNKNOWN,
            Provider.ESKOM: Stage.UNKNOWN,
        }
        try:
            data = self.api.status()
            status = data.get("status")

            eskom_stage = status.get("eskom", {}).get("stage", 0)
            stages[Provider.ESKOM] = Stage(int(eskom_stage))

            coct_stage = status.get("capetown", {}).get("stage", 0)
            stages[Provider.COCT] = Stage(int(coct_stage))
        except Exception as e:
            raise ProviderError(e)
        else:
            return stages

    def get_stage_forecast(self) -> List:
        """ Get Stage forecast from City Power."""
        try:
            stage_forecast = citypower.get_stage_forecast()

            for i in range(len(stage_forecast)):
                stage_forecast[i]["stage"] = Stage(stage_forecast[i].get("stage"))
                stage_forecast[i]["start_time"] = stage_forecast[i]["start_time"].astimezone(timezone.utc)
                stage_forecast[i]["end_time"] = stage_forecast[i]["end_time"].astimezone(timezone.utc)
        except Exception as e:
            raise ProviderError(e)
        else:
            return stage_forecast


# def stage_from_status(status: int) -> Stage:
#     return {
#         1: Stage.NO_LOAD_SHEDDING,
#         2: Stage.STAGE_1,
#         3: Stage.STAGE_2,
#         4: Stage.STAGE_3,
#         5: Stage.STAGE_4,
#         6: Stage.STAGE_5,
#         7: Stage.STAGE_6,
#         8: Stage.STAGE_7,
#         9: Stage.STAGE_8,
#     }.get(status, Stage.UNKNOWN)


def filter_empty_areas(suburbs: List[Area]) -> List[Area]:
    filtered: List[Area] = []
    for area in suburbs:
        if hasattr(area, "total") and not area.total:
            continue
        filtered.append(area)
    return filtered
