"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.ethernet_all_of import EthernetAllOf
from openapi_client.model.ethernet_interface import EthernetInterface
from openapi_client.model.profile_parcel import ProfileParcel
from openapi_client.model.variable import Variable
globals()['EthernetAllOf'] = EthernetAllOf
globals()['EthernetInterface'] = EthernetInterface
globals()['ProfileParcel'] = ProfileParcel
globals()['Variable'] = Variable
from openapi_client.model.ethernet import Ethernet


class TestEthernet(unittest.TestCase):
    """Ethernet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEthernet(self):
        """Test Ethernet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Ethernet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
