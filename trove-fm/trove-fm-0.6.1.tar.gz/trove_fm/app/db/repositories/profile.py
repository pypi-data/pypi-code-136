
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


from typing import List

from asyncpg.exceptions import UniqueViolationError
from databases import Database
from fastapi import HTTPException
from loguru import logger
import phonenumbers

from trove_fm.app.db.repositories.base import BaseRepository
from trove_fm.app.models.person import PersonInDB
from trove_fm.app.models.profile import (
    AddressDict, EmailAddressDict, PhoneNumberDict, PlatformDict,
    PersonProfileBase, PersonProfileCreate, PersonProfileUpdate, PersonProfilePublic
)
from trove_fm.app.services import auth_service


######################
### CREATE Queries ###
######################

# There is no CREATE_COMPANY query, as that would be in the company repo.
# All we would need to do here is GET or UPDATE a company on a person's profile.
PERSON_UPDATE_DETAILS_QUERY = """
    UPDATE person
    SET bio = :bio, dob = :dob, occupation = :occupation, image_file = :image_file
    WHERE id = :person_id
"""

PERSON_CREATE_ADDRESS_QUERY = """
    INSERT INTO address (person_id, addr_label, addr_primary, addr1, addr2, city, state, zip_code)
    VALUES (:person_id, :addr_label, :addr_primary, :addr1, :addr2, :city, :state, :zip_code)
"""

PERSON_CREATE_EMAIL_ADDRESS_QUERY = """
    INSERT INTO email_address (person_id, email_label, email, email_primary, email_login)
    VALUES (:person_id, :email_label, :email, :email_primary, :email_login)
"""

PERSON_CREATE_PHONE_NUMBER_QUERY = """
    INSERT INTO phone (person_id, phone_label, phone_number, phone_primary)
    VALUES (:person_id, :phone_label, :phone_number, :phone_primary)
"""

PERSON_CREATE_PLATFORM_QUERY = """
    INSERT INTO platform (platform_id, person_id, handle)
    SELECT pl.id, :person_id, :handle
    FROM platform_lookup pl
    WHERE pl.platform = :platform
"""

###################
### GET Queries ###
###################

PERSON_GET_COMPANY_QUERY = """
    SELECT p.title, c.company_name
    FROM person p,
        (
            SELECT company.company_name
            FROM company, person
            WHERE company.id = person.company_id
            AND person.id = :person_id
        ) as c
    WHERE p.id = :person_id
"""

PERSON_GET_DETAILS_QUERY = """
    SELECT bio, dob, occupation, image_file
    FROM person
    WHERE id = :person_id
"""


PERSON_GET_ADDRESSES_QUERY = """
    SELECT a.company_id, a.addr_label, a.addr_primary, a.addr1, a.addr2, a.city, a.state, a.zip_code
    FROM address a, person p
    WHERE (p.id = a.person_id OR p.company_id = a.company_id)
    AND p.id = :person_id
"""

PERSON_GET_EMAIL_ADDRESSES_QUERY = """
    SELECT ea.email_label, ea.email, ea.verified, ea.email_primary
    FROM email_address ea, person p
    WHERE ea.person_id = p.id
    AND p.id = :person_id
"""

PERSON_GET_PHONE_NUMBERS_QUERY = """
    SELECT ph.phone_label, ph.phone_number, ph.phone_primary
    FROM phone ph, person p
    WHERE ph.person_id = p.id
    AND p.id = :person_id
"""

PERSON_GET_PLATFORMS_QUERY = """
    SELECT pl.platform, pl.url, pf.handle
    FROM platform_lookup pl, platform pf, person p
    WHERE p.id = pf.person_id
    AND pf.platform_id = pl.id
    AND p.id = :person_id
"""


######################
### UPDATE Queries ###
######################

PERSON_UPDATE_COMPANY_QUERY = """
    UPDATE person
    SET title = :title, company_id =
        (
            SELECT company.id
            FROM company
            WHERE company.company_name = :company_name
        )
    WHERE id = :person_id
"""

# TODO: USE THIS!
PERSON_UPDATE_ADDRESS_QUERY = """
    UPDATE address
    SET addr_primary = :addr_primary,
        addr1 = :addr1,
        addr2 = :addr2,
        city = :city,
        state = :state,
        zip_code = :zip_code
    WHERE person_id = :person_id
    AND addr_label = :addr_label
    RETURNING addr_label, addr_primary, addr1, addr2, city, state, zip_code
"""

# TODO: USE THIS!
PERSON_UPDATE_EMAIL_ADDRESS_QUERY = """
    UPDATE email_address
    SET email_label = :email_label,
        email_primary = :email_primary,
        email_login = :email_login
    WHERE person_id = :person_id
    AND email = :email
    RETURNING email, email_label, email_primary, email_login, verified
"""

