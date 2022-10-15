#!/usr/bin/env python3
from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from unittest import TestCase

import pytz
from parameterized import parameterized

from junatum.common.utils import parse_date, parse_float, parse_int
from junatum.finance.constants import IntervalUnit
from junatum.finance.utils import (
    billing_period_to_days,
    format_currency,
    format_variation,
    get_next_billing_schedule,
)


class TestUtils(TestCase):
    def test_billing_period_to_days_with_raise(self):
        with self.assertRaises(AttributeError):
            billing_period_to_days(period='WRONG_PERIOD', period_days=1)

    def test_get_next_billing_schedule_with_raise(self):
        with self.assertRaises(ValueError):
            get_next_billing_schedule(start=datetime(2020, 2, 1, 23, 59, 58), period_days=1)

        with self.assertRaises(ValueError):
            get_next_billing_schedule(
                start=datetime(2020, 2, 1, 23, 59, 58, tzinfo=pytz.utc), period_days=1, buffer_days=-1
            )

    @parameterized.expand(
        [(IntervalUnit.DAY.value, 2, 2), (IntervalUnit.MONTH.value, 1, 30), (IntervalUnit.YEAR.value, 2, 365 * 2)]
    )
    def test_billing_period_to_days(self, period: str, days: int, expected: int):
        self.assertEqual(expected, billing_period_to_days(period=period, period_days=days))

    @parameterized.expand(
        [
            (datetime(2020, 2, 1, 23, 59, 58, tzinfo=pytz.utc), 1, 1, datetime(2020, 2, 3, 0, 0, 0, tzinfo=pytz.utc)),
            (datetime(2020, 2, 1, 23, 59, 58, tzinfo=pytz.utc), 2, 1, datetime(2020, 2, 4, 0, 0, 0, tzinfo=pytz.utc)),
            (datetime(2020, 2, 2, 0, 0, 0, tzinfo=pytz.utc), 1, 1, datetime(2020, 2, 4, 0, 0, 0, tzinfo=pytz.utc)),
            (datetime(2020, 2, 2, 0, 0, 0, tzinfo=pytz.utc), 1, 0, datetime(2020, 2, 3, 0, 0, 0, tzinfo=pytz.utc)),
        ]
    )
    def test_get_next_billing_schedule(self, start: datetime, period_days: int, buffer_days: int, expected: datetime):
        self.assertEqual(
            expected, get_next_billing_schedule(start=start, period_days=period_days, buffer_days=buffer_days)
        )

    @parameterized.expand(
        [
            (None, ''),
            ('', ''),
            (Decimal(-1.0), '-1.00'),
            (Decimal(-0.1), '-0.10'),
            (Decimal(0), '0'),
            (Decimal(0.0), '0'),
            (Decimal(0.1), '+0.10'),
            (Decimal(23.19), '+23.19'),
        ]
    )
    def test_format_variation(self, val: Optional[Decimal], expected: str):
        self.assertEqual(expected, format_variation(val))

    @parameterized.expand(
        [
            (None, '$', False, ''),
            ('', '$', False, ''),
            (Decimal(0), '$', False, '$ 0.00'),
            (0, '$', False, '$ 0.00'),
            (Decimal(0), '₩', False, '₩ 0.00'),
            (Decimal(1234567), '$', False, '$ 1,234,567.00'),
            (Decimal(-1234567), '$', False, '$ -1,234,567.00'),
            (-1234567, '$', False, '$ -1,234,567.00'),
            (Decimal(1234567), '$', True, '$ 1.23 M'),
            (1234567, '$', True, '$ 1.23 M'),
            (Decimal(-1234567), '$', True, '$ -1.23 M'),
            (-1234567, '$', True, '$ -1.23 M'),
            (Decimal(123450000), '$', True, '$ 123.45 M'),
            (Decimal(1234500000), '$', True, '$ 1.23 B'),
            (Decimal(1234500000000), '$', True, '$ 1.23 T'),
        ]
    )
    def test_format_currency(self, val: Optional[Decimal], currency: str, abbreviation: bool, expected: str):
        self.assertEqual(expected, format_currency(val=val, currency=currency, abbreviation=abbreviation))

    def test_parse_date_with_raise(self):
        with self.assertRaises(ValueError):
            parse_date(data='2021-02-32', raise_exception=True)

        with self.assertRaises(TypeError):
            parse_date(data=123, raise_exception=True)

    @parameterized.expand(
        [('2021-01-01', date(2021, 1, 1)), ('2021-03-01', date(2021, 3, 1)), (None, None), ('2021-02-32', None)]
    )
    def test_parse_date(self, data, expected):
        self.assertEqual(expected, parse_date(data=data))

    def test_parse_int_with_raise(self):
        with self.assertRaises(ValueError):
            parse_int(data='one', raise_exception=True)

        with self.assertRaises(TypeError):
            parse_int(data=None, raise_exception=True)

    @parameterized.expand([('1', 1), (None, None)])
    def test_parse_int(self, data, expected):
        self.assertEqual(expected, parse_int(data=data))

    def test_parse_float_with_raise(self):
        with self.assertRaises(ValueError):
            parse_float(data='one', raise_exception=True)

        with self.assertRaises(TypeError):
            parse_float(data=None, raise_exception=True)

    @parameterized.expand([('1.2', 1.2), (None, None)])
    def test_parse_float(self, data, expected):
        self.assertEqual(expected, parse_float(data=data))
