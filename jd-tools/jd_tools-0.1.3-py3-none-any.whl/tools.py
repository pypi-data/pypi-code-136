# -*- coding: utf8 -*-
# 文件:  tools.py
# 日期:  2021/10/7 14:02
"""
DATE        AUTHOR  DESCRIPTION
----------  ------  -----------------------------------------------------------------
2022-07-02  WXG     JdTools.str_to_datetime 支持格式 RFC 3339 , 版本改为 2.1
"""
import time
import datetime
import calendar
import os
import operator
import re
import xlrd
from PIL import Image
import qrcode
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation, DecimalException


__version__ = '2.4'

__all__ = [
    'dc_gen_code', 'dc_records_changed', 'start_end_time', 'start_end_time_ex',
    'JdCalendar', 'JdTools', 'JdDate', 'JdImage', 'JdList', 'JdPath', 'JdFmt',
    'DT_YM', 'DT_SHORT', 'DT_LONG_LESS', 'DT_LONG', 'DT_FULL',
    'DT_MD', 'DT_FULL_EX', 'DT_FULL_EX2',
    'name_list', 'sum_list', 'sum_ticket', 'Singleton', 'humanize_date_delta',
    'singleton'
]


def dc_gen_code(school_no, tag, date=None):
    """
    生成单据编号，包括学号，班级编号，收费单号等。
    :param school_no:       分校编号，例如：0001,0002
    :param tag:             单据标识，例如学号为 XH， 收费单为 SFD
    :param date:            日期，单据上附加日期信息
    :return:        生成的编号, 例如 0001-XH-181008-       [完整单据号：0001-XH-181008-001]
    """
    if date is None:
        date = datetime.datetime.today()
    data_str = datetime.datetime.strftime(date, '%y%m%d-')
    code_str = '%04d-%s-%s' % (int(school_no), tag, data_str)
    return code_str


def dc_records_changed(old: list, new: list, field='id'):
    """修改记录（全量）， 判断在原纪录基础上的删、改、增情况。
       var aa = [{id: 1, name:'Tom'},{id:2, name:'Peter'}]; 原始记录
       var bb = [{name:'Alice'}, {id:2, name: 'PP'}];       最终记录。
       var chg = dc_records_changed(aa, bb, 'id')
       则需要增加bb中的第一条，修改为bb中第二条，删除aa中第一个条。
       返回值为 {add:[0], del:[0], upd:[1]}
    :param old:     原始记录 [{}, {}]
    :param new:     修改后的记录  [ {}, {}]
    :param field:   比较字段，用于判断增、改、删
    :return:    {'add': list, 'del': list, 'upd': list}
        add -- new 中 下标
        upd -- new 中 下标
        del -- old 中 下标
    """
    add_idx = []
    del_idx = []
    upd_idx = []
    upd_idx_old = []    # old update index
    ori = set()
    cur = set()

    for i in old:
        if field in i:
            ori.add(i[field])
    for i in range(len(new)):
        if field in new[i]:
            cur.add(new[i][field])
        else:
            add_idx.append(i)
    del_key = ori.difference(cur)
    upd_key = ori.intersection(cur)
    add_key = cur.difference(ori)

    # 找出 del_key, upd_key, add_key  对应的下标
    for i in range(len(old)):
        if field in old[i] and old[i][field] in del_key:
            del_idx.append(i)
    for i in range(len(new)):
        if field in new[i] and new[i][field] in upd_key:
            upd_idx.append(i)
            for j in range((len(old))):
                if field in old[j] and old[j][field] == new[i][field]:
                    upd_idx_old.append(j)   # 记录 old 中 和 new 对应 key 的索引
    for i in range(len(new)):
        if field in new[i] and new[i][field] in add_key:
            add_idx.append(i)

    return {'add': add_idx, 'del': del_idx, 'upd': upd_idx, 'upd_old': upd_idx_old}


def start_end_time(tm, val=None):
    """
    返回 日期 tm，对应的开始和结束日期
    :param tm:  日期名：today, yesterday, this-week, last-week, this-month, last-month,
                    year-month, time_range
    :param val:  日期字符串， 当为 year-month 时： 年-月。 time_range时：年-月-日 - 年-月-日
    :return: 开始日期 和 结束日期
    """
    one_day = datetime.timedelta(hours=23, minutes=59, seconds=59, microseconds=999999)
    if tm == 'year-month':      # 按照 年 月 查询
        ym = val.split('-')     # 年-月： 2019-09
        year = int(ym[0])
        month = int(ym[1])
        d1 = datetime.datetime(year=year, month=month, day=1)
        month_range = calendar.monthrange(year, month)
        d2 = d1 + datetime.timedelta(days=month_range[1]-1) + one_day
    elif tm == 'today':     # 今天
        td = datetime.date.today()
        d1 = datetime.datetime.strptime(str(td), '%Y-%m-%d')
        d2 = d1 + one_day
    elif tm == 'yesterday':
        td = datetime.date.today()
        d1 = datetime.datetime.strptime(str(td), '%Y-%m-%d') - datetime.timedelta(days=1)
        d2 = d1 + one_day
    elif tm == 'this-week':
        cal = JdCalendar()
        # cal.set_monday_is_first(False)
        d1, d2 = cal.this_week()
    elif tm == 'last-week':
        cal = JdCalendar()
        # cal.set_monday_is_first(False)
        d1, d2 = cal.last_week()
    elif tm == 'this-month':
        cal = JdCalendar()
        d1, d2 = cal.this_month()
    elif tm == 'last-month':
        cal = JdCalendar()
        d1, d2 = cal.last_month()
    elif tm == 'time_range':
        times = val.split(' - ')
        if len(val) <= 17:  # val 格式 2020-01 - 2020-12
            ym = times[0].split('-')
            d1 = datetime.datetime(year=int(ym[0]), month=int(ym[1]), day=1)
            ym = times[1].split('-')
            d = datetime.datetime(year=int(ym[0]), month=int(ym[1]), day=1)
            month_range = calendar.monthrange(int(ym[0]), int(ym[1]))
            d2 = d + datetime.timedelta(days=month_range[1] - 1) + one_day
        else:   # val 格式 2019-11-01 - 2019-11-17
            d1 = datetime.datetime.strptime(JdTools.trim(times[0]), '%Y-%m-%d')
            d2 = datetime.datetime.strptime(JdTools.trim(times[1]), '%Y-%m-%d') + one_day
    else:
        d1 = datetime.datetime.strptime(tm, '%Y-%m-%d')
        d2 = d1 + one_day
    return d1, d2


