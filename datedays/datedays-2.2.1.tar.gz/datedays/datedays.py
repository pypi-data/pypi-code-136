"""

@productname：PyCharm
@projectname：datedays
@filename：datedays
@time: 2022/8/5 15:00
@author：liang1024
@desc：

datedays

Python Date Tools

What can it do?
1. Get common date data
2. Operating excel report
3. Perform common encryption signature
4. Obtain the encrypted signature of the file

I hope it can help you
            --liang1024

"""
__email__ = "chinalzge@gmail.com"
__author__ = 'liang1024'

import base64
import calendar
import datetime
import random
import string
import time
import traceback
import uuid
from datetime import date
from urllib.parse import urlencode, quote, unquote

import openpyxl
import xlrd
from Cryptodome.Hash import MD5, SHA1, MD2, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512
from dateutil.relativedelta import relativedelta
from openpyxl import Workbook


def getnow(format_='%Y-%m-%d %H:%M:%S'):
    '''
    get current time

    :param format_: format
    :return:
    '''
    return time.strftime(format_, time.localtime(time.time()))


def gettomorrow(days=1):
    '''
    get tomorrow date

    :param days: today + future days
    :param mode:
    :return:
    '''
    return date.today() + relativedelta(days=days)


def getyesterday(days=1):
    '''
    get yesterday date

    :param days:today - past days
    :param mode:
    :return:
    '''
    return date.today() - relativedelta(days=days)


def getdays(number=3):
    '''
    get the required date quantity list, within 3 months by default

    :param number: Number of months generated
    :return: list
    '''
    _days = gettodaydays()
    for _ in range(1, number + 1):
        _days += getnextdays(next_months=_)
    return _days


def getasctime(t=None):
    '''

    :param t: specify timestamp
    :return: such as Wed Aug 17 08:54:46 2022
    '''
    if t:
        time.asctime(time.gmtime(t))
    return time.asctime()


def getnowtimestamp(t=1000):
    '''
    :param t:
    t=1 second
    t=1000 millisecond
    t=1000000 Microsecond

    :return: timestamp
    '''
    return int(round(time.time() * t))


def gettodaydays(today=None):
    '''
    obtain the remaining days of the specified month,
    if today is empty,
    the current remaining days will be obtained

    :param today:'%Y-%m-%d'
    :return:_list
    '''
    _list = []
    if today:
        _today = today.split('-')
        _year = int(_today[0])
        _month = int(_today[1])
        __day = int(_today[2])
    else:
        _today = date.today()
        _year = _today.year
        _month = _today.month
        __day = _today.day
    if _month < 10:
        _month = f'0{_month}'
    for _day in [i for i in range(__day, calendar.monthrange(_year, int(_month))[1] + 1)]:
        if _day < 10:
            _day = f'0{_day}'
        _list.append(f'{_year}-{_month}-{_day}')
    return _list


def getnextdays(today=None, next_months=1):
    '''
    return to the next month date list (automatically cross year)

    :param today: specified month '%Y-%m-%d'
    :param next_months:  Specify the interval of the month
    :return:_list
    '''
    _list = []
    if today:
        _today = today.split('-')
        _year = int(_today[0])
        _month = int(_today[1])
        next_month = date(_year, _month, 1) + relativedelta(months=next_months)
    else:
        next_month = date.today() + relativedelta(months=next_months)
    _year = next_month.year
    _month = next_month.month
    if _month < 10:
        _month = f'0{_month}'
    for _day in [i for i in range(1, calendar.monthrange(_year, int(_month))[1] + 1)]:
        if _day < 10:
            _day = f'0{_day}'
        _list.append(f'{_year}-{_month}-{_day}')
    return _list


def getstr2timestamp(date_str, format_='%Y-%m-%d %H:%M:%S'):
    '''
    string to timestamp

    :param date_str: such as 2022-08-17 16:34:24
    :param format_: such as %Y-%m-%d %H:%M:%S
    :return: timestamp
    '''
    return int(time.mktime(time.strptime(date_str, format_)))


def getcurrent_days(current_date=None):
    '''
    old function
    recommended datedays.gettodaydays()

    :param current_date:'%Y-%m-%d'
    :return:
    '''
    return gettodaydays(current_date)


