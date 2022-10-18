
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


from datetime import date
from typing import List, Optional, TypedDict

from pydantic import constr, EmailStr, Field, HttpUrl

from trove_fm.app.models.core import CoreModel


class AddressDict(TypedDict):
    addr_label: constr(to_lower=True, min_length=3, max_length=20)
    addr_primary: bool
    addr1: constr(min_length=3, max_length=100)
    addr2: constr(max_length=100)
    city: constr(min_length=2, max_length=50)
    state: constr(min_length=2, max_length=2)
    zip_code: constr(min_length=5, max_length=5)


class EmailAddressDict(TypedDict, total=False):
    email_label: constr(to_lower=True, min_length=3, max_length=12)
    email: EmailStr
    verified: bool
    email_primary: bool


class PhoneNumberDict(TypedDict):
    phone_label: constr(max_length=12)
    phone_number: constr(max_length=15)
    phone_primary: bool


class PlatformDict(TypedDict, total=False):
    """
    docstring for PlatformDict
    """
    platform: constr(max_length=30)
    url: HttpUrl
    handle: constr(max_length=30)


class URLDict(TypedDict):
    url_label: constr(max_length=30)
    url: HttpUrl
    display_name: Optional[constr(max_length=30)]
    description: Optional[str]


class PersonProfileBase(CoreModel):
    dob: Optional[date] = Field(description="Date Of Birth in format 'YYYY-MM-DD'", title="Birthday")
    occupation: Optional[constr(max_length=50)]
    company: Optional[constr(max_length=100)]
    title: Optional[constr(max_length=30)]
    image_file: Optional[str]
    bio: Optional[str]
    addresses: Optional[List[AddressDict]]
    email_addresses: Optional[List[EmailAddressDict]]
    phone_numbers: Optional[List[PhoneNumberDict]]
    platforms: Optional[List[PlatformDict]]


class PersonProfileCreate(PersonProfileBase):
    """
    The only field required to create a profile is the users id
    """
    pass


class PersonProfileUpdate(PersonProfileBase):
    """
    Allow users to update any or no fields, as long as it's not user_id
    """
    pass


class PersonProfileInDB(PersonProfileBase):
    """
    Though our profiles table doesn't have a username field or an email field, we still add them
    to the PersonProfileInDB model. The PersonProfilePublic model inherits them as well.
    Depending on the situation, this may be useful for displaying user profiles in our UI.
    """
    pass


class PersonProfilePublic(PersonProfileBase):
    pass


class CompanyProfileBase(CoreModel):
    home_page: Optional[HttpUrl]
    logo_file: Optional[str]
    urls: Optional[List[URLDict]]


class CompanyProfileCreate(CompanyProfileBase):
    pass


class CompanyProfileInDB(CompanyProfileBase):
    pass


class CompanyProfilePublic(CompanyProfileBase):
    pass
