
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


from databases import Database


class BaseRepository:
    """
    Our BaseRepository will be a simple class needed only to keep a reference
    to our database connection. In the future we can add functionality for
    common db actions, but we'll keep it lightweight for now.
    """

    def __init__(self, db: Database) -> None:
        self.db = db
