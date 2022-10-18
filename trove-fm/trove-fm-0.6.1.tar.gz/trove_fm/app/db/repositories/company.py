
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


from asyncpg.exceptions import UniqueViolationError
from databases import Database
from fastapi import HTTPException
from loguru import logger

from trove_fm.app.db.repositories.base import BaseRepository
from trove_fm.app.models.company import CompanyCreate, CompanyInDB


CREATE_NEW_COMPANY_QUERY = """
    INSERT INTO company(company_id, company_name, relationship, office, logo_file)
    VALUES (:company_id, :company_name, :relationship, :office, :logo_file)
    RETURNING id, company_id, company_name, relationship, office, logo_file
"""


class CompanyRepository(BaseRepository):
    def __init__(self, db: Database) -> None:
        """
        By adding the ProfilesRepository as a sub-repo of the PersonRepository,
        we can insert any profile-related logic directly into our person-related logic.
        """
        super().__init__(db)
        # self.profile_repo = PersonProfileRepository(db)

    async def create_new_company(self, new_company: CompanyCreate) -> CompanyInDB:
        try:
            created_company = await self.db.fetch_one(
                query=CREATE_NEW_COMPANY_QUERY, values=new_company.dict()
            )
        except UniqueViolationError:
            detail = f"The {new_company.office} office of {new_company.company_name} already exists in the database."
            logger.error(detail)
            raise HTTPException(status_code=409, detail=detail)

        return CompanyInDB(**dict(created_company._mapping.items()))
