# Heath --- Manage projections
# Copyright © 2022 Bioneland
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

from typing import Callable

from bl_event_sourcing.core import Status
from bl_event_sourcing_sqlalchemy.core import LEDGER_REGISTRY, Ledger
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore


class UnknownProjection(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Unknown projection `{name}`!")


def session_maker(dsn: str) -> sessionmaker:
    return sessionmaker(bind=create_engine(dsn))()


def initialise(dsn: str) -> None:
    LEDGER_REGISTRY.metadata.create_all(create_engine(dsn))


def status(dsn: str, echo: Callable[[str], None]) -> None:
    with session_maker(dsn) as session:
        ledger = Ledger(session)
        ledger.status(
            lambda status, name, position: echo(
                f"[{status}] {name} at position {position}."
            )
        )


def purge(dsn: str, name: str) -> None:
    with session_maker(dsn) as session:
        ledger = Ledger(session)
        if not ledger.knows(name):
            raise UnknownProjection(name)

        ledger.forget(name)
        create_engine(dsn).connect().execute(f"DROP TABLE IF EXISTS {name}")
        session.commit()


def stall(dsn: str, name: str) -> None:
    with session_maker(dsn) as session:
        ledger = Ledger(session)
        if not ledger.knows(name):
            raise UnknownProjection(name)

        ledger.mark_as(name, Status.STALLED)
        session.commit()
