import os
from contextlib import contextmanager

import boto3


@contextmanager
def connect(endpoint_url: str | None, access_key_id: str, secret_access_key: str):
    yield boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
    )


def download(client, bucket: str, key: str, path: str):
    # ensure depth
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(f"{path}", "wb") as f:
        client.download_fileobj(bucket, key, f)


def upload(client, bucket: str, key: str, path: str):
    with open(path, "rb") as f:
        client.upload_fileobj(f, bucket, key)
