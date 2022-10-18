
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

from fastapi import Depends, HTTPException, status
from loguru import logger

from trove_fm.app.api.dependencies.database import get_repository
from trove_fm.app.config import API_PREFIX, SECRET_KEY
from trove_fm.app.db.repositories.person import PersonRepository
from trove_fm.app.models.person import AppRole, PersonInDB
from trove_fm.app.services import auth_service, OAuth2PasswordBearerSecure


oauth2_scheme = OAuth2PasswordBearerSecure(tokenUrl=f"{API_PREFIX}/person/login/token/")


async def get_account_from_token(
    *,
    token: str = Depends(oauth2_scheme),
    person_repo: PersonRepository = Depends(get_repository(PersonRepository)),
) -> Optional[PersonInDB]:
    """Return a PersonInDB model if a valid access token is presented with the request

    By injecting the oauth2_scheme as a dependency, FastAPI will inspect the request for
    an Authorization cookie or header, check if the value is Bearer plus some token, and
    return the token as a str. If it doesn't see an Authorization header or cookie, or
    the value doesn't have a Bearer token, it will respond with an HTTP_401_UNAUTHORIZED
    status code.
    """
    try:
        person_id = auth_service.get_person_id_from_token(token=token, secret_key=SECRET_KEY)
        person = await person_repo.get_person_by_id(person_id=person_id)
    except Exception as e:
        raise e
    return person


def get_current_active_person(current_person: PersonInDB = Depends(get_account_from_token)) -> Optional[PersonInDB]:
    """Attempt to accquire a person's record from the database and return a PersonInDB model to the caller

    If no person with the account presented in the token is found in the database, or
    if the account found has been deactivated, raise an HTTP 401 Unauthorized exception.
    """
    if not current_person:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authenticated user.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not current_person.active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not an active user.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_person


class AppRoleAuth:
    """
    Implements Role-based Access Control (RBAC) for persons using TroveFM.
    This dependency is actually expressed via module-level attributes defined below.
    """

    def __init__(self, min_role: AppRole):
        self.min_role = min_role

    def __call__(self, person=Depends(get_current_active_person)):
        if person.app_role < self.min_role:
            logger.debug(f"User with role {person.app_role} not authorized for this action.")
            raise HTTPException(status_code=403, detail="Operation not permitted")


"""
Attributes:
    admin_auth (AppRoleAuth): Check to see if current active person is authorized for an ADMIN action
    power_auth (AppRoleAuth): Check to see if current active person is authorized for a POWER action
    staff_auth (AppRoleAuth): Check to see if current active person is authorized for a STAFF action
    vendor_auth (AppRoleAuth): Check to see if current active person is authorized for a VENDOR action

    These checks require the minimum auth level in order to proceed.
    An ADMIN may perform ALL actions.
    A POWER user may perform all actions except those delegated to an ADMIN user.
    A STAFF user may perform all actions except those delegated to an ADMIN or a POWER user.
    A VENDOR user may perform all actions except those delegated to ADMIN, POWER, or STAFF users.
    A CUSTOMER user is the least priviledged authorized user.
    A GUEST user is not authorized to perform ANY action, other than registering for a CUSTOMER account.
"""
admin_auth = AppRoleAuth(AppRole.ADMIN)
power_auth = AppRoleAuth(AppRole.POWER)
staff_auth = AppRoleAuth(AppRole.STAFF)
vendor_auth = AppRoleAuth(AppRole.VENDOR)
