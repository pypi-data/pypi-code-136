
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


from time import sleep
from typing import Callable, Optional, Type, Union
from urllib.parse import urlparse

from databases import Database
from dirty_equals import IsDatetime, IsNow, IsPositiveInt, IsStr
from fastapi import FastAPI, HTTPException, status
from httpx import AsyncClient
from itsdangerous.exc import BadTimeSignature, SignatureExpired
import jwt
from pydantic import ValidationError
import pytest
from starlette.datastructures import Secret

from trove_fm.app.config import (
    ACCESS_TOKEN_EXPIRE_MINUTES, BASE_URL, JWT_ALGORITHM, JWT_AUDIENCE, MAIL_LINK_EXPIRES, SECRET_KEY
)
from trove_fm.app.db.repositories.person import PersonRepository
from trove_fm.app.models.person import PersonPublic, PersonUnverified
from trove_fm.app.services import auth_service, verification_service
from trove_fm.app.services import security
from trove_fm.tests.models import UsualSuspect


class TestPersonRoutes:
    @pytest.mark.asyncio
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        new_person_creds = {
            "name_first": "Automated",
            "name_last": "Test",
            "username": "test@email.io",
            "email_label": "work",
            "password": "testpassword3456"
        }
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code != status.HTTP_404_NOT_FOUND