def start_end_time_ex(tm, val=None):
    """
    返回 日期 tm，对应的开始和结束日期，带时间段描述
    :param tm:  日期，见 start_end_time
    :param val: 日期字符串， 当为 year-month 时： 年-月。 time_range时：年-月-日 - 年-月-日
    :return:  开始日期, 结束日期, 开始到结束日期的文字描述
    """
    d1, d2 = start_end_time(tm, val)
    if d1.date() == d2.date():  # 今天或者昨天的时间段
        date_from_to = '%s' % (JdTools.date_ymd(d1))
    else:
        date_from_to = '从 %s 至 %s' % (JdTools.date_ymd(d1), JdTools.date_ymd(d2))
    return d1, d2, date_from_to


class JdCalendar(object):
    def __init__(self, date_time=None, monday_is_first=True):
        self.date_time = date_time if date_time else datetime.datetime.today()
        self.date = datetime.datetime.strptime(str(self.date_time.date()), '%Y-%m-%d')
        self.iso_weekday = self.date.isoweekday()
        self.weekday = self.date.weekday()
        self.one_day = datetime.timedelta(hours=23, minutes=59, seconds=59, microseconds=999999)
        self.monday_is_first = monday_is_first

    def last_week(self):
        date_to = self.date - datetime.timedelta(days=self.iso_weekday)
        date_from = date_to - datetime.timedelta(days=6)
        date_to += self.one_day
        if self.monday_is_first is False:
            date_from -= datetime.timedelta(days=1)
            date_to -= datetime.timedelta(days=1)
        return date_from, date_to

    def this_week(self):
        date_from = self.date - datetime.timedelta(days=self.iso_weekday-1)
        date_to = date_from + self.one_day + datetime.timedelta(days=6)
        if self.monday_is_first is False:
            date_from -= datetime.timedelta(days=1)
            date_to -= datetime.timedelta(days=1)
        return date_from, date_to

    def set_monday_is_first(self, is_first=True):
        self.monday_is_first = is_first

    def this_month(self):
        year = self.date.year
        month = self.date.month
        date_from = datetime.datetime(year, month, 1, 0, 0, 0)
        month_range = calendar.monthrange(year, month)
        date_to = date_from + datetime.timedelta(days=month_range[1] - 1) + self.one_day
        return date_from, date_to

    def last_month(self):
        month = 12 if self.date.month == 1 else self.date.month - 1
        year = self.date.year if month != 12 else self.date.year - 1
        date_from = datetime.datetime(year, month, 1, 0, 0, 0)
        month_range = calendar.monthrange(year, month)
        date_to = date_from + datetime.timedelta(days=month_range[1] - 1) + self.one_day
        return date_from, date_to


# 日期格式
DT_YM = 5  # 年-月
DT_SHORT = 1  # 年-月-日 y4-mm-dd
DT_LONG_LESS = 3  # 年-月-日 时:分 y4-mm-dd HH:MM
DT_LONG = 2  # 年-月-日 时:分:秒 y4-mm-dd HH:MM:SS
DT_FULL = 4  # 年-月-日 时:分:秒.毫秒 y4-mm-dd HH:MM:SS.ms
DT_MD = 6       # 月-日 mm-dd
DT_FULL_EX = 12  # 年月日-时分秒-毫秒
DT_FULL_EX2 = 13  # 年月日_时分秒_毫秒


