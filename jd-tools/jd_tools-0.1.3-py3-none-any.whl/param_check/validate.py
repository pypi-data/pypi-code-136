# -*- coding: utf8 -*-
# =============================================================================
# 文件:  validate.py
# 日期:  2021/4/29 11:07
# 修改记录：
#   2022-05-12  WXG  verify date格式 支持 参数 no-hms, 时分秒为 00:00:00
#   2022-06-05  WXG  verify in参数增加缺少结束符 ']' 的校验。版本 1.1.3
#   2022-07-08  WXG  verify 增加ppt，自定义错误提示。版本 1.1.4
# =============================================================================
from collections import defaultdict
from abc import ABCMeta, abstractmethod

from ..tools import JdTools, JdDate
from .errcode import *


__version__ = "1.1.7"
__author__ = "WXG"
__all__ = ['verify', 'validation']


class Validator(object):
    """
    参数校验类， 纯虚基类
    """

    __metaclass__ = ABCMeta
    err_message = ""

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError


class Range(Validator):
    """
    范围： [start, end], inclusive 是否包含，为假时的取值范围：(start, end)
    # Example:
        validations = {
            "field": [Range(0, 10)]
        }
        passes = {"field": 10}
        fails = {"field" : 11}
    """

    def __init__(self, start, end, inclusive=True):
        self.start = start
        self.end = end
        self.inclusive = inclusive
        self.err_message = f"取值范围必须在 [{start}-{end}]"

    def __call__(self, value):
        if self.inclusive:
            return self.start <= value <= self.end
        else:
            return self.start < value < self.end


class Length(Validator):
    """
    长度校验： 最小长度、最大长度 二者必填其一
    # Example:
        validations = {
            "field": [Length(0, maximum=5)]
        }
        passes = {"field": "hello"}
        fails  = {"field": "hello world"}
    """

    err_messages = {
        "maximum": "最大长度为 {0}",
        "minimum": "最小长度为 {0}",
        "range": "长度必须在 {0}-{1} 之间",
        "equal": "长度必须为 {0}"
    }

    def __init__(self, minimum, maximum=0):
        if not minimum and not maximum:
            raise ValueError("Length must have a non-zero minimum or maximum parameter.")
        if minimum < 0 or maximum < 0:
            raise ValueError("Length cannot have negative parameters.")

        self.minimum = minimum
        self.maximum = maximum
        if minimum and maximum:
            if minimum == maximum:
                self.err_message = self.err_messages["equal"].format(minimum)
            else:
                self.err_message = self.err_messages["range"].format(minimum, maximum)
        elif minimum:
            self.err_message = self.err_messages["minimum"].format(minimum)
        elif maximum:
            self.err_message = self.err_messages["maximum"].format(maximum)

    def __call__(self, value):
        length = len(str(value))
        if self.maximum:
            return self.minimum <= length <= self.maximum
        else:
            return self.minimum <= length


class GreaterThan(Validator):
    """
    大于(等于):
    # Example:
        validations = {
            "field": [GreaterThan(10)]
        }
        passes = {"field": 11}
        fails = {"field" : 10}
    """

    def __init__(self, lower_bound, inclusive=False):
        self.lower_bound = lower_bound
        self.inclusive = inclusive
        self.err_message = "必须大于%s%s" % ('等于' if inclusive else '', lower_bound)

    def __call__(self, value):
        if self.inclusive:
            return value >= self.lower_bound
        else:
            return value > self.lower_bound


class LessThan(Validator):
    """
    小于（等于）
    # Example:
        validations = {
            "field": [LessThan(10)]
        }
        passes = {"field": 9}
        fails = {"field" : 10}
    """

    def __init__(self, upper_bound, inclusive=False):
        self.upper_bound = upper_bound
        self.inclusive = inclusive
        self.err_message = "必须小于%s%s" % ('等于' if inclusive else '', upper_bound)

    def __call__(self, value):
        if self.inclusive:
            return value <= self.upper_bound
        else:
            return value < self.upper_bound