class TestPersonRegistration:
    @pytest.mark.asyncio
    async def test_person_can_register_successfully(
        self,
        app: FastAPI,
        client: AsyncClient,
        db: Database,
    ) -> None:
        """
        To register successfully, the person should post the registration form and receive an HTTP 201 response,
        along with a PersonUnverified JSON object.
        """
        person_repo = PersonRepository(db)
        new_person_creds = {
            "name_first": "Kurt",
            "name_last": "Gödel",
            "username": "kgodel@live.com",
            "email_label": "home",
            "password": "Uj#Vy9r+b6D>@HD=BQd23yYT"
        }

        # make sure person doesn't exist yet
        person_in_db = await person_repo.get_person_by_email(email=new_person_creds["username"])
        assert person_in_db is None

        # send post request to create person and ensure it is successful
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status.HTTP_201_CREATED

        person_unverified = res.json()
        assert person_unverified == {
            "username": "kgodel@live.com",
            "email_label": "home",
            "name_first": "Kurt",
            "name_last": "Gödel",
            "link_expiration": IsNow(delta=MAIL_LINK_EXPIRES, iso_string=True, enforce_tz=False),
            "message": "Your confirmation email has been sent to kgodel@live.com",
            "help_message": f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"
        }

        # ensure that the person now exists in the db
        person_in_db = await person_repo.get_person_by_email(email=new_person_creds["username"], get_profile=False)
        assert person_in_db is not None
        assert person_in_db.username == new_person_creds["username"]

        # check that the person returned in the response is equal to the person in the database
        created_person = PersonUnverified(**res.json()).dict(exclude={
            "link_expiration",
            "message",
            "help_message"
        })
        assert created_person == person_in_db.dict(exclude={
            "id",
            "active",
            "app_role",
            "password",
            "salt",
            "email_login",
            "verified",
            "created_at",
            "updated_at",
            "profile"
        })

    @pytest.mark.parametrize(
        "attr, value, status_code",
        [
            pytest.param("username", "amazing.angier@outlook.com", 201, id="username_valid"),
            pytest.param("username", "amazing.angier@outlook.com", 400, id="username_duplicate"),
            pytest.param("username", "invalid_email@one@two.io", 422, id="username_two_@"),
            pytest.param("username", "angier@#$%^<>", 422, id="username_@_no_domain"),
            pytest.param("username", "robert", 422, id="username_not_email"),
        ]
    )
    @pytest.mark.asyncio
    async def test_user_registration_fails_with_bad_username(
        self,
        app: FastAPI,
        client: AsyncClient,
        db: Database,
        attr: str,
        value: str,
        status_code: int,
    ) -> None:
        new_person_creds = {
            "name_first": "Robert",
            "name_last": "Angier",
            "username": "",
            "email_label": "home",
            "password": "Z*73VC@h&Nu?CHb^iN7sL7TU"
        }
        new_person_creds[attr] = value
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status_code

    @pytest.mark.parametrize(
        "attr, value, status_code",
        [
            pytest.param("password", "", 422, id="password_missing"),
            pytest.param("password", "zMvgBFkF-4_JqH2", 422, id="password_short"),
            pytest.param("password", "MBFF-4_JH2KL*5D7Z", 422, id="password_no_lower_chars"),
            pytest.param("password", "zvgk-4_q2se*5v7!", 422, id="password_no_upper_chars"),
            pytest.param("password", "zMvgBFkF-_JqHKLse*DvZ", 422, id="password_no_numbers"),
            pytest.param("password", "zMvgBFkF4JqH2KLse5Dv7Z", 422, id="password_no_special_chars"),
        ],
    )
    @pytest.mark.asyncio
    async def test_user_registration_fails_with_bad_password(
        self,
        app: FastAPI,
        client: AsyncClient,
        db: Database,
        attr: str,
        value: str,
        status_code: int,
    ) -> None:
        new_person_creds = {
            "name_first": "David",
            "name_last": "Morley",
            "username": "dutchmorley@hotmail.com",
            "email_label": "home",
            "password": ""
        }
        new_person_creds[attr] = value
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status_code

    @pytest.mark.parametrize(
        "name_first, name_last, username, password, status_code",
        [
            pytest.param(
                None, "Lebowski",
                "onechillindude5@gmail.com", "w9sp3nbBTU!NnvV*KfaBZ#L.y",
                201, id="last_name_provided"
            ),
            pytest.param(
                "Dude", None,
                "one.chillindude@live.com", "w9sp3nbBTU!NnvV*KfaBZ#L.y",
                201, id="first_name_provided"
            ),
        ],
    )
    @pytest.mark.asyncio
    async def test_person_can_register_with_only_one_name(
        self,
        app: FastAPI,
        client: AsyncClient,
        db: Database,
        name_first: str,
        name_last: str,
        username: str,
        password: str,
        status_code: int,
    ) -> None:
        """
        When a user registers, they MUST provide AT LEAST a first name OR a last name.
        """
        person_repo = PersonRepository(db)

        if name_first:
            new_person_creds = {
                "name_first": name_first,
                "username": username,
                "email_label": "home",
                "password": password
            }
        elif name_last:
            new_person_creds = {
                "name_last": name_last,
                "username": username,
                "email_label": "home",
                "password": password
            }

        # make sure person doesn't exist yet
        person_in_db = await person_repo.get_person_by_email(email=new_person_creds["username"])
        assert person_in_db is None

        # send post request to create person and ensure it is successful
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status_code

        person_unverified = res.json()

        if name_first:
            assert person_unverified == {
                "username": username,
                "email_label": "home",
                "name_first": name_first,
                "link_expiration": IsNow(delta=MAIL_LINK_EXPIRES, iso_string=True, enforce_tz=False),
                "message": f"Your confirmation email has been sent to {username}",
                "help_message": f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"
            }
        elif name_last:
            assert person_unverified == {
                "username": username,
                "email_label": "home",
                "name_last": name_last,
                "link_expiration": IsNow(delta=MAIL_LINK_EXPIRES, iso_string=True, enforce_tz=False),
                "message": f"Your confirmation email has been sent to {username}",
                "help_message": f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"
            }

    @pytest.mark.asyncio
    async def test_person_cannot_register_without_name(
        self,
        app: FastAPI,
        client: AsyncClient,
        db: Database,
    ) -> None:
        """
        When a user registers, they MUST provide AT LEAST a first name OR a last name.
        """
        person_repo = PersonRepository(db)
        new_person_creds = {
            "username": "one.chillinduderino@outlook.com",
            "email_label": "home",
            "password": "w9sp3nbBTU!NnvV*KfaBZ#L.y"
        }

        # make sure person doesn't exist yet
        person_in_db = await person_repo.get_person_by_email(email=new_person_creds["username"])
        assert person_in_db is None

        # send post request to create person
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        person_unverified = res.json()
        assert person_unverified == {
            "detail": [
                {
                    "loc": [
                        "body",
                        "new_person_creds",
                        "__root__"
                    ],
                    "msg": "First Name and Last Name cannot both be blank.  Please provide at least one.",
                    "type": "type_error"
                }
            ]
        }

    @pytest.mark.parametrize(
        "name_prefix, name_first, name_last, name_suffix, "
        "username, email_label, password, "
        "status_code, field, min_length",
        [
            pytest.param(
                "", "Sh'ron", "Guest", "V",
                "shron@trove.fm", "home", "ic8pazN_BD!N9z*a2i7LpARC2",
                422, "name_prefix", 1, id="name_prefix"
            ),
            pytest.param(
                "Mr.", "", "Guest", "V",
                "shron@trove.fm", "home", "ic8pazN_BD!N9z*a2i7LpARC2",
                422, "name_first", 1, id="name_first"
            ),
            pytest.param(
                "Mr.", "Sh'ron", "", "V",
                "shron@trove.fm", "home", "ic8pazN_BD!N9z*a2i7LpARC2",
                422, "name_last", 1, id="name_last"
            ),
            pytest.param(
                "Mr.", "Sh'ron", "Guest", "",
                "shron@trove.fm", "home", "ic8pazN_BD!N9z*a2i7LpARC2",
                422, "name_suffix", 1, id="name_suffix"
            ),
            pytest.param(
                "Mr.", "Sh'ron", "Guest", "V",
                "shron@trove.fm", "", "ic8pazN_BD!N9z*a2i7LpARC2",
                422, "email_label", 1, id="email_label"
            ),
            pytest.param(
                "Mr.", "Sh'ron", "Guest", "V",
                "shron@trove.fm", "home", "",
                422, "password", 16, id="password"
            ),
        ],
    )
    @pytest.mark.asyncio
    async def test_included_fields_have_value(
        self,
        app: FastAPI,
        client: AsyncClient,
        db: Database,
        name_prefix: str,
        name_first: str,
        name_last: str,
        name_suffix: str,
        username: str,
        email_label: str,
        password: str,
        status_code: int,
        field: str,
        min_length: int
    ) -> None:
        """
        When a user registers, they MUST a value for each field that is specified.

        We DO NOT test for length of username, as its validation already requires it to be
        a valid email address.
        """

        new_person_creds = {
            "name_prefix": name_prefix,
            "name_first": name_first,
            "name_last": name_last,
            "name_suffix": name_suffix,
            "username": username,
            "email_label": email_label,
            "password": password
        }

        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        person_unverified = res.json()
        assert person_unverified == {
            "detail": [
                {
                    "ctx": {
                        "limit_value": min_length
                    },
                    "loc": [
                        "body",
                        "new_person_creds",
                        field
                    ],
                    "msg": f"ensure this value has at least {min_length} characters",
                    "type": "value_error.any_str.min_length"
                }
            ]
        }

    @pytest.mark.asyncio
    async def test_person_saved_password_is_hashed_and_has_salt(
        self,
        app: FastAPI,
        client: AsyncClient,
        db: Database,
    ) -> None:
        person_repo = PersonRepository(db)
        new_person_creds = {
            "name_first": "Jeffery",
            "name_last": "Lebowski",
            "username": "one.chillindude@me.com",
            "email_label": "home",
            "password": "acW@sPZ3BfWVy!i9.NdtGkH49"
        }

        # send post request to create person and ensure it is successful
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status.HTTP_201_CREATED

        # ensure that the person password is hashed in the db
        # and that we can verify it using our auth service
        person_in_db = await person_repo.get_person_by_email(email=new_person_creds["username"], get_profile=False)
        assert person_in_db is not None
        assert person_in_db.salt is not None and person_in_db.salt != "123"
        assert person_in_db.password != new_person_creds["password"]
        assert auth_service.verify_password(
            password=new_person_creds["password"],
            salt=person_in_db.salt,
            hashed_pw=person_in_db.password,
        )


