"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.umbrella_api import UmbrellaApi  # noqa: E501


class TestUmbrellaApi(unittest.TestCase):
    """UmbrellaApi unit test stubs"""

    def setUp(self):
        self.api = UmbrellaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_keys_from_umbrella(self):
        """Test case for get_all_keys_from_umbrella

        """
        pass

    def test_get_management_keys_from_umbrella(self):
        """Test case for get_management_keys_from_umbrella

        """
        pass

    def test_get_network_keys_from_umbrella(self):
        """Test case for get_network_keys_from_umbrella

        """
        pass

    def test_get_reporting_keys_from_umbrella(self):
        """Test case for get_reporting_keys_from_umbrella

        """
        pass


if __name__ == '__main__':
    unittest.main()
