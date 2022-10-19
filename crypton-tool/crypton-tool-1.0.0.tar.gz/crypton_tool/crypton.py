import base64
import os
import secrets
import string
import typing
from pathlib import Path

from cryptography.fernet import Fernet

from crypton_tool.logger import logger

log = logger().getLogger(__name__)


class Crypton:
    def __init__(self, key: typing.Union[bytes, str]):
        self.key = key

    @classmethod
    def generate_key(cls, to_file=None) -> bytes:
        alphabet = string.ascii_letters + string.digits
        key_base = os.urandom(22) + str.encode(
            "".join(secrets.choice(alphabet) for i in range(10))
        )
        key = base64.urlsafe_b64encode(key_base)
        if not to_file:
            return key
        Path(to_file / "token.crypton").write_bytes(key)

    @classmethod
    def read_token_file(self, path) -> bytes:
        if isinstance(path, str):
            path = Path(path)
        return path.read_bytes()

    def path_handler(self, path, pattern=None):
        if isinstance(path, str):
            path = Path(path)
            if path.is_dir():
                pattern = pattern if pattern else "*"
                return list(path.rglob(pattern))
            return [path]
        else:
            if isinstance(path, list):
                return [Path(p) for p in path]
            if path.is_dir():
                pattern = pattern if pattern else "*"
                return list(path.rglob(pattern))
            return [path]

    def _encrypt_file(self, file):
        try:
            cf = Fernet(self.key)
            file_content = file.read_bytes()
            token = cf.encrypt(file_content)
            file.write_bytes(token)
            return file
        except Exception as e:
            log.exception(e)
            return None

    def _decrypt_file(self, file):
        try:
            cf = Fernet(self.key)
            file_content = file.read_bytes()
            token = cf.decrypt(file_content)
            file.write_bytes(token)
            return file
        except Exception as e:
            log.exception(e)
            return None

    def encrypt_file(self, path, pattern=None):
        pattern = pattern if pattern else "*"
        path_list = self.path_handler(path, pattern)
        result = []
        for path in path_list:
            result.append(self._encrypt_file(path))
        return result

    def decrypt_file(self, path, pattern=None):
        pattern = pattern if pattern else "*"
        path_list = self.path_handler(path, pattern)
        result = []
        for path in path_list:
            result.append(self._decrypt_file(path))
        return result

    def encrypt_content(self, content):
        try:
            cf = Fernet(self.key)
            token = cf.encrypt(str.encode(content))
            return token
        except Exception as e:
            log.exception(e)
            return None

    def decrypt_content(self, content):
        try:
            cf = Fernet(self.key)
            token = cf.decrypt(str.encode(content))
            return token.decode("utf-8")
        except Exception as e:
            log.exception(e)
            return None
