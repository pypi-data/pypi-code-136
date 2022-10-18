import json

from .keys import USERNAME, LABELS, META_UPDATES_ARRAY
import requests


class DatalakeInterface:

    def __init__(self, auth_token: str, dalalake_url: str):
        self.auth_token = auth_token
        self.dalalake_url = dalalake_url

    def create_datalake_label_coco(self, label, username='Python SDK'):
        hed = {'Authorization': 'Basic ' + self.auth_token}
        payload = {
            USERNAME: username,
            LABELS: label,
        }
        url = f'{self.dalalake_url}/api/client/cocojson/import/label/create'

        try:
            response = requests.post(url=url, json=payload, headers=hed)
            return response.json()
        except requests.exceptions.RequestException as e:
            print("An exception occurred")
            print(e)

    def find_datalake_label_references(self, label_attribute_values_dict, username='Python SDK'):
        hed = {'Authorization': 'Basic ' + self.auth_token}
        payload = {
            LABELS: label_attribute_values_dict,
            USERNAME: username
        }
        url = f'{self.dalalake_url}/api/client/system/label/references'

        try:
            response = requests.post(url=url, json=payload, headers=hed)
            return response.json()
        except requests.exceptions.RequestException as e:
            print("An exception occurred | find_datalake_label_references")
            print(e)

    def upload_metadata_updates(self, meta_updates, operation_type, operation_mode, operation_id):
        hed = {'Authorization': 'Basic ' + self.auth_token}
        payload = {
            META_UPDATES_ARRAY: json.dumps(meta_updates),
        }
        url = f'{self.dalalake_url}/api/metadata/operationdata/{operation_type}/{operation_mode}/{operation_id}/update'

        try:
            response = requests.post(url=url, json=payload, headers=hed)
            return response.json()
        except requests.exceptions.RequestException as e:
            print("An exception occurred | find_datalake_label_references")
            print(e)
