# -*- coding:utf-8 -*-
# 文件:  jd_check.py
from .validate import verify
from ..tools import JdTools
from .errcode import *


class JdCheck(object):
    """
    输入参数校验， 用于 web 请求参数校验
    """
    @staticmethod
    def verify(obj, **kwargs):  # 参数校验， 用法说明，请参考 verify 函数
        return verify(obj, **kwargs)

    # =========================================================================
    # 以下校验方式 兼容 旧项目使用， 新项目请统一使用 verify
    # =========================================================================

    @staticmethod
    def decimal(obj, field, description, pt=2):
        """
        校验 obj[field] 是否可以转成 Decimal， 且 小数点 后面的位数 为 pt
        若转换成功 obj[field] 已经是 Decimal 类型
        :param obj:     被检查对象
        :param field:   被检查字段
        :param description:    字段 中文名称
        :param pt:      允许小数点后的位数
        :return:    成功返回 {'code': 0, 'msg': 'ok'}， 失败，code 不为 0
        """
        dd = JdTools.decimal(obj.get(field), pt=pt + 1)
        passed, obj[field] = JdTools.decimal_check(obj.get(field))
        if not passed:
            return {"code": ERR_PUB_NUM, "msg": ERR_PUB_NUM_MSG % description}
        if obj[field] != dd:
            return {"code": ERR_PUB_NUM_PT2, "msg": ERR_PUB_NUM_PT2_MSG % description}

        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def decimal_ex(obj, **kwargs):
        """
        校验 obj 中多个字段是否可以转为 Decimal 类型
        :param obj:     被校验参数，dict
        :param kwargs:  被校验字段，dict, {字段名称='中文字段名称'}
        :return:  成功 - {'code': 0, 'msg': 'ok'}
                   失败 - {'code': 706, 'msg': 错误信息}
        用法： JdCheck.decimal_ex(obj, real_fee='实收学费', total='应收学费')
        """
        for k, v in kwargs.items():
            vv = obj.get(k)

            dd = JdTools.decimal(vv, pt=3)
            passed, obj[k] = JdTools.decimal_check(vv)
            if not passed:
                return {"code": ERR_PUB_NUM, "msg": ERR_PUB_NUM_MSG % v}
            if obj[k] != dd:
                return {"code": ERR_PUB_NUM_PT2, "msg": ERR_PUB_NUM_PT2_MSG % v}

        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def decimal_gte0(obj, **kwargs):
        """obj 中字段需为 Decimal，且 大于等于0"""
        for k, v in kwargs.items():
            vv = obj.get(k)

            dd = JdTools.decimal(vv, pt=3)
            passed, obj[k] = JdTools.decimal_check(vv)
            if not passed:
                return {"code": ERR_PUB_NUM, "msg": ERR_PUB_NUM_MSG % v}
            if obj[k] != dd:
                return {"code": ERR_PUB_NUM_PT2, "msg": ERR_PUB_NUM_PT2_MSG % v}

            if dd and dd < 0:
                return {"code": ERR_PUB_GT_EQ_0, "msg": ERR_PUB_GT_EQ_0_MSG % v}

        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def int_gte0(obj, **kwargs):
        """obj 中字段需为 int，且 大于等于0， 输入值，不能转换为 int时，不报错，默认为0"""
        for k, v in kwargs.items():
            vv = obj.get(k)
            _, obj[k] = JdTools.int(vv)
            if obj[k] < 0:
                return {"code": ERR_PUB_GT_EQ_0, "msg": ERR_PUB_GT_EQ_0_MSG % v}

        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def int_gte0_err(obj, **kwargs):
        """obj 中字段需为 int，且 【大于等于0】。 输入值，不能转换为 int时，【报错】. 【输入 None 不报错】"""
        for k, v in kwargs.items():
            vv = obj.get(k)
            if vv is None:
                continue
            passed, obj[k] = JdTools.int(vv)
            if not passed:
                return {"code": ERR_PUB_GT_EQ_0, "msg": ERR_PUB_GT_EQ_0_MSG % v}
            if obj[k] < 0:
                return {"code": ERR_PUB_GT_EQ_0, "msg": ERR_PUB_GT_EQ_0_MSG % v}

        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def str(obj, **kwargs):
        """
        对 obj 中 字符串类型的参数校验长度， 参数可以不填，若填写 不能超长
        :param obj:     被校验参数，dict
        :param kwargs:  被校验字段，dict, {字段名称='长度，中文字段名称'}
        :return:  成功 - {'code': 0, 'msg': 'ok'}
                   失败 - {'code': 700, 'msg': 错误信息}
        用法： JdCheck.str(row, paper_receipt='15,收据号', remark='240,备注')
        """
        for k, v in kwargs.items():
            arr = v.split(',')
            _, length = JdTools.int(arr[0])
            tip = JdTools.trim(arr[1]) or k

            if k not in obj:  # key 未传递
                continue
            obj[k] = JdTools.trim(obj.get(k))
            if obj[k] and len(str(obj[k])) > length:
                return {'code': ERR_PUB_LEN, 'msg': ERR_PUB_LEN_MSG % (tip, length)}

        return {'code': 0, 'msg': 'ok'}

    @staticmethod
    def date(obj, **kwargs):
        """
        校验日期格式是否正确。
        :param obj:         被校验 对象, dict
        :param kwargs:      被校验字段，dict, {字段名称='中文字段名称'}
        :return:    {code: 错误码， msg： 错误提示}
        """
        tip = '“%s”格式错误【%s】，期望 年-月-日！'
        for k, v in kwargs.items():
            dt = obj.get(k)
            try:
                obj[k] = JdTools.str_to_datetime(JdTools.trim(dt), True)
            except (ValueError, TypeError):
                return {'code': ERR_DATE_FMT, 'msg': tip % (v, dt)}
        return {'code': 0, 'msg': 'ok'}
