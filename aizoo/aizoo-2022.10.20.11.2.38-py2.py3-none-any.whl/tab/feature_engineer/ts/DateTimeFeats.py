#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : iWork.
# @File         : DateTimeFeat
# @Time         : 2019-06-13 23:16
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :


from meutils.pipe import *


class DateTimeFeats(object):
    """
    pandas_utils 时间/日期特征工程
    常见格式：
        1. 时间戳
        2. 时间字符串

    # 很强大: 解析不出为空
    pd.to_datetime(ts, 'coerce', unit='s', infer_datetime_format=True)
    """

    def __init__(self, feats=None):
        """利用python获取某年中每个月的第一天和最后一天

        :param feats: {
                "year", "quarter", "month", "day", "hour", "minute", "second",
                "week", "weekday",  # week==weekofyear== .dt.isocalendar().week
                "day_of_year",
                "days_in_month",  # 月的天数

                # bool
                'is_month_end',
                'is_month_start',
                'is_quarter_end',
                'is_quarter_start',
                'is_year_end',
                'is_year_start',
                'is_leap_year',

                # 自定义
                "monthweek",  # 获取指定的某天是某个月的第几周

            }
        """

        self.feats = feats
        if feats is None:
            self.feats = (
                "year", "quarter", "month", "day", "hour", "minute", "second",
                "week", "weekday",  # week==weekofyear== .dt.isocalendar().week
                "day_of_year",
                "days_in_month",  # 月的天数

                # bool
                'is_month_end',
                'is_month_start',
                'is_quarter_end',
                'is_quarter_start',
                'is_year_end',
                'is_year_start',
                'is_leap_year',
                'is_weekend',  #
                'is_holiday',  #
                'is_in_lieu',  #
                'is_special_day',  #

                # 自定义
                "monthweek",  # 获取指定的某天是某个月的第几周
                'solar_terms',  # 节气
                'holiday_name',  #
                'day_part',  # 拆分为早中晚

            )

    def transform(self, s: pd.Series):
        assert s.dtypes == 'datetime64[ns]'

        df = s.to_frame()
        for feat in tqdm(self.feats, "🕛"):
            if hasattr(s.dt, feat):
                _ = s.dt.__getattribute__(feat)
            else:
                _ = self.__getattribute__(feat)(s)

            if _.dtypes == 'bool':
                _ = _.astype(int)

            df[f"{s.name}_{feat}"] = _

        return df

    def timestamp2date(self, ts):
        return pd.to_datetime(ts, 'coerce', unit='s', infer_datetime_format=True)

    def datestr2date(self, ts):
        try:
            _ = ts.astype('datetime64[ns]')
        except Exception as e:
            print(f"astype('datetime64[ns]'): {e}")
            _ = pd.to_datetime(ts, 'coerce', infer_datetime_format=True)
        return _

    @staticmethod
    def monthweek(ts: pd.Series):
        """
        获取指定的某天是某个月的第几周
        周一为一周的开始
        实现思路：就是计算当天在本年的第y周，本月一1号在本年的第x周，然后求差即可。
        """
        e = ts.dt.strftime("%W").astype(int)
        b = (ts - pd.to_timedelta(ts.dt.day - 1, 'day')).dt.strftime("%W").astype(int)
        return e - b + 1

    @staticmethod
    def is_weekend(s: pd.Series):
        return s.dt.dayofweek >= 5

    @staticmethod
    def is_holiday(s: pd.Series):  # 法定节假日
        from chinese_calendar import is_holiday, is_workday, is_in_lieu, get_holiday_detail, get_solar_terms

        return s.map(is_holiday)

    @staticmethod
    def is_in_lieu(s: pd.Series):  # 调休日
        from chinese_calendar import is_holiday, is_workday, is_in_lieu, get_holiday_detail, get_solar_terms

        return s.map(is_in_lieu)

    @staticmethod
    def solar_terms(s: pd.Series):  # 节气
        from chinese_calendar import is_holiday, is_workday, is_in_lieu, get_holiday_detail, get_solar_terms

        _ = lru_cache(256)(lambda x: get_solar_terms(x, x))

        return s.map(_).str[-1]

    @staticmethod
    def holiday_name(s: pd.Series):
        from chinese_calendar import is_holiday, is_workday, is_in_lieu, get_holiday_detail, get_solar_terms

        # 或者在判断的同时，获取节日名
        _ = lru_cache(256)(lambda x: get_holiday_detail(x)[1])  # on_holiday, holiday_name

        return s.map(_)

    @staticmethod
    def is_special_day(s: pd.Series):
        """双十一等等"""  # todo
        special_days = {
            '06-18', '08-18', '11-11'
        }
        pattern = "|".join(special_days)
        return s.astype(str).str.contains(pattern)

    @staticmethod
    def day_part(s: pd.Series):
        @lru_cache(32)
        def f(hour):
            if hour in [4, 5]:
                return "dawn"
            elif hour in [6, 7]:
                return "early morning"
            elif hour in [8, 9, 10]:
                return "late morning"
            elif hour in [11, 12, 13]:
                return "noon"
            elif hour in [14, 15, 16]:
                return "afternoon"
            elif hour in [17, 18, 19]:
                return "evening"
            elif hour in [20, 21, 22]:
                return "night"
            elif hour in [23, 24, 1, 2, 3]:
                return "midnight"
            else:
                return np.nan

        return s.dt.hour.map(f)


if __name__ == '__main__':
    import pandas as pd

    ts = pd.date_range('2022-10-01', '2022-10-30', freq='h').to_series()
    print(DateTimeFeats(['day_part']).transform(ts))
