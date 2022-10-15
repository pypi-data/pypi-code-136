#!/usr/bin/env python3
import re
from datetime import date, datetime
from typing import Optional, Union

import validators
from dateutil.parser import parse
from furl import furl
from pytz import utc

from junatum.common.decorators import ensure_positive_number
from junatum.common.exceptions import ParseException


def is_empty_or_blank(s: str) -> bool:
    """빈 문자열인지 판단합니다.

    :param s: str 검사할 값
    :return: bool 파라미터가 empty 또는 strip() 후에 blank 값이면 True, 아니면 False

    예제:
        다음과 같이 사용하세요:

        >>> is_empty_or_blank('  ')
        True
    """
    return not (s and isinstance(s, str) and s.strip())


def date_to_fiscal_period(target_date: date) -> str:
    """date 값을 분기를 표현하는 형식으로 반환합니다.

    :param target_date: date 변환이 필요한 값
    :return: str 분기를 표현하는 형식의 str 값

    예제:
        다음과 같이 사용하세요:

        >>> date_to_fiscal_period(date(2019, 1, 1))
        'Q1 2019'
    """
    if not isinstance(target_date, date):
        raise ValueError

    if 1 <= target_date.month < 4:
        period = 1
    elif 4 <= target_date.month < 7:
        period = 2
    elif 7 <= target_date.month < 10:
        period = 3
    else:
        period = 4

    return f'Q{period} {target_date.year}'


def fiscal_period_to_date(target_date: str) -> date:
    """분기를 표현하는 형식의 str 값을 date 값으로 변환하여 반환합니다.

    :param target_date: str 분기를 표현하는 형식의 값
    :return: date fiscal period str 값을 date 로 변환한 값

    예제:
        다음과 같이 사용하세요:

        >>> fiscal_period_to_date('Q1 2019')
        date(2019, 1, 1)
    """
    fiscal_period_dict = {
        'Q1': '01-01',
        'Q2': '04-01',
        'Q3': '07-01',
        'Q4': '10-01',
    }
    fiscal_period_regex = re.compile(r"""(?P<period>Q[1-4])\s+(?P<year>[12][0-9]{3})""", re.I)
    parsed_fiscal_period = re.search(fiscal_period_regex, target_date)
    if not parsed_fiscal_period:
        raise ParseException()

    parsed_fiscal_period = parsed_fiscal_period.groupdict()
    parsed_fiscal_period = (
        f'{parsed_fiscal_period["year"]}-' f'{fiscal_period_dict[parsed_fiscal_period["period"].upper()]}'
    )
    return parse(parsed_fiscal_period).date()


def period_to_days(period: str, max_days: int = 1825) -> int:
    """주기를 표현하는 str 값을 days 값으로 변환하여 반환합니다.

    :param period: str 주기를 표현하는 형식의 값
    :param max_days: int 변환된 최대 값, 기본 값 1825
    :return: int 변환된 days 값. 단, 변환된 값은 최대 값을 넘을 수 없음.

    예제:
        다음과 같이 사용하세요:

        >>> period_to_days('1d')
        1
        >>> period_to_days('2m')
        60
    """
    if is_empty_or_blank(period):
        return max_days

    days_per_unit = {
        'd': 1,
        'w': 7,
        'm': 30,
        'y': 365,
    }
    period_regex = re.compile(r"""(?P<number>\d+)(?P<unit>y|w|m|d)""", re.I)
    parsed_period = re.search(period_regex, period)
    if not parsed_period:
        return max_days

    parsed_period = parsed_period.groupdict()
    number = int(parsed_period['number']) if int(parsed_period['number']) > 0 else 1
    days = days_per_unit.get(parsed_period['unit'], 'y')

    return number * days if number * days < max_days else max_days


