"""
    Cisco-Reservable-SD-WAN

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.sdwan_fabric_devices_api import SDWANFabricDevicesApi  # noqa: E501


class TestSDWANFabricDevicesApi(unittest.TestCase):
    """SDWANFabricDevicesApi unit test stubs"""

    def setUp(self):
        self.api = SDWANFabricDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dataservice_device_counters_get(self):
        """Test case for dataservice_device_counters_get

        Device Counters  # noqa: E501
        """
        pass

    def test_dataservice_device_get(self):
        """Test case for dataservice_device_get

        Fabric Devices  # noqa: E501
        """
        pass

    def test_dataservice_device_monitor_get(self):
        """Test case for dataservice_device_monitor_get

        Devices Status  # noqa: E501
        """
        pass

    def test_dataservice_statistics_interface_get(self):
        """Test case for dataservice_statistics_interface_get

        Interface statistics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
