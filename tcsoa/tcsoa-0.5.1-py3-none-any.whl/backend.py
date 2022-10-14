import dataclasses
import json
import logging
import re
import sys
from enum import Enum
from typing import List, Dict, Iterable

import requests

from datetime import datetime

from tcsoa.config import TcSoaConfig
from tcsoa.gen.Server import ServiceData
from tcsoa.utils import TcBoClass


class RestBackend:
    def __init__(self, host: str):
        """
        Initializes the REST Backend. Should be useable for all Teamcenter Backends which have AWC installed.

        @param host: The address to your web server - for example: http://webserver:7001/tc
        """
        self.host = host
        self.base_url = f'{self.host}/RestServices'
        self.policy = {
            "useRefCount": False,
            "types": list()
        }
        self.state = {
            "stateless": True,
            "unloadObjects": True,
            "enableServerStateHeaders": True,
            "formatProperties": True,
            "clientID": "TcSoaClient"
        }
        self.session = requests.session()
        self.session.trust_env = False
        self.session.proxies = {
            "http": None,
            "https": None,
        }

    def set_object_load_policy(self, bo_name, properties: List[str]):
        types_list = self.policy['types']
        matching_type = list(t for t in types_list if t['name'] == bo_name)
        if matching_type:
            object_policy = matching_type[0]
        else:
            object_policy = {
                'name': bo_name
            }
            types_list.append(object_policy)
        object_policy['properties'] = [{'name': p} for p in properties]

    def input_obj_to_json(self, input_obj):
        if input_obj is None:
            return ''
        if type(input_obj) in (str, int, float, bool):
            return input_obj
        if isinstance(input_obj, TcBoClass):
            return {k: self.input_obj_to_json(v) for k, v in input_obj.__dict__.items() if k != 'props'}
        if dataclasses.is_dataclass(input_obj):
            return {k[:-1] if k.endswith('_') else k: self.input_obj_to_json(v) for k, v in input_obj.__dict__.items()}
        if isinstance(input_obj, datetime):
            return input_obj.strftime(TcSoaConfig.date_format)
        if isinstance(input_obj, Enum):
            return input_obj.value
        if isinstance(input_obj, dict):
            return {k: self.input_obj_to_json(v) for k, v in input_obj.items()}
        if type(input_obj) in (list, set, tuple) or isinstance(input_obj, Iterable):
            return [self.input_obj_to_json(o) for o in input_obj]
        raise NotImplementedError()

    def qname2type(self, qname):
        # example: http://teamcenter.com/Schemas/Core/2011-06/Session.LoginResponse
        qname_match = re.search(r'Schemas\/[a-zA-Z0-9]*\/[0-9]{4}-[0-9]{2}\/[a-zA-Z0-9]*$', qname)
        assert qname_match
        _, library, date, service, typename = qname_match.group().replace('.', '/').split('/')
        # https://stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string
        # todo: add cache for qname types

    def response_to_output_obj(self, response_cls, response):
        try:
            response_data: Dict[str: any] = response.json()
            qname = response_data.pop('.QName')
            # todo: some kind of check...
            # todo: also - what to do when response_cls in None??
            if response_cls:
                response_data = self.dataclass_from_dict(response_cls, response_data)
            return response_data
        except ValueError:
            # note to self: when XML is returned, you dont have a valid cookie
            return response.content  # todo: handle this better

    @staticmethod
    def eval_str_type(cls, field):
        """ Black Magic - Evaluates the type annotation in context of the class """
        return eval(field, globals(), sys.modules[cls.__module__].__dict__)

    @staticmethod
    def dataclass_from_dict(cls, from_dict):
        try:
            fieldtypes = cls.__annotations__
        except AttributeError:
            if dataclasses.is_dataclass(cls):
                fieldtypes = dict()     # __annotations__ is only set to data classes with attributes
            elif isinstance(from_dict, (tuple, list)):
                return [RestBackend.dataclass_from_dict(cls.__args__[0], f) for f in from_dict]
            elif isinstance(from_dict, dict):
                return {
                    RestBackend.dataclass_from_dict(cls.__args__[0], k):
                        RestBackend.dataclass_from_dict(cls.__args__[1], v)
                    for k, v in from_dict.items()
                }
            else:
                # logging.warning(f'Warning! Expected attribute class {str(cls)} but received {from_dict} !')
                return from_dict

        instance = cls()
        for f in from_dict:
            dest_f = f
            if f == 'ServiceData' and 'serviceData' in fieldtypes:
                dest_f = 'serviceData'

            if dest_f in fieldtypes:
                field = fieldtypes[dest_f]
            else:
                logging.debug(f'Warning! unregistered attribute "{f}" is tried to be set on class "{cls.__name__}"!')
                setattr(instance, dest_f, from_dict[f])
                continue

            if isinstance(field, str):  # black magic incoming
                field = RestBackend.eval_str_type(cls, field)
            setattr(instance, dest_f, RestBackend.dataclass_from_dict(field, from_dict[f]))
        if TcSoaConfig.global_obj_cache_enabled:
            if isinstance(instance, ServiceData):
                TcSoaConfig.internal_handle_sd(instance)
        return instance

    def execute(self, service_id, method_name, input_obj, response_cls):
        json_body = dict(
            header=dict(
                state=self.state,
                policy=self.policy,
            ),
            body=self.input_obj_to_json(input_obj)
        )
        url = f'{self.base_url}/{service_id}/{method_name}'
        data = json.dumps(json_body, ensure_ascii=False).encode('utf8')
        response = self.session.post(url, data=data, headers={
            'Operation-Name': method_name,
            'App-Xml': 'application/json',
            'Content-Type': 'application/json',
        })
        response.encoding = "utf-8"
        response_obj = self.response_to_output_obj(response_cls, response)
        return response_obj
