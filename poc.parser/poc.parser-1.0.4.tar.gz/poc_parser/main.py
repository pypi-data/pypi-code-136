import json
import http.client
from typing import *
from urllib.parse import urlparse

import yaml

from .gtlog import GTLog
from .expression import ExpressionParser, SnapShot, Socket
from .thirdparty_packages import requests


class PocArgs(object):
    """
    poc 规则单个 uri 参数
    """
    def __init__(self, jdata: Dict) -> None:
        """
        构造
        """
        self.uri = jdata.get('uri', None)
        self.uriencode = jdata.get('uriencode', True)
        self.method = jdata.get('method', 'GET')
        self.headers = jdata.get('headers', {})
        self.body: str = jdata.get('body', '')
        self.allow_redirects: bool = jdata.get("allow_redirects", True)
        self.assign: str = str(jdata.get('assign', ''))
        self.expression: str = str(jdata.get('expression', ''))
        self.timeout = jdata.get('timeout', 15)
        self.size_limit = jdata.get('size_limit', 0)

        # 文件上传漏洞body内有的服务器不认\n分隔符, 这个分支把\n替换为\r\n
        if "multipart/form-data" in self.headers.get("Content-Type", "") and self.body:
            str_list = list(self.body)
            for index in range(1, len(str_list)):
                if str_list[index - 1] != "\r" and str_list[index] == "\n":
                    str_list.insert(index, "\r")
            self.body = "".join(str_list)

    def __repr__(self):
        return str(self.__dict__)


