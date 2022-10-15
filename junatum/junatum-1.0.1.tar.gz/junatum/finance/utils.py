#!/usr/bin/env python3
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Union

import pytz
from humanize import intcomma, intword

from junatum.common.decorators import ensure_positive_number
from junatum.finance.constants import BILLING_PERIOD_TO_DAYS


@ensure_positive_number('period_days')
def billing_period_to_days(period: str, period_days: int) -> int:
    """빌링 주기를 날짜로 변환한 값을 반환합니다.

    :param period: str 빌링 주기
    :param period_days: int 빌링 주기의 반복 횟수
    :return: int 변환된 빌링 주기의 날짜 수
    """
    period = BILLING_PERIOD_TO_DAYS.get(period, None)
    if not period:
        raise AttributeError(f'period({period}) is invalid.')

    return period * period_days


@ensure_positive_number('period_days')
def get_next_billing_schedule(start: datetime, period_days: int, buffer_days: int = 0) -> datetime:
    """다음 빌링 스케쥴을 계산하여 UTC 기준의 값으로 반환합니다.

    :param start: datetime UTC 타임존을 가진 시작 시각
    :param period_days: int 다음 빌링 주기의 날짜 수
    :param buffer_days: int 버퍼로 제공할 날짜 수
    :return: datetime UTC 기준의 다음 빌링 스케쥴 시각
    """
    if start.tzinfo != pytz.utc:
        raise ValueError(f'start({start}) must have utc timezone.')
    if buffer_days < 0:
        raise ValueError(f'buffer_days({buffer_days}) can not be negative value.')

    target = start + timedelta(days=period_days + buffer_days)
    target = target.replace(hour=0, minute=0, second=0)
    return target


def format_variation(val: Union[Decimal, str, None]) -> str:
    """variation 형식으로 변환한 문자열 값을 반환합니다.

    :param val: decimal variation 포멧으로 변환하고 싶은 decimal 값
    :return: str variation 포멧으로 표현 된 문자열
    """
    if val is None or val == '':
        return ''

    result = val.compare(Decimal(0))
    if result == 0:
        return '0'

    prefix = '+' if result > 0 else ''
    return f'{prefix}{intcomma(val, 2)}'


def format_currency(val: Union[Decimal, int, str, None], currency: str = '$', abbreviation: bool = False) -> str:
    """currency 형식으로 변환한 문자열 값을 반환합니다.

    :param val: decimal currency 포멧으로 변환하고 싶은 decimal 값
    :param currency: str currency 기호
    :param abbreviation: bool 줄임말로 사용할지 여부
    :return: str currency 형식으로 변환한 문자열 값
    """
    if val is None or val == '':
        return ''

    if abbreviation:
        prefix = ''
        is_minus = False
        if isinstance(val, int):
            is_minus = val < 0
        if isinstance(val, Decimal):
            is_minus = val.compare(Decimal(0)) == -1
        if is_minus:
            val *= Decimal(-1)
            prefix = '-'
        word = intword(value=val, format='%.2f').lower()
        word = word.replace('million', 'M').replace('billion', 'B').replace('trillion', 'T')
        return f'{currency} {prefix}{word}'

    return f'{currency} {intcomma(val, 2)}'
