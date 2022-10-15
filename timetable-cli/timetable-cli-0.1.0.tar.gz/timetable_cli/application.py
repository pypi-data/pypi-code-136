import datetime
import logging
import sqlite3
from dataclasses import dataclass, field
from types import ModuleType
from typing import Any, List

from timetable_cli import default_config
from timetable_cli.enums import Columns
from timetable_cli.utils import check_colorscheme, now

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dataclass
class TableConfig:
    columns: List[Columns]
    combine_title_and_variation: bool
    ignore_time_status: bool
    table_kwargs: dict = field(default_factory=dict)


@dataclass
class Application:
    timetable: Any
    colorscheme: dict
    shortcuts: dict
    connection: sqlite3.Connection
    global_timedelta: datetime.timedelta
    table_config: TableConfig

    def today(self):
        return self.now().date()

    def now(self):
        return datetime.datetime.now() + self.global_timedelta

    @classmethod
    def from_config_module(
        cls,
        config_module: ModuleType,
        connection: sqlite3.Connection,
        global_timedelta: datetime.timedelta,
        table_config: TableConfig,
    ):
        try:
            timetable = config_module.get_timetable(
                now(global_timedelta))
        except AttributeError:
            timetable = default_config.get_timetable(
                now(global_timedelta))

        try:
            colorscheme = config_module.get_colorscheme()
            check_colorscheme(colorscheme)
        except AttributeError:
            colorscheme = {}

        try:
            shortcuts = config_module.get_shortcuts()
        except AttributeError:
            shortcuts = default_config.get_shortcuts()
        return cls(
            timetable=timetable,
            colorscheme=colorscheme,
            shortcuts=shortcuts,
            connection=connection,
            global_timedelta=global_timedelta,
            table_config=table_config,
        )
