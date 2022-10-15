import imp
import json
import logging
import os
import re
import sqlite3
import subprocess
from time import sleep

import click
from appdirs import AppDirs
import rich

from timetable_cli import selectors
from timetable_cli.application import Application, RenderConfig, TableConfig
from timetable_cli.enums import Columns
from timetable_cli.render import DEFAULT_COLUMNS_STR, get_activity_prop_str, show
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
@click.option("-c", "--columns", default=DEFAULT_COLUMNS_STR)
@click.option("--table-kwargs", default="{}")
@click.option("--ignore-time-status", is_flag=True, default=False)
@click.option("--combine-title-and-variation", is_flag=True, default=True)
@click.pass_context
def commands(context, config, db, debug, global_timedelta, **kwargs):
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
    )


@commands.command("show")
@click.argument("selectors", nargs=-1, type=str)
@click.pass_context
def show_activities(context, selectors):
    app = context.obj
    if len(selectors) == 0:
        selectors = ["0"]
    timetable = context.obj.timetable
    selectors = parse_selectors(selectors)
    logger.debug(selectors)
    for selector in selectors:
        activities = selector.get(timetable, app.now())
        logger.debug(type(activities))
        logger.debug(len(activities))
        show(activities, app, app.table_config, app.render_config)


@commands.command("watch")
@click.option("--text", default="timetable-cli")
@click.option("--interval", default=5)
@click.pass_context
def watch(context, text, interval):
    app = context.obj
    timetable = app.timetable
    previous_activity = timetable.for_datetime(app.now())
    while True:
        sleep(interval)
        current_activity = timetable.for_datetime(app.now())
        line = current_activity.line()
        if previous_activity != current_activity:
            show([current_activity], app, app.table_config)
            command = [
                "notify-send",
                "--expire-time",
                30000,
                text,
                line,
                current_activity,
            ]
            subprocess.call(command)
        previous_activity = current_activity


@commands.command("status")
@click.pass_context
def status(context):
    app = context.obj
    timetable = app.timetable
    a1 = timetable.for_datetime(app.now())
    a2 = a1.next()
    a1_title = get_activity_prop_str(a1, Columns.TITLE, app, app.render_config).strip()
    a2_title = get_activity_prop_str(a2, Columns.TITLE, app, app.render_config).strip()
    a2_eta = get_activity_prop_str(a2, Columns.ETA, app, app.render_config).strip()
    now_str = format_time(app.now())
    rich.print(f"""{now_str} {a1_title} -> {a2_title}, ETA {a2_eta}""")



if __name__ == "__main__":
    commands()
