
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


from fastapi import APIRouter, Body, Depends, status

from trove_fm.app.api.dependencies.auth import staff_auth
from trove_fm.app.api.dependencies.database import get_repository
from trove_fm.app.db.repositories.company import CompanyRepository
from trove_fm.app.models.company import CompanyCreate, CompanyInDB, CompanyPublic


router = APIRouter()


@router.post(
    "/",
    name="company:create-new-company",
    dependencies=[Depends(staff_auth)],
    response_model=CompanyPublic,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_company(
    new_company: CompanyCreate = Body(..., embed=True),
    company_repo: CompanyRepository = Depends(get_repository(CompanyRepository)),
) -> CompanyPublic:
    created_company = await company_repo.create_new_company(new_company=new_company)

    return created_company
