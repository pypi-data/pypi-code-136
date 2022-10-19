# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pytest_advance
# FileName:     test_change_assert.py
# Author:      Jakiro
# Datetime:    2022/10/8 15:23
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

def test_4():
    assert 1 is 1


class TestClass23():
    def test_2(self):
        assert 1 == 1

    def test_3(self):
        assert 1 == 2

    def test_4(self):
        assert 1 in (3, 2)

    def test_5(self):
        assert 1 in [3, 2]

    def test_6(self):
        assert 1 in {3, 2}

    def test_7(self):
        assert 'a' in 'abc'

    def test_8(self):
        assert 1 > 2

    def test_9(self):
        assert 2 < 1

    def test_10(self):
        assert 2 <= 1

    def test_11(self):
        assert 1 >= 2

    def test_12(self):
        assert 1 != 2

    def test_13(self):
        assert 1 in {3: 2, 2: 1}


# class TestClass2():
#     def test_3(self):
#         assert 1 == 1
#
#     def test_4(self):
#         assert 1 == 2
