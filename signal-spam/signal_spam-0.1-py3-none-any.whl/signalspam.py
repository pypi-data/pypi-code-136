"""Send .eml files to signal-spam.fr."""

from base64 import b64encode
from pathlib import Path
from getpass import getpass
import argparse

import requests

__version__ = "0.1"


CONF = Path("~/.signal-spam").expanduser()


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("eml", type=Path, help="An email file to report as spam.")
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        username, password = CONF.read_text(encoding="UTF-8").splitlines()
    except FileNotFoundError:
        username = input("signal spam username: ")
        password = getpass("signal spam password: ")
        CONF.write_text(f"{username}\n{password}\n", encoding='UTF-8')
        CONF.chmod(0o600)
    payload = {"dossier": 0, "message": b64encode(args.eml.read_text(encoding="UTF-8").encode("UTF-8"))}
    response = requests.post(
        "https://www.signal-spam.fr/api/signaler",
        auth=(username, password),
        timeout=10,
        data=payload)
    print("Sent")
    print(response.text)


if __name__ == '__main__':
    main()
