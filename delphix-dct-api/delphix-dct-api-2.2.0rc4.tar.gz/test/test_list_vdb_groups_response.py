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
from delphix.api.gateway.model.paginated_response_metadata import PaginatedResponseMetadata
from delphix.api.gateway.model.vdb_group import VDBGroup
globals()['PaginatedResponseMetadata'] = PaginatedResponseMetadata
globals()['VDBGroup'] = VDBGroup
from delphix.api.gateway.model.list_vdb_groups_response import ListVDBGroupsResponse


class TestListVDBGroupsResponse(unittest.TestCase):
    """ListVDBGroupsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListVDBGroupsResponse(self):
        """Test ListVDBGroupsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListVDBGroupsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
