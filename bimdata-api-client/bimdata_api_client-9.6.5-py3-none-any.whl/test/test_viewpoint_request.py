"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bimdata_api_client
from bimdata_api_client.model.clipping_plane_request import ClippingPlaneRequest
from bimdata_api_client.model.components_parent_request import ComponentsParentRequest
from bimdata_api_client.model.line_request import LineRequest
from bimdata_api_client.model.orthogonal_camera_request import OrthogonalCameraRequest
from bimdata_api_client.model.perspective_camera_request import PerspectiveCameraRequest
from bimdata_api_client.model.pin_request import PinRequest
from bimdata_api_client.model.snapshot_request import SnapshotRequest
globals()['ClippingPlaneRequest'] = ClippingPlaneRequest
globals()['ComponentsParentRequest'] = ComponentsParentRequest
globals()['LineRequest'] = LineRequest
globals()['OrthogonalCameraRequest'] = OrthogonalCameraRequest
globals()['PerspectiveCameraRequest'] = PerspectiveCameraRequest
globals()['PinRequest'] = PinRequest
globals()['SnapshotRequest'] = SnapshotRequest
from bimdata_api_client.model.viewpoint_request import ViewpointRequest


class TestViewpointRequest(unittest.TestCase):
    """ViewpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testViewpointRequest(self):
        """Test ViewpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ViewpointRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
