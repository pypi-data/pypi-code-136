import unittest
import datetime
from rsoniutils.utils.datetimeext import DateTimeExt
import os,sys

filepath =os.path.abspath('rsoniUtils/tests/testdata/')
print(filepath)
currentdate="20200620"
filename ="abc.txt" 
filextension="txt"  

class TestDateTimeExt(unittest.TestCase):
    dt= DateTimeExt()
    def test_GetCurrentDateYYYYMMDD(self):
        print(self.dt.GetCurrentDateYYYYMMDD())
        self.assertIsNotNone(self.dt.GetCurrentDateYYYYMMDD())

    def test_GetCurrentDateTimeInStr(self):
        print(self.dt.GetCurrentDateTimeInStr())
        self.assertIsNotNone(self.dt.GetCurrentDateTimeInStr())
   
    def test_GetCurrentDateTime(self): 
        print(self.dt.GetCurrentDateTime())
        self.assertIsNotNone(self.dt.GetCurrentDateTime())

    def test_TimeDiff(self):
        dt=datetime.datetime.now()
        tdiff=self.dt.TimeDiff(dt)
        print(tdiff)
        self.assertIsNotNone(tdiff)

if __name__ == '__main__':
    unittest.main()
