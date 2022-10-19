import pytz
import traceback
import pandas as pd
from datetime import datetime, timedelta
from qtc.consts.enums import DateDataType
from qtc.ext.logging import set_logger
logger = set_logger()


DEFAULT_TIME_ZONE = 'America/New_York'


def datetime_to_dateid(date):
    """
    :param date: Date in datetime type.
    :type date: datetime
    :return: int - Date in '%Y%m%d' format.

    >>> from datetime import datetime
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.datetime_to_dateid(datetime(2019, 9, 25))
    20190925
    >>> adt_utc = datetime(2020, 8, 7, 2, 0, 0, tzinfo=pytz.UTC)
    >>> adt_ny = adt_utc.astimezone(pytz.timezone('America/New_York'))
    >>> dtu.datetime_to_dateid(adt_utc)
    20200807
    >>> dtu.datetime_to_dateid(adt_ny)
    20200806
    """
    formatted_date = date.strftime('%Y%m%d %Z')[:8]
    return int(formatted_date)


def dateid_to_datetime(dateid, timezone=None):
    """
    :param dateid: Date in '%Y%m%d' format.
    :type dateid: int
    :return: datetime - Date in datetime type.

    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.dateid_to_datetime(20190925)
    datetime.datetime(2019, 9, 25, 0, 0)
    """
    dt = datetime.strptime(str(dateid), '%Y%m%d')
    if timezone is not None:
        # dt = pytz.timezone(timezone).localize(dt)
        dt = dt.replace(tzinfo=pytz.timezone(timezone))

    return dt


def dateid_to_datestr(dateid, sep='-'):
    """
    :param dateid: Date in '%Y%m%d' format.
    :type dateid: int
    :param sep: Separator in the returned date str.
    :type date: int
    :return: str - Date in f"%Y{sep}%m{sep}%d" format.

    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.dateid_to_datestr(20190925)
    '2019-09-25'
    >>> dtu.dateid_to_datestr(20191013, sep='/')
    '2019/10/13'
    """
    dateid = str(dateid)
    date_str = f"{dateid[0:4]}{sep}{dateid[4:6]}{sep}{dateid[6:8]}"
    return date_str


def curr_dateid(timezone=None):
    """
    :return: int - TODAY in '%Y%m%d' format.

    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.curr_dateid()
    """
    today = datetime.now() if timezone is None else datetime.now(pytz.timezone(timezone))
    return datetime_to_dateid(today)


def is_weekday(date):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.is_weekday(20200511)
    True
    >>> dtu.is_weekday(20200516)
    False
    """

    if isinstance(date, int):
        date = dateid_to_datetime(date)
    elif not isinstance(date, datetime):
        raise Exception(f"Supported date types are [dateid | datetime] !")

    return date.weekday() not in [5, 6]


def get_biz_dateids(start_date, end_date):
    bdates = pd.bdate_range(dateid_to_datestr(dateid=normalize_date_to_dateid(date=start_date), sep='-'),
                            dateid_to_datestr(dateid=normalize_date_to_dateid(date=end_date), sep='-')).strftime('%Y%m%d')
    return [int(date) for date in bdates]


def next_biz_dateid(date):
    one_day = timedelta(days=1)
    next_day = dateid_to_datetime(date) + one_day
    while not is_weekday(next_day):
        next_day += one_day

    return datetime_to_dateid(next_day)


def parse_datetime(dt, format=None, timezone=None, ret_as_timestamp=False):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.parse_datetime(20200210)
    datetime.datetime(2020, 2, 10, 0, 0)
    >>> dtu.parse_datetime('2020-02-10', ret_timestamp=True)
    Timestamp('2020-02-10 00:00:00')
    >>> dtu.parse_datetime('20200210-164523', timezone='US/Eastern')
    datetime.datetime(2020, 2, 10, 16, 45, 23, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 STD>)
    >>> dtu.parse_datetime('2020/02/10 16:45:23', format='%Y/%m/%d %H:%M:%S', timezone='Asia/Shanghai')
    datetime.datetime(2020, 2, 10, 16, 45, 23, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)
    >>> dtu.parse_datetime('2020-08-06', timezone=pytz.timezone('Europe/London'))
    datetime.datetime(2020, 8, 6, 0, 0, tzinfo=<DstTzInfo 'Europe/London' BST+1:00:00 DST>)
    """

    if isinstance(dt, int):
        dt = str(dt)

    if (isinstance(dt, datetime) and not ret_as_timestamp) or \
            (isinstance(dt, pd.Timestamp) and ret_as_timestamp):
        return dt

    try:
        dt = pd.Timestamp(dt)
        if timezone is not None:
            dt = dt.tz_localize(timezone)

    except Exception as e:
        pass

    if isinstance(dt, pd.Timestamp):
        return dt if ret_as_timestamp else dt.to_pydatetime()

    if isinstance(dt, str):
        dt = pd.to_datetime(dt, format=format)
        if timezone is not None:
            dt = dt.tz_localize(timezone)

        return dt if ret_as_timestamp else dt.to_pydatetime()

    raise Exception(f"'dt' has to be of type [dateid | str | datetime | pd.Timestamp | np.datetime64] !")


