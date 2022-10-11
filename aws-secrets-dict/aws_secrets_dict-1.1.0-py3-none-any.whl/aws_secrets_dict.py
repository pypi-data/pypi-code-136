import json
from os import environ

import boto3
from botocore.exceptions import ClientError

class AwsSecrets():

    def __init__(self, key=None, secret=None, region=None):
        self.key = key or environ.get('AWS_ACCESS_KEY_ID')
        self.secret = secret or environ.get('AWS_SECRET_ACCESS_KEY')
        self.region = region or environ.get('AWS_REGION', 'us-east-2')
        self.service_name = 'secretsmanager'
        self.session = boto3.session.Session(
            aws_access_key_id = key,
            aws_secret_access_key = secret,
        )
        self.client = self.session.client(
            service_name = 'secretsmanager',
            region_name = self.region
        )

    def _get_secret(self, secret_name):
        response = self.client.get_secret_value(SecretId=str(secret_name))
        return response

    def _create_secret(self, secret_key, secret_value, secret_description=""):
        response = self.client.create_secret(
            Name = str(secret_key),
            Description = str(secret_description),
            SecretString = json.dumps(secret_value),
        )
        return response

    def _delete_secret(self, secret_ARN):
        response = self.client.delete_secret(
            SecretId = secret_ARN,
            ForceDeleteWithoutRecover = True,
        )
        return response
    
    def _update_secret(self, secret_ARN, new_value, description=""):
        response = self.client.update_secret(
            SecretId = secret_ARN,
            Description = str(description),
            SecretString = json.dumps(new_value),
        )
        return response
    
    def _list_secrets(self, max_results, next_token=None):
        response = None
        if next_token is None:
            response = self.client.list_secrets(
                MaxResults = max_results,
            )
        else:
            response = self.client.list_secrets(
                MaxResults = max_results,
                NextToken = next_token,
            )
        return response

    def __getitem__(self, key):
        response = self._get_secret(key)
        return json.loads(response["SecretString"])

    def __delitem__(self, name):
        response = self._get_secret(name)
        self._delete_secret(response["ARN"])
        return response["SecretString"]

    def __setitem__(self, key, value):
        try:
            response = self._create_secret(key, value)
            return
        except ClientError as e:
            if e.response["Error"]["Code"] == "ResourceExistsException":
                response = self._get_secret(key)
                self._update_secret(response["ARN"], value)
            else:
                raise e

    def _list_attribute(self, attribute):
        result = []
        response = self._list_secrets(100)
        for secret in response["SecretList"]:
            result.append(secret[attribute])
        while "NextToken" in response:
            response = self._list_secrets(100, response["NextToken"])
            for secret in response["SecretList"]:
                result.append(secret[attribute])
        return result

    def keys(self):
        return self._list_attribute("Name")