class In(Validator):
    """
    取值范围， 判断是否属于某 集合 （列表）
    # Example:
        validations = {
            "field": [In([1, 2, 3])]
        }
        passes = {"field":1}
        fails  = {"field":4}
    """

    def __init__(self, collection):
        self.collection = collection
        self.err_message = "取值范围不在 %r 中" % collection

    def __call__(self, value):
        return value in self.collection


class OpValidator(Validator):
    def __call__(self, value):
        return True  # 校验不返回失败


class Optional(OpValidator):
    """可选， 可选参数"""
    pass


class Required(OpValidator):
    """必填"""
    pass


class Must(OpValidator):
    """必填， 日期时， None 和 ''空字符 报错 """
    pass


class NoHms(OpValidator):
    """无 时分秒， 日期时, 只有 年-月-日， 时分秒 赋值为 00:00:00 """
    pass


class Default(OpValidator):
    """默认值"""
    def __init__(self, default):
        self.default = default


class Point(OpValidator):
    """小数点位数"""
    def __init__(self, point):
        self.point = point


class Any(OpValidator):
    """任意取值， 同类型内，比如 int / decimal"""
    pass


class Prompt(OpValidator):
    """提示语，代替默认提示"""
    def __init__(self, ppt):
        self.ppt = ppt


class _WRONG(object):
    pass


def _set_default(default, who):
    """
    计算默认值， ds
        ds 默认值， str 默认值为 空字符串("")， date/time -- None,
        decimal/int -- 0, dateRange -- 不支持
    :param default:     默认值， s for ds， 0/1/5.6 for int, decimal: d0, d5.6
    :param who:         参数类型：int, date, str, ...
    :return:    默认值 or _WRONG
    """
    dd = default
    if default in ["s", "0"]:  # 默认值 ds
        if who in ['int', 'i', 'D', 'decimal']:
            dd = 0
        elif who in ['s', 'str']:
            dd = ""
        elif who in ['t', 'dateRange']:
            dd = _WRONG
        elif who in ['d', 'date', 't', 'time']:     # time 也支持 ds
            dd = None
    return dd


