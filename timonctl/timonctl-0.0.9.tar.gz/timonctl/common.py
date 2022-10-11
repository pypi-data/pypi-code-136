import json
import jwt
import os
import uuid

from . import logger, settings, user_config_dir
from .models import Token


def is_valid_uuid(value: str):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False


def get_token_from_file(profile: str):
    path = os.path.join(user_config_dir(), f"{profile}.json")
    logger.debug(f"Trying to load token for {profile}: {path}")
    try:
        with open(path, "r") as fp:
            data = json.load(fp)
            token = Token(**data)

        logger.debug(f"Using cached token for {profile}: {path}")

    except FileNotFoundError:
        token = None

    return token


def remove_token_file(profile: str):
    path = os.path.join(user_config_dir(), f"{profile}.json")
    logger.debug(f"Removing token file for {profile}: {path}")

    try:
        os.remove(path)
    except FileNotFoundError as e:
        raise e


def write_token_to_file(profile: str, token: Token):
    path = os.path.join(user_config_dir(), f"{profile}.json")
    logger.debug(f"Writing token for {profile}: {path}")
    with open(path, "w+") as fp:
        json.dump(token.dict(), fp)


def encode_token(token: Token) -> str:
    return jwt.encode(
        token.dict(),
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm
    )
