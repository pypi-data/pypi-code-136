# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.typing import cast_MultiT, cast_OptMultiT

class TestTyping(unittest.TestCase):
    def test_multit(self):
        self.assertEqual(cast_MultiT(2), (2,))
        self.assertEqual(cast_MultiT("ab"), ("ab",))
        self.assertEqual(cast_MultiT(range(2)), (0, 1))

        self.assertIs(cast_OptMultiT(None), None)
        self.assertEqual(cast_OptMultiT(2), (2,))
        self.assertEqual(cast_OptMultiT("ab"), ("ab",))
        self.assertEqual(cast_OptMultiT(range(2)), (0, 1))