def validation(s, key, who):
    """
    字符串 转 参数校验对象
    """
    validations = []

    arr = JdTools.split(s, ',')
    name = arr[0]
    a2 = arr[1:]

    mode = 0    # 0-无任何模式， 1-in 模式，当前解析 in 语句
    in_list = []
    errors = defaultdict(list)
    for i in a2:
        if mode == 1:  # 1-in 模式，当前解析 in 语句
            if ']' in i:
                mode = 0  # 退出 in 模式
                m = JdTools.split(i, ']')
                in_list.append(m[0])

                in_arr = []
                for m in in_list:
                    if who in ['i', 'int']:
                        passed, v = JdTools.int(m)
                        if not passed:
                            errors[key].append(f"取值范围(In) 转换为int失败[ {m[0]} ]！")
                        in_arr.append(v)
                    else:
                        in_arr.append(m)
                validations.append(In(in_arr))
            else:
                in_list.append(i)
        elif i == 'opt':  # 可选参数
            validations.insert(0, Optional)
        elif i == 'must':  # 必填参数，默认为 必填
            validations.append(Must)
        elif i == 'no-hms':     # 时分秒为 00:00:00
            validations.append(NoHms)
        elif i[0] == 'd':  # default，默认值
            val = i[1:]
            success = True
            if val in ['s', '0']:  # ds - 默认值
                default = _set_default(val, who)
                if default == _WRONG:
                    errors[key].append("time/dateRange不支持默认值！")
                    success = False
            elif '.' in val:
                success, default = JdTools.decimal(val)
                if not success:
                    errors[key].append("默认值不合法！")
            else:
                success, default = JdTools.int(val)
                if not success:
                    errors[key].append("默认值不合法，应该为整数！")
            if success:
                validations.append(Default(default))
        elif i[:3] == 'ppt':    # 提示语
            arr_ppt = JdTools.split(i, 'ppt')
            if not arr_ppt[1]:
                errors[key].append("提示语不能为空！")
            else:
                validations.append(Prompt(arr_ppt[1]))
        elif i[0] == 'p':  # 小数点后几位
            success, val = JdTools.int(i[1])
            if not success:
                errors[key].append("p后应为整数！")
            else:
                validations.append(Point(val))
        elif i[0] == '<':   # 小于
            if i[1] == '=':  # 小于等于 <=
                success, operand = JdTools.int(i[2:])
                if not success:
                    errors[key].append("取值范围书写错误！")
                else:
                    validations.append(LessThan(operand, inclusive=True))
            else:  # 小于 <
                success, operand = JdTools.int(i[1:])
                if not success:
                    errors[key].append("取值范围书写错误！")
                else:
                    validations.append(LessThan(operand))
        elif i[:2].lower() == 'in':  # in 语句， 例如 state=状态, in[0,1]
            mode = 1
            m = JdTools.split(i, '[')
            in_list = [m[-1]]
        else:  # 范围
            if '-' in i:
                start, end = JdTools.split(i, '-')
            else:
                start, end = 0, i
            success1, start = JdTools.int(start)
            success2, end = JdTools.int(end)
            if not success1:
                errors[key].append("取值范围最小值书写错误！")
            if not success2:
                errors[key].append("取值范围最大值书写错误！")
            if success1 and success2:
                validations.append(Length(start, end))
                if who in ['s', 'str'] and start == 0:  # 可选字符
                    validations.insert(0, Optional)

    if mode == 1:
        errors[key].append(f"in 参数缺少结束符']'！")

    # 第一次分隔 取值范围校验
    if who in ['int', 'i', 'D', 'decimal']:
        first = name
        arr = JdTools.split(first, '>')
        if len(arr) > 1:  # 存在大于号（'>'）
            if arr[1][0] == '=':  # op = 'gte' 大于等于 >=
                success, operand = JdTools.int(arr[1][1:])
                if not success:
                    errors[key].append("取值范围书写错误！")
                else:
                    validations.append(GreaterThan(operand, inclusive=True))
            else:  # op = 'gt'  # 大于  >
                success, operand = JdTools.int(arr[1])
                if not success:
                    errors[key].append("取值范围书写错误！")
                else:
                    validations.append(GreaterThan(operand))
        else:
            arr = JdTools.split(first, 'any')
            if len(arr) > 1:  # op = 'any'  # 能转换为 int/decimal 的任何值
                validations.append(Any)
            else:
                validations.append(GreaterThan(0, inclusive=True))  # int, decimal 默认 >= 0
    name = arr[0]

    return name, validations, errors  # name-key对象的中文名称, errors-错误列表


