import json
import shutil
import urllib.request as request
from contextlib import closing
from pathlib import Path

import requests
from batchx import bx

from .debug import debug_print


# load/save
def load_json(fp: Path | str):
    with open(fp, "r") as f:
        contents = f.read()
    return json.loads(contents)


def save_json(
    contents,
    fp: Path | str,
    verbose: bool = True,
):
    fp = Path(fp)

    dp = fp.parent
    dp.mkdir(parents=True, exist_ok=True)

    if isinstance(contents, str):
        contents = json.dumps(contents, default=str)

    with open(fp, "w+") as f:
        json.dump(contents, f, default=str)

    debug_print("Saved json to {}".format(fp), verbose=verbose)
    return


# download protocols
def download_resource(url: Path | str, fp: Path | str, verbose: bool = True, **kwargs):
    actions = dict(
        http=download_http,
        https=download_http,
        s3=download_s3,
        ftp=download_ftp,
        bx=download_bx,
    )

    protocol = Path(url).parts[0].split(":")[0]
    return actions.get(protocol)(url=url, fp=fp, verbose=verbose, **kwargs)


def download_encode(url: str, fp: Path | str):
    """Download file from the ENCODE portal."""

    def _obtain_json(url: str):
        headers = dict(
            accept="application/json"
        )  # Force return from the server in JSON format
        response = requests.get(url, headers=headers)  # GET the object
        return response.json()

    encode_json = _obtain_json(url)
    return download_s3(url=encode_json.get("s3_uri"), fp=fp)


def download_s3(url: Path | str, fp: Path | str, verbose: bool = True):
    try:
        import boto3
    except:
        raise ImportError("You should install boto3 if you want this functionality.")

    def _bucket_key_from_s3_uri(uri: Path | str):
        uri = str(uri)
        return uri.split("/", 2)[-1].split("/", 1)

    url = str(url)

    s3 = boto3.client("s3")
    bucket, key = _bucket_key_from_s3_uri(url)
    s3.download_file(bucket, key, str(fp))
    return


def download_bx(url: Path | str, fp: Path | str, env="test", verbose: bool = True):
    url = str(url)

    bx.connect()
    fs = bx.FilesystemService()
    request = fs.DownloadPresignedRequest(environment=env, path=url)
    response = fs.DownloadPresigned(request)

    return download_http(url=response.url, fp=fp, verbose=verbose)


def download_ftp(url: Path | str, fp: Path | str, verbose: bool = True):
    url = str(url)
    with closing(request.urlopen(url)) as src:
        with open(fp, "wb") as dst:
            shutil.copyfileobj(src, dst)
    return


def download_http(url: Path | str, fp: Path | str, verbose: bool = True):
    url = str(url)

    with open(fp, "wb") as f:
        f.write(requests.get(url).content)

    if verbose:
        fp = Path(fp)
        msg = """
        curl {url} --output {fn}
        """.format(
            url=url, fn=fp.name
        )
        print(msg)
    return