def milliseconds_to_datetime(milliseconds: Union[str, int]) -> datetime:
    """밀리세컨드를 표현한 str or int 값을 UTC 기준의 datetime 값으로 변환하여 반환합니다.

    :param milliseconds: str or tin 밀리세컨드 형식의 값
    :return: datetime UTC 기준으로 변환한 값

    예제:
        다음과 같이 사용하세요:

        >>> milliseconds_to_datetime('1559852284000')
        datetime(2019, 6, 6, 20, 18, 4)
    """
    if isinstance(milliseconds, str) and is_empty_or_blank(milliseconds):
        raise ParseException('milliseconds can not be empty or blank.')
    if isinstance(milliseconds, int) and milliseconds < 1000:
        raise ParseException('milliseconds must be greater than 1000.')

    seconds = int(milliseconds) / 1000
    return datetime.utcfromtimestamp(seconds)


def utc_now() -> datetime:
    """현재 UTC 타임존을 가지는 UTC datetime 값을 반환합니다.

    :return: datetime UTC datetime with UTC timezone.
    """
    return utc.localize(datetime.utcnow())


def remove_str_from_csv_str(csv_str: str, element: str) -> str:
    """csv 형식으로 표현된 문자열에서 특정 문자열을 제거하여 반환합니다.

    :param csv_str: str csv 형식의 값
    :param element: str 제거를 원하는 값
    :return: str 특정 문자열이 제거된 csv 형식의 값
    """
    if is_empty_or_blank(csv_str) or is_empty_or_blank(element):
        return csv_str.strip()

    csv_arr = csv_str.split(',')
    try:
        csv_arr.remove(element)
    except ValueError:
        pass

    return ','.join(csv_arr)


@ensure_positive_number('n')
def chunks(items: list, n: int) -> list:
    """list를 개별 사이즈 단위로 분리하여 반환합니다.

    :param items: list 분리는 원하는 리스트 값
    :param n: int 원하는 개별 리스트의 사이즈 값
    :return: list n 사이즈 별로 분리된 리스트

    예제:
        다음과 같이 사용하세요:

        >>> chunks(items=[1, 2, 3, 4, 5], n=2)
        [[1, 2], [3, 4], [5]]
    """
    if not isinstance(items, list):
        raise ValueError('items must be list.')

    return [items[i : i + n] for i in range(0, len(items), n)]


def parse_date(data, raise_exception: bool = False) -> Optional[date]:
    """date 객체로 변환을 하여 반환합니다.

    :param data: 변환이 필요한 값
    :param raise_exception: bool exception이 발생할 경우 raise를 시킬지 여부
    :return: Optional[date] 변환된 값
    """
    try:
        parsed = parse(data).date()
    except (ValueError, TypeError):
        if raise_exception:
            raise
        parsed = None

    return parsed


def parse_int(data, raise_exception: bool = False) -> Optional[int]:
    """int 값으로 변환을 하여 반환합니다.

    :param data: 변환이 필요한 값
    :param raise_exception: bool exception이 발생할 경우 raise를 시킬지 여부
    :return: Optional[int] 변환된 값
    """
    try:
        parsed = int(data)
    except (ValueError, TypeError):
        if raise_exception:
            raise
        parsed = None

    return parsed


def parse_float(data, raise_exception: bool = False) -> Optional[float]:
    """float 값으로 변환을 하여 반환합니다.

    :param data: 변환이 필요한 값
    :param raise_exception: bool exception이 발생할 경우 raise를 시킬지 여부
    :return: Optional[float] 변환된 값
    """
    try:
        parsed = float(data)
    except (ValueError, TypeError):
        if raise_exception:
            raise
        parsed = None

    return parsed


def parse_url(url: str) -> Optional[str]:
    """유효한 url 값인지 확인하여 반환합니다.

    :param url: str 확인이 필요한 값
    :return: Optional[str] 확인된 url 값
    """
    if is_empty_or_blank(url):
        return None

    if url and validators.url(url):
        try:
            return furl(url).url
        except ValueError:
            pass

    return None
