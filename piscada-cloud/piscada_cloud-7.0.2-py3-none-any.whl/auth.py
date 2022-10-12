"""Authentication module: Login, retrieve credentials, and extract service access tokens."""
import argparse
import getpass
import json
import os
import sys
from pathlib import Path

import requests


def login(username, password, host):
    """Login to a host with username/password and retrieve credentials."""
    payload = {"piscadaId": username, "password": password}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"https://{host}/login", json=payload, headers=headers)
    if not response.ok:
        raise RuntimeError(f"Error during authentication: {response.text}")
    return json.loads(response.text)


def login_interactive():
    """
    Perform an interactive login. Host, username, and password can also be piped.

    ```
    bash> echo "host
    > username
    > password" | ./some_tool_using_login_interactive.py
    ```
    """
    if sys.stdin.isatty():
        print("Enter host and credentials")
        host = input("Host: ")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
    else:
        host = sys.stdin.readline().rstrip()
        username = sys.stdin.readline().rstrip()
        password = sys.stdin.readline().rstrip()
    return login(username, password, host)


def login_persisted(credentials_file=Path.home() / ".piscada_credentials"):
    """
    Perform an interactive login as above.

    This will persist credentials in credential_file, by default `$HOME/.piscada_credentials`, for later non-interactive use.
    """
    if os.path.isfile(credentials_file):
        with open(credentials_file, "r", encoding="utf-8") as infile:
            return json.load(infile)
    else:
        credentials = login_interactive()
        with open(credentials_file, "w", encoding="utf-8") as outfile:
            json.dump(credentials, outfile, indent=2)
        return credentials


def get_historian_credentials(credentials):
    """Retrieve the historian credentials from the provided credentials."""
    if "accessTokens" not in credentials:
        raise RuntimeError("No access tokens in credentials.")
    host_and_token = [(key, credentials["accessTokens"][key]) for key in credentials["accessTokens"] if key.startswith("historian")]
    if not host_and_token:
        raise RuntimeError("No historian access token in credentials.")
    if len(host_and_token) > 1:
        raise RuntimeError("Multiple historian access token in credentials.")
    return host_and_token[0]


def get_writeapi_credentials(credentials):
    """Retrieve the write-api credentials from the provided credentials."""
    if "accessTokens" not in credentials:
        raise RuntimeError("No access tokens in credentials.")
    host_and_token = [(key, credentials["accessTokens"][key]) for key in credentials["accessTokens"] if key.startswith("api")]
    if not host_and_token:
        raise RuntimeError("No historian access token in credentials.")
    if len(host_and_token) > 1:
        raise RuntimeError("Multiple historian access token in credentials.")
    return host_and_token[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Gets credentials stored in `credentials_file` if it \
            exists, otherwise an interactive authentication prompt will be shown. \
            If the authentication is valid, the fetched credentials are stored in \
            `$HOME/.piscada_credentials` if not the filepath is overridden."
    )
    parser.add_argument(
        "-f",
        "--filepath",
        type=str,
        required=False,
        help="File path to read/write credentials from/to. When supplying \
            this will override the default `$HOME/.piscada_credentials`.",
    )
    filepath = parser.parse_args().filepath
    try:
        if filepath:
            print(json.dumps(login_persisted(filepath), indent=2))
        else:
            print(json.dumps(login_persisted(), indent=2))
    except RuntimeError as err:
        print(err)
