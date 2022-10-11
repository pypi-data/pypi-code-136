"""Test the Abode device classes."""
import unittest

import requests_mock

import abodepy
import abodepy.helpers.constants as CONST

import tests.mock.login as LOGIN
import tests.mock.oauth_claims as OAUTH_CLAIMS
import tests.mock.logout as LOGOUT
import tests.mock.panel as PANEL
import tests.mock.devices as DEVICES
import tests.mock.devices.valve as VALVE
import pytest


USERNAME = 'foobar'
PASSWORD = 'deadbeef'


class TestValve(unittest.TestCase):
    """Test the AbodePy valve."""

    def setUp(self):
        """Set up Abode module."""
        self.abode = abodepy.Abode(
            username=USERNAME, password=PASSWORD, disable_cache=True
        )

    def tearDown(self):
        """Clean up after test."""
        self.abode = None

    @requests_mock.mock()
    def tests_switch_device_properties(self, m):
        """Tests that switch devices properties work as expected."""
        # Set up URL's
        m.post(CONST.LOGIN_URL, text=LOGIN.post_response_ok())
        m.get(CONST.OAUTH_TOKEN_URL, text=OAUTH_CLAIMS.get_response_ok())
        m.post(CONST.LOGOUT_URL, text=LOGOUT.post_response_ok())
        m.get(CONST.PANEL_URL, text=PANEL.get_response_ok(mode=CONST.MODE_STANDBY))
        m.get(
            CONST.DEVICES_URL,
            text=VALVE.device(
                devid=VALVE.DEVICE_ID,
                status=CONST.STATUS_CLOSED,
                low_battery=False,
                no_response=False,
            ),
        )

        # Logout to reset everything
        self.abode.logout()

        # Get our power switch
        device = self.abode.get_device(VALVE.DEVICE_ID)

        # Test our device
        assert device is not None
        assert device.status == CONST.STATUS_CLOSED
        assert not device.battery_low
        assert not device.no_response
        assert not device.is_on
        assert not device.is_dimmable

        # Set up our direct device get url
        device_url = str.replace(CONST.DEVICE_URL, '$DEVID$', VALVE.DEVICE_ID)

        # Change device properties
        m.get(
            device_url,
            text=VALVE.device(
                devid=VALVE.DEVICE_ID,
                status=CONST.STATUS_OPEN,
                low_battery=True,
                no_response=True,
            ),
        )

        # Refesh device and test changes
        device.refresh()

        assert device.status == CONST.STATUS_OPEN
        assert device.battery_low
        assert device.no_response
        assert device.is_on

    @requests_mock.mock()
    def tests_switch_status_changes(self, m):
        """Tests that switch device changes work as expected."""
        # Set up URL's
        m.post(CONST.LOGIN_URL, text=LOGIN.post_response_ok())
        m.get(CONST.OAUTH_TOKEN_URL, text=OAUTH_CLAIMS.get_response_ok())
        m.post(CONST.LOGOUT_URL, text=LOGOUT.post_response_ok())
        m.get(CONST.PANEL_URL, text=PANEL.get_response_ok(mode=CONST.MODE_STANDBY))
        m.get(
            CONST.DEVICES_URL,
            text=VALVE.device(
                devid=VALVE.DEVICE_ID,
                status=CONST.STATUS_CLOSED,
                low_battery=False,
                no_response=False,
            ),
        )

        # Logout to reset everything
        self.abode.logout()

        # Get our power switch
        device = self.abode.get_device(VALVE.DEVICE_ID)

        # Test that we have our device
        assert device is not None
        assert device.status == CONST.STATUS_CLOSED
        assert not device.is_on

        # Set up control url response
        control_url = CONST.BASE_URL + VALVE.CONTROL_URL
        m.put(
            control_url,
            text=DEVICES.status_put_response_ok(
                devid=VALVE.DEVICE_ID, status=CONST.STATUS_OPEN_INT
            ),
        )

        # Change the mode to "on"
        assert device.switch_on()
        assert device.status == CONST.STATUS_OPEN
        assert device.is_on

        # Change response
        m.put(
            control_url,
            text=DEVICES.status_put_response_ok(
                devid=VALVE.DEVICE_ID, status=CONST.STATUS_CLOSED_INT
            ),
        )

        # Change the mode to "off"
        assert device.switch_off()
        assert device.status == CONST.STATUS_CLOSED
        assert not device.is_on

        # Test that an invalid status response throws exception
        m.put(
            control_url,
            text=DEVICES.status_put_response_ok(
                devid=VALVE.DEVICE_ID, status=CONST.STATUS_CLOSED_INT
            ),
        )

        with pytest.raises(abodepy.AbodeException):
            device.switch_on()
