# encoding: utf-8
"""
@project: djangoModel->valuation_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 计价生成服务
@created_time: 2022/10/13 9:40
"""

# 接口服务类
from ..utils.j_valuation import JExpression


class ValuationService:
    expression = None  # 表达式

    @staticmethod
    def valuate(rule_id=None, enroll_id=None, ):
        # 测试代码
        # 案例代码
        # 1.解析括号找到对应的括号，意义对应关系
        # 2.递归解析公式
        # 5+IF(
        #     ((IF(1 = 5, 5, 0) + ((3))) >= (1 + 3 + 4)),
        #     "号外号外",
        #     IF(2 >= 60, "及格", "不及格")
        # ) + SUM(1,2,5,7,8)
        expression_string = JExpression.parse_variables(
            "5+if(((IF(1 = 5, 5, 0)+((3)))>= (1 + 3 + 4)),'号外号外',IF(2 >= 60, '及格', '不及格')) + SUM(1,2,5,7,8)",
            {"a": 1, "b": 2, "c": 5}
        )
        calculator = JExpression()
        return calculator.process(expression_string)

        # # 初始化字典
        # query_obj = Enroll.objects.filter(id=enroll_id)
        # if query_obj:
        #     enroll = query_obj.first().to_json()
        # else:
        #     enroll = {}

        # # 获取计价规则
        # rule_query_set = EnrollRuleValuate.objects.filter(id=rule_id)
        # if rule_query_set:
        #     expression_string = rule_query_set.value("expression_string").first()
        # else:
        #     return None, "没有找到计价公式"
        # expression_string = JExpression.parse_variables(expression_string, enroll) # 如果需要 table2.filed,仅仅需要对input_dict就行修改即可
        # return JExpression().process
