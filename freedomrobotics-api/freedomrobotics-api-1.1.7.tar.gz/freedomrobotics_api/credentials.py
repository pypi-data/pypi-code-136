import os
import json
from json import JSONDecodeError

CREDENTIALS_PATH = os.path.expanduser("~/.freedom_credentials")
ENVIRONMENTS = ['dev', 'qa', 'staging', 'release']  # TODO: Handle envs on credentials
URLS = {
    'local': 'http://localhost:8001',
    'dev': 'https://dev.api.freedomrobotics.ai',
    'qa': 'https://qa.api.freedomrobotics.ai',
    'staging': 'https://staging.api.freedomrobotics.ai',
    'release': 'https://api.freedomrobotics.ai',
}
DEFAULT_URL = URLS['release']


def credentials_exist():
    return os.path.exists(CREDENTIALS_PATH)


def get_credentials(path=CREDENTIALS_PATH):
    return Credentials.from_path(path=path)


class Credentials:

    def __init__(self, token=None, secret=None, url=DEFAULT_URL, path=CREDENTIALS_PATH, **kwargs):
        if token is None or secret is None:
            raise CredentialsError("Both `token` and `secret` cannot be empty")
        self.token = token
        self.secret = secret
        if url is None:
            url = DEFAULT_URL
        self.url = url
        self.path = path

    def save(self):
        new_data = {
            'token': self.token,
            'secret': self.secret,
        }
        if self.url is not None:
            new_data['url'] = self.url
        # Read previous content to update it without overriding other envs
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                data = json.load(f)
            data.update(new_data)
        else:
            data = new_data
        # Saves new file
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def from_path(cls, path):
        """Loads the credentials from a path."""

        with open(path, 'r') as f:
            try:
                data = json.load(f)
            except JSONDecodeError as e:
                raise CredentialsError(f"Invalid JSON credentials on `{path}`. {e}")
        return cls(path=path, **data)


def validate_env(env):
    if env is not None and env not in ENVIRONMENTS:
        raise ValueError(
            f"Invalid environment `{env}`. Must be one of {ENVIRONMENTS}"
        )


class CredentialsError(Exception):
    pass