class PocRule(object):  # pylint: disable=too-many-instance-attributes
    """
    从路径或字典初始化poc 规则
    """
    def __init__(self, relativepath: str, debug=False, proxies=None, jdata=None) -> None:
        """
        构造
        """
        # 运行日志
        self.running_log = []

        self.debug = debug
        if isinstance(jdata, dict):
            jdata = jdata
        else:
            path = relativepath.replace(".", "/")
            path = path if path.endswith(".yml") else path + ".yml"
            with open(path, encoding="utf-8") as f:
                jdata = yaml.safe_load(f)

        # 信息参数
        self.product = jdata.get("product", '')
        self.name = jdata.get('name', '')
        self.holetype = jdata.get('holetype', 'other')
        self.level = jdata.get('level', None)

        self.desc = jdata.get('desc', '')
        self.author = jdata.get('author', '')
        self.cve = jdata.get('cve', None)
        self.cnvd = jdata.get('cnvd', None)

        # 规则参数
        self.poc_args = [PocArgs(poc_args) for poc_args in jdata.get('rules', [])]

        # 可选参数
        self.control = jdata.get('control', 'SEQ')  # 多个rule之间逻辑 SEQ/AND/OR
        self.http_version = jdata.get('http_version', "1.1")  # HTTP版本
        http.client.HTTPConnection._http_vsn_str = f"HTTP/{self.http_version}"
        self.set = jdata.get('set', {})  # 变量预定义
        self.ret = jdata.get('ret', f'检测到 {self.name}, {self.desc}')  # 命中后返回内容

        # 表达式解析器
        self._parser = None

        # 记录poc运行时的产生的结果
        self._snapshots: [SnapShot] = []

        self.proxies = proxies if proxies else {}
        self.session = requests.Session()

        # 初始化dnslog
        self.gtlog = GTLog()

    def __repr__(self) -> str:
        return str(self.__dict__)

    @property
    def parser(self):
        if not self._parser:
            self._parser = ExpressionParser(proxies=self.proxies)
        return self._parser

    @property
    def snapshots(self):
        # _snapshot内的值最后才混合tcp数据，时序可能不对，这里排个序
        return [s.to_dict() for s in sorted(self._snapshots, key=lambda k: k.start_time)]

    @staticmethod
    def __get_host(url):
        return urlparse(url).hostname

    @staticmethod
    def __get_port(url):
        parse_result = urlparse(url)
        if parse_result.port:
            return parse_result.port
        else:
            if parse_result.scheme == "http":
                return 80
            elif parse_result.scheme == "https":
                return 443
            else:
                return 0

    def __replace_vars(self, args):
        if isinstance(args, str):
            start = args.find("{{")
            end = args.find("}}")
        elif isinstance(args, bytes):
            start = args.find(b"{{")
            end = args.find(b"}}")
        else:
            return args
        if end > start > -1:
            arg_name = args[start + 2: end]  # 提取表达式
            flag = "{{" + arg_name + "}}"  # 要替换的标志位
            var = self.parser.parse(arg_name)  # 解析表达式
            if isinstance(var, bytes):
                args = args.encode().replace(flag.encode(), var)
            else:
                args = args.replace(flag, str(var))
            return self.__replace_vars(args)
        return args

    def __init_set(self):
        # 初始化poc中的set变量
        for k, expression in self.set.items():
            value = self._parser.parse(expression)
            self.parser.add_variable(**{k: value})

    def __request(self, url, poc_args: PocArgs):
        resp = self.session.request(
            method=poc_args.method,
            url=f'{url}{poc_args.uri}',
            headers=poc_args.headers,
            data=poc_args.body,
            allow_redirects=poc_args.allow_redirects,
            timeout=poc_args.timeout,
            proxies=self.proxies,
            uriencode=poc_args.uriencode,
            stream=True
        )
        if poc_args.size_limit > 0:
            content, size_temp = b"", 0
            for chunk in resp.iter_content():
                if chunk:
                    size_temp += len(chunk)
                    content += chunk
                    if size_temp >= poc_args.size_limit:
                        break
            resp.close()
            resp._content = content
        return resp

    def _exec_single_rules(self, url, poc_args: PocArgs) -> bool or None:
        # 替换表达式参数
        poc_args.uri = self.__replace_vars(poc_args.uri)
        poc_args.body = self.__replace_vars(poc_args.body)
        for k in poc_args.headers:
            poc_args.headers[k] = self.__replace_vars(poc_args.headers[k])

        # 执行请求和表达式
        if poc_args.uri is not None:
            snapshot = SnapShot()

            resp = self.__request(url, poc_args)
            self.parser.response = resp
            # 记录快照
            snapshot.send = requests.dump_request(resp)
            snapshot.recv = requests.dump_response(resp)
            self._snapshots.append(snapshot)

            if self.debug:
                self.log(requests.dump_all(resp))
        if poc_args.assign:
            self.parser.parse(poc_args.assign)
        if poc_args.expression:
            return bool(self.parser.parse(poc_args.expression))
        else:
            return None

    def execute(self, url, headers: dict = None):
        if headers is not None:
            for k, v in headers.items():
                self.session.headers[k] = v
        result = {"status": False}
        # 初始化运行过程中变量
        self.parser.add_variable(url=url, host=self.__get_host(url), port=self.__get_port(url))
        self.__init_set()

        if self.debug and self.proxies:
            self.log(f"正在使用代理: {self.proxies}")

        expression_results = []

        for i, poc_args in enumerate(self.poc_args):
            exp_result = self._exec_single_rules(url, poc_args)

            if self.debug:
                self.log(f"函数解析结果: {self.parser.last_ret}")
                self.log(f"表达式解析结果: {exp_result}")
                self.log(f"当前可用变量：{self.parser.variables}")

            if exp_result is not None:  # 没有表达式返回None，不参与逻辑判断，仅赋值使用
                expression_results.append(exp_result)
                if self.control == "OR" and exp_result is True:
                    # OR规则只需要有一个为真即跳出检测
                    break
                if self.control != "OR" and exp_result is False:
                    # AND, SEQ规则只需要有一个为假即跳出检测
                    break

        # 判断是否命中
        if self.control == "OR":
            result["status"] = any(expression_results)
        else:
            result["status"] = all(expression_results)

        for _, var in self.parser.variables.items():
            # 先凑合用，等全部运行完毕后一次获取全部数据包，避免处处回参传参，太麻烦
            if isinstance(var, Socket):
                self._snapshots += var.snapshots

        if result["status"]:
            result["ret"] = self.__replace_vars(self.ret)
        if self.debug:
            self.log("*" * 10)
            self.log(f"检测结果：{result}")
        return result

    def log(self, *args):
        for arg in args:
            if isinstance(arg, dict):
                arg = json.dumps(arg, indent=2)
            print(arg)
            self.running_log.append(arg)
