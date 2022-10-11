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
from openapi_client.model.banner import Banner
from openapi_client.model.bfd import Bfd
from openapi_client.model.connect_to_ntp_server import ConnectToNtpServer
from openapi_client.model.global_settings_all_of import GlobalSettingsAllOf
from openapi_client.model.ip_sec_security import IpSecSecurity
from openapi_client.model.logging_system_messages import LoggingSystemMessages
from openapi_client.model.login_access_to_router import LoginAccessToRouter
from openapi_client.model.omp import OMP
from openapi_client.model.profile_parcel import ProfileParcel
from openapi_client.model.systems import Systems
from openapi_client.model.variable import Variable
globals()['Banner'] = Banner
globals()['Bfd'] = Bfd
globals()['ConnectToNtpServer'] = ConnectToNtpServer
globals()['GlobalSettingsAllOf'] = GlobalSettingsAllOf
globals()['IpSecSecurity'] = IpSecSecurity
globals()['LoggingSystemMessages'] = LoggingSystemMessages
globals()['LoginAccessToRouter'] = LoginAccessToRouter
globals()['OMP'] = OMP
globals()['ProfileParcel'] = ProfileParcel
globals()['Systems'] = Systems
globals()['Variable'] = Variable
from openapi_client.model.global_settings import GlobalSettings


class TestGlobalSettings(unittest.TestCase):
    """GlobalSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGlobalSettings(self):
        """Test GlobalSettings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GlobalSettings()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
