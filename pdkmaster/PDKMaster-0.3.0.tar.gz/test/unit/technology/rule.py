# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import rule as _rle


class RuleTest(unittest.TestCase):
    def test_error(self):
        class MyRule(_rle._Rule):
            def __init__(self):
                pass

            def __eq__(self, other: object) -> bool:
                return super().__eq__(other)

            def __hash__(self):
                return super().__hash__()

        rule = MyRule()

        with self.assertRaises(TypeError):
            rule == rule
        with self.assertRaises(TypeError):
            hash(rule)
        with self.assertRaises(ValueError):
            bool(rule)

    def test_rule(self):
        class MyRule(_rle._Rule):
            def __init__(self, *, name: str):
                self.name = name

            def __eq__(self, other):
                return isinstance(other, MyRule) and self.name == other.name

            def __hash__(self):
                return hash(self.name)

        rule1 = MyRule(name="Rule1")
        rule1b = MyRule(name="Rule1")
        rule2 = MyRule(name="Rule2")

        self.assertEqual(rule1, rule1b)
        self.assertEqual(hash(rule1), hash(rule1b))
        self.assertNotEqual(rule1, rule2)

        # Just create a Rules object to increase code coverage
        rules = _rle.Rules((rule1, rule2))
        self.assertEqual(rule1, rules[0])

    def test_condition(self):
        class MyCond(_rle._Condition):
            def __init__(self, *, str1: str, str2: str):
                super().__init__(elements=(str1, str2))

            def __repr__(self):
                return f"MyCond(str1={self._elements[0]!r}, str2={self._elements[1]!r})"

        strs = ("Hello", "world")
        cond = MyCond(str1=strs[0], str2=strs[1])
        cond2 = MyCond(str1=strs[0], str2=strs[1])

        self.assertNotEqual(cond, strs[0])
        self.assertEqual(cond, cond2)
        self.assertEqual(hash(cond), hash(cond2))
        self.assertEqual(hash(cond), hash(strs))
