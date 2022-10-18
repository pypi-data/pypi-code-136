from tarfile import RECORDSIZE
from typing import OrderedDict
import requests
import json

class AirTable:
        
    def __init__(self, ws_url, base_key, api_key, table_name):
        self.ws_url = ws_url
        self.base_key = base_key
        self.api_key = api_key
        self.table_name = table_name

    def get_records(self) -> list:
        ''' Returns a list of record dictionaries'''
        url = f"{self.ws_url}{self.base_key}/{self.table_name}"
        data = self._get_data(url)
        records = data["records"]
        return records

    def get_record(self, id:str) -> dict:
        ''' Returns a single record dictionary'''
        url = f"{self.ws_url}{self.base_key}/{self.table_name}/{id}"
        record = self._get_data(url)
        return record

    def get_records_by_search(self, field:str, value:str) -> list:
        ''' Returns a list of record dictionaries based on field and value'''
        item = None
        url = f"{self.ws_url}{self.base_key}/{self.table_name}"
        filter = f"SEARCH(%22{value}%22%2C%7B{field}%7D)"
        param = f"filterByFormula={filter}"
        data = self._get_data(url, param)
        records = data["records"]
        return records
  
    def add_record(self, fields:dict) -> dict:
        ''' Adds a record'''
        data = json.dumps({"fields": fields})
        url = f"{self.ws_url}{self.base_key}/{self.table_name}"
        headers = {"Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json"}
        params = None
 
        r = requests.post(url=url, headers=headers, params=params, data=data)
    
        if r.status_code != 200:
            message = f"Bad request. Unable to create record. " + r.text
            if self.log_service:
                self.log_service.update("ERROR", message)
            raise Exception(message)
        else:
            record = r.json()
            return record
            
    def update_record(self, record:dict) -> dict:
        ''' Updates a record'''
        data = json.dumps({"fields":record["fields"]})
        
        url = f"{self.ws_url}{self.base_key}/{self.table_name}/{record['id']}"
        headers = {"Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json"}
        params = None
 
        r = requests.patch(url=url, headers=headers, params=params, data=data)
    
        if r.status_code != 200:
            message = f"Bad request. Unable to update record. " + r.text
            if self.log_service:
                self.log_service.update("ERROR", message)
            raise Exception(message)
        else:
            record = r.json()
            # record["id"] = r.json()["id"]
            # record["fields"] = r.json()["fields"]
            return record

    def delete_record(self, record:dict):
        ''' Deletes a record'''
        url = f"{self.ws_url}{self.base_key}/{self.table_name}/{record['id']}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = None
        r = requests.delete(url=url, headers=headers, params=params)
        
        if r.status_code != 200:
            message = f"Bad request. Unable to delete record. " + r.text
            if self.log_service:
                self.log_service.update("ERROR", message)
            raise Exception(message)


    def _get_data(self, url, params = None): 
        data = None
        headers = {"Authorization": f"Bearer {self.api_key}"}
        r = requests.get(url=url, headers=headers, params=params) #, verify=False)
        if r.status_code == 404:
            pass #okay return None, id is not found
        elif r.status_code != 200:
            message = f"Bad request. Unable to fetch report data. " + r.text
            if self.log_service:
                self.log_service.update("ERROR", message)
            raise Exception(message)
        else:
            data = r.json()
        return data




