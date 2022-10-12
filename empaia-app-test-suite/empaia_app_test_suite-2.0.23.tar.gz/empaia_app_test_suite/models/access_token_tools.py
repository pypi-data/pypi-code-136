import logging
import os
from calendar import timegm
from datetime import datetime, timezone
from typing import NewType, Type, Union

# jwt and rsa are not available in every project. This is ok if AccessToken and
# AccessTokenTools are not used. Catch and raise the import errors to silence pylint:
try:
    import jwt
    import rsa
except ImportError as e:
    raise e


class AccessTokenToolsException(RuntimeError):
    pass


class AccessTokenTools:
    KeyType = NewType("KeyType", Union[Type[rsa.PublicKey], Type[rsa.PrivateKey]])

    def __init__(self, keys_directory: str):
        self._private_key = None
        self._public_key = None
        self.algorithm = "RS256"
        self.last_token_id = 0
        self.keys_directory = keys_directory

    @property
    def private_key(self):
        if self._private_key is None:
            self._private_key = self._read_key_file(rsa.PrivateKey)
        return self._private_key

    @property
    def public_key(self):
        if self._public_key is None:
            self._public_key = self._read_key_file(rsa.PublicKey)
        return self._public_key

    def create_rsa_key_files(self, logger: logging.Logger):
        if not os.path.isdir(self.keys_directory):
            logger.info(f"RSA keys directory does not exist... creating '{self.keys_directory}'")
            os.makedirs(self.keys_directory)
        self._ensure_key_files_exist(logger)

    def _get_key_file(self, keyType: KeyType) -> str:
        return os.path.join(self.keys_directory, "rsa_id" if keyType is rsa.PrivateKey else "rsa_id.pub")

    def _ensure_key_files_exist(self, logger: logging.Logger):
        key_files = [
            self._get_key_file(rsa.PublicKey),
            self._get_key_file(rsa.PrivateKey),
        ]
        if not (os.path.isfile(key_files[0]) and os.path.isfile(key_files[1])):
            logger.debug(f"Creating RSA keys in directory '{self.keys_directory}': {key_files[0]}, {key_files[1]}")
            keys = rsa.newkeys(1024)
            for key_file, key in zip(key_files, keys):
                with open(key_file, "wb") as f:
                    f.write(key.save_pkcs1())

    def _read_key_file(self, keyType: KeyType) -> bytes:
        if not os.path.isdir(self.keys_directory):
            raise AccessTokenToolsException(
                "Class AccessTokenTools requires existing RSA keys, "
                f"but the storage directory does not exist: {self.keys_directory}"
            )
        key_file = self._get_key_file(keyType)
        if not os.path.isfile(key_file):
            raise AccessTokenToolsException(
                "Class AccessTokenTools requires existing RSA keys, " f"but a key file does not exist: {key_file}"
            )
        with open(key_file, "rb") as f:
            key = keyType.load_pkcs1(f.read())
            return key.save_pkcs1()

    def create_token(self, subject: str, expires_after_seconds) -> str:
        # store an id in the payload, so that each token will be unique
        self.last_token_id += 1
        payload = {
            "sub": subject,
            "exp": AccessTokenTools.get_current_time() + expires_after_seconds,
            "token_id": self.last_token_id,
        }
        return jwt.encode(payload, self.private_key, algorithm=self.algorithm)

    def create_wbs_fronend_token(self, app_id: str, app_ui_url: str, expires_after_seconds) -> str:
        # store an id in the payload, so that each token will be unique
        self.last_token_id += 1
        payload = {
            "app_id": app_id,
            "app_ui_url": app_ui_url,
            "exp": AccessTokenTools.get_current_time() + expires_after_seconds,
            "token_id": self.last_token_id,
        }
        return jwt.encode(payload, self.private_key, algorithm=self.algorithm)

    @staticmethod
    def get_current_time() -> int:
        # Same code to determine the time as PyJWT uses
        now = timegm(datetime.now(tz=timezone.utc).utctimetuple())
        assert type(now) is int
        return now