class JdTools(object):
    """工具类，实现常用函数"""
    @staticmethod
    def getdate():
        """获取当前日期字符串 返回 年-月-日_时分秒 例如：2018-09-21_084800"""
        date = datetime.datetime.today()
        data_str = datetime.datetime.strftime(date, '%Y-%m-%d_%H%M%S')
        return data_str

    @staticmethod
    def get_date():
        """获取当前日期字符串 返回 年-月-日_时分秒毫秒 例如：2018-09-21_084800_458394"""
        date = datetime.datetime.today()
        data_str = datetime.datetime.strftime(date, '%Y-%m-%d_%H%M%S_%f')
        return data_str

    @staticmethod
    def trim(s):
        """过滤字符串首尾空格，例如   '  Hello World  ' ->  'Hello World' """

        """
        s = s.strip()
        """
        space = [' ', '\t', '\n', '\r']
        if not isinstance(s, str) and not isinstance(s, bytes):
            return s
        while s and s[0] in space:
            s = s[1:]
        while s and s[-1] in space:
            s = s[:-1]

        return s

    @staticmethod
    def split(s, sep, num=-1):
        """分割字符串，并过滤首尾空格 """
        if not isinstance(s, str) and not isinstance(s, bytes):
            return s
        arr = s.split(sep, num)
        arr = [JdTools.trim(i) for i in arr]
        return arr

    @staticmethod
    def str2arr(s):  # 字符串（用英文逗号分隔） 转 列表。 例如：'1,2,3' -> [1, 2, 3]， 字符串非法，不报错
        if not isinstance(s, str) and not isinstance(s, bytes):
            return []
        arr = JdTools.split(s, ',')
        ret = []
        for i in arr:
            passed, v = JdTools.int(i)
            if passed:
                ret.append(v)
        return ret

    @staticmethod
    def get_year_month(str_date):
        """从字符串获取年和月份， str_date 字符串格式 '年-月-日 时:分:秒' """
        arr = str_date.split('-')
        if len(arr) < 2:
            raise Exception('str_date 格式错误，期望【年-月-日 时:分:秒】')
        year = int(arr[0])
        month = int(arr[1])
        return year, month

    @staticmethod
    def float_equal(f1, f2, precision=1e-5):
        """判断浮点数 f1 和 f2 是否相等。precision 为比较精度，默认为 1e-5 (10的-5次方) """
        if f1 is None and f2 is None:   # 都为None 返回 True
            return True
        if f1 is None or f2 is None:    # 只有一个是 None，返回 False
            return False
        return abs(float(f1)-float(f2)) <= precision

    @staticmethod
    def get_year_month_day(str_date):
        """从字符串获取年和月份和日， str_date 字符串格式 '年-月-日 时:分:秒' """
        arr = str_date.split('-')
        if len(arr) < 3:
            raise Exception('str_date 格式错误，期望【年-月-日 时:分:秒】')
        return arr[0], arr[1], arr[2]

    @staticmethod
    def list_eq(x, y):
        return operator.eq(x, y)    # Python 3  True or False

    @staticmethod
    def get_filename(name, excel2010=False, no_ext=False, no_ms=False):
        """
        返回 唯一 文件名，name 后面增加 年月日_时分秒_毫秒 后缀
        :param name:        文件名前缀
        :param excel2010:   excel文件后缀格式， True-4位后缀文件扩展名， False - xls
        :param no_ext:      不带文件名后缀
        :param no_ms:       文件名不带毫秒
        :return:    文件名 name + 日期 + 扩展名
        """
        tm = datetime.datetime.today()
        fmt = '_%Y%m%d_%H%M%S' if no_ms else '_%Y%m%d_%H%M%S_%f'
        time_str = datetime.datetime.strftime(tm, fmt)
        return name + time_str + ('' if no_ext else ('.xls' + ('x' if excel2010 else '')))

    @staticmethod
    def str(val):
        """ int to str， val 为 [0, 9]时 返回 '01', '02', ..., '09' """
        if not isinstance(val, int):
            raise Exception('JdTools.str expect int.')
        v = '0' + str(val) if 0 <= val <= 9 else str(val)
        return v

    @staticmethod
    def get_end_time(begin, minutes):
        """
        上课开始时间，上课时长，转 开始结束时间

        :param begin:       上课开始时间，例如 09:00
        :param minutes:     上课时长，单位分钟，例如 90
        :return:    开始时间-结束时间，例如：09:00-10:30
        """
        if isinstance(minutes, float):
            minutes = int(minutes)

        arr = begin.split('-')
        b = arr[0].split(':')

        h = int(b[0]) + minutes // 60
        m = int(b[1]) + minutes % 60
        if m >= 60:
            h += 1
            m -= 60
        begin_end_time = arr[0] + "-" + JdTools.str(h) + ":" + JdTools.str(m)
        return begin_end_time

    @staticmethod
    def is_float(val):
        """判断 val是否可以转为float。可以转换，返回True，不能转换，返回False"""
        try:
            float(val)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def float(val):
        """将val转为float。转换成功，返回 True 和 转换后的值；转换失败，返回 False, 0"""
        try:
            v = float(val)
            return True, v
        except (ValueError, TypeError):
            return False, 0

    @staticmethod
    def int(val, default=0):
        """将val转为 int。转换成功，返回 True 和 转换后的值；转换失败，返回 False, 0"""
        try:
            v = int(val)
            return True, v
        except (ValueError, TypeError):
            return False, default

    @staticmethod
    def get_user_code(code):
        """格式化用户（操作员）编号"""
        return 'USER-%03d' % int(code)

    @staticmethod
    def get_float(v, num=2, force=False):
        """ float to str,  保留2位小数。当 force 不填/'假', 小数点后全是0（是整数），则转换为整数（不带小数点）"""
        # 123.3456 --> '123.35';    180 -> '180'

        if v is None:  # 兼容性处理
            v = 0
            if not force:
                return v
        elif isinstance(v, str):
            _, v = JdTools.float(v)
        fmt_dot = '{:.%sf}' % num       # '{:.2f}'.format(v)  === '%.2f' % v
        val = fmt_dot.format(v)

        if force:
            return val
        '''
        c = val[-1]
        while c == '0':  # 消除 小数点 末尾 的 0
            val = val[: -1]
            c = val[-1]
        if val[-1] == '.':  # 对于整数，删除 小数点
            val = val[: -1]
        '''
        arr = val.rsplit('.')
        if arr[1] == '0'*num:
            val = arr[0]
        return val

    @staticmethod
    def get_float2(v):
        """返回字符串，带小数点后2位"""
        return JdTools.get_float(v, 2, True)

    @staticmethod
    def money_fmt(v):
        return float(JdTools.get_float(v, 2))

    @staticmethod
    def format_salary(fee, count_method, has_auth=True, num=None, stu_fee=None):
        """
        教师工资算法转字符串，转换结果示例：  100元/人 or 100元/节
        :param fee:     工资算法收费标准，单位 元
        :param count_method:    工资计费方式， 1 每节课固定 2 按学生人头  3-按创收比率计算  4 课次+人头 5-单次阶梯, 6-月带课数阶梯
        :param has_auth:    是否有权限，无权限时，屏蔽 fee 的值
        :param num:    当 count_method=4时，有效。超过人数
        :param stu_fee:    当 count_method=4时，有效。人头费
        :return:  fee对应的数值 元/人 or 元/节。 若 fee, count_method 其中一个为None，则返回 None
        """
        if fee is None or count_method is None:
            return None
        f = JdTools.get_float(fee)
        std = f if has_auth else '*' * len(f)
        if count_method == 1:
            text = '%s元/节' % std
        elif count_method == 2:
            text = '%s元/人' % std
        elif count_method == 3:
            text = '创收%s%%' % std
        elif count_method == 4:
            head = JdTools.get_float(stu_fee)
            head_std = head if has_auth else '*' * len(head)
            text = '%s元/节+%s元/人(>%s人)' % (std, head_std, num)
        elif count_method == 5:
            text = '单次阶梯算法'
        elif count_method == 6:
            text = '月带课数阶梯算法'
        else:
            text = None
        return text

    @staticmethod
    def str_to_datetime(s_dt, add_hms=False):
        """
        字符串 转 日期， datetime.datetime 格式

        RFC 3339格式：“{年}-{月}-{日}T{时}:{分}:{秒}.{毫秒}{时区}”；
        其中的年要用零补齐为4位，月日时分秒则补齐为2位。毫秒部分是可选的。
        最后一部分是时区，前面例子中的 Z 其实是零时区 Zulu 的缩写，它也可能是 +08:00 或 -08:00 等；
        2017-12-08T00:00:00.00Z
        2017-12-08T08:00:00.00+08:00
        都代表所在时区的本地时间。
        ISO8610与RFC3339有各自独特的表示法，也有重合部分。
        :param s_dt:    日期字符串
        :param add_hms: 转换后是否添加时分秒
        :return:
        """
        if isinstance(s_dt, (datetime.datetime, datetime.date)):
            return s_dt

        now = datetime.datetime.today()
        dt = datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)

        if s_dt == '' or s_dt is None:
            return None
        length = len(s_dt)
        has_dot = True if '.' in s_dt else False

        fmt = '%Y-%m-%d'
        if length <= 7:
            fmt = '%Y-%m'
        elif length <= 10:
            if has_dot:
                fmt = '%Y.%m.%d'
            elif '/' in s_dt:
                fmt = '%Y/%m/%d'
            else:
                fmt = '%Y-%m-%d'
        elif length <= 16:
            fmt = '%Y-%m-%d %H:%M'
        elif length <= 19:
            fmt = '%Y-%m-%d %H:%M:%S'
        elif 'T' in s_dt and '+08:00' in s_dt:  # '2015-05-20T13:29:35+08:00' rfc3339 标准格式 北京时间2015年05月20日13点29分35秒
            fmt = '%Y-%m-%dT%H:%M:%S%z'
            if has_dot:
                fmt = '%Y-%m-%dT%H:%M:%S.%f%z'
        elif has_dot:
            fmt = '%Y-%m-%d %H:%M:%S.%f'
        date_time = datetime.datetime.strptime(s_dt, fmt)

        # 添加 时分秒
        if add_hms and len(s_dt) <= 10:
            date_time += dt
        return date_time

    @staticmethod
    def str_to_time(s):
        """
        字符串 转 时间。
        s 格式：HH:MM:SS， 格式一点都不能错
        """
        if not s:
            return None
        if isinstance(s, datetime.time):
            return s
        return datetime.time.fromisoformat(s)

    @staticmethod
    def datetime_to_str(dt, fmt=DT_SHORT):
        """
        日期转 字符串
        :param dt:  要转换的日期 为 datetime 类型
        :param fmt: 转换格式    DT_SHORT = 1  # 年-月-日 y4-mm-dd
        :return:  成功返回转换后的字符串。 输入为None时，返回None
        """
        if dt is None or dt == '':
            return None
        fmt_str = '%Y-%m-%d'
        if fmt == DT_SHORT:
            fmt_str = '%Y-%m-%d'
        elif fmt == DT_LONG:
            fmt_str = '%Y-%m-%d %H:%M:%S'
        elif fmt == DT_LONG_LESS:
            fmt_str = '%Y-%m-%d %H:%M'
        elif fmt == DT_FULL:
            fmt_str = '%Y-%m-%d %H:%M:%S.%f'
        elif fmt == DT_FULL_EX:
            fmt_str = '%Y%m%d-%H%M%S-%f'
        elif fmt == DT_FULL_EX2:
            fmt_str = '%Y%m%d_%H%M%S_%f'
        elif fmt == DT_YM:
            fmt_str = '%Y-%m'
        elif fmt == DT_MD:
            fmt_str = '%m-%d'

        someday = datetime.datetime.strftime(dt, fmt_str)
        return someday

    @staticmethod
    def date_ymd(dt):
        return JdTools.datetime_to_str(dt, DT_SHORT)

    @staticmethod
    def date_to_str(dt):
        if isinstance(dt, datetime.datetime):
            val = datetime.datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
        elif isinstance(dt, datetime.date):
            val = datetime.date.strftime(dt, '%Y-%m-%d')
        elif isinstance(dt, datetime.time):
            val = datetime.time.strftime(dt, '%H:%M:%S')
        else:
            return dt
        return val

    @classmethod
    def int_to_date(cls, n, str_out=True):
        if isinstance(n, int) and 0 < n < 70000:
            d = datetime.datetime(1900, 1, 1) + datetime.timedelta(days=n-2)
            if str_out:
                d = cls.datetime_to_str(d)
            return d
        return None

    @staticmethod
    def time_to_datetime(t, dt=None):
        """ 日期字符串 转化为 datetime，例如 "09:00" 转为 "2019-11-18 09:00:00"，日期是当天 """
        n = dt or datetime.datetime.now()
        h = int(t.split(':')[0])
        m = int(t.split(':')[1])
        return datetime.datetime(year=n.year, month=n.month, day=n.day, hour=h, minute=m, second=0)

    @staticmethod
    def get_code(no=None, tag=None, school_no=None, date=None, hyphen=True,
                 no_width=3, school_width=4, full=False):
        """生成单据编号，包括学号，班级编号，收费单号等。

        :param no:              单据顺序号
        :param tag:             单据标识，例如学号为 XH， 收费单为 SF
        :param school_no:       分校编号，例如：0001,0002
        :param date:            日期，单据上附加日期信息。False，不带日期
        :param hyphen:          是否显示短横'-'
        :param no_width:        no 占用宽度，默认为3
        :param school_width:    分校编号占用宽度，默认为4
        :param full:            true: 日期格式为 年4月日时分秒。 false， 默认， 年2月日
        :return:        生成的编号, 例如 0001-XH-181008-001
        """
        fmt_no = '{:0%sd}' % (no_width or 3)
        fmt_sch = '{:0%sd}-' % (school_width or 4)

        fmt_date = '%y%m%d-' if not full else '%Y%m%d%H%M%S-'
        if date is None:
            date = datetime.datetime.today()
        data_str = datetime.datetime.strftime(date, fmt_date) if date is not False else ''
        sch_str = fmt_sch.format(int(school_no)) if school_no else ''
        tag_str = ('%s-' % tag) if tag else ''
        no_str = fmt_no.format(int(no)) if no is not None else ''
        code_str = '%s%s%s%s' % (sch_str, tag_str, data_str, no_str)
        if not hyphen:
            code_str = code_str.replace('-', '')
        return code_str

    @staticmethod
    def utc2local(utc_st):
        """
        UTC时间转本地时间（+8:00）
        :param utc_st:          utc datetime
        :return:                local datetime
        """
        now_stamp = time.time()
        local_time = datetime.datetime.fromtimestamp(now_stamp)
        utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
        offset = local_time - utc_time
        local_st = utc_st + offset
        return local_st

    @staticmethod
    def local2utc(local_st):
        """
        本地时间转UTC时间（-8:00）
        :param local_st:        local datetime
        :return:                utc datetime
        """
        time_s = time.mktime(local_st.timetuple())
        utc_st = datetime.datetime.utcfromtimestamp(time_s)
        return utc_st

    @staticmethod
    def find_sub_str(string, sub, n):
        """查找字符串中子串第 n 次出现的位置索引
        :param string:   被查找字符串
        :param sub:     子串
        :param n:       第 n 次出现的位置， 从 1 开始
        :return:        子串 第 n 次出现位置的索引。若没有则返回 -1
        """
        arr = string.split(sub, n)
        if len(arr) <= n:
            return -1
        return len(string) - len(arr[-1]) - len(sub)

    @staticmethod
    def is_date(string, fmt=1):
        """
        判断输入字符串 是否 为 日期格式
        :param string:  要校验的字符串
        :param fmt:     日期类型， 2 DT_LONG(默认): yyyy-MM-dd hh:mm:ss，1 DT_SHORT : yyyy-MM-dd， 5 DT_YM: yyyy-MM
        :return: True 符合日期格式， False，不符合
        """
        if fmt == 1:  # yyyy-MM-dd
            pt = r"^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
        elif fmt == 5:  # yyyy-MM
            pt = r"^[1-9]\d{3}-(0[1-9]|1[0-2])$"
        else:   # default 2  # yyyy-MM-dd hh:mm:ss
            pt = r'^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$'
        m = re.match(pt, string)
        # print(m)
        return m is not None

    @staticmethod
    def get_between_year_month(first_day, end_day):
        """
        根据开始日期和结束，获取中间月份
        :param first_day:      开始月份
        :param end_day:        结束年月
        :return:
        """
        date_arr = []
        months = (end_day.year - first_day.year) * 12 + end_day.month - first_day.month
        month_range = ['%s-%s' % (first_day.year + mon // 12, mon % 12 + 1)
                       for mon in range(first_day.month - 1, first_day.month + months)]
        for rec in month_range:
            year, month = JdTools.get_year_month(rec)
            # 将每个月末考勤日期存入数组
            if month != 12:
                end_day = datetime.datetime(year, month + 1, 1)
            else:
                end_day = datetime.datetime(year+1, 1, 1)
            end_day = end_day - datetime.timedelta(seconds=1)
            date_arr.append(end_day)
        return date_arr

    @staticmethod
    def is_birthday(days, date):
        # date 对应日期 是否进行生日提醒。 提前天数 为 days。
        today = datetime.date.today()
        end = today + datetime.timedelta(days=days)
        m = date.month
        d = date.day

        if today.month == end.month:    # 同一个月
            if m == today.month and today.day <= d <= end.day:
                return True
        elif today.month < end.month:   # 跨月
            if (m == today.month and d >= today.day) or (m == end.month and d <= end.day) \
                    or today.month < m < end.month:
                return True
        else:   # today.month > end.month   # 跨年情况
            if (m == today.month and d >= today.day) or (m == today.month, d >= today.day) \
                    or m > today.month or m < end.month:
                return True

        return False

    @staticmethod
    def get_birthday_diff(days, bd):
        # 比较今天距离生日日期间隔是否在 days 的天数内，如果是，返回间隔天数，否则返回-1
        y = datetime.date.today().year
        diff = -1
        if bd and isinstance(bd, (datetime.date, datetime.datetime)):
            d = (datetime.date(year=y, month=bd.month, day=bd.day) - datetime.date.today()).days
            if 0 <= d <= days:
                diff = d
        return diff

    @staticmethod
    def del_key(obj, key):
        try:
            del obj[key]
        except KeyError:
            pass

    @staticmethod
    def del_keys(obj, *args):
        for k in args:
            try:
                del obj[k]
            except KeyError:
                pass

    @staticmethod
    def list_remove(lst, e):
        try:
            lst.remove(e)
        except ValueError:
            pass

    @staticmethod
    def set_remove(obj, e):
        try:
            obj.remove(e)
        except KeyError:
            pass

    @staticmethod
    def excel_to_datetime(value):
        """
        excel 日期 (float) 转 日期格式:  40861.0 -> 2011-11-14 0:0:0

        使用 xlrd 从 excel 读取出日期后会变成一个 float 数值，比如  40861.5。
        其中整数部分表示 从 1900-1-1开始经过的天数。 1 -- 1900-1-1； 2 -- 1900-1-2
        小数部分表示 时间。24小数制。 0.5 -- 12:00:00, 0.15 -- 03:36:00
        24 * 60 * 60 = 86400(秒)

        :param value:   float, excel 读取的 日期值
        :return: 日期类型 datetime
        """
        if isinstance(value, str):
            _, value = JdTools.float(value)
        date = xlrd.xldate.xldate_as_datetime(value, 0)
        return date

    @staticmethod
    def name_phone(name, phone):
        # 获取学员 姓名、手机号 组成的 新名称。若 phone 为 None, ''，则不显示手机号
        _phone = (' (%s)' % JdTools.mask_phone(phone)) if phone else ''
        tip = '%s%s' % (name, _phone)
        return tip

    @staticmethod
    def mask_phone(phone):
        if phone:
            if len(phone) <= 4:
                _phone = phone
            else:
                _phone = phone[0:2] + '**' + phone[-4:]
        else:
            _phone = ''
        return _phone

    @staticmethod
    def check_id_card(id_card):
        """身份证验证"""
        area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古",
                "21": "辽宁", "22": "吉林", "23": "黑龙江", "31": "上海", "32": "江苏",
                "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东",
                "41": "河南", "42": "湖北", "43": "湖南", "44": "广东", "45": "广西",
                "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南",
                "54": "西藏", "61": "陕西", "62": "甘肃", "63": "青海", "64": "宁夏",
                "65": "新疆", "71": "台湾", "81": "香港", "82": "澳门", "91": "国外"}
        id_card = str(id_card)
        id_card = id_card.strip()

        # 地区校验
        key = id_card[0: 2]  # 地区中的键是否存在
        if key not in area.keys():
            return False, '身份证地区非法！'
        # 15位身份号码检测

        if len(id_card) == 15:
            if (int(id_card[6:8]) + 1900) % 4 == 0 or \
                    ((int(id_card[6:8]) + 1900) % 100 == 0 and (int(id_card[6:8]) + 1900) % 4 == 0):
                re_str = '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|'
                re_str += '(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$'
                erg = re.compile(re_str)  # // 测试出生日期的合法性
            else:
                re_str = '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|'
                re_str += '(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$'
                erg = re.compile(re_str)  # // 测试出生日期的合法性
            if re.match(erg, id_card):
                return True, None
            else:
                return False, '身份证号码出生日期超出范围或含有非法字符！'
        # 18位身份号码检测
        elif len(id_card) == 18:
            # 出生日期的合法性检查
            # 闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
            # 平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
            if int(id_card[6:10]) % 4 == 0 or (int(id_card[6:10]) % 100 == 0 and int(id_card[6:10]) % 4 == 0):
                re_str = '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])'
                re_str += '|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$'
                erg = re.compile(re_str)  # // 闰年出生日期的合法性正则表达式
            else:
                re_str = '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])'
                re_str += '|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$'
                erg = re.compile(re_str)  # // 平年出生日期的合法性正则表达式
            # 测试出生日期的合法性
            if re.match(erg, id_card):
                return True, None
            else:
                return False, '身份证号码出生日期超出范围或含有非法字符！'
        else:
            return False, '身份证号码位数不对！'

    @staticmethod
    def compare_time(time1, time2):
        """
        判断 两个时间段时间是否冲突
        :param time1:   时间段1, 例如 time1 = '08:00-09:00'
        :param time2:   时间段2，例如 time2 = '08:30-09:30'
        :return: 冲突返回 False, 不冲突，返回 True

        例：time1 = '08:00-09:00'
            time2 = '08:30-09:30'
            返回False
        """
        arr1 = time1.split('-')
        h1 = arr1[0].split(':')  # 开始时间
        h2 = arr1[1].split(':')  # 结束时间
        begin_time1 = int(h1[0]) * 100 + int(h1[1])  # 开始时间整数形式
        end_time1 = int(h2[0]) * 100 + int(h2[1])  # 结束时间整数形式
        arr2 = time2.split('-')
        h1 = arr2[0].split(':')  # 开始时间
        h2 = arr2[1].split(':')  # 结束时间
        begin_time2 = int(h1[0]) * 100 + int(h1[1])  # 开始时间整数形式
        end_time2 = int(h2[0]) * 100 + int(h2[1])  # 结束时间整数形式
        if end_time2 > begin_time1 and end_time1 > begin_time2:
            return False
        return True

    @staticmethod
    def decimal(number, result=False, pt=2):
        """将number数值转换为decimal类型，支持数值类型：int,str,float
            改为 四舍五入方式 ROUND_HALF_UP。 默认为 ROUND_HALF_EVEN 四舍六入，五平均（前一位是偶数时进位）
            result = True, 返回  number, 成功标识
            result = False, 返回  number
        """
        success = True
        exp = Decimal('0.' + pt * '0')
        if number == '' or number is None:      # 容错处理： None, ''(空串), 返回 0
            number = 0
        elif isinstance(number, float):
            number = Decimal.from_float(number).quantize(exp, rounding=ROUND_HALF_UP)
        elif isinstance(number, int):
            number = Decimal(number)
        elif isinstance(number, str):
            try:
                number = Decimal(number).quantize(exp, rounding=ROUND_HALF_UP)
            except (InvalidOperation, DecimalException):
                success = False
        elif isinstance(number, Decimal):
            number = number.quantize(exp, rounding=ROUND_HALF_UP)
        else:
            success = False

        if result:  # 需要返回是否转换成功结果时
            return number, success
        else:
            return number

    @staticmethod
    def decimal_check(number, pt=2):
        """对 JdTools.decimal 返回值进行 颠倒， 返回  (判断结果，number)"""
        n, check = JdTools.decimal(number, True, pt)
        return check, n

    @staticmethod
    def create_qrcode(content, center_img=None):
        """创建二维码
        content     str     创建二维码的内容
        center_img  str     中心图片，可选
        """
        qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
        qr.add_data(content)
        qr.make(fit=True)

        img = qr.make_image()
        img = img.convert("RGBA")
        if center_img and os.path.isfile(center_img):
            icon = Image.open(center_img)  # 这里是二维码中心的图片
            img_w, img_h = img.size
            factor = 4
            size_w = int(img_w / factor)
            size_h = int(img_h / factor)

            icon_w, icon_h = icon.size
            if icon_w > size_w:
                icon_w = size_w
            if icon_h > size_h:
                icon_h = size_h
            icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

            # 先添加白色框，比 logo 图标 大
            white_w = icon_w + 20
            white_h = icon_h + 20
            w = int((img_w - white_w) / 2)
            h = int((img_h - white_h) / 2)
            new_image = Image.new('RGBA', (white_w, white_h), (255, 255, 255))  # 生成白色图像
            img.paste(new_image, (w, h), new_image)

            w = int((img_w - icon_w) / 2)
            h = int((img_h - icon_h) / 2)
            icon = icon.convert("RGBA")
            img.paste(icon, (w, h), icon)
        return img

    @staticmethod
    def file_type(suffix, _type=0):
        """用于判断文件后缀是否在允许范围内
        suffix:  文件后缀名 例： jpg
        _type: 文件类型 0-图片 1-视频 2-待增加 默认为0
        """
        img_type = ['png', 'gif', 'jpg', 'jpeg', 'ico', 'bmp']  # 图片格式
        video = ['mpg', 'mpeg', 'avi', 'rm', 'rmvb', 'mov', 'wmv', 'asf', 'dat', 'mp4']  # 视频格式
        if _type == 0:  # 判断图片后缀是否在允许范围内
            if suffix not in img_type:
                return False
        elif _type == 1:  # 视频
            if suffix not in video:
                return False
        else:  # 其他
            return False
        return True

    @staticmethod
    def this_week(page=0, today=None):
        """通过星期，获取一周范围内日期 从星期一到星期日
            page:  翻页 默认为 0 本页
                   正数 例：1 下一周 2 下下周
                   负数 例：-1 上一周 2 上上周
            today: 当前日期 预留字段
        """
        if today is None:
            today = datetime.date.today()
        dates = {}  # 当前周 周一到周日日期集合
        week_day = today.weekday() + 1  # 当前星期
        one_day = datetime.timedelta(days=1)  # 一天
        if page > 0:  # 当前周之后
            today = today + ((7 * page) * one_day)
        elif page < 0:  # 当前周之前
            today = today + ((7 * page) * one_day)
        for i in range(1, 8):
            date = today - ((week_day - i) * one_day)
            dates[i] = date
        return dates

    @staticmethod
    def this_week2(page=0, today=None, num=None):
        """通过星期，获取一周范围内日期 从当天开始连续7天之内的星期
            page:  翻页 默认为 0 本页
                   正数 例：1 下一周 2 下下周
                   负数 例：-1 上一周 2 上上周
            today: 当前日期 预留字段
        """
        if today is None:
            today = datetime.date.today()
        dates = {}  # 当前周 周一到周日日期集合
        one_day = datetime.timedelta(days=1)  # 一天
        if page > 0:  # 当前周之后
            today = today + ((num * page) * one_day)
        elif page < 0:  # 当前周之前
            today = today + ((num * page) * one_day)
        for i in range(1, 8):
            date = today + (i * one_day)
            weekday = date.weekday() + 1
            dates[weekday] = date
        return dates

    @staticmethod
    def assign(out_dict, **kwargs):
        """对字典 out_dict 赋值， 按 kwargs 中 k， v。示例：

        d = {m: 3}
        assign(d, times=1, fee=100, m=2, n=None)
            d  => {times: 1, fee: 100, m:5, n: 0}
        """
        for k, v in kwargs.items():
            out_dict[k] = (v or 0) + (out_dict.get(k) or 0)

    @staticmethod
    def assign_ex(out_dict, **kwargs):
        """对字典 out_dict 赋值， 按 kwargs 中 k， v。示例：
        原来字典中 None值的key，若未累加，保持 None 值不变

        d = {m: 3, x: None}
        assign(d, times=1, fee=100, m=2, x=0, y=None)
            d  => {times: 1, fee: 100, m:5, x: None}
        """
        for k, v in kwargs.items():
            if not v:  # 输入为 0 或者 None，不做计算
                continue
            out_dict[k] = (v or 0) + (out_dict.get(k) or 0)

    @staticmethod
    def nested(out_dict, *args):
        """字典 out_dict 嵌套赋值， 按 args 中 v 逐级嵌套。 示例：

        d = {}, class_id = 10, student_id = 900
        nested(d, class_id, student_id)
        d  => {10: {900: {} } }
        """
        d = out_dict
        for v in args:
            if v not in d:
                d[v] = {}
            d = d[v]

    @staticmethod
    def calculate_age(born):
        # 根据生日获得其年龄，born 参数为 datetime.date 类型
        # 周岁年龄 = 当前年份 - 出生日期年份。周岁年龄又称实足年龄，指从出生到计算时为止，共经历的周年数或生日数。
        #
        # 例如，1990年7月1日零时进行人口普查登记，一个1989年12月15日出生的婴儿，按虚岁计算是2岁，实际刚刚6个多月，
        # 还未过一次生日，按周岁计算应为不满1周岁，即0岁。
        # 周岁年龄比虚岁年龄常常小1～2岁，它是人口统计中常用的年龄计算方法。周岁—出生时为0岁，每过一个公历生日长1岁。
        today = datetime.date.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError:
            # raised when birth date is February 29
            # and the current year is not a leap year
            birthday = born.replace(year=today.year, day=born.day - 1)
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    @staticmethod
    def int2time_str(n):
        """int转时间字符串，如800 -> 8:00,  未校验 分钟超过 59分的异常情况 """
        if isinstance(n, int) and 0 <= n < 2400:
            return '%02d:%02d' % (n // 100, n % 100)
        return None

    @staticmethod
    def time_str2int(s):
        """时间字符串转int，如8:00转800"""
        if isinstance(s, str) and ':' in s:
            list_ = s.split(':')
            try:
                h = int(list_[0])
                m = int(list_[1])
            except ValueError:
                return None
            if 0 <= h < 24 and 0 <= m <= 59:
                output = h * 100 + m
                return output
        return None

    @staticmethod
    def int2datetime(n, date: datetime.datetime = None):
        """int转datetime类型，日期为当天，如800 -> datetime.datetime(2021, 11, 5, 8, 0)"""
        if isinstance(n, int) and 0 <= n < 2400:
            now = date if date else datetime.datetime.now()
            h = n // 100
            m = n % 100
            output = datetime.datetime(now.year, now.month, now.day, h, m)
            return output

        return None

    @staticmethod
    def obj_from_key(obj: dict, key: str):
        """ 从 对象 obj 中取出 key 所对应的对象
            例如 key = 'show' 返回  obj['show']
            例如 key = 'program.show' 返回  obj['program']['show']
        """
        if key == '':
            return obj
        arr = key.split('.')
        o = obj

        for i in arr:
            o = o.get(i)
        return o

    @staticmethod
    def fen2yuan(s):
        """分转为元，微信支付专用
        :param s: 数字字符串，微信返回，单位为“分”
        :return yuan: Decimal类型，单位“元”
        """
        _, fen = JdTools.int(s)
        yuan = JdTools.decimal(fen / 100)
        return yuan

    @staticmethod
    def yuan2fen(yuan) -> int:
        """元 转 分"""
        return int(yuan * 100)

    @staticmethod
    def copy_dict(obj: dict, *args):
        # 安全拷贝 字典。将 字典 obj 中 选中的 key 生成新的字典
        out = {}
        d = obj
        for v in args:
            if v in d:
                out[v] = d[v]
        return out


class JdDate(object):
    """日期相关工具函数"""
    days = [31, ]

    @staticmethod
    def get_date(str_date, day=1):
        """获取 datetime.date 日期， str_date 格式为 年-月 or 年-月-日  字符串"""
        y, m = JdTools.get_year_month(str_date)
        start_date = datetime.date(y, m, day)
        return start_date

    @staticmethod
    def get_datetime(str_date, day=1):
        """获取 datetime.datetime 日期， str_date 格式为 年-月 or 年-月-日 字符串"""
        y, m = JdTools.get_year_month(str_date)
        start_date = datetime.datetime(y, m, day)
        return start_date

    @staticmethod
    def next_day(date):
        """获取 datetime.datetime 日期 的后一天， 返回 datetime """
        n = date + datetime.timedelta(days=1)
        m = datetime.datetime(year=n.year, month=n.month, day=n.day)
        return m

    @staticmethod
    def last_day_of_month(any_day):
        """
        获取一个月中的最后一天
        :param any_day: 任意日期    datetime.datetime, or datetime.date
        :return: string
        """
        next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # 确保到下一个月
        d = next_month - datetime.timedelta(days=next_month.day)
        if isinstance(d, datetime.datetime):
            d += datetime.timedelta(hours=23-d.hour, minutes=59-d.minute, seconds=59-d.second)
        return d

    @staticmethod
    def last_time_of_day(date: datetime.datetime) -> datetime.datetime:
        """获取某天的 23:59:59"""
        return datetime.datetime(date.year, date.month, date.day, 23, 59, 59)

    @staticmethod
    def begin_time_of_day(date: datetime.datetime) -> datetime.datetime:
        """获取某天的 00:00:00"""
        return datetime.datetime(date.year, date.month, date.day, 00, 00, 00)

    @staticmethod
    def year_month(date):
        """从 日期 对象返回 年-月 字符串 """
        if isinstance(date, (datetime.datetime, datetime.date)):
            month = '%d-%02d' % (date.year, date.month)
            return month
        return '<日期格式错误>'

    @staticmethod
    def prev_month(date):
        """ 1. 获取 月份字符串 2019-08 的前一个月： 2019-07
            2. date 为 datetime时， 返回值也是 datetime
        """
        return JdDate.month_dist(date, -1)

    @staticmethod
    def month_dist(date, month_num):
        """ 1. 获取 月份字符串 2019-08 的前/后 month_num 月： -1, 2019-07; 2, 2019-10
               month_num 正数，向后 偏移月份； 负数，向前
            2. date 为 datetime时， 返回值也是 datetime
        """
        if isinstance(date, str):
            y, m = JdTools.get_year_month(date)
        else:
            y = date.year
            m = date.month
        m += month_num - 1
        y += m // 12    # 计算 年份偏移
        m = m % 12 + 1

        if isinstance(date, str):
            month = '%d-%02d' % (y, m)
        else:
            month = datetime.datetime(year=y, month=m, day=1)
        return month

    @staticmethod
    def check_date(param, field, name):
        """
        校验日期格式是否正确。
        :param param:       被校验 对象 dict
        :param field:       字段，dict[field]必须存在
        :param name:        field 的 中文名称。用于错误提示
        :return:  {code: 错误码， msg： 错误提示}
        """
        # ERR_DATE_FMT = 200
        # ERR_DATE_FMT_MSG = '“%s”格式错误【%s】，期望 年-月-日！'
        tip = '“%s”格式错误【%s】，期望 年-月-日！'
        date = param.get(field)
        if isinstance(date, int):   # xlrd 读取日期格式的单元格。xls格式为 2， xlsx格式为 3（在读取时，已经转为日期）
            if date > 2958465 or date < 1:   # 日期范围 1990/01/01 - 9999/12/31
                return {'code': 200, 'msg': '输入日期【{}】不在正常范围内'.format(date)}
            d1 = xlrd.xldate.xldate_as_datetime(date, 0)
            date = d1
        try:
            param[field] = JdTools.str_to_datetime(date)
        except (ValueError, TypeError):
            return {'code': 200, 'msg': tip % (name, date)}
        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def verify_date(obj, **kwargs):
        """
        校验日期格式是否正确。
        :param obj:         被校验 对象, dict
        :param kwargs:      被校验字段，dict, {字段名称='中文字段名称'}
        :return:    {code: 错误码， msg： 错误提示}
        """
        tip = '“%s”格式错误【%s】，期望 年-月-日！'
        for k, v in kwargs.items():
            dt = obj.get(k)
            try:
                obj[k] = JdTools.str_to_datetime(dt)
            except (ValueError, TypeError):
                return {'code': 200, 'msg': tip % (v, dt)}
        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def month_num(month, num):
        # 返回 月，月数 对应 字符串。 month: str, 起始月，例如 '2019-10', num: int 月数
        if num == 1:
            return month
        else:
            end = JdDate.month_dist(month, num)
            return '%s到%s共%s月' % (month, end, num)

    @staticmethod
    def start_end_time(tm, val=None):
        try:
            d1, d2 = start_end_time(tm, val)
        except (AttributeError, ValueError, TypeError):
            return {'code': 600, 'msg': f'日期格式错误【{tm} {val}】'}

        if d1.date() == d2.date():  # 今天或者昨天的时间段
            date_from_to = '%s' % (JdTools.date_ymd(d1))
        else:
            date_from_to = '从 %s 至 %s' % (JdTools.date_ymd(d1), JdTools.date_ymd(d2))
        return {'code': 0, 'msg': 'ok', 'd1': d1, 'd2': d2, 'date_from_to': date_from_to}

    @staticmethod
    def is_leap_year(y):
        # 判断输入年 y 是否为公历闰年（满足以下任意条件： 1. 能被400整除，2. 能被4整除，不能被100整除）
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            return True
        return False

    @staticmethod
    def days_distant(m, d):
        # 判断 公历日期 月-日 (m-d) 和 “今天”的日期差。
        # 将 m-d 转换为 今年的日期。注意闰年
        today = datetime.date.today()
        y = today.year
        # 公历闰年 2-29
        if m == 2 and d == 29 and not JdDate.is_leap_year(y):
            d = (datetime.date(year=y, month=3, day=1) - today).days  # 公历 2-29日生日，在平年的3-1日作为生日
        else:
            d = (datetime.date(year=y, month=m, day=d) - today).days
        return d

    @staticmethod
    def get_dates_by_times(start_day, end_day):
        """根据开始日期、结束日期返回这段时间里所有天的集合"""
        result = []
        date_start = datetime.datetime.strptime(start_day, '%Y-%m-%d')
        date_end = datetime.datetime.strptime(end_day, '%Y-%m-%d')
        result.append(date_start.strftime('%Y-%m-%d'))
        while date_start < date_end:
            date_start += datetime.timedelta(days=1)
            result.append(date_start.strftime('%Y-%m-%d'))
        return result

    @staticmethod
    def get_hours_list():
        """返回最近24小时时间字符串列表，时间格式为 %Y-%m-%d %H"""
        now = datetime.datetime.now()
        value = []
        begin = 0
        while begin <= now.hour:
            if begin < 10:
                begin_str = '0' + str(begin)
            else:
                begin_str = str(begin)
            value.append(now.strftime('%Y-%m-%d' + ' ' + begin_str))
            begin += 1
        max_hour = 23
        s = 24 - len(value)
        if s:
            yesterday = (now.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
            while s:
                if max_hour < 10:
                    begin_str = '0' + str(max_hour)
                else:
                    begin_str = str(max_hour)
                value.insert(0, yesterday + ' ' + begin_str)
                max_hour -= 1
                s -= 1
        return value

    @staticmethod
    def equal(a, b):
        # 日期是否相同， 忽略 毫秒
        if isinstance(a, datetime.datetime) and isinstance(b, datetime.datetime):
            return a.year == b.year and a.month == b.month and a.day == b.day \
                   and a.hour == b.hour and a.minute == b.minute and a.second == b.second

        return False


class JdImage(object):
    """图片处理公共类"""

    @staticmethod
    def resize(infile, outfile=None, width=1280):
        """
        修改图片尺寸
        :param infile:  原始图片， 路径+文件，必须存在
        :param outfile: 修改后的图片，不填写，则覆盖原始图片
        :param width:   修改后的宽度，默认 1280
        :return: 无
        """
        im = Image.open(infile)
        (x, y) = im.size  # read image size
        _, width = JdTools.int(width, 1280)
        if x <= width:  # 原始图片小于调整后的 图片宽度，则不做调整
            return
        x_s = width     # define standard width
        y_s = int(y * x_s / x)  # calc height based on standard width
        out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
        out.save(outfile or infile)


class JdFmt(object):
    """格式化类"""

    @staticmethod
    def has_power(val, has_power=True):
        """是否有权限，显示 val， 若 has_power==True，则显示 val，否则显示 **** """
        return val if has_power else ('****' if val else 0)

    @staticmethod
    def discount_rate(val):
        # 转换折扣率  val float 小数点4位，转 百分比，保留小数点后2位
        v = ''
        if val:
            v = '%s' % JdTools.get_float2(val * 100) + '%'
        return v


class JdList(object):
    @staticmethod
    def index(lst, el):
        try:
            idx = lst.index(el)
        except ValueError:
            idx = -1
        return idx


class JdPath(object):
    @staticmethod
    def slash(url):
        url_new = url.replace('\\', '/')  # 将 反斜杠替换为 斜杠， 防止 url 打不开的问题。
        return url_new


def name_list(class_list, key='class_name'):
    """ 提取列表元素中的班级名称，过滤空值和重复值，返回字符串"""
    classes = set()
    for r in class_list:
        class_name = r.get(key)
        if class_name:
            classes.add(class_name)
    return '，'.join(list(classes))


def sum_ticket(class_receipt, arr='ticket', key='fee'):
    """提取列表元素 some_list(数组中数组) 中的现金券总面值"""
    s = 0
    for r in class_receipt:
        s += sum_list(r[arr], key)
    return s


def sum_list(some_list, *key):
    """提取列表元素 some_list 中的现金券总面值"""
    s = 0
    for r in some_list:
        for kk in key:
            s += r.get(kk) or 0
    return s


class Singleton(type):
    # 单例模式，用法  class YourClass(metaclass=Singleton):
    def __init__(cls, *args, **kwargs):
        cls.instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


# 通过装饰器实现
def singleton(cls):
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


def humanize_date_delta(start, end):
    """
    将时间差转换为友好格式，如“7天”，“3个月”，“2年”， end > start，否则返回 空''
    :param start:     起始时间，datetime.datetime 或 datetime.date
    :param end:       结束时间，datetime.datetime 或 datetime.date
    :return:          转换结果，string
    """
    if not isinstance(start, datetime.date) or not isinstance(end, datetime.date):
        return ''

    if isinstance(start, datetime.datetime):
        start = start.date()
    if isinstance(end, datetime.datetime):
        end = end.date()

    days = (end - start).days
    if days <= 0:  # 结束时间早于或等于开始时间的情况
        return ''

    if days < 30:
        return f'{days}天'
    elif 30 <= days < 365:
        months = days // 30
        return f'{months}个月'
    else:  # days >= 365
        years = days // 365
        return f'{years}年'
