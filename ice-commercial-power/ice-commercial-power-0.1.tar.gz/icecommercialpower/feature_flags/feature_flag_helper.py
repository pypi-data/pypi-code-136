"""
Helper to access Feature Flags form Azure App Configuration
"""

from __future__ import annotations
from functools import cache
from enum import Enum
import logging
import os
from typing import List
from azure.appconfiguration import (
    AzureAppConfigurationClient,
    FeatureFlagConfigurationSetting,
    FILTER_TARGETING,
)


class FeatureFlags(str, Enum):
    """Describes the existing feature flags"""

    # Feature flag to enable/disable the use of USSD payments
    USSD_PAYMENT = "ussd_payment"
    SUBSCRIPTION_PLAN = "subscription_plan"


class UnknownFeatureFlagFilterError(Exception):
    """
    Error in case there is not a valid filter
    """


class FeatureFlagHelper:
    """
    This is the Feature flag helper class.
    """

    def __init__(self, client: AzureAppConfigurationClient):
        """
        The constructor of the FeatureFlagHelper
        """
        self.client = client

    @classmethod
    def from_env(cls) -> FeatureFlagHelper:
        """
        Create a new FeatureFlagHelper from environment variable AZURE_APP_CONFIG_CONNECTION_STRING.
        """
        connection_string = os.getenv("AZURE_APP_CONFIG_CONNECTION_STRING")
        client = AzureAppConfigurationClient.from_connection_string(connection_string)
        return cls(client)

    def has_feature_enabled(
        self, groupnames: List[str], feature_flag: FeatureFlags | str
    ) -> bool:
        """
        Check if the given feature is enabled for the given groups.
        """
        feature_name = (
            feature_flag.value
            if isinstance(feature_flag, FeatureFlags)
            else feature_flag
        )

        feature_flag_setting = self.get_feature_flag(feature_name)

        if feature_flag_setting is None:
            logging.warning("Feature %s not found", feature_name)
            return False

        if feature_flag_setting.enabled is not True:
            logging.debug("Feature %s is disabled", feature_name)
            return False

        if (
            feature_flag_setting.filters is None
            or len(feature_flag_setting.filters) == 0
        ):
            # No filters -> we just look for enabled or not
            return feature_flag_setting.enabled is True

        # feature flag has filters
        if len(feature_flag_setting.filters) > 1:
            raise UnknownFeatureFlagFilterError("Only 0 or 1 filters are supported")

        if feature_flag_setting.filters[0]["name"] != FILTER_TARGETING:
            raise UnknownFeatureFlagFilterError(
                f"Only Filter of type {FILTER_TARGETING} supported"
            )

        has_groups = (
            feature_flag_setting.filters[0]["parameters"] is None
            or len(feature_flag_setting.filters[0]["parameters"]) == 0
            or feature_flag_setting.filters[0]["parameters"]["Audience"] is None
            or len(feature_flag_setting.filters[0]["parameters"]["Audience"]) == 0
            or feature_flag_setting.filters[0]["parameters"]["Audience"]["Groups"]
            is None
            or len(feature_flag_setting.filters[0]["parameters"]["Audience"]["Groups"])
            == 0
        )
        if has_groups:
            # when no parameters, audience or groups configured
            # we assume that there is no applicable filter and return true
            return True

        # check if the groupname is in valid group name
        ff_groups = feature_flag_setting.filters[0]["parameters"]["Audience"]["Groups"]

        valid_ff_group_names = [
            group["Name"] for group in ff_groups if group["RolloutPercentage"] >= 50
        ]
        # check group intersections
        return not set(groupnames).isdisjoint(valid_ff_group_names)

    @cache
    def get_feature_flag(self, feature_name) -> FeatureFlagConfigurationSetting:
        """Gets the feature flag from AzureAppConfigurationClient"""
        return self.client.get_configuration_setting(
            key=".appconfig.featureflag/" + feature_name
        )
