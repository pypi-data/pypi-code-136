import datetime
import time
import pytz
import arrow
import re
from .time_decode import MemArgs, TimeDecoder
from .filters import solar_chinese_to_num
from . import pyunit_time
from .pyunit_time import filters
from dateutil import tz
from dateutil.parser import parser


def _build_tzaware(self, naive, res, tzinfos):
    if callable(tzinfos) or (tzinfos and res.tzname in tzinfos):
        tzinfo = self._build_tzinfo(tzinfos, res.tzname, res.tzoffset)
        aware = naive.replace(tzinfo=tzinfo)
        aware = self._assign_tzname(aware, res.tzname)

    elif res.tzname and res.tzname in time.tzname:
        aware = naive.replace(tzinfo=tz.tzlocal())

        # Handle ambiguous local datetime
        aware = self._assign_tzname(aware, res.tzname)

        # This is mostly relevant for winter GMT zones parsed in the UK
        if (aware.tzname() != res.tzname and
                res.tzname in self.info.UTCZONE):
            aware = aware.replace(tzinfo=tz.UTC)

    elif res.tzoffset == 0:
        aware = naive.replace(tzinfo=tz.UTC)

    elif res.tzoffset:
        aware = naive.replace(tzinfo=tz.tzoffset(res.tzname, res.tzoffset))

    elif not res.tzname and not res.tzoffset:
        # i.e. no timezone information was found.
        aware = naive

    elif res.tzname:
        # tz-like string was parsed but we don't know what to do
        # with it
        # warnings.warn("tzname {tzname} identified but not understood.  "
        #               "Pass `tzinfos` argument in order to correctly "
        #               "return a timezone-aware datetime.  In a future "
        #               "version, this will raise an "
        #               "exception.".format(tzname=res.tzname),
        #               category=UnknownTimezoneWarning)
        aware = naive
    else:
        raise ValueError('aware is None')

    return aware


parser._build_tzaware = _build_tzaware


