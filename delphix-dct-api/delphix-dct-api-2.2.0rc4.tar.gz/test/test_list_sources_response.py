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
from delphix.api.gateway.model.errors import Errors
from delphix.api.gateway.model.paginated_response_metadata import PaginatedResponseMetadata
from delphix.api.gateway.model.source import Source
globals()['Errors'] = Errors
globals()['PaginatedResponseMetadata'] = PaginatedResponseMetadata
globals()['Source'] = Source
from delphix.api.gateway.model.list_sources_response import ListSourcesResponse


class TestListSourcesResponse(unittest.TestCase):
    """ListSourcesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListSourcesResponse(self):
        """Test ListSourcesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListSourcesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
