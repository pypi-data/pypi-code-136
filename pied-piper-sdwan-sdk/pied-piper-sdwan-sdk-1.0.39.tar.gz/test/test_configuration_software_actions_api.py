"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_software_actions_api import ConfigurationSoftwareActionsApi  # noqa: E501


class TestConfigurationSoftwareActionsApi(unittest.TestCase):
    """ConfigurationSoftwareActionsApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationSoftwareActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_remote_server(self):
        """Test case for add_remote_server

        """
        pass

    def test_create_image_url(self):
        """Test case for create_image_url

        """
        pass

    def test_delete_image_url(self):
        """Test case for delete_image_url

        """
        pass

    def test_delete_remote_server(self):
        """Test case for delete_remote_server

        """
        pass

    def test_find_software_images(self):
        """Test case for find_software_images

        """
        pass

    def test_find_software_images_with_filters(self):
        """Test case for find_software_images_with_filters

        """
        pass

    def test_find_software_version(self):
        """Test case for find_software_version

        """
        pass

    def test_find_v_edge_software_version(self):
        """Test case for find_v_edge_software_version

        """
        pass

    def test_find_ztp_software_version(self):
        """Test case for find_ztp_software_version

        """
        pass

    def test_get_image_properties(self):
        """Test case for get_image_properties

        """
        pass

    def test_get_pnf_properties(self):
        """Test case for get_pnf_properties

        """
        pass

    def test_get_remote_server_by_id(self):
        """Test case for get_remote_server_by_id

        """
        pass

    def test_get_remote_server_list(self):
        """Test case for get_remote_server_list

        """
        pass

    def test_get_vnf_properties(self):
        """Test case for get_vnf_properties

        """
        pass

    def test_update_image_url(self):
        """Test case for update_image_url

        """
        pass

    def test_update_remote_server(self):
        """Test case for update_remote_server

        """
        pass


if __name__ == '__main__':
    unittest.main()