class TestVerifyEmail:
    # TODO: Use Selenium to verify receipt of actual email.

    @pytest.mark.asyncio
    async def test_verification_fails_with_bad_SECRET_KEY(self, client):
        username = 'scully.believes@gmail.com'
        BAD_KEY = "77a17d8fe80a9b698d0e95e0a701f9abf145296b8fc1a9051999b5d4ce5bbb1b"
        base_url = "/api/person/verify/"

        bad_verification_service = security.NewAccountVerificationService(secret_key=BAD_KEY)

        verification_url = bad_verification_service.get_verification_url(username, base_url)
        parsed_url = urlparse(verification_url)
        token = parsed_url.path.split('/')[-1]

        good_verification_service = security.NewAccountVerificationService()

        with pytest.raises(BadTimeSignature):
            good_verification_service.verify_token(token)

        res = await client.get(verification_url, follow_redirects=True)

        assert res.status_code == status.HTTP_400_BAD_REQUEST

        assert res.json() == {
            'detail': 'The token presented has a bad signature. Please request a new verification email.'
        }

    @pytest.mark.asyncio
    async def test_verification_fails_with_bad_salt(self, client):
        username = 'scully.believes@gmail.com'
        bad_salt = "confirmation_token"
        base_url = "/api/person/verify/"

        bad_verification_service = security.NewAccountVerificationService(salt=bad_salt)

        verification_url = bad_verification_service.get_verification_url(username, base_url)
        parsed_url = urlparse(verification_url)
        token = parsed_url.path.split('/')[-1]

        good_verification_service = security.NewAccountVerificationService()

        with pytest.raises(BadTimeSignature):
            good_verification_service.verify_token(token)

        res = await client.get(verification_url, follow_redirects=True)

        assert res.status_code == status.HTTP_400_BAD_REQUEST

        assert res.json() == {
            'detail': 'The token presented has a bad signature. Please request a new verification email.'
        }

    @pytest.mark.asyncio
    async def test_verification_fails_with_expired_token(self, client):
        username = 'scully.believes@gmail.com'
        base_url = "/api/person/verify/"

        # verification_service = security.NewAccountVerificationService()

        verification_url = verification_service.get_verification_url(username, base_url)
        parsed_url = urlparse(verification_url)
        token = parsed_url.path.split('/')[-1]

        sleep(2)
        with pytest.raises(SignatureExpired):
            verification_service.verify_token(token, expiration=1)

        # Monkey patch the instance method verification_service.verify_token so that it has
        # expiration=1, rather than the default expiration=MAIL_LINK_EXPIRES
        def short_verify(self, token, expiration=1):
            username = self.secure_serializer.loads(
                token,
                salt=self.salt,
                max_age=expiration
            )

            return username

        orig_verify_token_method = verification_service.verify_token
        verification_service.verify_token = \
            lambda token, verification_service=verification_service: short_verify(verification_service, token)

        res = await client.get(verification_url, follow_redirects=True)

        assert res.status_code == status.HTTP_400_BAD_REQUEST

        assert res.json() == {
            'detail': 'The token presented has expired. Please request a new verification email.'
        }

        # Reset the instance method verification_service.verify_token
        verification_service.verify_token = orig_verify_token_method

    @pytest.mark.asyncio
    async def test_resend_verification_email(self, app, client, db):
        """
        """
        person_repo = PersonRepository(db)
        name_first = "Lester"
        name_last = "Bangs"
        username = "lesterbangs840@gmail.com"
        email_label = "home"
        password = "zFiuCUzFXrXaNPmPHzS3XM.-J"

        new_person_creds = {
            "name_first": name_first,
            "name_last": name_last,
            "username": username,
            "email_label": email_label,
            "password": password
        }

        # make sure person doesn't exist yet
        person_in_db = await person_repo.get_person_by_email(email=new_person_creds["username"])
        assert person_in_db is None

        # send post request to create person and ensure it is successful
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status.HTTP_201_CREATED

        person_unverified = res.json()
        assert person_unverified == {
            "username": username,
            "email_label": email_label,
            "name_first": name_first,
            "name_last": name_last,
            "link_expiration": IsNow(delta=MAIL_LINK_EXPIRES, iso_string=True, enforce_tz=False),
            "message": f"Your confirmation email has been sent to {username}",
            "help_message": f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"
        }

        # request to resend verification email
        res = await client.post(
            app.url_path_for("person:resend-verification-email"), json={"username": username}
        )
        assert res.status_code == status.HTTP_200_OK

        person_unverified_still = res.json()
        assert person_unverified_still == {
            "username": username,
            "email_label": email_label,
            "name_first": name_first,
            "name_last": name_last,
            "link_expiration": IsNow(delta=MAIL_LINK_EXPIRES, iso_string=True, enforce_tz=False),
            "message": f"Your confirmation email has been sent to {username}",
            "help_message": f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"
        }

    @pytest.mark.asyncio
    async def test_resend_verification_email_fails_with_unknown_username(self, app, client):
        username = "shron@trove.fm"
        res = await client.post(
            app.url_path_for("person:resend-verification-email"), json={"username": username}
        )
        assert res.status_code == status.HTTP_400_BAD_REQUEST

        msg = res.json()
        assert msg == {
            "detail": f"The email {username} is not found in the database. Please register first."
        }

    @pytest.mark.asyncio
    async def test_resend_or_click_verification_email_fails_after_verification(self, app, client, db):
        person_repo = PersonRepository(db)
        name_first = "Nathaniel"
        name_last = "Muir"
        username = "old.scotch24@gmail.com"
        email_label = "work"
        password = "dQh*NK9ZE3!LcKU2Qf-W@ys.r"

        new_person_creds = {
            "name_first": name_first,
            "name_last": name_last,
            "username": username,
            "email_label": email_label,
            "password": password
        }

        # make sure person doesn't exist yet
        person_in_db = await person_repo.get_person_by_email(email=new_person_creds["username"])
        assert person_in_db is None

        # send post request to create person and ensure it is successful
        res = await client.post(
            app.url_path_for("person:register-person-credentials"), json={"new_person_creds": new_person_creds}
        )
        assert res.status_code == status.HTTP_201_CREATED

        person_unverified = res.json()
        assert person_unverified == {
            "username": username,
            "email_label": email_label,
            "name_first": name_first,
            "name_last": name_last,
            "link_expiration": IsNow(delta=MAIL_LINK_EXPIRES, iso_string=True, enforce_tz=False),
            "message": f"Your confirmation email has been sent to {username}",
            "help_message": f"Didn't get the link? Click here to resend: {BASE_URL}/person/verify/resend/"
        }

        # verify email via verification link
        verification_url = verification_service.get_verification_url(
            person_unverified["username"], f"/api/person/verify/"
        )
        res = await client.get(verification_url, follow_redirects=True)

        assert res.status_code == status.HTTP_200_OK
        print(res.json())
        assert res.json() == {
            "username": username,
            "email_label": email_label,
            "name_first": name_first,
            "name_last": name_last,
            "id": IsPositiveInt()
        }

        # request to resend verification email
        res = await client.post(
            app.url_path_for("person:resend-verification-email"), json={"username": username}
        )
        assert res.status_code == status.HTTP_400_BAD_REQUEST

        assert res.json() == {
            "detail": f"The email {username} has already been verified."
        }

        # verify email via verification link AGAIN, after prior verification
        res = await client.get(verification_url, follow_redirects=True)

        assert res.status_code == status.HTTP_400_BAD_REQUEST

        assert res.json() == {
            "detail": f"The email {username} has already been verified."
        }


