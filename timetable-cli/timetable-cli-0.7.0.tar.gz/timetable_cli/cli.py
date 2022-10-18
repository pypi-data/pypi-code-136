import imp
import json
import logging
import os
import platform
import sqlite3
import subprocess
from time import sleep

import click
import rich
from rich.box import ROUNDED
from appdirs import AppDirs
from rich.table import Table

from timetable_cli import selectors
from timetable_cli.application import (Application, CategoriesRenderConfig,
                                       RenderConfig, TableConfig)
from timetable_cli.enums import Columns
from timetable_cli.render import (DEFAULT_COLUMNS_STR, get_activity_prop_str,
                                  show)
from timetable_cli.selectors import parse_selectors
from timetable_cli.utils import format_time, parse_timedelta_str

appdirs = AppDirs(appname="timetable_cli")
_default_config_dir = appdirs.user_config_dir
_default_config_file = os.path.join(_default_config_dir, "config.py")
_default_state_dir = appdirs.user_state_dir
_default_db = os.path.join(_default_state_dir, "db.sqlite3")


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_db_connection(db_filename):
    connection = sqlite3.connect(
        db_filename, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )
    cursor = connection.cursor()
    cursor.executescript(
        """
CREATE TABLE IF NOT EXISTS records (
    id int PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status int NOT NULL,
    date TIMESTAMP
)"""
    )
    connection.commit()
    return connection


@click.group()
@click.option("--config", required=True, default=_default_config_file)
@click.option("--db", required=True, default=_default_db)
@click.option("--debug", default=False, is_flag=True)
@click.option("-d", "--global-timedelta", default="")
@click.option("--list-categories", is_flag=True, default=True)
@click.option("-c", "--columns", default=DEFAULT_COLUMNS_STR)
@click.option("--table-kwargs", default="{}")
@click.option("-T", "--ignore-time-status", is_flag=True, default=False)
@click.option("--combine-title-and-variation", is_flag=True, default=True)
@click.pass_context
def commands(context, config, db, debug, global_timedelta, list_categories, **kwargs):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    config_module = imp.load_source("config_module", config)
    selectors.ShortcutSelector.shortcuts.update(
        config_module.get_shortcuts())
    connection = get_db_connection(db)
    context.obj = Application.from_config_module(
        config_module,
        connection=connection,
        global_timedelta=parse_timedelta_str(global_timedelta),
        table_config=TableConfig(
            table_kwargs=json.loads(kwargs["table_kwargs"]),
            columns=Columns.parse_str(kwargs["columns"]),
        ),
        render_config=RenderConfig(
            ignore_time_status=kwargs["ignore_time_status"],
            combine_title_and_variation=kwargs["combine_title_and_variation"],
        ),
        categories_render_config=CategoriesRenderConfig(
            list_categories=list_categories,
        ),
    )


@commands.command("show")
@click.argument("selectors", nargs=-1, type=str)
@click.pass_context
def show_activities(context, selectors):
    select_and_show_activities(context, selectors)


def select_and_show_activities(context, selectors):
    app = context.obj
    if len(selectors) == 0:
        selectors = ["0"]
    timetable = context.obj.timetable
    selectors = parse_selectors(selectors)
    logger.debug(selectors)
    activities = []
    for selector in selectors:
        activities += selector.get(timetable, app.now())
    show(
        activities,
        app,
        app.table_config,
        app.render_config,
        app.categories_render_config,
    )


@commands.command("watch")
@click.option("--text", default="timetable-cli")
@click.option("--interval", default=5)
@click.option("--notification", default=False, is_flag=True)
@click.option("--notification-cmd", default="notify-send --expire-time 60000")
@click.option("--voice", default=False, is_flag=True)
@click.option("--voice-cmd", default="espeak -s 0.1 -g 5 -p 1")
@click.option("--notify-eta", default="120m 60m 30m")
@click.option("--table-selectors", default="-3..3")
@click.pass_context
def watch(
    context: click.Context,
    text,
    interval,
    notification,
    notification_cmd,
    voice,
    voice_cmd,
    notify_eta,
    table_selectors,
):
    app = context.obj
    timetable = app.timetable
    previous_activity = timetable.for_datetime(app.now())
    while True:
        clear_screen()
        show_time_and_date(app)
        # show_status(app, timetable)
        rich.print("")
        current_activity = timetable.for_datetime(app.now())
        next_activity = current_activity.next()
        title = current_activity.title
        if current_activity.variation:
            title += " " + current_activity.variation
        if notify_eta:
            if current_activity != timetable[-1]:
                eta = next_activity.eta(app)
                if eta in notify_eta.split():
                    if notification:
                        command = notification_cmd.split()
                        command.extend(
                            [f'"{text}"', f'"{title}, ETA is {eta}"'])
                        subprocess.call(command)
                    if voice:
                        command = voice_cmd.split()
                        command.extend(
                            [f'"{text} says {title}, ETA is {eta}"'])
                        subprocess.call(command)
        if previous_activity != current_activity:
            if notification:
                command = notification_cmd.split()
                command.extend([f'"{text}"', f'"{title}"'])
                subprocess.call(command)
            if voice:
                command = voice_cmd.split()
                command.extend([f'"{text} says {title}"'])
                subprocess.call(command)
        previous_activity = current_activity
        select_and_show_activities(context, table_selectors.split())
        sleep(interval)


@commands.command("status")
@click.pass_context
def status(context):
    app = context.obj
    timetable = app.timetable
    show_status(app, timetable)


def show_time_and_date(app):
    table = Table(
            # show_edge=False,
            show_header=False,
            box=ROUNDED
            )
    table.add_row(
            app.now().time().isoformat()[:5],
            app.now().date().isoformat()
            )
    rich.print(table)


def show_status(app: Application, timetable):
    activity_1 = timetable.for_datetime(app.now())
    activity_2 = activity_1.next()
    a1_title = get_activity_prop_str(
        activity_1, Columns.TITLE, app, app.render_config
    ).strip()
    a2_title = get_activity_prop_str(
        activity_2, Columns.TITLE, app, app.render_config
    ).strip()
    a2_eta = get_activity_prop_str(
        activity_2, Columns.ETA, app, app.render_config
    ).strip()
    table = Table(show_header=False, show_edge=False, box=ROUNDED)
    table.add_row(
            # app.now().time().isoformat()[:5],
            a1_title,
            "ETA " + a2_eta,
            a2_title,
        )
    rich.print(table)


def clear_screen():
    if platform.system() == "Linux":
        subprocess.call("clear")
    else:
        raise ValueError


if __name__ == "__main__":
    commands()
