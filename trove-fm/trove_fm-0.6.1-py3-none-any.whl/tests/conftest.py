
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


import os
from typing import List, Callable
import warnings

import alembic
from alembic.config import Config
from asgi_lifespan import LifespanManager
from databases import Database
from dirty_equals import IsStr
from fastapi import FastAPI, status
from httpx import AsyncClient
import pytest
import pytest_asyncio

from trove_fm.app.config import JWT_TOKEN_PREFIX, SECRET_KEY

from trove_fm.app.db.repositories.person import PersonRepository
from trove_fm.app.models.person import PersonCredentialsCreate, PersonInDB
from trove_fm.app.services import auth_service, verification_service
from trove_fm.tests.models import UserAgent, UsualSuspect


#########################
##### Core Fixtures #####
#########################


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session")
def apply_migrations(save_state=False):
    print(f"\nsave_state: {save_state}\n")
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config(os.environ["ALEMBIC_CONFIG"])
    alembic.command.upgrade(config, "head")
    yield
    if save_state is not True:
        alembic.command.downgrade(config, "base")


# Create a new application for testing
@pytest.fixture
def app(apply_migrations: None) -> FastAPI:
    from trove_fm.app.main import get_application

    return get_application()


# Grab a reference to our database when needed
@pytest.fixture
def db(app: FastAPI) -> Database:
    return app.state._db


###########################
##### Client Fixtures #####
###########################

@pytest.fixture
def user_agent():
    def _get_user_agent(api_client):
        return UserAgent(api_client)

    return _get_user_agent


# Make requests in our tests
@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncClient:
    # ! IMPORTANT: http://testserver is an httpx "magic" url that tells the client to query the given app instance.
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            headers={"Content-Type": "application/json"}
        ) as client:
            yield client


# Make requests in tests with an authorized person
@pytest.fixture
def authorized_client(client: AsyncClient, person_muir: PersonInDB) -> AsyncClient:
    access_token = auth_service.create_access_token_for_user(person=person_muir, secret_key=str(SECRET_KEY))
    client.headers = {
        **client.headers,
        "Authorization": f"{JWT_TOKEN_PREFIX} {access_token}",
    }
    return client


# A helper fixture that constructs an authorized_client for any person we pass in.
# This will help us test authorized requests from multiple different users.
@pytest.fixture
def create_authorized_client(app: FastAPI, client: AsyncClient) -> Callable:
    async def _create_authorized_client(*, person: UsualSuspect, user_agent: UserAgent) -> AsyncClient:
        client.headers = {
            **client.headers,
            "user-agent": user_agent.user_agent,
        }
        request_headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        login_data = {
            "username": person.username,
            "password": person.password
        }

        url_path = app.url_path_for("person:login-email-and-password")
        print(f"\n\nURL PATH: {url_path}")
        print(f"\n\nHeaders: {client.headers}")

        res = await client.post(
            app.url_path_for("person:login-email-and-password"),
            headers=request_headers,
            data=login_data
        )
        assert res.status_code == status.HTTP_200_OK

        print(f"\n\nUSER AGENT: {user_agent.user_agent}")
        print(f"\n\nUSER AGENT STORES COOKIES: {user_agent.stores_cookies}")

        if user_agent.stores_cookies:
            assert res.json() == {
                "token_location": "cookie",
                "token_type": "bearer"
            }
            assert client.cookies["access_token"] == IsStr(regex=r'\"Bearer\s[\w|-]+\.[\w|-]+\.[\w|-]+\"')
        else:
            response_json = res.json()
            assert response_json == {
                "access_token": IsStr(regex=r'[\w|-]+\.[\w|-]+\.[\w|-]+'),
                "token_location": "json",
                "token_type": "bearer"
            }

            access_token = response_json["access_token"]

            client.headers = {
                **client.headers,
                "Authorization": f"{JWT_TOKEN_PREFIX} {access_token}",
            }

        return client

    return _create_authorized_client


###########################
##### Person Fixtures #####
###########################