def getnext_days(current_date=None, next_months=1):
    '''
    old function
    recommended datedays.getnextdays()

    :param current_date: '%Y-%m-%d'
    :param next_months:
    :return:
    '''
    return getnextdays(current_date, next_months)


def excel_write_openpyxl(filename, datas):
    '''
    openpyxl write excel
    support xls,xlsx...

    :param filename:
    :param datas: [[],[],[]]
    :return:
    '''
    try:
        openpyxl_wb = Workbook()
        openpyxl_ws = openpyxl_wb.active
        for i in datas:
            openpyxl_ws.append(i)
        openpyxl_wb.save(filename)
    except Exception:
        print(traceback.format_exc())
        return False
    return True


def excel_read_openpyxl(filename, sheet_index=0):
    '''
    openpyxl read excel
    not support xls

    :param filename:
    :param sheet_index:
    :return:
    '''
    datas = []
    try:
        wb = openpyxl.load_workbook(filename=filename)
        for item in [i for i in wb[wb.get_sheet_names()[sheet_index]].rows]:
            datas.append([str(i.value).replace("None", "") for i in item])
    except Exception:
        print(traceback.format_exc())
    return datas


def excel_read_xlrd(filename, sheet_index=0):
    '''
     xlrd read excel
     support xls,xlsx

    :param filename:
    :param sheet_index:
    :return:
    '''
    datas = []
    try:
        sh = xlrd.open_workbook(filename).sheet_by_index(sheet_index)
        for rx in range(sh.nrows):
            datas.append([str(i.value).replace("None", "") for i in sh.row(rx)])
    except Exception:
        print(traceback.format_exc())
    return datas


def md2(body, encode='utf-8'):
    '''
    MD2
    :param body:
    :param encode:
    :return:
    '''
    m = MD2.new()
    m.update(str(body).encode(encode))
    return m.hexdigest()


def md5(body, encode='utf-8', length_=32):
    '''
    MD5

    :param body:
    :param encode:
    :param length_:
    :return:
    '''
    m = MD5.new()
    m.update(str(body).encode(encode))
    if length_ == 16:
        return m.hexdigest()[8:-8]
    else:
        return m.hexdigest()


def sha1(body, encode='utf-8'):
    '''
    SHA1
    :param body:
    :param encode:
    :return:
    '''
    h = SHA1.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha2_224(body, encode='utf-8'):
    '''
    SHA2_224
    :param body:
    :param encode:
    :return:
    '''
    h = SHA224.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha2_256(body, encode='utf-8'):
    '''
    SHA2_256
    :param body:
    :param encode:
    :return:
    '''
    h = SHA256.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha2_384(body, encode='utf-8'):
    '''
    SHA2_384
    :param body:
    :param encode:
    :return:
    '''
    h = SHA384.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha2_512(body, encode='utf-8'):
    '''
    SHA2_512
    :param body:
    :param encode:
    :return:
    '''
    h = SHA512.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha3_224(body, encode='utf-8'):
    '''
    SHA3_224
    :param body:
    :param encode:
    :return:
    '''
    h = SHA3_224.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha3_256(body, encode='utf-8'):
    '''
    SHA3_256
    :param body:
    :param encode:
    :return:
    '''
    h = SHA3_256.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha3_384(body, encode='utf-8'):
    '''
    SHA3_384
    :param body:
    :param encode:
    :return:
    '''
    h = SHA3_384.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def sha3_512(body, encode='utf-8'):
    '''
    SHA3_512
    :param body:
    :param encode:
    :return:
    '''
    h = SHA3_512.new()
    h.update(str(body).encode(encode))
    return h.hexdigest()


def __encrypt_getmode__(mode):
    '''
    get encrypt mode

    :param mode:
    :return:
    '''
    mode = str(mode).upper()
    if 'SHA1' in mode:
        m = SHA1.new()
    elif 'SHA224' in mode:
        m = SHA224.new()
    elif 'SHA256' in mode:
        m = SHA256.new()
    elif 'SHA384' in mode:
        m = SHA384.new()
    elif 'SHA512' in mode:
        m = SHA512.new()
    elif 'SHA3_224' in mode:
        m = SHA3_224.new()
    elif 'SHA3_256' in mode:
        m = SHA3_256.new()
    elif 'SHA3_384' in mode:
        m = SHA3_384.new()
    elif 'SHA3_512' in mode:
        m = SHA3_512.new()
    else:
        m = MD5.new()
    return m


