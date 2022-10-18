import logging
from typing import List, Optional

import rich
from rich.box import ROUNDED
from rich.table import Table

from timetable_cli.activity import Activity
from timetable_cli.application import (Application, CategoriesRenderConfig,
                                       RenderConfig, TableConfig)
from timetable_cli.category import ActivityCategory
from timetable_cli.colorscheme import DEFAULT_COLORSCHEME
from timetable_cli.enums import ActivityTimeStatus, Columns
from timetable_cli.utils import format_time, parse_timedelta, tag

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def _columns_str_from_list(columns):
    return ",".join([str(x).lower() for x in columns])


DEFAULT_COLUMNS_STR = _columns_str_from_list(list(Columns))


def show(
    data: Activity | List[Activity],
    application: Application,
    table_config: TableConfig,
    render_config: RenderConfig,
    categories_render_config: CategoriesRenderConfig,
):
    """Display activities in a table format."""
    columns: Optional[List[Columns]] = table_config.columns
    table_kwargs: Optional[dict] = table_config.table_kwargs
    combine_title_and_variation = render_config.combine_title_and_variation

    # default kwargs
    if not isinstance(data, list):
        data = [data]
    if not table_kwargs:
        table_kwargs = {}
    if not columns:
        columns = list(Columns)
    if combine_title_and_variation:
        if Columns.VARIATION in columns:
            columns.remove(Columns.VARIATION)

    # table
    table = Table(box=ROUNDED, **table_kwargs)
    for column in columns:
        table.add_column(column.value)

    # rows
    for activity in data:
        elements = []
        for column in columns:
            element = get_activity_prop_str(
                activity, column, application, render_config
            )
            elements.append(element)
        if activity.time_status(application.now()) == ActivityTimeStatus.NOW:
            table.add_section()
            table.add_row(*elements)
            table.add_section()
        else:
            table.add_row(*elements)

    if categories_render_config.list_categories:
        show_categories_list(application.timetable.categories)
    rich.print(table)


def get_activity_prop_str(
    activity, column: Columns, application: Application, render_config: RenderConfig
) -> str:
    def add_tags(variable, colorscheme_element):
        # colorschemes
        global_colorscheme = application.colorscheme
        colorschemes = [DEFAULT_COLORSCHEME]
        if global_colorscheme:
            colorschemes.append(global_colorscheme)
        if activity.category:
            colorschemes.append(activity.category.colorscheme)
        if activity.colorscheme:
            colorschemes.append(activity.colorscheme)

        # suffix
        if render_config.ignore_time_status:
            suffix = "after"
        else:
            match activity.time_status(application.now()):
                case ActivityTimeStatus.BEFORE:
                    suffix = "before"
                case ActivityTimeStatus.NOW:
                    suffix = "now"
                case ActivityTimeStatus.AFTER:
                    suffix = "after"
                case _:
                    suffix = "after"

        # tag
        key = colorscheme_element + "_" + suffix
        tag_to_use = None
        for index, colorscheme in enumerate(colorschemes):
            try:
                tag_to_use = colorscheme[key]
                logger.debug(
                    f"Using '{key}': '{tag_to_use}' from colorscheme #'{index}'"
                )
            except KeyError:
                pass
        if not isinstance(tag_to_use, str):
            raise TypeError(
                f"No key '{key}' in colorschemes '{colorschemes}'")
        # TODO
        return tag(variable, tag_to_use)

    if activity.variation:
        variation_str = add_tags(
            str(activity.variation), "activity_variation")
    else:
        variation_str = ""

    element: str
    match column:
        case Columns.START:
            element = add_tags(
                str(format_time(
                    activity.start)), "activity_start_time")
        case Columns.END:
            element = add_tags(
                str(format_time(
                    activity.next().start)), "activity_end_time")
        case Columns.TOTAL:
            element = add_tags(
                str(parse_timedelta(
                    activity.total_time()).format_minutes()),
                "activity_total_time")
        case Columns.ETA:
            now = application.now()
            if activity.time_status(now) == ActivityTimeStatus.BEFORE:
                eta = "-"
            elif activity.time_status(now) == ActivityTimeStatus.NOW:
                eta = "now"
            else:
                eta = parse_timedelta(
                        activity.eta(application)
                        ).format_minutes()
            element = add_tags(
                str(eta), "activity_eta")
        case Columns.TITLE:
            title_str = add_tags(
                str(activity.title), "activity_title")
            if render_config.combine_title_and_variation:
                element = title_str + " " + variation_str
            else:
                element = title_str
        case Columns.VARIATION:
            element = variation_str
        case Columns.STATUS:
            element = add_tags(
                str(activity.get_status(application)), "activity_status")
    return element


def show_categories_list(
    data: List[ActivityCategory],
):
    table = Table(show_header=False, show_edge=False)
    categories_str_list: List[str] = []
    for category in data:
        colorscheme = category.colorscheme
        categories_str_list.append(
            tag(category.title,
                colorscheme[list(colorscheme.keys())[0]])
        )
    table.add_row(*categories_str_list)
    rich.print(table)
