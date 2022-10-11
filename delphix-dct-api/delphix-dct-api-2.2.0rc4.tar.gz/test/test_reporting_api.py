"""
    Delphix DCT API

    Delphix DCT API  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import delphix.api.gateway
from delphix.api.gateway.api.reporting_api import ReportingApi  # noqa: E501


class TestReportingApi(unittest.TestCase):
    """ReportingApi unit test stubs"""

    def setUp(self):
        self.api = ReportingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_reporting_schedule(self):
        """Test case for create_reporting_schedule

        Create a new report schedule.  # noqa: E501
        """
        pass

    def test_delete_reporting_schedule(self):
        """Test case for delete_reporting_schedule

        Delete report schedule by ID.  # noqa: E501
        """
        pass

    def test_get_api_usage_report(self):
        """Test case for get_api_usage_report

        Gets the report of API usage metrics over a given time period.  # noqa: E501
        """
        pass

    def test_get_dsource_usage_report(self):
        """Test case for get_dsource_usage_report

        Gets the usage report for virtualization engine dSources.  # noqa: E501
        """
        pass

    def test_get_product_info(self):
        """Test case for get_product_info

        Returns the DCT Product Information.  # noqa: E501
        """
        pass

    def test_get_reporting_schedule_by_id(self):
        """Test case for get_reporting_schedule_by_id

        Returns a report schedule by ID.  # noqa: E501
        """
        pass

    def test_get_reporting_schedules(self):
        """Test case for get_reporting_schedules

        List all report schedules.  # noqa: E501
        """
        pass

    def test_get_vdb_inventory_report(self):
        """Test case for get_vdb_inventory_report

        Gets the inventory report for virtualization engine VDBs.  # noqa: E501
        """
        pass

    def test_get_virtualization_storage_summary_report(self):
        """Test case for get_virtualization_storage_summary_report

        Gets the storage summary report for virtualization engines.  # noqa: E501
        """
        pass

    def test_search_dsource_usage_report(self):
        """Test case for search_dsource_usage_report

        Search the usage report for virtualization engine dSources.  # noqa: E501
        """
        pass

    def test_search_vdb_inventory_report(self):
        """Test case for search_vdb_inventory_report

        Search the inventory report for virtualization engine VDBs.  # noqa: E501
        """
        pass

    def test_search_virtualization_storage_summary_report(self):
        """Test case for search_virtualization_storage_summary_report

        Search the storage summary report for virtualization engines.  # noqa: E501
        """
        pass

    def test_update_reporting_schedule(self):
        """Test case for update_reporting_schedule

        Update a reporting schedule by ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
