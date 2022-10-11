"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.colocation_service_group_api import ColocationServiceGroupApi  # noqa: E501


class TestColocationServiceGroupApi(unittest.TestCase):
    """ColocationServiceGroupApi unit test stubs"""

    def setUp(self):
        self.api = ColocationServiceGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service_group_cluster(self):
        """Test case for create_service_group_cluster

        """
        pass

    def test_delete_service_group_cluster(self):
        """Test case for delete_service_group_cluster

        """
        pass

    def test_get_available_chains(self):
        """Test case for get_available_chains

        """
        pass

    def test_get_default_chain(self):
        """Test case for get_default_chain

        """
        pass

    def test_get_service_chain(self):
        """Test case for get_service_chain

        """
        pass

    def test_get_service_group_in_cluster(self):
        """Test case for get_service_group_in_cluster

        """
        pass

    def test_update_service_group_cluster(self):
        """Test case for update_service_group_cluster

        """
        pass


if __name__ == '__main__':
    unittest.main()
