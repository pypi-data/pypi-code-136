
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

from fastapi import APIRouter, BackgroundTasks, Body, Depends, Header, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from itsdangerous.exc import BadSignature, SignatureExpired
from loguru import logger
from pydantic import EmailStr
from ua_parser.user_agent_parser import ParseUserAgent

from trove_fm.app.config import BASE_URL, BROWSER_LIST
from trove_fm.app.api.dependencies.auth import get_current_active_person
from trove_fm.app.api.dependencies.database import get_repository
from trove_fm.app.db.repositories.person import PersonRepository
from trove_fm.app.db.repositories.profile import PersonProfileRepository
from trove_fm.app.exceptions import AuthFailure, UsernameExists, VerificationFailure
from trove_fm.app.models.token import AccessToken, TokenLocation
from trove_fm.app.models.person import PersonCredentialsCreate, PersonInDB, PersonPublic, PersonUnverified
from trove_fm.app.models.profile import PersonProfileCreate
from trove_fm.app.services import auth_service, email_service, verification_service


router = APIRouter()


@router.post(
    "/",
    response_model=PersonUnverified,
    response_model_exclude_none=True,
    name="person:register-person-credentials",
    status_code=status.HTTP_201_CREATED
)
async def register_person_credentials(
    background_tasks: BackgroundTasks,
    new_person_creds: PersonCredentialsCreate = Body(..., embed=True),
    person_repo: PersonRepository = Depends(get_repository(PersonRepository)),
) -> PersonUnverified:

    try:
        created_person_creds = await person_repo.register_person_credentials(new_person_creds=new_person_creds)
    except UsernameExists:
        logger.error(f"Username {new_person_creds.username} already exists in database.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="That email is already taken. Login with that email or register with another one."
        )

    verification_url = verification_service.get_verification_url(
        created_person_creds.username, f"{BASE_URL}/api/person/verify/"
    )

    link_expiration = await email_service.send_verification(created_person_creds, verification_url, background_tasks)
    message = f"Your confirmation email has been sent to {created_person_creds.username}"
    help_message = f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"

    person_unverified = PersonUnverified(
        **created_person_creds.dict(),
        link_expiration=link_expiration,
        message=message,
        help_message=help_message
    )

    return person_unverified


@router.post(
    "/verify/resend/",
    response_model=PersonUnverified,
    response_model_exclude_none=True,
    name="person:resend-verification-email",
)
async def resend_verification(
    background_tasks: BackgroundTasks,
    username: EmailStr = Body(..., embed=True),
    person_repo: PersonRepository = Depends(get_repository(PersonRepository))
) -> PersonUnverified:
    person_in_db = await person_repo.get_person_by_username(username=username)

    if not person_in_db:
        logger.error(f"Username {username} not found in database.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The email {username} is not found in the database. Please register first."
        )

    if person_in_db.verified is True:
        logger.error(f"The person with username {username} is already verified.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The email {username} has already been verified."
        )

    verification_url = verification_service.get_verification_url(
        person_in_db.username, f"{BASE_URL}/api/person/verify/"
    )

    link_expiration = await email_service.send_verification(person_in_db, verification_url, background_tasks)
    message = f"Your confirmation email has been sent to {person_in_db.username}"
    help_message = f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"

    person_unverified = PersonUnverified(
        **person_in_db.dict(),
        link_expiration=link_expiration,
        message=message,
        help_message=help_message
    )

    return person_unverified


@router.get(
    "/verify/{confirmation_token}/",
    response_model=PersonPublic,
    response_model_exclude_none=True,
    name="person:verify",
    status_code=status.HTTP_200_OK
)
async def verify_new_registration(
    confirmation_token: str, person_repo: PersonRepository = Depends(get_repository(PersonRepository))
) -> PersonPublic:
    # TODO: Send Welcome email, confirming registration
    try:
        username = verification_service.verify_token(confirmation_token)
    except SignatureExpired:
        logger.error(f"Signature expired for token {confirmation_token}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The token presented has expired. Please request a new verification email."
        )
    except BadSignature:
        logger.error(f"Bad signature for token {confirmation_token}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The token presented has a bad signature. Please request a new verification email."
        )

    try:
        person_verified = await person_repo.verify_new_person_creds(username)
    except VerificationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The email {username} has already been verified."
        )

    return person_verified


@router.post(
    "/login/token/",
    response_model=AccessToken,
    response_model_exclude_none=True,
    name="person:login-email-and-password"
)
async def person_login_with_email_and_password(
    response: Response,
    person_repo: PersonRepository = Depends(get_repository(PersonRepository)),
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    user_agent: Optional[str] = Header(None),
) -> AccessToken:
    """
    Allow person to login and return a JWT to them for continued authentication

    Use ua-parser to determine if person is logging in from a web browser, or from a different type
    of api client.
    - If client is web browser, return access token in secure, http-only cookie
    - Else return access token in JSON response

    **Example UA String for Firefox:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0`

    **Example UA String for Python Requests library:** `python-requests/2.26.0`
    """
    try:
        person = await person_repo.authenticate_account(email=form_data.username, password=form_data.password)
    except AuthFailure:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication was unsuccessful."
        )

    ua = ParseUserAgent(user_agent)

    logger.info(f"User Agent String: {user_agent}")
    logger.info(f"User Agent: {ua['family']}")

    if ua['family'] in BROWSER_LIST.split(","):
        token = auth_service.create_access_token_for_person(person=person)
        access_token = AccessToken(
            token_type="bearer",
            token_location=TokenLocation.cookie.value
        )
        response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True, secure=True)
    else:
        access_token = AccessToken(
            access_token=auth_service.create_access_token_for_person(person=person),
            token_type="bearer",
            token_location=TokenLocation.json.value
        )

    return access_token


@router.post(
    "/profile/",
    name="person:create-profile",
    response_model=PersonPublic,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED
)
async def create_profile(
    new_profile: PersonProfileCreate = Body(..., embed=True),
    profile_repo: PersonProfileRepository = Depends(get_repository(PersonProfileRepository)),
    current_person: PersonInDB = Depends(get_current_active_person)
) -> PersonPublic:
    created_profile = await profile_repo.create_profile_for_person(person=current_person, new_profile=new_profile)
    current_person.profile = created_profile

    return current_person


@router.get(
    "/profile/",
    response_model=PersonPublic,
    response_model_exclude_none=True,
    name="person:get-current-person")
async def get_currently_authenticated_person(
    current_person: PersonInDB = Depends(get_current_active_person)
) -> PersonPublic:
    return current_person
