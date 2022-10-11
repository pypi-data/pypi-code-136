# -*- coding:utf-8 -*-
# src/jd_parse.py


__all__ = [
    'JdParse'
]


class JdParse(object):

    @staticmethod
    def remove_comment(s):
        # 去除 s 字符串中的 注释： /**/，支持 一行中有多个注释
        r = ''
        begin = 0
        p = 0
        len_max = len(s)

        while p < len_max:
            while p < len_max and s[p] != r'/':     # 找到 字符 '/'
                p += 1
            if p >= len_max:
                break

            p += 1
            if p >= len_max:
                break

            if s[p - 1] != r'/':
                p += 1
                continue

            if s[p] == '*':     # 如果 '/' 后面的字符 是 '*'，说明为 注释开始
                r += s[begin: p - 1]

                p += 1
                end = False
                while not end and p < len_max:
                    while p < len_max and s[p] != '*':      # 继续找 注释结尾 '*/'
                        p += 1
                    if p >= len_max:
                        break

                    if s[p] != '*':
                        p += 1
                        continue

                    p += 1
                    if p >= len_max:
                        break

                    if s[p] == r'/':
                        p += 1
                        begin = p
                        end = True
            else:
                r += s[begin: p]
                begin = p
        r += s[begin: len_max]

        return r