passwords = {
    "muir": "N7jeo6D>oh;KF#.F)nV3Wu9y",
    "tesla": "BbD7DiGbfGE@nqT-*wrBmy5Y39z",
    "bishop": "WbL}@6pW7Qt8K).=XuowTG6q",
    "david": "q24WpcxRu.(eBt)@d*z6FH7W",
    "golightly": "pCYH3u*Cb2,Q3f6u]/fZ]ixL",
    "tenenbaum": "u%ob3EMqAFDGn/8c6?$V9b]c"
}


async def person_fixture_helper(
    *,
    client: AsyncClient,
    db: Database,
    new_person_creds: PersonCredentialsCreate,
) -> PersonInDB:
    person_repo = PersonRepository(db)

    # make sure person doesn't exist yet
    existing_person = await person_repo.get_person_by_email(email=new_person_creds.username)
    if existing_person:
        existing_person = UsualSuspect(**existing_person.dict())
        existing_person.password = passwords[existing_person.name_last.lower()]
        return existing_person
    else:
        person = await person_repo.register_person_credentials(new_person_creds=new_person_creds)
        person = UsualSuspect(**person.dict())
        person.password = passwords[person.name_last.lower()]
        verification_url = verification_service.get_verification_url(
            person.username, f"/api/person/verify/"
        )
        await client.get(verification_url, follow_redirects=True)
        return person


@pytest_asyncio.fixture
async def person_muir(client: AsyncClient, db: Database) -> PersonInDB:
    new_person_creds = PersonCredentialsCreate(
        name_first="Nathan",
        name_last="Muir",
        email_label="home",
        username="old.scotch@outlook.com",
        password=passwords["muir"],
    )

    return await person_fixture_helper(client=client, db=db, new_person_creds=new_person_creds)


@pytest_asyncio.fixture
async def person_tesla(client: AsyncClient, db: Database) -> PersonInDB:
    new_person_creds = PersonCredentialsCreate(
        name_first="Nikola",
        name_last="Tesla",
        email_label="work",
        username="tesla.conducts@gmail.com",
        password=passwords["tesla"],
    )
    return await person_fixture_helper(client=client, db=db, new_person_creds=new_person_creds)


@pytest_asyncio.fixture
async def person_bishop(client: AsyncClient, db: Database) -> PersonInDB:
    new_person_creds = PersonCredentialsCreate(
        name_first="Tom",
        name_last="Bishop",
        email_label="home",
        username="smugglebishop@yahoo.com",
        password=passwords["bishop"]
    )
    return await person_fixture_helper(client=client, db=db, new_person_creds=new_person_creds)


@pytest_asyncio.fixture
async def person_david(client: AsyncClient, db: Database) -> PersonInDB:
    new_person_creds = PersonCredentialsCreate(
        name_first="Ziva",
        name_last="David",
        email_label="home",
        username="ziva.sings@yahoo.com",
        password=passwords["david"]
    )
    return await person_fixture_helper(client=client, db=db, new_person_creds=new_person_creds)


@pytest_asyncio.fixture
async def person_golightly(client: AsyncClient, db: Database) -> PersonInDB:
    new_person_creds = PersonCredentialsCreate(
        name_first="Holly",
        name_last="Golightly",
        email_label="home",
        username="boughsof.holly@outlook.com",
        password=passwords["golightly"]
    )
    return await person_fixture_helper(client=client, db=db, new_person_creds=new_person_creds)


@pytest_asyncio.fixture
async def person_tenenbaum(client: AsyncClient, db: Database) -> PersonInDB:
    new_person_creds = PersonCredentialsCreate(
        name_first="Margot",
        name_last="Tenenbaum",
        email_label="work",
        username="margot.paints@gmail.com",
        password=passwords["tenenbaum"]
    )
    return await person_fixture_helper(client=client, db=db, new_person_creds=new_person_creds)


@pytest_asyncio.fixture
async def person_list(
    person_bishop: PersonInDB, person_david: PersonInDB, person_golightly: PersonInDB, person_tenenbaum: PersonInDB,
) -> List[PersonInDB]:
    return [person_bishop, person_david, person_golightly, person_tenenbaum]
