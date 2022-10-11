# -*- coding:utf-8 -*-
# 文件:  gen_key.py
# 日期:  2022/9/8 12:01
import random
import string

__version__ = '1.0'
__all__ = ['jd_create_key', 'get_nonce']


def jd_create_key(size=32, start=2):
    """
    生成随机 key
    :param size:    长度，默认为32个字符
    :param start:   开始字符，1-数字， 2-字母
    :return:  只包含大写字母和数字，且字母 和 数字交替出现
    """
    arr = []
    max_letter = 3
    cur_max = random.randint(1, max_letter)
    cnt = 0
    who = start  # 1-数字， 2-字母
    while len(arr) < size:
        if who == 1:
            i = random.randint(0, 9)
            arr.append(str(i))
        else:
            i = random.randint(0, 25)
            arr.append(chr(65 + i))
        cnt += 1
        if cnt >= cur_max:
            cnt = 0
            cur_max = random.randint(1, max_letter)
            who = 1 if who == 2 else 2
    
    return "".join(arr)


def get_nonce(size=16):
    """
    生成随机字符串
    :param size:    字符串长度默认为16,
    :return:  字符包括大小写字母 和 数字
    """
    nonce = ''.join(random.sample(string.ascii_letters + string.digits, size))
    return nonce


if __name__ == '__main__':
    print(jd_create_key())
