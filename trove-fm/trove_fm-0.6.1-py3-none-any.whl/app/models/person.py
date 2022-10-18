
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

from datetime import datetime
from enum import Enum, IntEnum
from typing import Optional

from pydantic import constr, EmailStr, root_validator


from trove_fm.app.models.core import CoreModel, DateTimeModelMixin, IDModelMixin
from trove_fm.app.models.profile import PersonProfileCreate, PersonProfilePublic


class AppRole(IntEnum):
    ADMIN = 90     # Full priviledges
    POWER = 80     # Manage users, issue refunds, run reports, manage inventory
    STAFF = 60     # Manage time, modify/process orders
    VENDOR = 40    # Supply compliance/quality assurance data, Check inventory
    CUSTOMER = 20  # Browse/Search inventory and place orders
    GUEST = 0      # No priviledges


class NamePrefix(str, Enum):
    DR = "Dr."
    MR = "Mr."
    MS = "Ms."
    MISS = "Miss"
    MRS = "Mrs."
    MX = "Mx."


class PersonBase(CoreModel):
    """
    Leaving off password and salt from base model
    """
    username: Optional[EmailStr]
    email_label: Optional[constr(to_lower=True, min_length=1, max_length=12)]
    name_prefix: Optional[constr(min_length=1, max_length=8)]
    name_first: Optional[constr(min_length=1, max_length=30)]
    name_last: Optional[constr(min_length=1, max_length=30)]
    name_suffix: Optional[constr(min_length=1, max_length=8)]


class PersonCreate(PersonBase):
    """
    Used when creating a person through the CMS interface

    If a login is created for this person:
        set 'change_pw' = True
        set 'temp_pw_used' = False
    """
    app_role: Optional[AppRole]
    employee: bool = False
    company_id: Optional[int]
    password: Optional[constr(min_length=16, max_length=100, regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$')]
    profile: Optional[PersonProfileCreate]

    @root_validator(pre=True)
    def check_for_name(cls, values) -> str:
        name_first, name_last = values.get("name_first"), values.get("name_last")
        username, password, email_label = values.get("username"), values.get("password"), values.get("email_label")
        if name_first is None and name_last is None:
            raise TypeError("First Name and Last Name cannot both be blank.  Please provide at least one.")
        if (username or password or email_label) and not (username or password or email_label):
            raise TypeError("If creating a login, Please provide username, password and email_label.")
        return values


class PersonCredentialsCreate(PersonBase):
    """
    Used when creating a person (or login) through the app sign-up page
    """
    username: EmailStr
    email_label: constr(to_lower=True, min_length=1, max_length=12)
    password: constr(min_length=16, max_length=100, regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$')

    @root_validator(pre=True)
    def check_for_name(cls, values) -> str:
        name_first, name_last = values.get("name_first"), values.get("name_last")
        if name_first is None and name_last is None:
            raise TypeError("First Name and Last Name cannot both be blank.  Please provide at least one.")
        return values


class PersonUnverified(PersonBase):
    link_expiration: datetime
    message: str
    help_message: str


class PersonUpdate(CoreModel):
    """
    Persons are allowed to update their email and/or username
    """
    username: Optional[EmailStr]


class PersonPasswordUpdate(CoreModel):
    """
    Persons can change their password
    """
    password: constr(min_length=16, max_length=100, regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$')
    salt: str


class PersonRegister(PersonCredentialsCreate):
    app_role: AppRole
    salt: str


class PersonInDB(IDModelMixin, DateTimeModelMixin, PersonBase):
    """
    Add in id, created_at, updated_at, and user's password and salt
    """
    active: bool
    app_role: AppRole
    email_login: bool
    verified: bool
    password: str
    salt: str
    profile: Optional[PersonProfilePublic]


class PersonPublic(IDModelMixin, DateTimeModelMixin, PersonBase):
    profile: Optional[PersonProfilePublic]
