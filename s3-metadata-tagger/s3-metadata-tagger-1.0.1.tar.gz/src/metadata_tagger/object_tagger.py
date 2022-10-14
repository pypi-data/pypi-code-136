"""
The object tagger is responsible for checking whether a file
has to be tagged, fetching it, and passing it to a supplied tagging
function
"""
from contextlib import contextmanager
import tempfile
import logging
import os
from typing import Callable, Dict, Generator, NamedTuple

import boto3
from botocore.exceptions import ClientError
from mypy_boto3_s3.type_defs import HeadObjectOutputTypeDef

if os.environ.get('LOCALSTACK_S3_ENDPOINT_URL'):
    s3_client = boto3.client(
        "s3", endpoint_url=os.environ.get('LOCALSTACK_S3_ENDPOINT_URL'))
else:
    s3_client = boto3.client("s3")


class S3ObjectPath(NamedTuple):
    """
    An object representing the location of an S3 object
    """
    key: str
    bucket: str


class MetadataHandler(NamedTuple):
    """
    The object containing the function for handling the actual metadata tagging of
    an S3 object.
    `already_tagged` is a function which determines
        whether a selected object has already been tagged.
    `extraction_function` is the function extracting the metadata from the passed object.
    `versioning_tags` is a dictionary of additional tags which are put onto the object.
        It can e.g. be used for tag versioning.
    """
    already_tagged: Callable[[Dict[str, str]], bool]
    extraction_function: Callable[[str], Dict[str, str]]
    versioning_tags: Dict[str, str] = {}


def tag_file(object_path: S3ObjectPath,
             metadata_handler: MetadataHandler) -> Dict[str, str]:
    """
    Returns a dictionary containing the metadata extracted by the passed
     `object_tagger.extraction_function` from the file found in the passed
     `object_path.bucket` with the passed `object_path.key`.
     The tagging is only done, if `object_tagger.already_tagged` returns `False`.
    """
    result = False
    retries = 0
    while not result and retries < 2:
        logging.info("Attempt %s", retries)
        object_info = _get_object_info(object_path)
        if metadata_handler.already_tagged(object_info["Metadata"]):
            logging.info("%s in %s is already tagged",
                         object_path.key, object_path.key)
            return object_info["Metadata"]
        with _download_file(object_path) as downloaded_file:
            custom_tags = metadata_handler.extraction_function(
                downloaded_file.name)
            metadata_tags = object_info["Metadata"] | custom_tags | metadata_handler.versioning_tags
            result = _tag_remote_file(
                object_path, metadata_tags, object_info["ETag"])
            retries = retries + 1
            if result:
                return custom_tags
    raise RuntimeError("Could not tag file succesfully")


def _get_object_info(object_path: S3ObjectPath) -> HeadObjectOutputTypeDef:
    logging.info("checking whether %s in %s is already tagged",
                 object_path.key, object_path.bucket)
    return s3_client.head_object(Bucket=object_path.bucket, Key=object_path.key)


@contextmanager
def _download_file(object_path: S3ObjectPath) -> Generator:
    with tempfile.NamedTemporaryFile() as target:
        s3_client.download_file(
            object_path.bucket, object_path.key, target.name)
        logging.debug("Downloaded %s from %s",
                      object_path.bucket, object_path.key)
        yield target


def _tag_remote_file(object_path: S3ObjectPath, metadata_tags: Dict[str, str], etag: str) -> bool:
    try:
        s3_client.copy_object(Key=object_path.key,
                              Bucket=object_path.bucket,
                              CopySource={
                                  "Bucket": object_path.bucket, "Key": object_path.key},
                              Metadata=metadata_tags,
                              MetadataDirective="REPLACE",
                              CopySourceIfMatch=etag)
        logging.info("Tagged %s from %s with %s", object_path.key,
                     object_path.bucket, metadata_tags)
        return True
    except ClientError as error:
        logging.error(error)
        return False
