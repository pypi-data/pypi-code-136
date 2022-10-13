# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   PytestAssertError
# FileName:     pytest_assert_error_plugin.py
# Author:      Jakiro
# Datetime:    2022/10/13 19:17
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--change_assert",
        action="store",
        default="off",
        help="'Default 'off' for change, option: on or off"
    )


def pytest_assertrepr_compare(op, left, right):
    if op == '==':
        if not isinstance(right, type(left)):
            return [
                f'断言错误，期望结果与实际结果的数据类型不一致， 期望数据类型为:{type(right)} 实际值为:{type(left)}',
                f'期望值为：{right},实际值为：{left}'
            ]
        else:
            return [
                f'断言错误，期望值与实际值不一致，期望值为：{right}实际值为：{left}'
            ]

    if op == 'in':
        if isinstance(right, set) or isinstance(right, tuple) or isinstance(right, list):
            if isinstance(right, set):
                return [
                    f'断言错误，期望{left}为集合{right}的一个元素，实际上集合{right}中没有{left}元素'
                ]
            elif isinstance(right, tuple):
                return [
                    f'断言错误，期望{left}为元祖{right}的一个元素，实际上元祖{right}中没有{left}元素'
                ]
            elif isinstance(right, list):
                return [
                    f'断言错误，期望{left}为列表{right}的一个元素，实际上列表{right}中没有{left}元素'
                ]

        elif isinstance(right, str) and isinstance(left, str):
            return [
                f'断言错误，期望{left}是{right}的子串，实际{left}不是{right}的子串'
            ]

        elif isinstance(right, dict):
            return [
                f'断言错误，期望{left}是字典{right}的key列表{right.keys()}的一个key，实际字典{right}中没有值为{left}的key'
            ]
        else:
            return [
                f'期望 {left} 是 {right} 中的一部分，实际上 {left} 并不是 {right} 的一部分'
            ]

    if op == 'not in':
        if isinstance(right, set) or isinstance(right, tuple) or isinstance(right, list):
            if isinstance(right, set):
                return [
                    f'断言错误，期望{left}不是集合{right}的一个元素，实际上集合{right}中有{left}元素'
                ]
            elif isinstance(right, tuple):
                return [
                    f'断言错误，期望{left}不是元祖{right}的一个元素，实际上元祖{right}中有{left}元素'
                ]
            elif isinstance(right, list):
                return [
                    f'断言错误，期望{left}不是列表{right}的一个元素，实际上列表{right}中有{left}元素'
                ]

        elif isinstance(right, str) and isinstance(left, str):
            return [
                f'断言错误，期望{left}不是{right}的子串，实际{left}是{right}的子串'
            ]

        elif isinstance(right, dict):
            return [
                f'断言错误，期望{left}不是字典{right}的key列表{right.keys()}的一个key，实际字典{right}中有值为{left}的key'
            ]
        else:
            return [
                f'期望 {left} 不是 {right} 中的一部分，实际上 {left} 是 {right} 的一部分'
            ]

    if op == '>':
        if not isinstance(right, type(left)):
            return [
                f'断言错误，期望结果与实际结果的数据类型不一致， 期望数据类型为:{type(right)} 实际值为:{type(left)}',
                f'期望值为：{right},实际值为：{left}'
            ]
        else:
            return [
                f'断言错误，期望{left}大于{right},实际{left}不大于{right}'
            ]

    if op == '<':
        if not isinstance(right, type(left)):
            return [
                f'断言错误，期望结果与实际结果的数据类型不一致， 期望数据类型为:{type(right)} 实际值为:{type(left)}',
                f'期望值为：{right},实际值为：{left}'
            ]
        else:
            return [
                f'断言错误，期望{left}小于{right},实际{left}不小于{right}'
            ]

    if op == '>=':
        if not isinstance(right, type(left)):
            return [
                f'断言错误，期望结果与实际结果的数据类型不一致， 期望数据类型为:{type(right)} 实际值为:{type(left)}',
                f'期望值为：{right},实际值为：{left}'
            ]
        else:
            return [
                f'断言错误，期望{left}大于等于{right},实际{left}不大于等于{right}'
            ]

    if op == '<=':
        if not isinstance(right, type(left)):
            return [
                f'断言错误，期望结果与实际结果的数据类型不一致， 期望数据类型为:{type(right)} 实际值为:{type(left)}',
                f'期望值为：{right},实际值为：{left}'
            ]
        else:
            return [
                f'断言错误，期望{left}下于等于{right},实际{left}不小于等于{right}'
            ]

    if op == "!=":
        if not isinstance(right, type(left)):
            return [
                f'断言错误，期望结果与实际结果的数据类型不一致， 期望数据类型为:{type(right)} 实际值为:{type(left)}',
                f'期望值为：{right},实际值为：{left}'
            ]
        else:
            return [
                f'断言错误，期望值{left}与实际值{right}不相等,实际期望值{left}等于实际值{right}'
            ]