def normalize_date_to_dateid(date=None):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.normalize_date_to_dateid(date=20210929)
    20210929
    >>> dtu.normalize_date_to_dateid(date='2021-09-29')
    20210929
    >>> dtu.normalize_date_to_dateid(datetime(2021,9,29))
    20210929
    """

    if date is None:
        return curr_dateid()

    return datetime_to_dateid(parse_datetime(date))


def convert_data_type_for_date_col(df, date_col=None,
                                   from_data_type=DateDataType.DATEID, to_data_type=DateDataType.TIMESTAMP,
                                   to_date_col_idx=None):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.convert_data_type_for_date_col(pd.DataFrame({'DateId':[20210927,20210928,20210929]}), date_col='DateId')
         DateId       Date
    0  20210927 2021-09-27
    1  20210928 2021-09-28
    2  20210929 2021-09-29
    """

    if isinstance(from_data_type, str):
        from_data_type = DateDataType.retrieve(from_data_type)

    if not isinstance(from_data_type, DateDataType):
        raise Exception(f"type(from_data_type)={type(from_data_type)} is not supported in [str|DateDataType] !")

    if isinstance(to_data_type, str):
        to_data_type = DateDataType.retrieve(to_data_type)

    if not isinstance(to_data_type, DateDataType):
        raise Exception(f"type(to_data_type)={type(to_data_type)} is not supported in [str|DateDataType] !")

    if from_data_type==to_data_type:
        # logger.warn(f'Skipping since from_data_type={from_data_type} is the same as to_data_type={to_data_type} !')
        return df

    if date_col is None:
        date_col = from_data_type.value

    if to_date_col_idx is None:
        to_date_col_idx = list(df.columns).index(date_col)+1

    from_date_col_keyword = from_data_type.value
    if 'DateTime' in date_col and (from_data_type==DateDataType.TIMESTAMP or from_data_type==DateDataType.DATETIME):
        from_date_col_keyword = 'DateTime'
    to_date_col = date_col.replace(from_date_col_keyword, to_data_type.value)

    if to_date_col in df.columns:
        df = df.drop(columns=[to_date_col])
        logger.warn(f'Column to_date_col={to_date_col} found in df and dropped !')
        to_date_col_idx -= 1

    if to_data_type==DateDataType.TIMESTAMP:
        if from_data_type==DateDataType.DATEID:
            new_dates = pd.to_datetime(df[date_col], format='%Y%m%d')
        else:
            new_dates = pd.to_datetime(df[date_col])
    elif to_data_type==DateDataType.DATEID:
        if from_data_type==DateDataType.TIMESTAMP:
            new_dates = [int(date) for date in df[date_col].dt.strftime('%Y%m%d')]
        else:
            raise Exception(f'{from_data_type} -> {to_data_type} not implemented yet!')
    else:
        raise Exception(f'{from_data_type} -> {to_data_type} not implemented yet!')

    df = df.copy()
    df.insert(to_date_col_idx, to_date_col, new_dates)
    return df


def normalize_dt(dt=None, timezone=None):
    if timezone is not None:
        if isinstance(timezone, str):
            timezone = pytz.timezone(timezone)

    if dt is None:
        dt = datetime.now() if timezone is None else datetime.now(tz=timezone)

    try:
        if isinstance(dt, str) or isinstance(dt, int):
            dt = parse_datetime(dt=dt, ret_as_timestamp=False, timezone=timezone)
        elif isinstance(dt, pd.Timestamp):
            if timezone is not None:
                dt = dt.tz_localize(timezone)
        elif isinstance(dt, datetime):
            if timezone is not None:
                dt = dt.astimezone(timezone)
    except Exception as e:
        logger.error(f"dt={dt} cannot be recognized as a datetime !")
        traceback.print_exc()
        return None

    return dt


def get_month_end(date):
    date = parse_datetime(dt=date)
    return date.replace(day=31) if date.month==12 else \
           (date.replace(month=date.month+1, day=1)-timedelta(days=1))


def get_week_start_dateid(date):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.get_week_start_dateid(date=20220629)
    20220627
    """
    date = parse_datetime(dt=date)
    week_start_date = date - timedelta(days=date.weekday())
    return normalize_date_to_dateid(date=week_start_date)


def get_month_start_dateid(date):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.get_month_start_dateid(date=20220629)
    20220601
    """
    date = parse_datetime(dt=date)
    return normalize_date_to_dateid(date=date.replace(day=1))


def get_year_start_dateid(date=None):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.get_year_start_dateid(date=20220629)
    20220101
    """
    if date is None:
        date = curr_dateid()

    date = parse_datetime(dt=date)
    return normalize_date_to_dateid(date=date.replace(month=1, day=1))


def get_ttm_start_dateid(date):
    """
    >>> import qtc.utils.datetime_utils as dtu
    >>> dtu.get_ttm_start_dateid(date=20220629)
    20210629
    >>> dtu.get_ttm_start_dateid(date=20200229)
    20190228
    """
    date = parse_datetime(dt=date)
    try:
        ttm_start_date = date.replace(year=date.year-1)
    except:
        ttm_start_date = date.replace(year=date.year-1, day=date.day-1)

    return normalize_date_to_dateid(date=ttm_start_date)

