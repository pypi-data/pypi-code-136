import base64
import asyncio
import time
import aiohttp
from typing import List
from salure_helpers import SalureConnect


class ProfitExtractAsync:
    def __init__(self, salureconnect_connection: SalureConnect, token_reference: str, debug=False):
        self.salureconnect_connection = salureconnect_connection
        if self.salureconnect_connection.test_environment:
            self.base_url = 'resttest.afas.online'
        else:
            self.base_url = 'rest.afas.online'
        credentials = self.salureconnect_connection.get_system_credential(system='profit', reference=token_reference)
        self.environment = credentials['environment']
        base64token = base64.b64encode(credentials['token'].encode('utf-8')).decode()
        self.headers = {'Authorization': 'AfasToken ' + base64token}
        self.got_all_results = False
        self.debug = debug

    async def get_data(self, connectors: List = None, parameters: dict = {}, batch_size: int = 8, take: int = 40000) -> dict:
        """
        This (asynchronous) function functions as a wrapper that can carry out multiple single get requests to be able
        to get all data from profit in an asynchronous and efficient way. Only use this function in async code, otherwise use the profit class to call this from a sync function.
        :param connectors: Names of the connectors to be extracted. If not provided, keys of parameters dict will be used
        :param parameters: multilevel dict of filters per connector. Key must always be the connector, then dict like {connector: {"filterfieldids": fields, "filtervalues": values, "operatortypes": operators}
        :return: data in json format
        """
        url = f'https://{self.environment}.{self.base_url}/profitrestservices/connectors/'
        batch_number = 0

        total_response = {}
        self.got_all_results = False
        while not self.got_all_results:
            async with aiohttp.ClientSession(headers=self.headers, timeout=aiohttp.ClientTimeout()) as session:
                requests = [self.get_request(url=url,
                                             connector=connector,
                                             params={**(parameters[connector] if connector in parameters.keys() else {}), **{
                                                 "skip": take * (i + batch_number * batch_size),
                                                 "take": take}},
                                             session=session,
                                             take=take) for i in range(batch_size) for connector in connectors]
                response = await asyncio.gather(*requests, return_exceptions=False)

                # Flatten response (multiple dicts with the same key (connectorname) and different values are returned)
                for item in response:
                    for key, value in item.items():
                        if key in total_response.keys():
                            total_response[key].extend(value)
                        else:
                            total_response[key] = value

                batch_number += 1

        return total_response

    async def get_request(self, url: str, connector: str, params: dict, session: aiohttp.ClientSession, take: int):
        """
        This function carries out a single get request given the inputs. It is used as input for the abovementioned wrapper,
        get_data_content. Note that this function cannot be called it itself, but has to be started via get_data_content.

        :param url: profit url to retrieve the data.
        :param params: body of the request.
        :param session: type of the request.
        :return: data in json format
        """
        if self.debug:
            print(f"started request for {connector} at: {time.time()}")
        async with session.get(url=f"{url}{connector}", params=params) as resp:
            if resp.status >= 400:
                raise ConnectionError(f"Got error: {resp.status, await resp.text()} while retrieving data from connector {connector}")
            response = await resp.json()
            response = response['rows']
            if len(response) < take:
                if self.debug:
                    print(f"request with params: {params} was the last request with {len(response)} rows")
                self.got_all_results = True
            else:
                if self.debug:
                    print(f"request with params: {params} has {len(response)} rows")

            return {connector: response}

    async def get_meta_data(self, connector: str = None):
        """
        This function makes sure that you can create a list of connector names without having to call another class.
        :return: returns a list of all connectors in the environment.
        """

        url = f"https://{self.environment}.{self.base_url}/profitrestservices/metainfo{f'/get/{connector}' if connector is not None else ''}"

        async with aiohttp.ClientSession(headers=self.headers, timeout=aiohttp.ClientTimeout(), raise_for_status=True) as session:
            async with session.get(url=f"{url}") as resp:
                if resp.status >= 400:
                    raise ConnectionError(f"Got error: {resp.status, await resp.text()} while retrieving data from connector {connector}")
                response = await resp.json()
                response = response[f"{'getConnectors' if connector is None else 'fields'}"]

                return response