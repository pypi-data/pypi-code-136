
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""


from typing import Callable, Type

from databases import Database
from fastapi import Depends
from starlette.requests import Request

from trove_fm.app.db.repositories.base import BaseRepository


def get_database(request: Request) -> Database:
    return request.app.state._db


def get_repository(repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(db: Database = Depends(get_database)) -> Type[BaseRepository]:
        return repo_type(db)

    return get_repo
