# -*- coding: utf-8 -*-
# @Time    :2022/10/12 16:51
# @Author  :Sang Jiajun
# @Email   :jiajun_sang@outlook.com
# @File    :roman.py
def roman2integer(s):
    Num = 0
    n = len(s)
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(n - 1):
        if dic[s[i]] >= dic[s[i + 1]]:
            Num += dic[s[i]]
        else:
            Num -= dic[s[i]]
    return Num + dic[s[-1]]

THOUSANDS = ["", "M", "MM", "MMM"]
HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


def integer2roman(num):
    return THOUSANDS[num // 1000] + \
           HUNDREDS[num % 1000 // 100] + \
           TENS[num % 100 // 10] + \
           ONES[num % 10]

if __name__ == "__main__":
    print(integer2roman(24))