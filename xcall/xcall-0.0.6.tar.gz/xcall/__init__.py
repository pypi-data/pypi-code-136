# -*- coding: utf8 -*-
import json
import socket
import subprocess

from xcall.SocketStreamReader import SocketStreamReader
from xcall.xcall_consts import TYPE_INT, TYPE_BOOLEAN, TYPE_STRING, TYPE_FLOAT, EXTRA_TARGET, \
    EXTRA_TYPES, EXTRA_PARAMS, EXTRA_WAY, EXTRA_WAY_METHOD, EXTRA_CONVERTER, EXTRA_CONVERTER_STRING, \
    EXTRA_WAY_CONSTRUCTOR, EXTRA_WAY_WRITE_FIELD, EXTRA_WAY_READ_FIELD, EXTRA_CONVERTER_OBJID, PREFIX_OBJECT_ID, \
    TYPE_OBJECT, EXTRA_CONVERTER_JSON

"""
必填，需指定手机设备端口号
"""
phone_port = 0

"""
可选，电脑上运行的端口号，默认8888，如有冲突再修改
"""
local_port = 8888

"""
可选，调试模式
"""
debug = False

"""
可选，是否使用局域网直接连接，而不是adb
"""
use_lan = False

"""
可选，手机的局域网ip，当use_lan=true时会使用
"""
phone_ip = ""


def call(request: dict) -> dict:
    """
    自己构建一个json请求发起一个调用，获取调用结果
    :param request: json请求
    :return: 请求结果
    """
    if phone_port == 0:
        raise Exception("需要指定phone_port")
    if use_lan:
        if len(phone_ip) == 0:
            raise Exception("需要指定phone_ip")
        socket_ip = phone_ip
        socket_port = phone_port
    else:
        if local_port == 0:
            raise Exception("需要指定local_port")
        socket_ip = "localhost"
        socket_port = local_port
        try:
            forward_info = exec_adb_cmd("adb forward --list")
            if f"tcp:{local_port} tcp:{phone_port}" not in forward_info:
                forward_result = exec_adb_cmd(f"adb forward tcp:{local_port} tcp:{phone_port}")
                if "error" in forward_result:
                    raise Exception("adb forward执行失败!")
        except Exception:
            raise Exception("adb命令执行失败，请检查是否安装adb")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((socket_ip, socket_port))
        byteArray = bytes(json.dumps(request) + "\n", encoding='utf-8')
        sock.sendall(byteArray)
        data = json.loads(str(SocketStreamReader(sock).read_line(), encoding='utf-8'))
        sock.close()
    return data


def call_with(target, params, way, converter, mainThread) -> dict:
    """
    https://bytedance.feishu.cn/docx/doxcnZIl0MV7n0XjW92Na3X8G5b
    :param target: 调用的目标方法
    :param params: 参数列表
    :param way: 哪种调用方式
    :param converter: 如何转换结果：0->toString、1->toJson、2->objId
    :param mainThread: 是否在主线程执行
    :return: 调用结果
    """
    request = build_request(target, params, way, converter, mainThread)
    if debug:
        print(request)
    response = call(request)
    if debug:
        print(response)
    # 解析结果
    return response