def verify(obj, **kwargs):
    """
    参数校验
    :param obj:
    :param kwargs:
        key     type                opt    length  scope  default point  in   ppt
        name    s for str           √     √      -      √      -      √
                d for date          √     -       -      √      -      -
                D for decimal       √     -       √     √      √     √
                i for int           √     -       √     √      -      √   √
                t for time          √     -       -      √      -      -
                dateRange           √     -       -      -       -      -

        用法示例：
        ret = JdCheck.verify(obj, s=dict(name='客户名称, 1-50', short_name='简名, 1-10', person='联系人, 20',
            remark='备注, 140'))

        ***********************************************************************
        规则：
        优先级  opt > must > d(default)
        1. 【opt】 为 可选参数， 没有对应 key 时， 写库不传递该 key ； 有对应
           key 时，opt 不起作用。
           - 优先级 opt < default(d)  即有默认值时，opt 无效
           - 不加 opt，按必填参数处理 ★★★。
        2. 【must】 为 必填参数。 没有对应 key 时 报错。 日期时， None 值报错
        3. 【d】 为 默认值(default)， 未传递 key 或者 值为 '', None 时，赋默认值。
            - ds 默认值， str 默认值为 空字符串("")， date -- None,
              decimal/int -- 0, time / dateRange -- 不支持
        4. scope 取值范围包括： >=0(int, decimal 默认范围), >0, >x, >=x;
           any (任意取值)。
        5. 【p】point, 默认为 p2 小数点后2位，只对 decimal 有效 。
        6. 【length】 目前对 str 类型有效， 长度区间 [min, max]， min默认为0 。
        7. ppt:  错误提示语， 不加 ppt 按 系统原有提示。
        ***********************************************************************
        【str】
        name='客户名称, 1-50'     必填，长度 1-50。 长度不在范围内，报错
        person='联系人, 20        可选，长度最大 20。 长度超过最大值，报错
        person='联系人, 20, opt   允许没有 person 参数，若有 person，按照 上述方式校验。

        【decimal】  不能转为 Decimal 报错。None 或者 '' 转为 0。
        fee='学费'                大于等于0
        fee='学费 >= 0'           大于等于0
        fee='学费>0'              必填，大于0， 默认小数点后2位
        fee='学费 >= 0, p2'       大于等于0， 小数点后2位
        fee='学费 any'            可以转换为 Decimal 的任何值

        【date】  不能转为 日期 报错。无 must 时，None 或者 '' 转为 None。 有 must 时， None/'' 报错
        date='充值日期'           必填。 日期 按 年-月-日 时:分:秒 赋值，无时分秒，填写当前时分秒
        date='充值日期, opt'      可选。
        date='充值日期, must'     必填，None/'' 值报错。
        date='考勤日期, no-hms'   必填， 时分秒 为 0:0:0

        【time】
        time='演出时长'          必填，    时间字符串格式 HH:MM:SS，例如：'00:05:34' 为 5分34秒
        time='演出时长，opt'     可选

        【int】  不能转为 int 报错。None 或者 '' 报错。
        times='课时'              大于等于0
        times='课时 >0'           大于0
        times='课时 any'          可以转为 int 的任何值
        times='课时,d2'           默认值为2， 若填写，按之前规则校验（这里为大于等于0）
        times='课时,opt'          可选，没有该参数，不报错。有该参数，按照 上述规则校验
        state='状态, in[0,1]'     取值范围属于列表

        【dateRange】 可转换为日期范围， 否则报错
        dataVal='2022-1-1 - 2022-1-31'      obj中生成 d1, d2，且 d1=2022-1-1(datetime类型) d2=2022-1-31
                                  date_from_to='从 2022-01-01 至 2022-01-31'
    """
    extra_tip = ''
    for k, v in kwargs.items():
        if k == 'tip':
            extra_tip = v or ''  # 附加提示信息，放在开头。 比如 对续班子表校验时，可输入 学员姓名
        else:
            if not isinstance(v, dict):  # 异常处理
                return {'code': ERR_SYNTAX, 'msg': ERR_SYNTAX_MSG % f"{k}={v}"}
            for k2, v2 in v.items():    # 遍历 date， int 等 具体类型的校验
                ret = _validate_single_key(k2, v2, obj, k, extra_tip)
                if ret['code'] != 0:
                    return ret

    return {'code': 0, 'msg': 'ok'}


