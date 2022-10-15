import requests
import shutil
import os

from ..errors import AccessError, RequestError


def get_api(url: str, session: requests.Session | None = None):
    """Function to get api and deal with errors."""
    if session is None:
        req = requests.get(url)
    else:
        req = session.get(url)

    if req.status_code != 200:
        raise AccessError(f"Bad response: {req.status_code}")

    if req.json().get("error"):
        # hint to where error might be.
        error_url = url.replace('&', '&\n\t\t').replace('?', '?\n\t\t')
        raise RequestError(f"Something went wrong. Error message: {req.json()['error']['error_msg']}"
                           f"\n\nPlease check parameters in the URL below.\n"
                           f"URL: \t{error_url}")
    return req


def download_from_url(url: str, folder: str, filename: str, session: None | requests.Session = None) -> bytearray:
    """Downloads file from url to a specified folder, returns file's binary data."""

    if session is None:
        req = requests.get(url)
    else:
        req = session.get(url)

    if req.status_code == 200:
        _, extension = req.headers.get('content-type').split("/")
        if not os.path.exists(folder):
            os.makedirs(folder)
        filename = f"{filename}.{extension}"
        with open(os.path.join(folder, filename), 'wb') as f:
            f.write(req.content)
    return req.content
