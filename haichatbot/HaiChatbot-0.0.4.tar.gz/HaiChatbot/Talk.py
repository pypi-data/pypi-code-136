# -*- coding: utf-8 -*-
# @Time : 2022/9/9 14:33
# @Author : Wang Hai
# @Email : nicewanghai@163.com
# @Code Specification : PEP8
# @File : Talk.py
# @Project : HaiHai

class Talk:

    @staticmethod
    def talk():
        while True:
            others_words = input()
            print("好的，知道了{}".format(others_words))