def _validate_single_key(key, s, dictionary, who, extra_tip):
    """
     将 key 对应 规则字符串 s，转为 Validator 列表。
     被校验者：  dictionary
     类型： who , 字符串类型，取值  s, str, i, int, date, decimal 等
     额外提示： extra_tip
    """
    tip, validations, errors = validation(s, key, who)
    name = f'{extra_tip}“{tip}”' if extra_tip else f'{tip}'
    if errors:
        return {'code': ERR_VERIFY_ERROR, 'msg': f'{extra_tip}“{tip}”，{errors[key][0]}'}

    # 读取特殊 校验 对象
    special = {'ppt': {'has': False, 'val': ''},        # ppt， 提示
               'default': {'has': False, 'val': ''},    # 默认值
               'point': {'has': False, 'val': ''},      # 小数点后位数
               'add_hms': {'has': True},                # 是否添加 时分秒 for date
               }
    for validator in validations:
        if isinstance(validator, Prompt):  # 自定义提示
            special['ppt'].update({'has': True, 'val': validator.ppt})
        elif isinstance(validator, Default):  # 默认值
            special['default'].update({'has': True, 'val': validator.default})
        elif isinstance(validator, Point):  # 小数点
            special['point'].update({'has': True, 'val': validator.point})
        elif validator == NoHms:  # 不需要添加 年月日
            special['add_hms'].update({'has': False})

    # 默认值
    if key not in dictionary or dictionary[key] == '' or dictionary[key] is None:
        if special['default']['has']:
            dictionary[key] = special['default']['val']

    if Optional in validations and key not in dictionary:  # 可选参数
        return {'code': 0, 'msg': 'ok'}
    if Required in validations and key not in dictionary:  # 必填参数
        return {'code': ERR_VERIFY_NEED_PARAM, 'msg': f'请输入【{name}】'}
    if Must in validations:
        if key not in dictionary:  # 必填参数
            return {'code': ERR_VERIFY_NEED_PARAM, 'msg': f'请输入【{name}】'}
        else:
            if who in ['date', 'd']:
                if dictionary[key] is None or dictionary[key] == '':
                    return {'code': ERR_VERIFY_NEED_PARAM, 'msg': f'请输入【{name}】'}

    if key not in dictionary:
        return {'code': ERR_PUB_NEED, 'msg': special['ppt']['val'] or ERR_PUB_NEED_MSG % name}

    val = dictionary[key]
    if who in ['s', 'str']:
        dictionary[key] = JdTools.trim(str(val or ''))
    elif who in ['D', 'decimal']:
        pt = 2  # for decimal，小数点后的最大位数
        if special['point']['has']:
            pt = special['point']['val']

        passed, dictionary[key] = JdTools.decimal_check(val, pt)
        if not passed:
            return {"code": ERR_PUB_NUM, "msg": special['ppt']['val'] or ERR_PUB_NUM_MSG % name}
        dec = JdTools.decimal(val, pt=pt + 1)
        if dictionary[key] != dec:
            return {"code": ERR_PUB_NUM_PT2, "msg": f'{name} 最多 {pt} 位小数！'}
        # 校验 decimal 数值 不能超过 7 位数字
        if dec > 9999999:
            return {'code': ERR_VERIFY_VAL_EXCEED, 'msg': special['ppt']['val'] or f'{name} 数值越限，最多7位（除小数外）'}
    elif who in ['d', 'date']:
        add_hms = special['add_hms']['has']
        try:
            dictionary[key] = JdTools.str_to_datetime(val, add_hms=add_hms)
        except (ValueError, TypeError):
            return {'code': ERR_DATE_FMT, 'msg': special['ppt']['val'] or f'{name} 格式错误【{val}】，期望 年-月-日！'}
    elif who in ['t', 'time']:      # 时间 时分秒
        try:
            dictionary[key] = JdTools.str_to_time(val)
        except (ValueError, TypeError):
            return {'code': ERR_TIME_FMT, 'msg': special['ppt']['val'] or f'{name} 格式错误【{val}】，期望 HH:MM:SS！'}
    elif who in ['i', 'int']:
        passed, dictionary[key] = JdTools.int(val)
        if not passed:
            return {"code": ERR_PUB_NUM_INT, "msg": special['ppt']['val'] or ERR_PUB_NUM_INT_MSG % name}
    elif who in ['dateRange']:
        ret = JdDate.start_end_time('time_range', val)
        if ret['code'] != 0:
            return ret
        dictionary['d1'] = ret['d1']
        dictionary['d2'] = ret['d2']
        dictionary['date_from_to'] = ret['date_from_to']
    else:
        return {"code": ERR_VERIFY_WHO, "msg": f'未知的校验类型 {who}'}

    for validator in validations:
        if validator in [Any, Optional, Required, Must, NoHms]:
            continue
        passed = validator(dictionary[key])
        if not passed:
            return {'code': ERR_VERIFY_ERROR, 'msg': special['ppt']['val'] or f'[{name}] {validator.err_message}'}

    return {'code': 0, 'msg': 'ok'}
