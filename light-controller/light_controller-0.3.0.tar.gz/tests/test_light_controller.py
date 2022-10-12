#!/usr/bin/env python

"""Tests for `light_controller` package."""
import time
import unittest

from light_controller.light_controller import LightManager


class TestLight_controller(unittest.TestCase):

    def init_lm(self):
        self.lm = LightManager(port="COM1", baudrate=9600, list_channels=[1])
        pass

    def setUp(self):
        self.lm.switch_on(list_intensity=[20])

    def off_light(self):
        self.lm.switch_off()


if __name__ == '__main__':
    unittest.main()
