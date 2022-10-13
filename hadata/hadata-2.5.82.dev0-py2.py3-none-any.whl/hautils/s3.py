import logging
import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

from hautils.logger import logger
from hautils.missconfig import MissingConfiguration
from hautils.web import exception_log

load_dotenv(override=False)

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

if ACCESS_KEY is None:
    raise MissingConfiguration("AWS_ACCESS_KEY_ID")
if SECRET_KEY is None:
    raise MissingConfiguration("AWS_SECRET_ACCESS_KEY")


def get_s3_client() -> boto3.client:
    """
    The get_s3_client function creates a boto3 s3 client object.
    It requires the ACCESS_KEY and SECRET_KEY variables to be set in the environment.
    The region is set to ap-southeast-2 as that's where our S3 bucket is located.

    :return: A boto3
    :doc-author: Trelent
    """
    logger.info("getting s3 client")
    return boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name='ap-southeast-1')


def upload_file(file_obj, object_name=None, CallBack=None):
    """
    The upload_file function uploads a file to an S3 bucket.



    :param file_obj: Pass the file object to upload
    :param object_name=None: Specify the name of the s3 object
    :return: True on success
    :doc-author: Trelent
    """
    logger.info(f"uploading a file to s3 bucket {S3_BUCKET_NAME}")
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_obj
    try:
        s3_client: boto3 = get_s3_client()
        logger.debug(f"uploading file {object_name} ")
        result = s3_client.upload_fileobj(file_obj, S3_BUCKET_NAME, f"{object_name}", Callback=CallBack)
        logger.debug(f"error upload {result} ")
        return True
    except Exception as e:
       exception_log(e)


def upload_file_2(file_obj, object_name=None):
    """
    The upload_file_2 function uploads a file to an S3 bucket.


    :param file_obj: Store the file object
    :param object_name=None: Specify the name of the file to be uploaded
    :return: True if the file was uploaded, and false otherwise
    :doc-author: Trelent
    """
    # If S3 object_name was not specified, use file_name
    s3_client = get_s3_client()
    if object_name is None:
        object_name = file_obj
    try:
        s3_client.upload_file(file_obj, S3_BUCKET_NAME, f"{object_name}")
    except ClientError as e:
        logging.error(e)
        return False
    return True


def delete_file(file_obj):
    """
    The delete_file function deletes a file from the s3 bucket.
    It takes in a file object and deletes it from the s3 bucket.

    :param file_obj: Pass the file name to be deleted
    :return: True if the file was deleted successfully
    :doc-author: Trelent
    """
    logger.info(f"deleting a file from s3 {file_obj} ")
    try:
        s3 = get_s3_client()
        ok, meta = s3.delete_object(Bucket=S3_BUCKET_NAME, Key=file_obj)
        return ok
    except Exception as ex:
        exception_log(ex)


def create_presigned_url(object_name, expiration):
    """
    The create_presigned_url function creates a pre-signed URL for the S3 object
       identified by the given input key. A URL can be created for any S3 object in your bucket.
       The expiration time, specified in seconds, is also an input parameter.

    :param object_name: Specify the object that you want a pre-signed url for
    :param expiration: Set the time for which the url is valid
    :return: A presigned url that you can use to download the object
    :doc-author: Trelent
    """
    logger.info("creating a pre signed url for object")
    s3_client = get_s3_client()
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': S3_BUCKET_NAME,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    return response


def download_file(bucket, local_file, s3_file):
    """
    The download_file function downloads a file from an S3 bucket to the local machine.
       The function takes three arguments:
           1) bucket - the name of the S3 bucket where you are downloading from (string)
           2) local_file - path and filename for your downloaded file on your local machine (string)
           3) s3_file - path and filename for your uploaded file in the S3 bucket (string).

       The function returns True if successful, otherwise it will return False.

    :param bucket: Specify the bucket name in s3
    :param local_file: Specify the name of the local file to be created
    :param s3_file: Specify the name of the file in s3
    :return: True
    :doc-author: Trelent
    """
    logger.info("downloading from s3")
    client = get_s3_client()
    client.download_file(bucket, s3_file, local_file)
    logger.info(f"Download Successful of remote file {s3_file} to local file {local_file}")

    return True
