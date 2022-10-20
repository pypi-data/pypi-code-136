import abc
from code_util.log import process_status_bar


class IterationProcessModelBase(metaclass=abc.ABCMeta):
    """
    遍历的模型定义（抽象类）
    """

    def __init__(self, name):
        """
        模型的初始化
        :param name: 模型的名称
        """
        self._name = name

    @property
    def Name(self):
        """
        模型的名称
        :return: str类型的名称
        """
        return self._name

    def prepare(self):
        """
        循环前的准备过程
        :return: 无返回
        """
        pass

    @abc.abstractmethod
    def call(self, item, process_bar: process_status_bar, state=None):
        """
        抽象方法，每个循环体Item的执行过程
        :param item: 循环体的Item
        :param item: 循环的processbar实例，用于对状态进行输出
        :param state: 状态信息
        :return: 无返回
        """
        pass
