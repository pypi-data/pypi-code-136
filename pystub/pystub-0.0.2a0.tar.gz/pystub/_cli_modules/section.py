"""
Stub for CLI Section
"""

import logging

LOG = logging.getLogger(__name__)


class CommandA:
    """
    Implements CommandA
    """

    def __init__(self):
        self.description = "CommandA"

    def cmd_a1(self):
        LOG.info("Logic for cmd_a1")

    def cmd_a2(self):
        LOG.info("Logic for cmd_a2")


class CommandB:
    """
    Implements CommandA
    """

    def __init__(self):
        self.description = "CommandB"

    def cmd_b1(self):
        LOG.info("Logic for cmd_b1")

    def cmd_b2(self):
        LOG.info("Logic for cmd_b2")
