
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


from typing import Optional

from pydantic import constr


from trove_fm.app.models.core import CoreModel, DateTimeModelMixin, IDModelMixin
from trove_fm.app.models.profile import CompanyProfilePublic


class CompanyBase(CoreModel):
    """
    Basic company information
    """
    company_name: Optional[constr(max_length=100)]
    office: Optional[constr(max_length=40)]
    relationship: Optional[constr(max_length=20)]


class CompanyCreate(CompanyBase):
    """
    Used when creating a person through the CMS interface
    """
    company_id: Optional[int]  # The id of the parent company record, if this is a division or regional office


class CompanyInDB(IDModelMixin, DateTimeModelMixin, CompanyBase):
    """
    Add in id, created_at, updated_at, and company_id foreign key
    """
    active: bool = False
    company_id: Optional[int]  # The id of the parent company record, if this is a division or regional office
    profile: Optional[CompanyProfilePublic]


class CompanyPublic(IDModelMixin, DateTimeModelMixin, CompanyBase):
    profile: Optional[CompanyProfilePublic]
