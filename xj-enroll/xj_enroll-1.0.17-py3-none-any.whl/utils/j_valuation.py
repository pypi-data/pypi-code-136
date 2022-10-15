# encoding: utf-8
"""
@project: djangoModel->j_valuation
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 计价服务类
@created_time: 2022/10/13 16:58
"""
import re


# 计算器基类
class JBaseExpression:
    __result = None  # 结果
    __expression = None
    fun_type = ""

    # 获取所有子类
    @staticmethod
    def get_child_info():
        try:
            return {getattr(i, "name"): i for i in JBaseExpression.__subclasses__() if getattr(i, "name", None)}, None
        except AttributeError:
            return None, "扩展类name属性可以重复"

    # 解析变量
    @staticmethod
    def parse_variables(expression_string, input_dict):
        if expression_string is None:
            return 0
        # 变量解析替换
        this_cell_value_match = re.compile("{{.*?}}").findall(str(expression_string))
        # 得到变量解析的键值对
        parsed_variable_map = {}
        for i in this_cell_value_match:
            parsed_variable_map.update({i: input_dict.get(i.replace("{{", "").replace("}}", ""), 0)})
        # 比那辆键值对替换
        for k, v in parsed_variable_map.items():
            expression_string = expression_string.replace(k, str(v))
        return expression_string

    # 解析括号，成对解析
    @staticmethod
    def parsed_brackets(expression):
        twain_index_map = {}
        forward_index_list = twain_index_list = []
        for char, index in zip(expression, range(len(expression))):
            if char == "(":
                forward_index_list.append(index)
            if char == ")":
                forward_bracket = forward_index_list.pop(-1)
                twain_index_map[forward_bracket] = (forward_bracket, index)

        return twain_index_list, twain_index_map


# 计算器
class JExpression(JBaseExpression):
    def process(self, expression_string):
        if expression_string is None:
            return "", None
        if not len(re.findall("\(", expression_string)) == len(re.findall("\)", expression_string)):
            return None, "语法错误，括号应该成对存在"
        child_class, err = self.get_child_info()
        if err:
            return None, err
        # 全部转换大写
        expression_string = expression_string.upper().replace(" ", "").replace("=", "==")
        # 解析括号和函数
        brackets_twain_index, brackets_twain_map = self.parsed_brackets(expression_string)
        for name, instance in child_class.items():
            for r in re.finditer(name, expression_string):
                name_start, name_end = r.span()
                bracket_start, bracket_end = brackets_twain_map[name_end]
                fun_str = expression_string[name_start:bracket_end + 1]
                result_str = instance().process(fun_str)
        result = CalculateExpression().process(expression_string)
        # 运行公式
        return result, None


# ================================= 公式封装类 =======================================
#  基础计算
class CalculateExpression(JBaseExpression):

    def process(self, expression_string):
        try:
            return eval(expression_string), None  # 加加减乘除
        except ZeroDivisionError:
            return 0, None  # 0/n  的情况
        except Exception as e:
            return expression_string, str(e)


# 布尔值判断、三元运算
class IFExpression(JBaseExpression):
    name = "IF"
    patt = "^IF\((.*?),(.*?),(.*?)\)&"

    # if(((if( a==5,5,0)+((3))) >= (1+3+4)), '号外号外', if(x>=60, '及格', '不及格'))

    def resolve(self, expression):
        pass

    def process(self, expression, *args, ):
        bool_expression, yes_expression, no_expression = expression.split(",")
        if bool_expression:
            return yes_expression
        else:
            return no_expression


# 求和计算、（多参数在服务中获取）
class SUMExpression(JBaseExpression):
    name = "SUM"
    patt = "SUM(.*?)"  # SUM(a,b,c) == a+b+c

    def process(self, expression):
        args = expression.split(",")
        result = 0
        for i in args:
            result += i
        return result