def encrypt_smallfile(filename, mode='md5'):
    '''
    encrypt smallfile
    default MD5 encrypt

    :param filename:
    :param mode:
    :return:
    '''
    m = __encrypt_getmode__(mode)
    with open(filename, 'rb') as f:
        m.update(f.read())
    return m.hexdigest()


def encrypt_bigfile(filename, mode, buffer=8192):
    '''
    encrypt bigfile
    default MD5 encrypt

    :param filename:
    :param mode:
    :param buffer:
    :return:
    '''
    m = __encrypt_getmode__(mode)
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(buffer)
            if not chunk:
                break
            m.update(chunk)
    return m.hexdigest()


def sleep(seconds=1, max_=None):
    '''
    random sleep

    :param seconds:default 1 seconds
    :param max_:
    :return:
    '''
    if max_:
        seconds = random.random() * max_

    print(f" random sleep：{seconds} seconds!")
    time.sleep(seconds)


def getuuid(mode=4, merge=False, **kwargs):
    '''
    get uuid

    :param mode:
    :param merge: replace('-', '')
    :param kwargs:
    :return:
    '''
    if mode == 1:
        u = uuid.uuid1(**kwargs)
    elif mode == 3:
        u = uuid.uuid3(**kwargs)
    elif mode == 5:
        u = uuid.uuid5(**kwargs)
    else:
        u = uuid.uuid4()
    if merge:
        return str(u).replace('-', '')
    return u


def getrandompassword(k=12, more_characters=None, _=string.ascii_letters + string.digits):
    '''
    randomly generated password
    default 12 bits

    recommended more_characters !@#$%.*&+-

    :param k: length
    :param more_characters: recommended   !@#$%.*&+-
    :param _: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+0123456789
    :return:
    '''
    if more_characters:
        _ += more_characters
    if k > len(_):
        k = len(_)
    return ''.join(random.sample(_, k))


def gettimestamp2str(timestamp):
    '''
    timestamp to string

    :param timestamp:  such as 1660726667690
    :return: %Y-%m-%d %H:%M:%S
    '''
    return datetime.datetime.fromtimestamp(float(timestamp))


def base64_encode(s, urlsafe=False):
    if urlsafe:
        return base64.urlsafe_b64encode(s)
    return base64.b64encode(s)


def base64_decode(s, urlsafe=False):
    if urlsafe:
        return base64.urlsafe_b64decode(s)
    return base64.b64decode(s).decode('utf-8')


def urlencodes(body):
    if isinstance(body, dict):
        return urlencode(body)
    return quote(str(body))


def urldecodes(body):
    return unquote(body)


def getstartend(start_date, end_date=date.today(), list_=False):
    '''
    get interval days or days list

    :param start_date: %Y-%m-%d
    :param end_date: %Y-%m-%d , default today
    :param list_: datelist
    :return:
    '''

    s_ = [int(_) for _ in str(start_date).split('-')]
    e_ = [int(_) for _ in str(end_date).split('-')]
    s_d = date(s_[0], s_[1], s_[2])
    days = (date(e_[0], e_[1], e_[2]) - s_d).days
    if list_:
        return [(s_d + datetime.timedelta(days=_)).strftime('%Y-%m-%d') for _ in range(days + 1)]
    return days


def headers2dict(headers_string):
    '''
    copy headers string convert dict
    :param headers_string:
    :return:
    '''
    _dict = {}
    if headers_string:
        for h in [h if len(h) == 2 else None for h in [h.split(':', 1) for h in headers_string.splitlines()]]:
            if h:
                _dict[h[0].strip()] = h[1].strip()
    return _dict


if __name__ == '__main__':
    print(headers2dict('''
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    Pragma: no-cache
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
    X-Requested-With: XMLHttpRequest
    '''))