class TestAuthTokens:
    @pytest.mark.asyncio
    async def test_can_create_access_token_successfully(
        self, app: FastAPI, client: AsyncClient, person_muir: UsualSuspect
    ) -> None:
        person = PersonPublic(**person_muir.dict())
        access_token = auth_service.create_access_token_for_person(
            person=person,
            secret_key=str(SECRET_KEY),
            audience=JWT_AUDIENCE,
            expires_in=ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        creds = jwt.decode(access_token, str(SECRET_KEY), audience=JWT_AUDIENCE, algorithms=[JWT_ALGORITHM])
        assert creds.get("sub") is not None
        assert creds["sub"] == person_muir.username
        assert creds["aud"] == JWT_AUDIENCE

    @pytest.mark.asyncio
    async def test_token_missing_user_is_invalid(self, app: FastAPI, client: AsyncClient) -> None:
        access_token = auth_service.create_access_token_for_person(
            person=None,
            secret_key=str(SECRET_KEY),
            audience=JWT_AUDIENCE,
            expires_in=ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        # If no person is passed to auth_service.create_access_token_for_person, method SHOULD return None.
        assert access_token is None
        with pytest.raises(jwt.PyJWTError):
            jwt.decode(access_token, str(SECRET_KEY), audience=JWT_AUDIENCE, algorithms=[JWT_ALGORITHM])

    @pytest.mark.parametrize(
        "secret_key, jwt_audience, exception",
        (
            ("wrong-secret", JWT_AUDIENCE, jwt.InvalidSignatureError),
            (None, JWT_AUDIENCE, jwt.InvalidSignatureError),
            (SECRET_KEY, "othersite:auth", jwt.InvalidAudienceError),
            (SECRET_KEY, None, ValidationError),
        )
    )
    @pytest.mark.asyncio
    async def test_invalid_token_content_raises_error(
        self,
        app: FastAPI,
        client: AsyncClient,
        person_muir: UsualSuspect,
        secret_key: Union[str, Secret],
        jwt_audience: str,
        exception: Type[BaseException],
    ) -> None:
        with pytest.raises(exception):
            person = PersonPublic(**person_muir.dict())
            access_token = auth_service.create_access_token_for_person(
                person=person,
                secret_key=str(secret_key),
                audience=jwt_audience,
                expires_in=ACCESS_TOKEN_EXPIRE_MINUTES,
            )
            jwt.decode(access_token, str(SECRET_KEY), audience=JWT_AUDIENCE, algorithms=[JWT_ALGORITHM])

    @pytest.mark.asyncio
    async def test_can_retrieve_username_from_token(
        self, app: FastAPI, client: AsyncClient, person_muir: UsualSuspect
    ) -> None:
        person = PersonPublic(**person_muir.dict())
        token = auth_service.create_access_token_for_person(person=person, secret_key=str(SECRET_KEY))
        person_id = auth_service.get_person_id_from_token(token=token, secret_key=str(SECRET_KEY))
        assert person_id == person_muir.id

    @pytest.mark.parametrize(
        "secret, wrong_token",
        (
            (SECRET_KEY, "asdf"),  # use wrong token
            (SECRET_KEY, ""),  # use wrong token
            (SECRET_KEY, None),  # use wrong token
            ("ABC123", "use correct token"),  # use wrong secret
        ),
    )
    @pytest.mark.asyncio
    async def test_error_when_token_or_secret_is_wrong(
        self,
        app: FastAPI,
        client: AsyncClient,
        person_muir: UsualSuspect,
        secret: Union[Secret, str],
        wrong_token: Optional[str],
    ) -> None:
        person = PersonPublic(**person_muir.dict())
        token = auth_service.create_access_token_for_person(person=person, secret_key=str(SECRET_KEY))
        if wrong_token == "use correct token":
            wrong_token = token
        with pytest.raises(HTTPException):
            auth_service.get_person_id_from_token(token=wrong_token, secret_key=str(secret))


class TestPersonLogin:
    @pytest.mark.asyncio
    async def test_user_can_login_successfully_and_receives_valid_token(
        self, app: FastAPI, client: AsyncClient, person_muir: UsualSuspect,
    ) -> None:
        client.headers["content-type"] = "application/x-www-form-urlencoded"
        login_data = {
            "username": person_muir.username,
            "password": person_muir.password,  # insert person's plaintext password
        }
        res = await client.post(app.url_path_for("person:login-email-and-password"), data=login_data)
        assert res.status_code == status.HTTP_200_OK
        # check that token exists in response and has person encoded within it
        token = res.json().get("access_token")
        creds = jwt.decode(token, str(SECRET_KEY), audience=JWT_AUDIENCE, algorithms=[JWT_ALGORITHM])
        assert "sub" in creds
        assert creds["sub"] == person_muir.username
        # check that token is proper type
        assert "token_type" in res.json()
        assert res.json().get("token_type") == "bearer"

    @pytest.mark.parametrize(
        "credential, wrong_value, status_code",
        (
            ("username", "wrong@email.com", 401),
            ("username", None, 422),
            ("username", "notemail", 401),
            ("password", "wrongpassword", 401),
            ("password", None, 422),
        ),
    )
    @pytest.mark.asyncio
    async def test_user_with_wrong_creds_doesnt_receive_token(
        self,
        app: FastAPI,
        client: AsyncClient,
        person_muir: UsualSuspect,
        credential: str,
        wrong_value: str,
        status_code: int,
    ) -> None:
        # TODO: Revisit this test, which is carried-over from POC
        client.headers["content-type"] = "application/x-www-form-urlencoded"
        user_data = person_muir.dict()
        user_data["password"] = "heatcavslakers"  # insert person's plaintext password
        user_data[credential] = wrong_value
        login_data = {
            "username": user_data["username"],
            "password": user_data["password"],  # insert password from parameters
        }
        res = await client.post(app.url_path_for("person:login-email-and-password"), data=login_data)
        assert res.status_code == status_code
        assert "access_token" not in res.json()

    @pytest.mark.asyncio
    async def test_login_from_browser_gets_cookie(self, app, client, person_muir):
        orig_user_agent = client.headers["user-agent"]
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
        headers = {
            "user-agent": user_agent,
            "content-type": "application/x-www-form-urlencoded"
        }
        login_data = {
            "username": person_muir.username,
            "password": person_muir.password
        }

        res = await client.post(
            app.url_path_for("person:login-email-and-password"),
            headers=headers,
            data=login_data
        )

        assert res.status_code == status.HTTP_200_OK
        assert res.json() == {
            "token_location": "cookie",
            "token_type": "bearer"
        }

        assert len(client.cookies) > 0
        assert client.cookies["access_token"] == IsStr(regex=r'\"Bearer\s[\w|-]+\.[\w|-]+\.[\w|-]+\"')

        client.headers["user-agent"] = orig_user_agent


class TestPersonMe:
    @pytest.mark.parametrize(
        "api_client",
        [
            pytest.param("Andorid", id="Andorid"),
            pytest.param("Chrome", id="Chrome"),
            pytest.param("Edge", id="Edge"),
            pytest.param("Firefox", id="Firefox"),
            pytest.param("IE", id="IE"),
            pytest.param("iOS WebView", id="iOS WebView"),
            pytest.param("Opera", id="Opera"),
            pytest.param("Safari", id="Safari"),
            pytest.param("Paw", id="Paw"),
            pytest.param("curl", id="curl"),
            pytest.param("python requests", id="python requests"),
        ],
    )
    @pytest.mark.asyncio
    async def test_authenticated_user_can_retrieve_own_data(
        self,
        api_client: str,
        app: FastAPI,
        create_authorized_client: Callable,
        person_muir: UsualSuspect,
        user_agent: Callable
    ) -> None:
        ua = user_agent(api_client)
        client = await create_authorized_client(person=person_muir, user_agent=ua)

        if ua.stores_cookies:
            cookies = {"access_token": client.cookies["access_token"]}
            res = await client.get(app.url_path_for("person:get-current-person"), cookies=cookies)
            assert res.status_code == status.HTTP_200_OK
        else:
            res = await client.get(app.url_path_for("person:get-current-person"))
            assert res.status_code == status.HTTP_200_OK

        assert res.json() == {
            "username": person_muir.username,
            "email_label": person_muir.email_label,
            "name_first": person_muir.name_first,
            "name_last": person_muir.name_last,
            "id": IsPositiveInt(),
            "created_at": IsDatetime(iso_string=True, enforce_tz=False),
            "updated_at": IsDatetime(iso_string=True, enforce_tz=False),
            'profile': {
                'email_addresses': [
                    {
                        'email': person_muir.username,
                        'email_label': person_muir.email_label,
                        'email_primary': True,
                        'verified': True
                    }
                ],
            }
        }

    @pytest.mark.asyncio
    async def test_user_cannot_access_own_data_if_not_authenticated(
        self, app: FastAPI, client: AsyncClient, person_muir: UsualSuspect,
    ) -> None:
        res = await client.get(app.url_path_for("person:get-current-person"))
        assert res.status_code == status.HTTP_401_UNAUTHORIZED
