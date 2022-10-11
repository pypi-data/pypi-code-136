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
from openapi_client.model.cellular_all_of import CellularAllOf
from openapi_client.model.profile_parcel import ProfileParcel
from openapi_client.model.sim_slot_config import SimSlotConfig
from openapi_client.model.variable import Variable
globals()['CellularAllOf'] = CellularAllOf
globals()['ProfileParcel'] = ProfileParcel
globals()['SimSlotConfig'] = SimSlotConfig
globals()['Variable'] = Variable
from openapi_client.model.cellular import Cellular


class TestCellular(unittest.TestCase):
    """Cellular unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCellular(self):
        """Test Cellular"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Cellular()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
