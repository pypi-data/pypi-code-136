import unittest
import math
from fin_crawler.plugins.utils import convert_num,convert_tw_year

class Test_convert_num(unittest.TestCase):

    def test_comma(self):
        self.assertEqual(123456789,convert_num('123,456,789'))
        self.assertEqual(123,convert_num('123'))
    def test_negitive(self):
        self.assertEqual(-1,convert_num('-1'))
    def test_zero(self):
        self.assertEqual(0,convert_num('X0'))
    def test_nan(self):
        self.assertEqual(True,math.isnan(convert_num('--')))
    def test_error(self):
        with self.assertRaises(ValueError):
            convert_num('1ioj2o3i')
class Test_convert_tw_year(unittest.TestCase):

    def test_convert(self):
        self.assertEqual('20220202',convert_tw_year('111/02/02'))
        self.assertEqual('20210910',convert_tw_year('110/09/10'))
        with self.assertRaises(ValueError):
            convert_tw_year('123123')