# TODO: USE THIS!
PERSON_UPDATE_PHONE_NUMBER_QUERY = """
    UPDATE phone
    SET phone_label = :phone_label,
        phone_primary = :phone_primary
    WHERE person_id = :person_id
    AND phone_number = :phone_number
    RETURNING phone_number, phone_label, phone_primary
"""

# TODO: USE THIS!
PERSON_UPDATE_PLATFORM_QUERY = """
    UPDATE platform
    SET handle = :handle
    WHERE person_id = :person_id
    AND platform_id =
        (
            SELECT id
            FROM platform_lookup
            WHERE platform = :platform
        )
"""


######################
### DELETE Queries ###
######################

PERSON_DELETE_ADDRESS_QUERY = """

"""

PERSON_DELETE_EMAIL_ADDRESS_QUERY = """

"""

PERSON_DELETE_PHONE_NUMBER_QUERY = """

"""

PERSON_DELETE_PLATFORM_QUERY = """

"""


class PersonProfileRepository(BaseRepository):
    def __init__(self, db: Database) -> None:
        super().__init__(db)
        self.auth_service = auth_service

    async def update_person_details(self, person_id: int, profile: PersonProfileBase):
        details = {
            "dob": profile.dob,
            "bio": profile.bio,
            "occupation": profile.occupation,
            "image_file": profile.image_file,
            "person_id": person_id
        }
        await self.db.execute(query=PERSON_UPDATE_DETAILS_QUERY, values=details)

    async def update_person_company(self, person_id, title, company_name):
        values = {"title": title, "company_name": company_name, "person_id": person_id}
        await self.db.execute(query=PERSON_UPDATE_COMPANY_QUERY, values=values)

    async def create_addresses(self, *, person_id: int, addresses: List[AddressDict]):
        for address in addresses:
            address.update({"person_id": person_id})
        try:
            await self.db.execute_many(
                query=PERSON_CREATE_ADDRESS_QUERY, values=addresses
            )
        except UniqueViolationError as e:
            logger.error(e.detail)
            raise HTTPException(status_code=409, detail=e.detail)

    async def create_email_addresses(self, *, person_id: int, email_addresses: List[EmailAddressDict]):
        for email_address in email_addresses:
            email_address.update({"person_id": person_id})
        try:
            await self.db.execute_many(
                query=PERSON_CREATE_EMAIL_ADDRESS_QUERY, values=email_addresses
            )
        except UniqueViolationError as e:
            logger.error(e.detail)
            raise HTTPException(status_code=409, detail=e.detail)

    async def create_phone_numbers(self, *, person_id: int, phone_numbers: List[PhoneNumberDict]):
        valid_numbers = list()
        invalid_numbers = list()
        for phone_number in phone_numbers:
            # FIXME: Don't Hardcode 'US' in parse function, below
            number_given = phonenumbers.parse(phone_number["phone_number"], 'US')
            if phonenumbers.is_valid_number(number_given):
                phone_number["phone_number"] = phonenumbers.format_number(
                    number_given,
                    phonenumbers.PhoneNumberFormat.E164
                )
                phone_number.update({"person_id": person_id})
                valid_numbers.append(phone_number)
            else:
                invalid_numbers.append(phone_number)
        try:
            await self.db.execute_many(
                query=PERSON_CREATE_PHONE_NUMBER_QUERY, values=valid_numbers
            )
        except UniqueViolationError as e:
            logger.error(e.detail)
            raise HTTPException(status_code=409, detail=e.detail)

        return invalid_numbers

    async def create_platforms(self, *, person_id: int, platforms: List[PlatformDict]):
        for platform in platforms:
            platform.update({"person_id": person_id})
        try:
            await self.db.execute_many(
                query=PERSON_CREATE_PLATFORM_QUERY, values=platforms
            )
        except UniqueViolationError as e:
            logger.error(e.detail)
            raise HTTPException(status_code=409, detail=e.detail)

    async def create_profile_for_person(
        self, *, person: PersonInDB, new_profile: PersonProfileCreate
    ) -> PersonProfilePublic:
        await self.update_person_details(person.id, new_profile)

        if new_profile.company:
            # FIXME: Check if update fails because company doesn't exist on company table
            await self.update_person_company(person.id, new_profile.title, new_profile.company)

        if new_profile.addresses:
            await self.create_addresses(person_id=person.id, addresses=new_profile.addresses)

        if new_profile.email_addresses:
            await self.create_email_addresses(person_id=person.id, email_addresses=new_profile.email_addresses)

        if new_profile.phone_numbers:
            invalid_numbers = await self.create_phone_numbers(
                person_id=person.id, phone_numbers=new_profile.phone_numbers
            )
            for number in invalid_numbers:
                logger.warning(f"Invalid phone number {number} not set in DB for {person.username}")

        if new_profile.platforms:
            await self.create_platforms(person_id=person.id, platforms=new_profile.platforms)

        return await self.get_profile(person)

    async def get_person_details(self, person_id):
        details = await self.db.fetch_one(query=PERSON_GET_DETAILS_QUERY, values={"person_id": person_id})

        return details

    async def get_company(self, person_id: int) -> str:
        company_detail = await self.db.fetch_one(query=PERSON_GET_COMPANY_QUERY, values={"person_id": person_id})

        return company_detail

    async def get_addresses(self, person_id: int) -> List[AddressDict]:
        addresses = await self.db.fetch_all(query=PERSON_GET_ADDRESSES_QUERY, values={"person_id": person_id})

        if addresses:
            address_list = list()
            for address in addresses:
                address_list.append(dict(address._mapping.items()))

            return address_list

    async def get_email_addresses(self, person_id: int) -> List[EmailAddressDict]:
        email_addresses = await self.db.fetch_all(
            query=PERSON_GET_EMAIL_ADDRESSES_QUERY, values={"person_id": person_id}
        )

        if email_addresses:
            email_address_list = list()
            for email_address in email_addresses:
                email_address_list.append(dict(email_address._mapping.items()))

            return email_address_list

    async def get_phone_numbers(self, person_id: int) -> List[PhoneNumberDict]:
        phone_numbers = await self.db.fetch_all(query=PERSON_GET_PHONE_NUMBERS_QUERY, values={"person_id": person_id})

        if phone_numbers:
            phone_number_list = list()
            for phone_number in phone_numbers:
                phone_number_list.append(dict(phone_number._mapping.items()))

            return phone_number_list

    async def get_platforms(self, person_id: int) -> List[PlatformDict]:
        platforms = await self.db.fetch_all(query=PERSON_GET_PLATFORMS_QUERY, values={"person_id": person_id})

        if platforms:
            platform_list = list()
            for platform in platforms:
                platform_list.append(dict(platform._mapping.items()))

            return platform_list

    async def get_profile(self, person: PersonInDB) -> PersonProfilePublic:
        company_detail = await self.get_company(person.id)
        details = await self.get_person_details(person.id)
        addresses = await self.get_addresses(person.id)
        email_addresses = await self.get_email_addresses(person.id)
        phone_numbers = await self.get_phone_numbers(person.id)
        platforms = await self.get_platforms(person.id)

        profile = PersonProfilePublic(
            image_file=details["image_file"],
            dob=details["dob"],
            bio=details["bio"],
            occupation=details["occupation"],
            title=company_detail["title"] if company_detail else None,
            company=company_detail["company_name"] if company_detail else None,
            addresses=addresses,
            email_addresses=email_addresses,
            phone_numbers=phone_numbers,
            platforms=platforms
        )

        return profile

    async def update_profile(self, profile_update: PersonProfileUpdate):
        pass


