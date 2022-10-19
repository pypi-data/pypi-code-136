"""Models for alarm."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import time
from enum import Enum, IntEnum
from typing import TypedDict

from ..const import ATTR_COLOR, ATTR_ID, ATTR_NAME, ATTR_REPEAT, ATTR_SOUND, ATTR_VOLUME
from .color import Color, ColorDict


class RepeatDayOfWeek(str, Enum):
    """Day of the week to repeat alarm enum."""

    MONDAY = "Mo"
    TUESDAY = "Tu"
    WEDNESDAY = "We"
    THURSDAY = "Th"
    FRIDAY = "Fr"
    SATURDAY = "Sa"
    SUNDAY = "Su"


class AlarmSource(IntEnum):
    """Alarm source enum."""

    SYSTEM = 0
    APP = 1
    ALEXA = 2


class AlarmDict(TypedDict):
    """Representation of an alarm."""

    id: int
    name: str
    time_hr: int
    time_min: int
    repeat: str
    color: ColorDict
    volume: int
    status: int
    src: int
    sound: str


@dataclass
class Alarm:
    """Alarm class."""

    id: int
    name: str
    time: time
    repeat: list[RepeatDayOfWeek]
    color: Color
    volume: int
    enabled: bool
    src: AlarmSource
    sound: str

    def update(self, alarm: Alarm) -> None:
        """Update alarm."""
        self.name = alarm.name
        self.time = alarm.time
        self.repeat = alarm.repeat
        self.color = alarm.color
        self.volume = alarm.volume
        self.enabled = alarm.enabled
        self.src = alarm.src
        self.sound = alarm.sound

    def to_dict(self) -> AlarmDict:
        """Convert Alarm to AlarmDict."""
        return {
            ATTR_ID: self.id,
            ATTR_NAME: self.name,
            "time_hr": self.time.hour,
            "time_min": self.time.minute,
            ATTR_REPEAT: "".join([day_of_week.value for day_of_week in self.repeat]),
            ATTR_COLOR: {
                "red": self.color.red,
                "green": self.color.green,
                "blue": self.color.blue,
            },
            ATTR_VOLUME: self.volume,
            "status": self.enabled == 1,
            "src": self.src.value,
            ATTR_SOUND: self.sound,
        }

    @staticmethod
    def from_dict(alarm_dict: AlarmDict) -> "Alarm":
        """Create Alarm from dict."""
        repeat = alarm_dict["repeat"].replace("0", "")
        return Alarm(
            id=alarm_dict[ATTR_ID],
            name=alarm_dict[ATTR_NAME],
            time=time(hour=alarm_dict["time_hr"], minute=alarm_dict["time_min"]),
            repeat=[
                RepeatDayOfWeek(day)
                for day in [
                    alarm_dict[ATTR_REPEAT][i : i + 2]
                    for i in range(0, len(repeat), 2)
                    if alarm_dict[ATTR_REPEAT][i : i + 2]
                ]
            ],
            color=Color.from_dict(alarm_dict[ATTR_COLOR]),
            volume=alarm_dict[ATTR_VOLUME],
            enabled=1 if alarm_dict["status"] else 10,
            src=AlarmSource(alarm_dict["src"]),
            sound=alarm_dict[ATTR_SOUND],
        )