class GuessTime:
    def __init__(self, time_any=None, cut_float=True, raise_err=True):
        self.time_offset_hour = 0
        self.time_float_str = ''
        if not time_any:
            time_any = time.time()
        if isinstance(time_any, (int, float)):
            if time_any > 100000000000:
                time_any /= 1000
            time_any = arrow.get(time_any).datetime.__str__()
        elif isinstance(time_any, (datetime.datetime, datetime.date)):
            time_any = time_any.__str__()

        if isinstance(time_any, str):
            if re.findall(r'[\-\+][0-1][0-9]:?00', time_any).__len__():
                self.time_offset_hour = int(re.findall(r'([\-\+][0-1][0-9]):?00', time_any)[0])
                time_any = re.sub(r'[\-\+][0-1][0-9]:?00', '', time_any)
            if cut_float and re.findall(r'\.[0-9]{3,6}', time_any).__len__():
                self.time_float_str = re.findall(r'\.[0-9]{3,6}', time_any)[0]
                time_any = re.sub(r'\.[0-9]{3,6}', '', time_any)
            time_any = re.sub(r'[.。|=,、?\\，!#%_\-—@]', '/', time_any)
            # print(pyunit_time.filters.filters_string(time_any, remove_re='`'))
            time_any = solar_chinese_to_num(time_any)  # 关于中文的十的转换为阿拉伯数字
            time_any = filters.symbol_replace(time_any)  # 符号替换
            time_any = filters.ten_to_number(time_any)  # 关于中文的十的转换为阿拉伯数字
            time_any = re.sub(r'[号月年（）(){}\[\]秒日點点时時分]$', '', time_any)
            time_any = re.sub(r'[号月年（）(){}\[\]]', '/', time_any)
            time_any = re.sub(r'[秒日]', ' ', time_any)
            time_any = re.sub(r'[點点时時分]', ':', time_any)
            # time_any = re.sub(r'/$', ' ', time_any)
            # time_any = re.sub(r'/ ', ' ', time_any)
            # time_any = re.sub(r':$', ' ', time_any)
            # time_any = re.sub(r': ', ' ', time_any)

        self.time_any = time_any or datetime.datetime.now().__str__()
        # print(self.time_any)
        self.res = TimeDecoder(MemArgs(self.time_any)).run()

        try:
            self.res_time_int = int(self.res[0][0][1].split('\t')[-1])

            if self.time_offset_hour:
                self.res_time_int -= self.time_offset_hour * 3600
            self.res_time = float(str(self.res_time_int) + self.time_float_str)
            self.res_time_arrow = arrow.get(self.res_time)
            self.res_time_datetime = self.res_time_arrow.datetime
        except Exception as ex:
            if raise_err:
                raise ValueError(f'时间解析出错：{self.time_any} {self.res} {ex}')
            else:
                self.res_time_int = None
                self.res_time = None
                self.res_time_arrow = None
                self.res_time_datetime = None

    def offset(self, seconds=None, minutes=None, hours=None):
        res_int = self.res_time_int
        if seconds:
            res_int = res_int+seconds
        if minutes:
            res_int = res_int+(minutes*60)
        if hours:
            res_int = res_int+(hours*3600)
        return self.__class__(res_int)

    def to_timestamp_int(self, default=None):
        return self.res_time_int or default

    def to_timestamp(self, default=None):
        return self.res_time or default

    def to_datetime(self, default=None):
        return self.res_time_datetime or default

    def to_datetime_with_change_timezone(
            self, default=None, in_timezone="Europe/London", out_timezone='Asia/Shanghai'):
        i_zone = pytz.timezone(in_timezone)
        o_zone = pytz.timezone(out_timezone)
        time_o = self.res_time_datetime or default
        return time_o.replace(tzinfo=i_zone).astimezone(o_zone)

    def to_arrow(self, default=None):
        return self.res_time_arrow or default

    def to_date_str(self, default=None, fmt="%Y-%m-%d %H:%M:%S"):
        if fmt == 1:
            fmt = '%Y-%m-%d %H:%M:%S %Z'
        elif fmt == 2:
            fmt = '%Y-%m-%d %H:%M:%S%z'
        elif fmt == 3:
            fmt = '%Y-%m-%dT%H:%M:%S.%f%z'
        elif fmt == 4:
            fmt = '%Y-%m-%d'
        elif fmt == 5:
            fmt = '%Y-%m-%d %H:%M:%S'
        return time.strftime(fmt, time.localtime(self.res_time)) or default

    def to_date_str_with_change_timezone(
            self, default=None, in_timezone="Europe/London", out_timezone='Asia/Shanghai',
            strftime='%Y-%m-%d %H:%M:%S %Z'):
        if strftime == 1:
            strftime = '%Y-%m-%d %H:%M:%S %Z'
        elif strftime == 2:
            strftime = '%Y-%m-%d %H:%M:%S%z'
        elif strftime == 3:
            strftime = '%Y-%m-%dT%H:%M:%S.%f%z'
        elif strftime == 4:
            strftime = '%Y-%m-%d'
        elif strftime == 5:
            strftime = '%Y-%m-%d %H:%M:%S'
        i_zone = pytz.timezone(in_timezone)
        o_zone = pytz.timezone(out_timezone)
        time_o = self.res_time_datetime or default
        return time_o.replace(tzinfo=i_zone).astimezone(o_zone).strftime(strftime)

    def to_guess_filter_string(self):
        return self.time_any

    def parse(self, string, **kwargs):
        """
        print(GuessTime('2020-4-22 00:00:00').parse('这个月的第三个星期天'))
        # [{'key': '这个月第3个星期天', 'keyDate': '2020-04-19 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('前2年的国庆节的后一天晚上8点半'))
        # [{'key': '前2年国庆节后1天晚上8点半', 'keyDate': '2018-09-30 20:30:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('上上个月'))
        # [{'key': '上上个月', 'keyDate': '2020-02-22 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('今天晚上8点'))
        # [{'key': '今天晚上8点', 'keyDate': '2020-04-22 20:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('今年儿童节晚上九点一刻'))
        # [{'key': '今年儿童节晚上9点1刻', 'keyDate': '2020-06-01 21:15:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('今天中午十二点'))
        # [{'key': '今天中午12点', 'keyDate': '2020-04-22 12:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('明年春节'))
        # [{'key': '明年春节', 'keyDate': '2021-02-12 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('明年的感恩节'))
        # [{'key': '明年感恩节', 'keyDate': '2021-11-25 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('下3个星期1早上7点半'))
        # [{'key': '下3个星期1早上7点半', 'keyDate': '2020-05-11 07:30:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('今年的大寒'))
        # [{'key': '今年大寒', 'keyDate': '2021-01-20 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('2019年12月'))
        # [{'key': '2019年12月', 'keyDate': '2019-12-01 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('8年前'))
        # [{'key': '8年前', 'keyDate': '2012-04-22 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('三天以后'))
        # [{'key': '3天以后', 'keyDate': '2020-04-25 00:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('三天之内的下午3点'))
        # [{'key': '3天之内下午3点', 'keyDate': '2020-04-25 15:00:00', 'baseDate': '2020-04-22 00:00:00'}]

        print(GuessTime('2020-4-22 00:00:00').parse('后三天的下午4点56秒'))
        # [{'key': '后3天下午4点56秒', 'keyDate': '2020-04-25 16:00:56', 'baseDate': '2020-04-22 00:00:00'}]

        :param string:
        :return: dict
        """
        return self.__class__(
            arrow.get(pyunit_time.Time(self.res_time_datetime).parse(string=string, **kwargs)[0]['keyDate']).datetime)