def call_method(target, *params, mainThread=True) -> str:
    """
    调用一个方法，返回的是objectId
    :param target: 调用方法名
    :param params: 调用参数
    :param mainThread: 是否在主线程执行
    :return: 方法调用结果的objectId
    """
    result = call_with(target, params, 0, 2, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return result['data']


def call_method_str(target, *params, mainThread=True) -> str:
    """
    调用一个方法，返回的是toString的结果
    :param target: 调用方法名
    :param params: 调用参数
    :param mainThread: 是否在主线程执行
    :return: 方法调用结果的objectId
    """
    result = call_with(target, params, 0, 0, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return result['data']


def call_method_json(target, *params, mainThread=True) -> dict:
    """
    调用一个方法，返回的是toJson的结果
    :param target: 调用方法名
    :param params: 调用参数
    :param mainThread: 是否在主线程执行
    :return: 方法调用结果的objectId
    """
    result = call_with(target, params, 0, 1, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return json.loads(result['data'])


def call_constructor(target, *params, mainThread=True) -> str:
    """
    调用一个构造方法，返回objectId
    :param target: 构造方法名
    :param params: 构造参数
    :param mainThread: 是否在主线程执行
    :return: 创建的对象的objectId
    """
    result = call_with(target, params, 1, 2, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return result['data']


def call_constructor_str(target, *params, mainThread=True) -> str:
    """
    调用一个构造方法，返回toString结果
    :param target: 构造方法名
    :param params: 构造参数
    :param mainThread: 是否在主线程执行
    :return: 创建的对象的objectId
    """
    result = call_with(target, params, 1, 0, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return result['data']


def call_constructor_json(target, *params, mainThread=True) -> dict:
    """
    调用一个构造方法，返回toJson结果
    :param target: 构造方法名
    :param params: 构造参数
    :param mainThread: 是否在主线程执行
    :return: 创建的对象的objectId
    """
    result = call_with(target, params, 1, 1, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return json.loads(result['data'])


def call_read_field(target, mainThread=True) -> str:
    """
    获取一个属性值，返回objectId
    :param target: 获取属性名
    :param mainThread: 是否在主线程执行
    :return: 属性值，格式{'data':xx, 'code':xx}
    """
    result = call_with(target, (), 2, 2, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return result['data']


def call_read_field_str(target, mainThread=True) -> str:
    """
    获取一个属性值，返回toString的结果
    :param target: 获取属性名
    :param mainThread: 是否在主线程执行
    :return: 属性值，格式{'data':xx, 'code':xx}
    """
    result = call_with(target, (), 2, 0, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return result['data']


def call_read_field_json(target, mainThread=True) -> dict:
    """
    获取一个属性值，返回toJson的结果
    :param target: 获取属性名
    :param mainThread: 是否在主线程执行
    :return: 属性值，格式{'data':xx, 'code':xx}
    """
    result = call_with(target, (), 2, 1, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return json.loads(result['data'])


def call_write_field(target, param, field_type=None, mainThread=True) -> str:
    """
    修改一个属性值，返回code
    :param target: 属性名
    :param param: 修改的属性值
    :param field_type: 属性的类型，如为None则自动转换
    :param mainThread: 是否在主线程执行
    :return: 成功的提示
    """
    if field_type is not None:
        target += "(" + field_type + ")"
    result = call_with(target, (param,), 3, 0, mainThread)
    if result['code'] != 0:
        raise Exception(result['data'])
    return result['data']


def build_request(target, param_list, way, converter, mainThread) -> dict:
    """
    生成json请求
    """
    request = {}
    # 去掉空格
    target = target.replace(' ', '')
    type_list = []
    if '(' in target and ')' in target:
        # 指定了参数类型的列表
        param_type_start_index = target.index('(')
        param_type_end_index = target.index(')')
        param_type_str = target[param_type_start_index + 1:param_type_end_index]
        if len(param_type_str) > 0:
            # 做一个判断，主要是为了处理无参的方法签名
            type_list = target[param_type_start_index + 1:param_type_end_index].split(',')
        if len(type_list) != len(param_list):
            raise Exception(f"传参数量{len(param_list)}和方法参数数量{len(type_list)}不一致")
        target = target[:param_type_start_index]
    request['target'] = target.replace(' ', '')
    if len(param_list) > 0 and len(type_list) == 0:
        # 需要自动识别指定type
        for param in param_list:
            type_list.append(get_type_str(param))
    params = []
    for i in param_list:
        if i is None:
            params.append(None)
        else:
            params.append(i)
    request['types'] = type_list
    request['params'] = params
    request['way'] = way
    request['converter'] = converter
    request['mainThread'] = mainThread
    return request


def get_type_str(param) -> str:
    """
    将python类型转换为xcall识别的类型
    :param param: python值
    :return:
    """
    param_type = type(param)
    if param_type is int:
        return TYPE_INT
    elif param_type is bool:
        return TYPE_BOOLEAN
    elif param_type is str:
        if len(param) > 0 and param[0] == PREFIX_OBJECT_ID:
            # 对象类型
            return TYPE_OBJECT
        return TYPE_STRING
    elif param_type is float:
        return TYPE_FLOAT
    elif param_type is list or param_type is tuple:
        # 列表类型
        return "[" + get_type_str(param[0])
    elif param_type is None:
        raise Exception("参数为None时需要显式指定类型")
    else:
        raise Exception("不支持的参数类型: " + str(param))


def exec_adb_cmd(cmd):
    """
    执行一个命令，返回执行结果
    :param cmd: 命令
    :return:
    """
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE)
        return str(result, encoding='utf-8')
    except subprocess.CalledProcessError:
        try:
            # 可能环境变量没生效，再试一次
            result = subprocess.check_output("source ~/.bash_profile ; " + cmd, shell=True, stderr=subprocess.PIPE)
            return str(result, encoding='utf-8')
        except subprocess.CalledProcessError:
            # 可能没配置好，再试一次
            result = subprocess.check_output(f"~/Library/Android/sdk/platform-tools/{cmd}", shell=True)
            return str(result, encoding='utf-8')
