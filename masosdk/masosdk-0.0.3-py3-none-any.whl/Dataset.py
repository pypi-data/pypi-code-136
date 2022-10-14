import os
import numpy as np
import requests

from .config import Config


class Dataset:
    def __init__(self, api_token, **kwargs):
        self.api_token = api_token
        self.name = None
        self.shape = None
        self.id = None

        if kwargs.get('name') and kwargs.get('shape'):
            self.create_new(kwargs.get('name'), kwargs.get('shape'))
        elif kwargs.get('id'):
            self.create_from_id(kwargs.get('id'))

    def create_new(self, name, shape):
        self.name = name

        self.shape = shape

        response = requests.post(
            f'{Config.base_url}/dataset/',
            headers={"Authorization": f"{self.api_token}"},
            json={
                'name': self.name,
                'shape': self.shape
            },
            verify=False
        )

        response.raise_for_status()

        if response.status_code == 200:
            self.id = response.json()

    def create_from_id(self, id):
        self.id = id

        response = requests.get(
            f'{Config.base_url}/dataset/{self.id}',
            headers={"Authorization": f"{self.api_token}"},
            verify=False,
        )

        response.raise_for_status()

        data = response.json()

        self.name = data['path']

        self.shape = data['shape']

    def upload_array(self, data, slc):
        response = requests.put(
            f'{Config.base_url}/array/{self.id}/',
            headers={"Authorization": f"{self.api_token}"},
            json={
                'data': list(data.flatten('F')),
                'slice': slc
            },
            verify=False
        )

        response.raise_for_status()

    def get_array(self, slc):
        response = requests.get(
            f'{Config.base_url}/array/{self.id}/',
            headers={"Authorization": f"{self.api_token}"},
            params={
                'slice': tuple(slc)
            },
            verify=False
        )

        response.raise_for_status()

        data = np.array(response.json()['data'])

        shape = tuple([self.shape[i] for i, x in enumerate(slc) if x == -1])

        data = np.reshape(data, shape)

        return data

    def get_parameter(self, key):
        response = requests.get(
            f'{Config.base_url}/parameter/{self.id}/',
            headers={"Authorization": f"{self.api_token}"},
            params={
                'key': key
            },
            verify=False
        )

        response.raise_for_status()

        return response.json()

