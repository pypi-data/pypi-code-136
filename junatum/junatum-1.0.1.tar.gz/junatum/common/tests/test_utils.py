#!/usr/bin/env python3
from datetime import date, datetime, timedelta
from unittest import TestCase

from parameterized import parameterized

from junatum.common.decorators import ensure_positive_number
from junatum.common.exceptions import ParseException
from junatum.common.utils import (
    chunks,
    date_to_fiscal_period,
    fiscal_period_to_date,
    is_empty_or_blank,
    milliseconds_to_datetime,
    parse_url,
    period_to_days,
    remove_str_from_csv_str,
    utc_now,
)


class TestCommonUtils(TestCase):
    def test_is_empty_or_blank(self):
        self.assertEqual(True, is_empty_or_blank(s=''))
        self.assertEqual(True, is_empty_or_blank(s='  '))
        self.assertEqual(False, is_empty_or_blank(s='a  '))
        self.assertEqual(False, is_empty_or_blank(s='  b  '))

    def test_date_to_fiscal_period(self):
        with self.assertRaises(ValueError):
            date_to_fiscal_period(target_date=' ')

        self.assertEqual('Q1 2018', date_to_fiscal_period(target_date=date(2018, 1, 1)))
        self.assertEqual('Q1 2018', date_to_fiscal_period(target_date=date(2018, 1, 1)))
        self.assertEqual('Q1 2018', date_to_fiscal_period(target_date=date(2018, 3, 31)))
        self.assertEqual('Q2 2018', date_to_fiscal_period(target_date=date(2018, 4, 1)))
        self.assertEqual('Q3 2018', date_to_fiscal_period(target_date=date(2018, 7, 1)))
        self.assertEqual('Q4 2018', date_to_fiscal_period(target_date=date(2018, 10, 1)))

    def test_fiscal_period_to_date(self):
        with self.assertRaises(ParseException):
            fiscal_period_to_date(target_date='Q 2018')

        self.assertEqual(date(2018, 1, 1), fiscal_period_to_date(target_date='Q1 2018'))
        self.assertEqual(date(2018, 4, 1), fiscal_period_to_date(target_date='Q2 2018'))
        self.assertEqual(date(2018, 7, 1), fiscal_period_to_date(target_date='Q3 2018'))
        self.assertEqual(date(2018, 10, 1), fiscal_period_to_date(target_date='Q4 2018'))

    def test_period_to_days(self):
        self.assertEqual(365, period_to_days(period='fast', max_days=365))
        self.assertEqual(180, period_to_days(period=' ', max_days=180))
        self.assertEqual(1, period_to_days(period='1d'))
        self.assertEqual(7 * 2, period_to_days(period='2w'))
        self.assertEqual(30 * 2, period_to_days(period='2m'))
        self.assertEqual(365 * 3, period_to_days(period='3y'))
        self.assertEqual(365 * 5, period_to_days(period='10y'))

    def test_remove_element_from_csv_str(self):
        csv_str = 'A,B,C,D'
        self.assertEqual('A,C,D', remove_str_from_csv_str(csv_str=csv_str, element='B'))
        self.assertEqual('', remove_str_from_csv_str(csv_str='A', element='A'))
        self.assertEqual('', remove_str_from_csv_str(csv_str='', element='A'))
        self.assertEqual(csv_str, remove_str_from_csv_str(csv_str=csv_str, element='F'))
        self.assertEqual(csv_str, remove_str_from_csv_str(csv_str=csv_str, element=''))

    def test_milliseconds_to_datetime(self):
        with self.assertRaises(ParseException):
            self.assertEqual(None, milliseconds_to_datetime(''))

        with self.assertRaises(ParseException):
            self.assertEqual(None, milliseconds_to_datetime(900))

        milliseconds = 1559852284000
        self.assertEqual(
            datetime(year=2019, month=6, day=6, hour=20, minute=18, second=4), milliseconds_to_datetime(milliseconds)
        )

        milliseconds = str(milliseconds)
        self.assertEqual(
            datetime(year=2019, month=6, day=6, hour=20, minute=18, second=4), milliseconds_to_datetime(milliseconds)
        )

    def test_ensure_positive_number(self):
        with self.assertRaises(TypeError):

            @ensure_positive_number
            def inner_func1(limit: int = 5) -> int:
                return limit

            inner_func1()

        with self.assertRaises(TypeError):

            @ensure_positive_number()
            def inner_func2(limit: int = 5) -> int:
                return limit

            inner_func2()

        with self.assertRaises(ValueError):

            @ensure_positive_number('limit')
            def inner_func3(limit: int = 5) -> int:
                return limit

            inner_func3(limit=-1)

        with self.assertRaises(ValueError):

            @ensure_positive_number('limit', 'period')
            def inner_func4(limit: int = 5, period: str = '') -> tuple:
                return limit, period

            inner_func4(limit=10, period='month')

        @ensure_positive_number('limit')
        def inner_func5(limit: int = 5, period: str = '') -> tuple:
            return limit, period

        inner_func5(limit=10, period='year')

    def test_chunks(self):
        with self.assertRaises(ValueError):
            chunks(items='awesome', n=2)

        with self.assertRaises(ValueError):
            chunks(items=[1, 2, 3], n=-1)

        result = chunks(items=[1, 2, 3, 4], n=2)
        self.assertEqual(2, len(result))
        self.assertEqual(1, result[0][0])
        self.assertEqual(2, result[0][1])

        result = chunks(items=[1, 2, 3, 4, 5], n=2)
        self.assertEqual(3, len(result))

        result = chunks(items=[1, 2, 3, 4], n=10)
        self.assertEqual(1, len(result))
        self.assertEqual(4, len(result[0]))

    def test_utc_now(self):
        utc = utc_now()
        self.assertTrue(isinstance(utc, datetime))
        self.assertEqual(timedelta(0), utc.utcoffset())

    @parameterized.expand(
        [
            (' ', None),
            ('httttpsdf://asdfasf1', None),
            ('http://google.com', 'http://google.com'),
            ('https://google.com', 'https://google.com'),
        ]
    )
    def test_parse_url(self, url, expected):
        self.assertEqual(parse_url(url=url), expected)
