""" This Module is created to enable Hepsiburada Data Science to communicate with Cloud Storage. """

import os
import json
import pickle
from io import BytesIO
import pandas as pd

from colorama import Fore, init  ##Style
from google.cloud import storage
from google.oauth2 import service_account
from google.api_core.exceptions import NotFound


init(autoreset=True)


class BucketOperations(storage.Client):
    """This class is created to enable Hepsiburada Data Science to communicate with Cloud Storage"""

    _implemented_type = ["dataframe", "json", "pickle"]

    def __init__(self, **kwargs) -> None:
        self.gcp_key = kwargs.get("gcp_key_path")
        self.credentials = kwargs.get("gcp_key_path")
        super().__init__(
            project=self.credentials.project_id,
            credentials=self.credentials
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(Project ID: {self.credentials.project_id}, "
            f"Service Account: {self.credentials._service_account_email.split('@')[0]})"
        )

    def upload_from_filepath(self,bucket_name, blob_name, filepath):
        """This function is to upload data from filepath."""
        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(filepath)

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

        except Exception:
            print(f"No such file in this path: <{filepath}>")
    
    def upload_from_memory(self, bucket_name, blob_name, contents, upload_type):
        """This function is to upload data from memory."""
        if upload_type not in BucketOperations._implemented_type:
            raise NotImplementedError(
                Fore.RED + f"Download type {upload_type} not implemented !!"
            )

        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)

            if upload_type == 'json':
                send_data = json.dumps(contents, indent=4).encode('utf-8')
            elif upload_type == 'pickle':
                send_data = pickle.dumps(contents)
            elif upload_type == "dataframe":
                send_data = contents.to_csv()

            blob.upload_from_string(send_data)

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

    def download_to_filepath(self,bucket_name, blob_name, filepath): 
        """This function is to download data from filepath."""
        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            if blob.exists():
                with open(filepath, 'wb') as f:
                    self.download_blob_to_file(blob, f)
            else:
                print(f"Blob <{blob_name}> does not exist.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")
        
        except Exception:
            print(f"No such file in this path: <{filepath}>")

    def download_to_memory(self,bucket_name, blob_name, download_type):
        """This function is to download data from memory."""
        if download_type not in BucketOperations._implemented_type:
            raise NotImplementedError(
                Fore.RED + f"Download type {download_type} not implemented !!"
            )

        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            if blob.exists():
                if download_type == 'dataframe':
                    df = pd.read_csv(
                            BytesIO(
                                blob.download_as_string()
                            ) ,
                            encoding='UTF-8',
                            sep=','
                        )
                    return df

                elif download_type == 'json':
                    data = blob.download_as_string().decode('utf8').replace("'", '"')
                    load_json = json.loads(data)
                    json_data = json.dumps(load_json, indent=4, sort_keys=True)
                    return json_data

                elif download_type == 'pickle':
                    data = blob.download_as_string()
                    load_pickle = pickle.loads(data)
                    return load_pickle
            else:
                print(f"Blob <{blob_name}> does not exist.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")

    def create_new_folders(self, bucket_name, folder_name):
        """This function is to create new folder from the bucket."""
        try:
            bucket = self.bucket(bucket_name)
            dst_bucket = self.bucket(bucket_name)

            blob = bucket.blob("New_Folder_Starter/")
            new_blob = bucket.copy_blob(blob, dst_bucket, new_name=folder_name)
            
            new_blob.acl.save(blob.acl)
            print(f"<{folder_name}> folder created.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")
    
    def delete_folder_from_bucket(self, bucket_name, folder_name):
        """This function is to create new folder from the bucket."""
        try:
            bucket = self.get_bucket(bucket_name)
            blobs = bucket.list_blobs(prefix=folder_name)
            for blob in blobs:
                blob.delete()
            
            print(f"Folder <{folder_name}> deleted.")

        except NotFound:
            print(f"Bucket <{bucket_name}> does not exist.")
    
    def delete_file_from_bucket(self, bucket_name, blob_name):
        """This function is to delete file from the bucket."""

        try:
            bucket = self.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.delete()
            print(f"Blob <{blob_name}> deleted.")

        except NotFound:
            print(f"No such file in this path: <{bucket_name}/{blob_name}>")


    @property
    def gcp_key(self):
        """This function is to get GCP key."""
        return self._gcp_key

    @gcp_key.setter
    def gcp_key(self, provided_gcp_key):
        """This function is to set GCP key."""
        if provided_gcp_key is not None:
            self._gcp_key = str(provided_gcp_key)
            self.credentials = str(provided_gcp_key)
        elif os.environ.get("SERVICE_ACCOUNT_KEY_PATH"):
            self._gcp_key = os.environ.get("SERVICE_ACCOUNT_KEY_PATH")
        else:
            self._gcp_key = None
            print(
                Fore.RED + "Warning!! GCP Key Path for Service Account is not specified"
            )

    @property
    def credentials(self):
        """This function is to get credentials."""
        return self._credentials

    @credentials.setter
    def credentials(self, provided_credentials):
        """This function is to set credentials."""
        if provided_credentials is not None:
            self._credentials = service_account.Credentials.from_service_account_file(
                self.gcp_key,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        elif os.environ.get("SERVICE_ACCOUNT_KEY_PATH"):
            self._credentials = service_account.Credentials.from_service_account_file(
                self.gcp_key,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        else:
            self._credentials = None
            print(
                Fore.RED + "Warning!! Credentials for Service Account is not specified"
            )
