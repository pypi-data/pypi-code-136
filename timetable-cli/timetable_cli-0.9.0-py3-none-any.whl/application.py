import datetime
import logging
import sqlite3
from dataclasses import dataclass, field
from types import ModuleType
from typing import Any, List, Optional

from timetable_cli.enums import Columns
from timetable_cli.selectors import DEFAULT_SHORTCUTS
from timetable_cli.utils import check_colorscheme, now

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dataclass
class CategoriesRenderConfig:
    list_categories: bool


@dataclass
class TableConfig:
    columns: List[Columns]
    table_kwargs: dict = field(default_factory=dict)


@dataclass
class RenderConfig:
    ignore_time_status: bool = False
    combine_title_and_variation: bool = False


@dataclass
class Application:
    timetable: Any
    colorscheme: dict
    shortcuts: dict
    connection: sqlite3.Connection
    global_timedelta: datetime.timedelta
    table_config: TableConfig
    render_config: RenderConfig
    config_module: ModuleType
    categories_render_config: CategoriesRenderConfig
    rules: Optional[List[str]] = None
    quotes: Optional[List[str]] = None

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
        render_config: RenderConfig,
        categories_render_config: CategoriesRenderConfig,
    ):
        timetable = config_module.get_timetable(
            now(global_timedelta))

        try:
            colorscheme = config_module.get_colorscheme()
            check_colorscheme(colorscheme)
        except AttributeError:
            colorscheme = {}

        try:
            shortcuts = config_module.get_shortcuts()
        except AttributeError:
            shortcuts = DEFAULT_SHORTCUTS
        try:
            rules = config_module.get_rules()
        except AttributeError:
            rules = None
        try:
            quotes = config_module.get_quotes()
        except AttributeError:
            quotes = None
        return cls(
            timetable=timetable,
            colorscheme=colorscheme,
            shortcuts=shortcuts,
            rules=rules,
            quotes=quotes,
            config_module=config_module,
            connection=connection,
            global_timedelta=global_timedelta,
            table_config=table_config,
            render_config=render_config,
            categories_render_config=categories_render_config,
        )
