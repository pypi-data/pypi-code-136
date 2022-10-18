import hashlib
import json

import requests
from salure_helpers import SalureConnect


class AllSolutions:
    def __init__(self, salureconnect_connection: SalureConnect, token_reference: str = None):
        self.salureconnect_connection = salureconnect_connection
        self.token_reference = token_reference
        self.system = 'all-solutions'
        self.headers = {'Content-Type': 'application/json'}
        self.token = None
        self.refresh_token = None
        self.debug = False

    def _get_refreshtoken(self):
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        signature = hashlib.sha1(f"{credentials['username']}{credentials['client_id']}{credentials['secret_id']}".encode()).hexdigest()
        response = requests.post(url=f"{credentials['url']}login",
                                 headers=self.headers,
                                 data=json.dumps({
                                     "Username": credentials['username'],
                                     "Signature": signature,
                                     "Password": credentials['password'],
                                     "ClientId": credentials['client_id']
                                 }))
        if self.debug:
            print(response.content)
        response.raise_for_status()
        self.token = response.json()['Token']
        self.refresh_token = response.json()['RefreshToken']

    def _get_token(self):
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        signature = hashlib.sha1(f"{self.refresh_token}{credentials['secret_id']}".encode()).hexdigest()
        response = requests.post(url=f"{credentials['url']}refreshtoken",
                                 headers=self.headers,
                                 data=json.dumps({
                                     "RefreshToken": self.refresh_token,
                                     "Signature": signature
                                 }))
        if self.debug:
            print(response.content)
        response.raise_for_status()
        self.token = response.json()['Token']
        self.refresh_token = response.json()['RefreshToken']

        return credentials

    def _get_authentication(self):
        if self.token is None:
            self._get_refreshtoken()
        else:
            self._get_token()

    def get_employees(self, filter: str = None):
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        self._get_authentication()
        headers = {**self.headers, **{'Authorization': f'{self.token}'}}
        total_response = []
        more_results = True
        params = {"pageSize": 500}
        params.update({"$filter-freeform": filter}) if filter else None
        while more_results:
            response = requests.get(url=f"{credentials['url']}mperso",
                                    headers=headers,
                                    params=params)
            if self.debug:
                print(response.content)
            response.raise_for_status()
            more_results = response.json()['Paging']['More']
            total_response += response.json()['Data']

        return total_response

    def get_persons(self, filter: str = None):
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        self._get_authentication()
        headers = {**self.headers, **{'Authorization': f'{self.token}'}}
        total_response = []
        more_results = True
        params = {"pageSize": 500}
        params.update({"$filter-freeform": filter}) if filter else None
        while more_results:
            response = requests.get(url=f"{credentials['url']}mrlprs",
                                    headers=headers,
                                    params=params)
            if self.debug:
                print(response.content)
            response.raise_for_status()
            more_results = response.json()['Paging']['More']
            total_response += response.json()['Data']

        return total_response

    def create_employee(self, data: dict) -> json:
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        self._get_authentication()
        headers = {**self.headers, **{'Authorization': f'{self.token}'}}
        payload = {
            "Data": [
                {
                    "ab02.persnr": data['employee_code'],
                    "ab02.geb-dat": data['birth_date'],
                    "ab02.mail-nr": data['employee_id_afas'],
                    "h-default7": True,
                    "h-default6": True,  # Find corresponding employee details
                    "h-default5": True,  # Find name automatically
                    "h-default1": True,  # check NAW automatically from person
                    "h-corr-adres": True,  # save address as correspondence address
                    # "h-aanw": "32,00", # hours per week
                    "ab02.indat": data['date_in_service'],
                    "ab02.uitdat": data['termination_date'],
                    "ab02.email-int": data['email_work'],
                    "ab02.email": data['email_private'],
                    "ab02.telefoon-int": data['phone_work'],
                    "ab02.mobiel-int": data['mobile_phone_work'],
                    "ab02.ba-kd": data['costcenter'],
                    "ab02.funktie": data['function'],
                    "ab02.contr-srt-kd": "1",
                    "ab02.srt-mdw": "ms01",
                    "ab02.notitie-edit": "Test API Afas"
                }
            ]
        }
        if self.debug:
            print(json.dumps(payload))
        response = requests.post(url=f"{credentials['url']}mperso",
                                 headers=headers,
                                 data=json.dumps(payload))
        if self.debug:
            print(response.content)
        response.raise_for_status()

        return response.json()

    def update_employee(self, data: dict, employee_id: str) -> json:
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        self._get_authentication()
        headers = {**self.headers, **{'Authorization': f'{self.token}'}}
        payload = {
            "Data": [
                {
                    "h-default7": True,
                    "h-default6": True,  # Find corresponding employee details
                    "h-default5": True,  # Find name automatically
                    "h-default1": True,  # check NAW automatically from person
                    "h-corr-adres": True,  # save address as correspondence address
                    # "h-aanw": "32,00", # hours per week
                    "ab02.contr-srt-kd": "1",
                    "ab02.srt-mdw": "ms01",
                    "ab02.notitie-edit": "Test API Afas"
                }
            ]
        }
        payload['Data'][0].update({"ab02.persnr": data['employee_code']}) if 'employee_code' in data else None
        payload['Data'][0].update({"ab02.geb-dat": data['birth_date']}) if 'birth_date' in data else None
        payload['Data'][0].update({"ab02.mail-nr": data['person_id']}) if 'person_id' in data else None
        payload['Data'][0].update({"ab02.indat": data['date_in_service']}) if 'date_in_service' in data else None
        payload['Data'][0].update({"ab02.uitdat": data['termination_date']}) if 'termination_date' in data else None
        payload['Data'][0].update({"ab02.email-int": data['email_work']}) if 'email_work' in data else None
        payload['Data'][0].update({"ab02.email": data['email_private']}) if 'email_private' in data else None
        payload['Data'][0].update({"ab02.telefoon-int": data['phone_work']}) if 'phone_work' in data else None
        payload['Data'][0].update({"ab02.mobiel-int": data['mobile_phone_work']}) if 'mobile_phone_work' in data else None
        payload['Data'][0].update({"ab02.ba-kd": data['costcenter']}) if 'costcenter' in data else None
        payload['Data'][0].update({"ab02.funktie": data['function']}) if 'function' in data else None
        if self.debug:
            print(json.dumps(payload))
        response = requests.put(url=f"{credentials['url']}mperso/{employee_id}",
                                headers=headers,
                                data=json.dumps(payload))
        if self.debug:
            print(response.content)
        response.raise_for_status()

        return response.json()

    def create_person(self, data: dict) -> json:
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        self._get_authentication()
        headers = {**self.headers, **{'Authorization': f'{self.token}'}}
        payload = {
            "Data": [
                {
                    "ma01.zoeknaam": data['search_name'],
                    'h-mail-nr': data['employee_id_afas'],
                    "ma01.telefoon": data['phone_work'],
                    "ma01.persnr": data['employee_code'],
                    "ma01.geb-dat": data['birth_date'],
                    "ma01.voorl": data['initials'],
                    "ma01.voornaam": data['firstname'],
                    "ma01.voor[1]": data['prefix'],
                    "ma01.b-wpl": data['city'],
                    "ma01.persoon[1]": data['lastname'],
                    "ma01.b-adres": data['street'],
                    "ma01.b-num": data['housenumber'],
                    "ma01.b-appendix": data['housenumber_addition'],
                    "ma01.b-pttkd": data['postal_code'],
                    "ma01.mobiel": data['mobile_phone_work'],
                    "ma01.email": data['email_work'],
                    # "h-default7": True,
                    # "h-aanw": "32,00", # hours per week
                    "h-default6": True,
                    "h-default8": True,
                    "ma01.rel-grp": 'Medr',
                    "ma01.notitie-edit": "Test API Afas",
                    "h-chk-ma01": True  # Check if person already exists
                }
            ]
        }
        if self.debug:
            print(json.dumps(payload))
        response = requests.post(url=f"{credentials['url']}mrlprs",
                                 headers=headers,
                                 data=json.dumps(payload))
        if self.debug:
            print(response.content)
        response.raise_for_status()

        return response.json()

    def update_person(self, data: dict, employee_id: str) -> json:
        credentials = self.salureconnect_connection.get_system_credential(system=self.system, reference=self.token_reference)[0]
        self._get_authentication()
        headers = {**self.headers, **{'Authorization': f'{self.token}'}}
        payload = {
            "Data": [
                {
                    # "h-default7": True,
                    # "h-aanw": "32,00", # hours per week
                    "h-default6": True,
                    "h-default8": True,
                    "ma01.rel-grp": 'Medr',
                    "ma01.notitie-edit": "Test API Afas",
                    "h-chk-ma01": True  # Check if person already exists
                }
            ]
        }
        payload['Data'][0].update({"ma01.zoeknaam": data['search_name']}) if 'search_name' in data else None
        payload['Data'][0].update({"ma01.mail-nr": data['employee_id_afas']}) if 'employee_id_afas' in data else None
        payload['Data'][0].update({"ma01.telefoon": data['phone_work']}) if 'phone_work' in data else None
        payload['Data'][0].update({"ma01.persnr": data['employee_code']}) if 'employee_code' in data else None
        payload['Data'][0].update({"ma01.geb-dat": data['birth_date']}) if 'birth_date' in data else None
        payload['Data'][0].update({"ma01.voorl": data['initials']}) if 'initials' in data else None
        payload['Data'][0].update({"ma01.voornaam": data['firstname']}) if 'firstname' in data else None
        payload['Data'][0].update({"ma01.voor[1]": data['prefix']}) if 'prefix' in data else None
        payload['Data'][0].update({"ma01.b-wpl": data['city']}) if 'city' in data else None
        payload['Data'][0].update({"ma01.b-persoon[1]": data['lastname']}) if 'lastname' in data else None
        payload['Data'][0].update({"ma01.b-adres": data['street']}) if 'street' in data else None
        payload['Data'][0].update({"ma01.b-num": data['housenumber']}) if 'housenumber' in data else None
        payload['Data'][0].update({"ma01.b-appendix": data['housenumber_addition']}) if 'housenumber_addition' in data else None
        payload['Data'][0].update({"ma01.b-pttkd": data['postal_code']}) if 'postal_code' in data else None
        payload['Data'][0].update({"ma01.mobiel": data['mobile_phone_work']}) if 'mobile_phone_work' in data else None
        payload['Data'][0].update({"ma01.email": data['email_work']}) if 'email_work' in data else None
        if self.debug:
            print(json.dumps(payload))
        response = requests.put(url=f"{credentials['url']}mrlprs/{employee_id}",
                                headers=headers,
                                data=json.dumps(payload))
        if self.debug:
            print(response.content)
        response.raise_for_status()

        return response.json()
