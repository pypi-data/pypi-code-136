# Estory --- Read from and write to event stores
# Copyright © 2021, 2022 Bioneland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import json
import os
import re
import sys
from dataclasses import asdict
from pathlib import Path

import pkg_resources
import typer
from bl_event_sourcing.core import Event
from bl_event_sourcing_sqlalchemy.core import EVENT_REGISTRY, EventStore
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import Session, sessionmaker  # type: ignore

__version__ = pkg_resources.get_distribution(__name__).version
app = typer.Typer()


class CannotGuessDsn(Exception):
    pass


@app.command()
def guess(dsn: str) -> None:
    typer.echo(guess_real_dsn(dsn))


@app.command()
def init(dsn: str) -> None:
    try:
        real_dsn = guess_real_dsn(dsn)
    except CannotGuessDsn:
        path = Path(dsn)
        path.touch()
        real_dsn = f"sqlite:///{dsn}"

    EVENT_REGISTRY.metadata.create_all(create_engine(real_dsn))


@app.command()
def read(dsn: str) -> None:
    store = build_store(build_session(guess_real_dsn(dsn)))
    for event in store.get_stream():
        e = asdict(event)
        typer.echo(json.dumps(e))


@app.command()
def write(dsn: str) -> None:
    session = build_session(guess_real_dsn(dsn))
    store = build_store(session)
    for line in sys.stdin:
        data = json.loads(line.strip())
        event = Event(**data)
        store.record(event)
        # FIXME speed up insertion!
        # https://docs.sqlalchemy.org/en/14/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow
        session.commit()


def guess_real_dsn(dsn: str) -> str:
    if real_dsn := guess_real_dsn_from_env(dsn):
        return real_dsn
    if real_dsn := guess_real_dsn_from_uri(dsn):
        return real_dsn
    if real_dsn := guess_real_dsn_from_file(dsn):
        return real_dsn
    raise CannotGuessDsn(dsn)


def guess_real_dsn_from_env(dsn: str) -> str:
    if uri := os.environ.get(f"ESTORY_DSN_{dsn}"):
        return uri
    return ""


def guess_real_dsn_from_uri(dsn: str) -> str:
    if re.search(r"^[^:]+://.+$", dsn):
        return dsn
    return ""


def guess_real_dsn_from_file(dsn: str) -> str:
    if Path(dsn).exists():
        return f"sqlite:///{dsn}"
    return ""


def build_session(dsn: str) -> Session:
    with sessionmaker(bind=create_engine(dsn))() as session:
        with session.begin():
            return session


def build_store(session: Session) -> EventStore:
    return EventStore(session)
