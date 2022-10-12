import logging
from tempfile import TemporaryDirectory
from uuid import uuid4

# jwt, rsa, and freezegun are not available in every project. This is ok if the tests are not executed there.
# Catch and raise the import errors to silence pylint:
try:
    import freezegun
    import jwt
    import rsa
    from jwt.exceptions import InvalidTokenError
except ImportError as importError:
    raise importError

from ..access_token_tools import AccessTokenTools, AccessTokenToolsException


def decode_payload(access_token: str, access_token_tools: AccessTokenTools) -> dict:
    return jwt.decode(access_token, access_token_tools.public_key, algorithms=access_token_tools.algorithm)


def validate_access_token(access_token: str, subject: str, access_token_tools: AccessTokenTools) -> bool:
    is_valid = False
    try:
        payload = decode_payload(access_token, access_token_tools)
    except InvalidTokenError:
        payload = None
    if payload is not None and payload["sub"] == subject:
        is_valid = True
    return is_valid


def test_access_token():
    logger = logging.getLogger("test_access_token")
    logger.setLevel(logging.DEBUG)
    with TemporaryDirectory() as temp_directory:
        keys_directory = str(temp_directory)

        keys_creator = AccessTokenTools(keys_directory)
        keys_creator.create_rsa_key_files(logger)

        access_token_tools = AccessTokenTools(keys_directory)

        test_id = str(uuid4())
        test_id_2 = str(uuid4())
        valid_period = 5 * 60

        with freezegun.freeze_time("1970-01-01T00:00:00"):
            # Create a first token and verify its data
            token = access_token_tools.create_token(subject=test_id, expires_after_seconds=valid_period)
            assert type(token) == str
            assert len(token) > 0
            payload = decode_payload(token, access_token_tools)
            assert payload["sub"] == test_id
            assert payload["exp"] == valid_period
            assert validate_access_token(token, test_id, access_token_tools)
            assert not validate_access_token(token, test_id_2, access_token_tools)

            # Create a second token with the same data, it must have a different access token
            token2 = access_token_tools.create_token(subject=test_id, expires_after_seconds=valid_period)
            assert type(token2) == str
            assert token2 != token
            payload2 = decode_payload(token2, access_token_tools)
            assert payload2["sub"] == test_id
            assert payload2["exp"] == valid_period
            assert validate_access_token(token2, test_id, access_token_tools)
            assert not validate_access_token(token2, test_id_2, access_token_tools)

            # Create a third token with a different id, it must have a different access token
            token3 = access_token_tools.create_token(subject=test_id_2, expires_after_seconds=valid_period)
            assert type(token3) == str
            assert token3 != token
            assert token3 != token2
            payload3 = decode_payload(token3, access_token_tools)
            assert payload3["sub"] == test_id_2
            assert payload3["exp"] == valid_period
            assert validate_access_token(token3, test_id_2, access_token_tools)
            assert not validate_access_token(token3, test_id, access_token_tools)

            # Token must validate with the same test_id
            assert validate_access_token(token, test_id, access_token_tools) is True
            assert validate_access_token(token2, test_id, access_token_tools) is True
            assert validate_access_token(token3, test_id_2, access_token_tools) is True

            # Token may not validate with a different test_id
            assert validate_access_token(token, str(uuid4()), access_token_tools) is False
            assert validate_access_token(token2, test_id_2, access_token_tools) is False
            assert validate_access_token(token3, test_id, access_token_tools) is False

        # Let the tokens expire, they may not validate afterwards
        with freezegun.freeze_time("1970-01-01T00:05:01"):
            assert validate_access_token(token, test_id, access_token_tools) is False
            assert validate_access_token(token2, test_id, access_token_tools) is False
            assert validate_access_token(token3, test_id_2, access_token_tools) is False

        # Create a new token that will be refreshed before it expires
        with freezegun.freeze_time("1970-01-01T00:00:00"):
            token = access_token_tools.create_token(subject=test_id, expires_after_seconds=valid_period)
            token2 = access_token_tools.create_token(subject=test_id_2, expires_after_seconds=valid_period)

        with freezegun.freeze_time("1970-01-01T00:04:59"):
            assert validate_access_token(token, test_id, access_token_tools) is True
            assert validate_access_token(token2, test_id, access_token_tools) is False
            assert validate_access_token(token2, test_id_2, access_token_tools) is True
            token = access_token_tools.create_token(subject=test_id, expires_after_seconds=valid_period)
            token2 = access_token_tools.create_token(subject=test_id_2, expires_after_seconds=valid_period)

        with freezegun.freeze_time("1970-01-01T00:09:59"):
            assert validate_access_token(token, test_id, access_token_tools) is True
            assert validate_access_token(token2, test_id_2, access_token_tools) is True

        with freezegun.freeze_time("1970-01-01T00:10:00"):
            assert validate_access_token(token, test_id, access_token_tools) is False
            assert validate_access_token(token2, test_id_2, access_token_tools) is False


def test_access_token_verify_private_public_keys():
    logger = logging.getLogger("test_access_token")
    logger.setLevel(logging.DEBUG)
    with TemporaryDirectory() as temp_directory:
        keys_directory = str(temp_directory)

        keys_creator = AccessTokenTools(keys_directory)
        keys_creator.create_rsa_key_files(logger)

        access_token_tools = AccessTokenTools(keys_directory)
        assert b"BEGIN RSA PUBLIC KEY" in access_token_tools.public_key
        assert b"BEGIN RSA PUBLIC KEY" not in access_token_tools.private_key
        assert b"BEGIN RSA PRIVATE KEY" not in access_token_tools.public_key
        assert b"BEGIN RSA PRIVATE KEY" in access_token_tools.private_key

        try:
            rsa.PublicKey.load_pkcs1(access_token_tools.private_key)
            assert not "AccessTokenTools.private_key contains a public key"
        except ValueError as e:
            assert "No PEM start marker \"b'-----BEGIN RSA PUBLIC KEY-----'\" found" in str(e)

        try:
            rsa.PrivateKey.load_pkcs1(access_token_tools.public_key)
            assert not "AccessTokenTools.public_key contains a private key"
        except ValueError as e:
            assert "No PEM start marker \"b'-----BEGIN RSA PRIVATE KEY-----'\" found" in str(e)

        assert rsa.PublicKey.load_pkcs1(access_token_tools.public_key) is not None
        assert rsa.PrivateKey.load_pkcs1(access_token_tools.private_key) is not None


def test_access_token_key_files_must_exist():
    logger = logging.getLogger("test_access_token")
    logger.setLevel(logging.DEBUG)
    with TemporaryDirectory() as temp_directory:
        keys_directory = str(temp_directory)
        try:
            assert AccessTokenTools(f"{keys_directory}/does_not_exist").public_key is None
            assert AccessTokenTools(f"{keys_directory}/does_not_exist").private_key is None
            assert not "Expected 'AccessTokenToolsException' did not occur"
        except AccessTokenToolsException:
            pass

        try:
            assert AccessTokenTools(keys_directory).public_key is None
            assert AccessTokenTools(keys_directory).private_key is None
            assert not "Expected 'AccessTokenToolsException' did not occur"
        except AccessTokenToolsException:
            pass

        try:
            AccessTokenTools(keys_directory).create_rsa_key_files(logger)
            assert AccessTokenTools(keys_directory).public_key is not None
            assert AccessTokenTools(keys_directory).private_key is not None
        except AccessTokenToolsException as e:
            assert not f"Unexpected 'AccessTokenToolsException' occurred: {e}"
