from random import randint
import re


def findstr(dic, text):
    res = []
    for key in dic:
        if re.search(text, key):
            res.append(key)
    return res


def randomitem(dic):
    key = list(dic.keys())[randint(0, len(dic)-1)]
    return key, dic[key]


def flat(dic):
    # 把字典裡的value，如果是list的話就全部展開，變成key值，如果不是list的話，就只是把value和key顛倒而已
    res = {}
    for key, value in dic.items():
        if isinstance(value, list) is True:
            res.update(dict.fromkeys(value, key))
        else:
            res[value] = key
    return res


def stack(dic):
    # 把有相同value的key值，全部把value當作key值，收攏每一個key值到list，是flat_dict的反向操作
    res = {}
    for key, value in dic.items():
        if value not in res:
            res[value] = []
        res[value].append(key)
    return res