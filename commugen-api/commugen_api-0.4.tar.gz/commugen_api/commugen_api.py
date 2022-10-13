import base64

import requests

from commugen_api.response_objects import CommugenModel, CommugenDomains, CommugenTables, CommugenSingleRecord, \
    CommugenOptions

MAX_COUNT = 100


class CommugenException(Exception):

    def __init__(self, code=None, id=None, description=None, **kwargs):
        self.code = code
        self.id = id
        self.description = description
        self.kwargs = ', '.join(f'{k}: {v}' for k, v in kwargs.items())

    def __str__(self):
        return 'http status: {0}, id: {1} - {2}, {3}'.format(
            self.code, self.id, self.description, self.kwargs)


class CommugenAPI:
    """
        Example usage::
            from commugen_api import CommugenAPI
            c = CommugenAPI(user=USER, password=PASSWORD, host=HOST, port=8080)
            model = c.get_model(model=model_name, domain=domain_name)
            print(model)
    """

    def __init__(self, user, password, host, port, **kwargs):
        """
        Creates a Commugen API client.
        :param str user: commugen API username
        :param str password:
        :param str host: commugen server host name
        :param int port: the API port
        :param bool verify: default True, If False Ignores ssl warning (optional)
        """
        self.prefix = f'https://{host}:{port}/v0'
        self.headers = self._authentication_header(user, password)
        self._session = requests.api
        self.verify = kwargs.pop('verify', True)

    def _authentication_header(self, user, password):
        """
        :param str user:
        :param str password:
        :return dict: authentication header
        """

        message = f'{user}:{password}'
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return {'Authorization': f'Basic {base64_message}'}

    def _send_request(self, method, url, params=None, json=None):
        """
        handles all requests
        :param str method: http method (GET, PUT and so on...)
        :param str url: api endpoint utilized in request
        :param dict params: http query params
        :param dict json: request payload
        :return dict: raw API answer
        """
        try:
            response = self._session.request(method=method,
                                             url=url,
                                             headers=self.headers,
                                             params=params,
                                             json=json,
                                             verify=self.verify
                                             )
            response.raise_for_status()
            results = response.json()
        except requests.exceptions.HTTPError as http_error:
            response = http_error.response
            json_response = response.json()
            error = json_response.get("error", {})
            raise CommugenException(
                **error
            )
        return results

    def get_model(self, domain, model, published=True, f='', **kwargs):
        """
        by default gets 20 first rows of requested table. you can get up to 100 rows by using count parameter
        and choose which rows to see by using filters, f, and offset param. example use:

        c = CommugenAPI(user=USER, password=PASSWORD, host=HOST, port=8080)
        model = c.get_model(model=model_name, domain=domain_name, offset=42, count=50)
        print(model)

        with filters:

        c = CommugenAPI(user=USER, password=PASSWORD, host=HOST, port=8080)
        model = c.get_model(model=model_name, domain=domain_name, f='apiNumber.gte.10 apiNumber.lte.20')
        print(model)


        :param domain:
        :param model:
        :param bool published: show only entries with status published
        :param f: filter strings separated by spaces. format: 'column_name.operand.value' (see api guide doc).
                    there is logical 'and' between filters always
        :param kwargs: see options in api guide doc
        :rtype CommugenModel:
        """
        if published:
            f = ' '.join([f, '_publicState.eq.0'])

        if f:
            f = f.split()
            kwargs = list(kwargs.items()) + [('f', filter) for filter in f]

        url = '/'.join([self.prefix, domain, model])
        response = self._send_request(method='GET', url=url, params=kwargs)
        return CommugenModel(response)

    def get_entry(self, domain, model, id):
        """
        get single row according to id
        :param domain:
        :param model:
        :param int id:
        :rtype: CommugenSingleRecord
        """
        url = '/'.join([self.prefix, domain, model, str(id)])
        response = self._send_request(method='GET', url=url)
        return CommugenSingleRecord(response)

    def add_entry(self, domain, model, payload):
        """
        add row of data to model
        :param domain:
        :param model:
        :param dict payload: example: {
            'text_column': 'text'
            'number_column': 7
            'options_column': {option:True}
            'alt_options_column': ['another_option']
        }
        :rtype: CommugenSingleRecord
        """
        url = '/'.join([self.prefix, domain, model])
        response = self._send_request(method='POST', url=url, json=payload)
        return CommugenSingleRecord(response)

    def update_entry(self, domain, model, id, payload):
        """
        update an existing row
        :param domain:
        :param model:
        :param int id: the row id
        :param payload: see add entry
        :rtype: CommugenSingleRecord
        """
        url = '/'.join([self.prefix, domain, model, str(id)])
        response = self._send_request(method='PUT', url=url, json=payload)
        return CommugenSingleRecord(response)

    def get_full_table(self, domain, model, **kwargs):
        """
        returns all rows in requested table. see get_model for filter use.
        the use of count and offset params is prohibited
        :param domain:
        :param model:
        :param kwargs:
        :rtype CommugenModel:
        """
        table = self.get_model(domain=domain, model=model, count=MAX_COUNT, **kwargs)
        offset = MAX_COUNT
        while table.records.hasMore:
            extention = self.get_model(domain=domain, model=model, count=MAX_COUNT, offset=offset, **kwargs)
            table.records.list.extend(extention.records.list)
            table.records.hasMore = extention.records.hasMore
            offset += MAX_COUNT
        return table

    def get_domains(self):
        """
        gets all allowed domains for user.
        :return:
        """
        response = self._send_request('GET', self.prefix)
        return CommugenDomains(response)

    def get_models(self, domain):
        """
        gets all allowed models in specific domain for user
        :param domain:
        :return:
        """
        url = '/'.join([self.prefix, domain])
        response = self._send_request('GET', url)
        return CommugenTables(response)

    def get_options(self, domain, model, id=''):
        """
        gets structure of requested model or raw and allowed api verbs
        :param domain:
        :param model:
        :param id:
        :rtype: CommugenOptions
        """
        url = '/'.join([self.prefix, domain, model, str(id)])
        response = self._send_request('OPTIONS', url)
        return CommugenOptions(response)