######################
### CREATE Queries ###
######################

# There is no CREATE_COMPANY query, as that would be in the company repo.
# All we would need to do here is GET or UPDATE a company on a person's profile.
COMPANY_UPDATE_DETAILS_QUERY = """

"""

COMPANY_CREATE_ADDRESS_QUERY = """

"""

COMPANY_CREATE_EMAIL_ADDRESS_QUERY = """

"""

COMPANY_CREATE_PHONE_NUMBER_QUERY = """

"""

COMPANY_CREATE_PLATFORM_QUERY = """

"""

###################
### GET Queries ###
###################

COMPANY_GET_DETAILS_QUERY = """

"""


COMPANY_GET_ADDRESSES_QUERY = """

"""

COMPANY_GET_EMAIL_ADDRESSES_QUERY = """

"""

COMPANY_GET_PHONE_NUMBERS_QUERY = """

"""

COMPANY_GET_PLATFORMS_QUERY = """

"""


######################
### UPDATE Queries ###
######################

COMPANY_UPDATE_DETAILS_QUERY = """

"""

COMPANY_UPDATE_ADDRESS_QUERY = """

"""

COMPANY_UPDATE_EMAIL_ADDRESS_QUERY = """

"""

COMPANY_UPDATE_PHONE_NUMBER_QUERY = """

"""

COMPANY_UPDATE_PLATFORM_QUERY = """

"""


######################
### DELETE Queries ###
######################

COMPANY_DELETE_ADDRESS_QUERY = """

"""

COMPANY_DELETE_EMAIL_ADDRESS_QUERY = """

"""

COMPANY_DELETE_PHONE_NUMBER_QUERY = """

"""

COMPANY_DELETE_PLATFORM_QUERY = """

"""
