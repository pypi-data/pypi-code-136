from copy import deepcopy
from typing import Union, Tuple, Dict, List
from pydigitalenergy.models import Result
from pydigitalenergy.adapter import RestAdapter


class BaseGroup:
    def __init__(self, adapter: RestAdapter):
        """
        Base class for all Digital Energy API Groups

        :param adapter: 
            Low-lever adapter for Digital Energy API
        """
        self._adapter = adapter

    def _get_data(self, endpoint, ep_params = None, method='POST') -> Result:
        """
        Get raw data using REST adapter methods post or get

        :param endpoint: 
            URL Endpoint as a string
        :param ep_params: (Optional)
            Dictionary of Endpoint parameters
        :param method: 
            HTTP method in this case POST or GET
        """
        if method.upper() == 'POST':
            return self._adapter.post(endpoint, ep_params)
        elif method.upper() == 'GET':
            return self._adapter.get(endpoint, ep_params)

    def _remove_fields(self, data: Dict, fields: Union[List, Tuple]):
        """ 
        Remove redundant fields from recieved data

        :param data:
            Dictionary with data recieved via API
        :param fields:
            List or tuple with fields which should be removed from data
        """
        for key in fields:
            data.pop(key, None)

    def _rename_fields(self, data: Dict, names: Dict):
        """ 
        Remove redundant fields from recieved data

        :param data:
            Dictionary with data recieved via API
        :param names:
            Dictionary with the followind structure {'old_name': 'new_name'}
        """
        for old_name, new_name in names.items():
            if old_name in data:
                data[new_name] = data.pop(old_name)

    def _add_fields_prefix(self, data: Dict, prefix: str):
        """ 
        Add prefix to all recieved data fields 

        :param data:
            Dictionary with data recieved via API
        :param prefix:
            Prefix which should be added before every field name
        """
        source_data = deepcopy(data)
        for key, val in source_data.items():
            data[prefix + key[0].upper() + key[1:]] = data.pop(key)
