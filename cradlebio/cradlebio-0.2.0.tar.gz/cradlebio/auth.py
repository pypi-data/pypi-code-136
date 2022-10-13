"""Helper functions for authenticating users to Google Services such as Firebase or GCS """
import contextlib
import json
import logging
from datetime import datetime, timedelta
import os
import sys
from typing import Union, List, Optional
from getpass import getpass

from fsspec import config
from google.auth.credentials import Credentials, Scoped
from google.auth import transport, jwt
from google.cloud import firestore, storage
from importlib_metadata import version
from packaging.version import parse as version_parse


class IdentityPlatformTokenCredentials(Credentials):
    """A refreshable Identity Platform JWT ID Token.

    See: https://cloud.google.com/identity-platform/docs/use-rest-api#section-refresh-token for details
    Can be loaded from a JSON file available at https://auth.internal.cradle.bio

    In addition to parent attributes provides:
    uid: A string with the Identity Platform specific user ID
    """

    def __init__(self, refresh_token: str, token: str, api_key: str):
        """Initialize directly from token values.

        :param refresh_token: Signed token used to fetch new ID tokens from the secure token service
        :param token: JWT used to access resources.
        :param api_key: Key used to identify this application to the identity platform
        """
        super().__init__()
        self.refresh_token = refresh_token
        self.token = token
        self.api_key = api_key

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value: str):
        """Decode the JWT and populate necessary values for the parent class."""
        if value:
            data = jwt.decode(value, verify=False)
            self._quota_project_id = data['aud']
            self.project_id = data['aud']
            self.expiry = datetime.utcfromtimestamp(int(data['exp']))
            self.uid = data['sub']
        self._token = value

    def refresh(self, request: transport.Request):
        logging.debug(self.token)
        resp = request(
            f'https://securetoken.googleapis.com/v1/token?key={self.api_key}',
            method='POST',
            json={'grant_type': 'refresh_token', 'refresh_token': self.refresh_token})
        data = json.loads(resp.data.decode('utf-8'))
        if 'access_token' not in data:
            raise RuntimeError(f'JWT token retrieval failed: response {str(data)}')

        self.token = data['access_token']

    @classmethod
    def from_file(cls, filepath: str):
        with open(filepath, 'r', encoding='utf-8') as f:
            return cls(**json.load(f))

    @classmethod
    def from_string(cls, creds: str):
        return cls(**json.loads(creds))

    def as_access_token_credentials(self, scopes: List[str] = None):
        """Get credentials that use an access token obtained via Workload Identity (see STSCredentials)."""
        return WorkloadIdentityCredential(self, scopes=scopes)


def _fetch_minimum_version(auth: IdentityPlatformTokenCredentials) -> str:
    client = get_client(auth)
    return client.document("python-client/required-version").get().get("afaas")


def _enforce_version(auth: IdentityPlatformTokenCredentials):
    package_version = version_parse(version("cradlebio"))
    minimum_version = version_parse(_fetch_minimum_version(auth))

    if minimum_version <= package_version:
        return

    raise RuntimeError(
        f"Package cradlebio v.{package_version} is deprecated. "
        f"Please run \"pip install cradlebio -U\" to upgrade to the latest client version"
    )


def authorize(*, safe_creds_file: Optional[str] = None) -> IdentityPlatformTokenCredentials:
    """
    Fetches credentials for using the Alphafold service.

    Args:
        safe_creds_file: A path to your credentials from `auth.cradle.bio <https://auth.cradle.bio>`_.
    """
    if safe_creds_file and os.path.isfile(safe_creds_file):
        return IdentityPlatformTokenCredentials.from_file(safe_creds_file)

    creds = getpass(prompt='Credentials from https://auth.cradle.bio/ ')
    auth = IdentityPlatformTokenCredentials.from_string(creds)

    _enforce_version(auth=auth)

    if safe_creds_file:
        with open(safe_creds_file, 'w', encoding='utf-8') as f:
            f.write(creds)
            print(
                f"Credentials written to '{safe_creds_file}'. Make sure not to share this file with anyone!", file=sys.stderr)

    return auth

@contextlib.contextmanager
def fsspec_creds(creds: IdentityPlatformTokenCredentials):
    """Context manager for loading files with fsspec using Cradle credentials."""
    old_value = config.conf.setdefault("gcs", {}).get('token', 'default')
    config.conf['gcs']['token'] = creds.as_access_token_credentials().with_scopes(
        storage.Client.SCOPE)
    yield
    config.conf['gcs']['token'] = old_value



class WorkloadIdentityCredential(Credentials, Scoped):
    """Fetches access tokens for a Workload Identity Principal using a JWT from the Identity Platform

    See https://cloud.google.com/iam/docs/configuring-workload-identity-federation for details on how this works
    """

    def __init__(self, jwt_creds: IdentityPlatformTokenCredentials,
                 scopes: List[str] = None,
                 default_scopes: List[str] = None):
        super().__init__()
        self.jwt_creds = jwt_creds
        self.token = None
        self.expiry = datetime.fromtimestamp(0)
        self._quota_project_id = self.jwt_creds.quota_project_id
        self.project_id = self.jwt_creds.project_id
        self._scopes = [] if scopes is None else scopes
        self._default_scopes = [] if default_scopes is None else default_scopes

    @property
    def requires_scopes(self):
        return True

    def with_scopes(self, scopes, default_scopes=None):
        return WorkloadIdentityCredential(self.jwt_creds, scopes, default_scopes)

    def refresh(self, request: transport.Request):
        # Make sure the identity platform JWT token is fresh
        if not self.jwt_creds.valid:
            self.jwt_creds.refresh(request)

        resp = request(
            'https://sts.googleapis.com/v1/token',
            method='POST',
            json={
                "audience": "//iam.googleapis.com/projects/473699240866/locations/global/workloadIdentityPools/firebase/providers/firebase",
                "grantType": "urn:ietf:params:oauth:grant-type:token-exchange",
                "requestedTokenType": "urn:ietf:params:oauth:token-type:access_token",
                "scope": " ".join(self.scopes or self.default_scopes),
                "subjectTokenType": "urn:ietf:params:oauth:token-type:jwt",
                "subjectToken": self.jwt_creds.token
            }
        )
        data = json.loads(resp.data.decode('utf-8'))
        if 'access_token' not in data:
            raise RuntimeError(f'Access token retrieval failed: response {str(data)}')
        self.expiry = datetime.utcnow() + timedelta(seconds=int(data['expires_in']))
        self.token = data['access_token']


def get_client(credentials: Union[IdentityPlatformTokenCredentials, str]) -> firestore.Client:
    if isinstance(credentials, str):
        credentials = IdentityPlatformTokenCredentials.from_file(credentials)

    return firestore.Client(
        credentials=credentials,
        project=credentials.quota_project_id)
