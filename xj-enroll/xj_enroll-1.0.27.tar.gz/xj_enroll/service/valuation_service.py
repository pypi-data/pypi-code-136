# encoding: utf-8
"""
@project: djangoModel->valuation_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 计价生成服务
@created_time: 2022/10/13 9:40
"""

# 接口服务类
from ..models import Enroll, EnrollRuleValuate
from ..utils.j_valuation import JExpression


class ValuationService:
    expression = None  # 表达式

    @staticmethod
    def valuate(expression_string=None, input_dict={}):
        # 测试代码
        expression_string = JExpression.parse_variables(
            expression_string,
            input_dict
        )
        calculator = JExpression()
        data, err = calculator.process(expression_string)
        return data, err

    @staticmethod
    def enroll_valuate(enroll_id, rule_id):
        # 获取计价规则
        rule_query_set = EnrollRuleValuate.objects.filter(id=rule_id)
        if rule_query_set:
            expression_string = rule_query_set.value("expression_string").first()
        else:
            return None, "没有找到计价公式"

        # 初始化变量字典
        query_obj = Enroll.objects.filter(id=enroll_id)
        if query_obj:
            enroll_params_dict = query_obj.first().to_json()
        else:
            enroll_params_dict = {}

        # 计算公式
        expression_string = JExpression.parse_variables(
            expression_string,
            enroll_params_dict
        )
        calculator = JExpression()
        data, err = calculator.process(expression_string)
        return data, err
