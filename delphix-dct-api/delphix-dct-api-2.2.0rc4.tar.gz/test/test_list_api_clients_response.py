"""
    Delphix DCT API

    Delphix DCT API  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import delphix.api.gateway
from delphix.api.gateway.model.model_api_client import ModelApiClient
from delphix.api.gateway.model.paginated_response_metadata import PaginatedResponseMetadata
globals()['ModelApiClient'] = ModelApiClient
globals()['PaginatedResponseMetadata'] = PaginatedResponseMetadata
from delphix.api.gateway.model.list_api_clients_response import ListApiClientsResponse


class TestListApiClientsResponse(unittest.TestCase):
    """ListApiClientsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListApiClientsResponse(self):
        """Test ListApiClientsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListApiClientsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
