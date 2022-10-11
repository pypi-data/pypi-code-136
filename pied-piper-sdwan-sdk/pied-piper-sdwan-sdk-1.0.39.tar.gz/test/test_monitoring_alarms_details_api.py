"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.monitoring_alarms_details_api import MonitoringAlarmsDetailsApi  # noqa: E501


class TestMonitoringAlarmsDetailsApi(unittest.TestCase):
    """MonitoringAlarmsDetailsApi unit test stubs"""

    def setUp(self):
        self.api = MonitoringAlarmsDetailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clear_stale_alarm(self):
        """Test case for clear_stale_alarm

        """
        pass

    def test_correl_anti_entropy(self):
        """Test case for correl_anti_entropy

        """
        pass

    def test_create_alarm_query_config(self):
        """Test case for create_alarm_query_config

        """
        pass

    def test_create_notification_rule(self):
        """Test case for create_notification_rule

        """
        pass

    def test_delete_notification_rule(self):
        """Test case for delete_notification_rule

        """
        pass

    def test_disable_enable_alarm(self):
        """Test case for disable_enable_alarm

        """
        pass

    def test_dump_correlation_engine_data(self):
        """Test case for dump_correlation_engine_data

        """
        pass

    def test_enable_disable_link_state_alarm(self):
        """Test case for enable_disable_link_state_alarm

        """
        pass

    def test_get_alarm_aggregation_data(self):
        """Test case for get_alarm_aggregation_data

        """
        pass

    def test_get_alarm_details(self):
        """Test case for get_alarm_details

        """
        pass

    def test_get_alarm_severity_custom_histogram(self):
        """Test case for get_alarm_severity_custom_histogram

        """
        pass

    def test_get_alarm_severity_mappings(self):
        """Test case for get_alarm_severity_mappings

        """
        pass

    def test_get_alarm_types_as_key_value(self):
        """Test case for get_alarm_types_as_key_value

        """
        pass

    def test_get_alarms(self):
        """Test case for get_alarms

        """
        pass

    def test_get_alarms_by_severity(self):
        """Test case for get_alarms_by_severity

        """
        pass

    def test_get_count1(self):
        """Test case for get_count1

        """
        pass

    def test_get_count_post1(self):
        """Test case for get_count_post1

        """
        pass

    def test_get_device_topic(self):
        """Test case for get_device_topic

        """
        pass

    def test_get_link_state_alarm_config(self):
        """Test case for get_link_state_alarm_config

        """
        pass

    def test_get_master_manager_state(self):
        """Test case for get_master_manager_state

        """
        pass

    def test_get_non_viewed_active_alarms_count(self):
        """Test case for get_non_viewed_active_alarms_count

        """
        pass

    def test_get_non_viewed_alarms(self):
        """Test case for get_non_viewed_alarms

        """
        pass

    def test_get_notification_rule(self):
        """Test case for get_notification_rule

        """
        pass

    def test_get_post_alarm_aggregation_data(self):
        """Test case for get_post_alarm_aggregation_data

        """
        pass

    def test_get_post_stat_bulk_alarm_raw_data(self):
        """Test case for get_post_stat_bulk_alarm_raw_data

        """
        pass

    def test_get_raw_alarm_data(self):
        """Test case for get_raw_alarm_data

        """
        pass

    def test_get_stat_bulk_alarm_raw_data(self):
        """Test case for get_stat_bulk_alarm_raw_data

        """
        pass

    def test_get_stat_data_fields1(self):
        """Test case for get_stat_data_fields1

        """
        pass

    def test_get_stat_query_fields1(self):
        """Test case for get_stat_query_fields1

        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        """
        pass

    def test_list_disabled_alarm(self):
        """Test case for list_disabled_alarm

        """
        pass

    def test_mark_alarms_as_viewed(self):
        """Test case for mark_alarms_as_viewed

        """
        pass

    def test_mark_all_alarms_as_viewed(self):
        """Test case for mark_all_alarms_as_viewed

        """
        pass

    def test_restart_correlation_engine(self):
        """Test case for restart_correlation_engine

        """
        pass

    def test_set_periodic_purge_timer(self):
        """Test case for set_periodic_purge_timer

        """
        pass

    def test_start_tracking(self):
        """Test case for start_tracking

        """
        pass

    def test_stop_tracking(self):
        """Test case for stop_tracking

        """
        pass

    def test_update_notification_rule(self):
        """Test case for update_notification_rule

        """
        pass


if __name__ == '__main__':
    unittest.main()
