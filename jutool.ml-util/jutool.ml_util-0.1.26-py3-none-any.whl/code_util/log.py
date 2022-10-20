import math
from enum import Enum
import time, sys


class log_level_enum(Enum):
    """
    log级别枚举
    """
    Error = 1
    Warning = 2
    normal = 3
    pigeonhole = 4


def log(str, log_level: log_level_enum = log_level_enum.normal):
    """
    打印log
    :param str: log内容
    :param log_level: log级别，使用枚举
    :return: 无返回
    """
    print(f"{log_level}:{str}")


def log_error(error_message: str):
    """
    输出错误log，并抛出异常
    :param error_message: 异常信息
    :return: 无返回
    """
    log(error_message, log_level_enum.Error)
    raise Exception(error_message)


class process_status_bar:
    """
    控制台的进度条
    """

    def __init__(self, processbar_length=20):
        """
        初始化函数
        :param processbar_length: 进度条长度（打印长度）
        """
        self._iter_stack = []
        self._process_bar_len = processbar_length
        self._print_str = ""
        self._print_logs = []

    def _flush_(self):
        stack_str = ""
        for iter_i in range(len(self._iter_stack) - 1):
            p_value = self._iter_stack[iter_i]['value'] / float(self._iter_stack[iter_i]['max'])
            p_value = "%.2f" % (p_value * 100)
            stack_str += f"[{self._iter_stack[iter_i]['key']} {p_value}%] >>"
            pass

        current_item = self._iter_stack[-1]
        p_value = current_item["value"] / float(current_item["max"])
        p_value_str = "%.2f" % (p_value * 100)

        bar_size = math.floor(p_value * self._process_bar_len)

        bar_str = ""
        for i in range(self._process_bar_len):
            if i + 1 <= bar_size:
                bar_str += "*"
            else:
                bar_str += " "

        bar_str = f'{stack_str} {current_item["key"]} {current_item["value"]}/{current_item["max"]}  [{bar_str}]{p_value_str}% - {self._print_str} '

        if len(self._print_logs) == 0:
            sys.stdout.write('\r' + bar_str)
        else:
            sys.stdout.write('\r')
            for s in self._print_logs:
                sys.stdout.write(s + "\n")
            self._print_logs.clear()
            sys.stdout.write(bar_str)
        sys.stdout.flush()

    def iter_bar(self, iter_item, value=0, key=None, max=None):
        """
        进度条的遍历方法
        :param iter_item: 主遍历对象
        :param value: value起始
        :param key: 遍历名称
        :param max: 遍历的数量
        :return: 可遍历对象
        """
        if max is None:
            if iter_item is list:
                max = len(iter_item)
            elif iter_item is {}:
                max = len(iter_item.keys())
            else:
                log_error("需要制定max值")

        if key is None:
            key = f"Iter {len(self._iter_stack)}"
        self._iter_stack.append({
            'key': key,
            'value': value,
            'max': max
        })

        for _iter in iter_item:
            self._flush_()
            yield _iter
            self._iter_stack[-1]['value'] += 1

        self._flush_()
        self._iter_stack.pop(-1)

    def update_process_value(self, v):
        """
        强制更新进度条的进度数值
        :param v: 要更新的数值
        :return: 无返回
        """
        self._iter_stack[-1]['value'] = v

    def process_print(self, str):
        """
        打印过程中的状态信息（覆盖输出）
        :param str: 状态信息
        :return: 无返回
        """
        self._print_str = str

    def print_log(self, str):
        """
        过程中打印log（不覆盖，使用换行）
        :param str: 状态信息
        :return: 无返回
        """
        self._print_logs.append(str)


def process_bar_iter(iter_item, key=None, max=None):
    """
    迭代过程的简易进度条
    :param iter_item: 迭代对象
    :param key: 迭代名称
    :param max: 最大迭代数量
    :return: 无返回
    """
    pb = process_status_bar()
    for item in pb.iter_bar(iter_item, key=key, max=max):
        yield item

# psb = process_status_bar()
# for s1 in psb.iter_bar([1, 2, 3], "key1", max=3):
#     for s2 in psb.iter_bar([1, 2, 3], "key2", max=3):
#         for s2 in psb.iter_bar([1, 2, 3], "key3", max=3):
#             time.sleep(0.3)
