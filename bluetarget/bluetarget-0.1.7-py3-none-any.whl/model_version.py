

import os
from typing import Dict, List

import requests

from bluetarget.api_endpoint import APIEndpoint
from bluetarget.errors import AuthorizationError, EntityNotFound, FileNotFound, ServerValidationException


class ModelVersion:
    api_key: str
    model_id: str
    model_version_id: str
    endpoint: APIEndpoint
    data: Dict

    def __init__(self, api_key: str, model_id: str) -> None:
        self.api_key = api_key
        self.model_id = model_id
        self.endpoint = APIEndpoint(api_key)

    def get(self, model_version_id: str):

        response, status = self.endpoint.get(
            f"models/{self.model_id}/versions/{model_version_id}")

        if status == 403:
            raise AuthorizationError()

        if status == 404:
            raise EntityNotFound("Model version", model_version_id)

        if status != 200:
            raise ServerValidationException(
                response['code'], response['description'])

        self.data = response
        self.set_model_version_id(response)

        return response

    def set_model_version_id(self, data):
        self.model_version_id = data['id']

    def create(self, model_class: str, model_files: List[str], requirements_file: str, metadata: Dict = None, environment: Dict = None, algorithm: str = None, implementation: str = None, framework: str = None):
        body = {
            "modelClass": model_class,
            "files": model_files,
            "requirementsFile": requirements_file
        }

        if metadata != None:
            body["metadata"] = metadata

        if environment != None:
            body["environment"] = environment

        if algorithm != None:
            body["algorithm"] = algorithm

        if implementation != None:
            body["implementation"] = implementation

        if framework != None:
            body["framework"] = framework

        response, status = self.endpoint.post(
            f"models/{self.model_id}/version", body=body)

        if status == 403:
            raise AuthorizationError()

        if status == 404:
            raise EntityNotFound("Model", self.model_id)

        if status != 200:
            raise ServerValidationException(
                response['code'], response['description'])

        self.data = response
        self.set_model_version_id(response)

        return response

    def upload_package(self, package_url: str):

        if os.path.exists(package_url) == False:
            raise FileNotFound(package_url)

        presigned_url, status = self.endpoint.post(
            f"models/{self.model_id}/versions/{self.model_version_id}/upload")

        url = presigned_url["uploadUrl"]
        fields = presigned_url["formData"]

        with open(package_url, 'rb') as f:
            files = {'file': (package_url, f)}
            requests.post(url, data=fields, files=files)

    def deploy(self):
        response, status = self.endpoint.post(
            f"models/{self.model_id}/versions/{self.model_version_id}/deploy")

        if status != 200:
            raise ServerValidationException(
                response['code'], response['description'])
