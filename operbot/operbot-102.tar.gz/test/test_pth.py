# This file is placed in the Public Domain.


import unittest


from op import fntime


FN = "store/oper.evt.Event/2022-04-11/22:40:31.259218"


class TestPath(unittest.TestCase):

    def test_path(self):
        fnt = fntime(FN)
        self.assertEqual(fnt, 1649709631.259218)
