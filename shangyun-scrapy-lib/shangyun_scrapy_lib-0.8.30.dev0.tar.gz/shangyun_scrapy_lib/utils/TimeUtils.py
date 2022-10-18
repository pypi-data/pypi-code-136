import re
from datetime import datetime

import pytz
import arrow


def now():
    return pytz.timezone('Asia/Shanghai').localize(datetime.now())


# def parse_time(time_str: str, format: str = "%Y-%m-%d %H:%M:%S"):
#     parse_time = datetime.strptime(time_str, format)
#     return pytz.timezone('Asia/Shanghai').localize(parse_time)


def parse_timestamp(timestamp: int):
    bit = len(str(timestamp))
    if bit == 13:
        timestamp /= 1000
    elif bit == 15:
        timestamp /= 1000
    return datetime.fromtimestamp(timestamp, pytz.timezone('Asia/Shanghai'))


def parse_time(time_str: str, format: str = "%Y-%m-%d %H:%M:%S"):
    if "分钟前" in time_str:
        minutes = int(time_str.replace("分钟前", ""))
        time_str = arrow.now().shift(minutes=-minutes).format()
    elif "小时前" in time_str:
        hours = int(time_str.replace("小时前", ""))
        time_str = arrow.now().shift(hours=-hours).format()
    elif "天前" in time_str:
        day = int(time_str.replace("天前", ""))
        time_str = arrow.now().shift(day=-day).format()
    elif "昨天" in time_str:
        time_str = time_str.replace("昨天", arrow.now().shift(days=-1).format("YYYY-MM-DD "))
    elif "前天" in time_str:
        time_str = time_str.replace("前天", arrow.now().shift(days=-2).format("YYYY-MM-DD "))
    elif "月" in time_str and "日" in time_str:
        time_str = str(arrow.now().date().year) + "-" + time_str.replace("月", "-").replace("日", "")
    elif "年" in time_str and "月" in time_str and "日" in time_str:
        time_str = time_str.replace("年", "-").replace("月", "-").replace("日", "")
    elif time_str.isdigit():
        time_str = parse_timestamp(int(time_str))
    return arrow.get(time_str, tzinfo='Asia/Shanghai').astimezone(pytz.timezone('Asia/Shanghai'))


if __name__ == '__main__':
    # print(parse_time("1分钟前"))
    # print(parse_time("1小时前"))
    # print(parse_time("2020年8月11日 11:12"))
    # print(parse_time("2020年8月11日"))
    # print(parse_time("2020-8-11 11:12:10"))
    # print(parse_time("2020-8-11"))
    # print(parse_time("1655555556"))
    print(parse_time("昨天15:31"))
    print(parse_time("前天14:25"))
    print(parse_time("5月7日"))

