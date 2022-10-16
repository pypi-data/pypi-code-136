import datetime as dt
from io import StringIO
from unittest import TestCase

from htimeseries import HTimeseries, TzinfoFromString, UnknownTimezone, naive_to_aware


class TzinfoFromStringTestCase(TestCase):
    def test_simple(self):
        atzinfo = TzinfoFromString("+0130")
        self.assertEqual(atzinfo.offset, dt.timedelta(hours=1, minutes=30))

    def test_brackets(self):
        atzinfo = TzinfoFromString("DUMMY (+0240)")
        self.assertEqual(atzinfo.offset, dt.timedelta(hours=2, minutes=40))

    def test_brackets_with_utc(self):
        atzinfo = TzinfoFromString("DUMMY (UTC+0350)")
        self.assertEqual(atzinfo.offset, dt.timedelta(hours=3, minutes=50))

    def test_negative(self):
        atzinfo = TzinfoFromString("DUMMY (UTC-0420)")
        self.assertEqual(atzinfo.offset, -dt.timedelta(hours=4, minutes=20))

    def test_zero(self):
        atzinfo = TzinfoFromString("DUMMY (UTC-0000)")
        self.assertEqual(atzinfo.offset, dt.timedelta(hours=0, minutes=0))

    def test_wrong_input(self):
        for s in ("DUMMY (GMT+0350)", "0150", "+01500"):
            self.assertRaises(ValueError, TzinfoFromString, s)


class NaiveToAwareTestCase(TestCase):
    def test_htimeseries_containing_timezone(self):
        ahtimeseries = HTimeseries()
        ahtimeseries.timezone = "EET (UTC+0200)"
        adate = dt.datetime(2022, 10, 16, 22, 24, 16)
        newdate = naive_to_aware(adate, ahtimeseries)
        eet = dt.timezone(offset=dt.timedelta(hours=2), name="EET")
        expected_date = dt.datetime(2022, 10, 16, 22, 24, 16, tzinfo=eet)
        self.assertEqual(newdate, expected_date)

    def test_ignores_default_timezone_if_htimeseries_contains_timezone(self):
        ahtimeseries = HTimeseries()
        ahtimeseries.timezone = "EET (UTC+0200)"
        adate = dt.datetime(2022, 10, 16, 22, 24, 16)
        newdate = naive_to_aware(adate, ahtimeseries, default_timezone="Etc/GMT-1")
        eet = dt.timezone(offset=dt.timedelta(hours=2), name="EET")
        expected_date = dt.datetime(2022, 10, 16, 22, 24, 16, tzinfo=eet)
        self.assertEqual(newdate, expected_date)

    def test_uses_default_timezone(self):
        ahtimeseries = HTimeseries()
        adate = dt.datetime(2022, 10, 16, 22, 24, 16)
        newdate = naive_to_aware(adate, ahtimeseries, default_timezone="Etc/GMT-2")
        eet = dt.timezone(offset=dt.timedelta(hours=2), name="EET")
        expected_date = dt.datetime(2022, 10, 16, 22, 24, 16, tzinfo=eet)
        self.assertEqual(newdate, expected_date)

    def test_raises_exception_if_no_timezone(self):
        ahtimeseries = HTimeseries()
        adate = dt.datetime(2022, 10, 16, 22, 24, 16)
        with self.assertRaises(UnknownTimezone):
            naive_to_aware(adate, ahtimeseries)
