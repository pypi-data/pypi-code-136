"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_network_design_api import ConfigurationNetworkDesignApi  # noqa: E501


class TestConfigurationNetworkDesignApi(unittest.TestCase):
    """ConfigurationNetworkDesignApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationNetworkDesignApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acquire_attach_lock(self):
        """Test case for acquire_attach_lock

        """
        pass

    def test_acquire_edit_lock(self):
        """Test case for acquire_edit_lock

        """
        pass

    def test_create_network_design(self):
        """Test case for create_network_design

        """
        pass

    def test_edit_network_design(self):
        """Test case for edit_network_design

        """
        pass

    def test_get_device_profile_config_status(self):
        """Test case for get_device_profile_config_status

        """
        pass

    def test_get_device_profile_config_status_by_profile_id(self):
        """Test case for get_device_profile_config_status_by_profile_id

        """
        pass

    def test_get_device_profile_task_count(self):
        """Test case for get_device_profile_task_count

        """
        pass

    def test_get_device_profile_task_status(self):
        """Test case for get_device_profile_task_status

        """
        pass

    def test_get_device_profile_task_status_by_profile_id(self):
        """Test case for get_device_profile_task_status_by_profile_id

        """
        pass

    def test_get_global_parameters(self):
        """Test case for get_global_parameters

        """
        pass

    def test_get_network_design(self):
        """Test case for get_network_design

        """
        pass

    def test_get_service_profile_config(self):
        """Test case for get_service_profile_config

        """
        pass

    def test_push_device_profile_template(self):
        """Test case for push_device_profile_template

        """
        pass

    def test_push_network_design(self):
        """Test case for push_network_design

        """
        pass

    def test_run_my_test(self):
        """Test case for run_my_test

        """
        pass


if __name__ == '__main__':
    unittest.main()
