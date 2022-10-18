import abc, importlib


class MLComponentBase(metaclass=abc.ABCMeta):
    """
    统一ML处理过程的基类，抽象类
    """
    def __init__(self, modules=None):
        """
        初始化
        :param modules: 需要倒入的module
        """
        if modules is not None:
            for mo in modules:
                mo_item = importlib.import_module(mo)
                setattr(self, mo, mo_item)

    def __getitem__(self, item):
        return getattr(self, item)

    def load_model(self, model_path):
        """
        模型的加载过程，（如有）
        :param model_path: 模型存储的路径
        :return: 无返回
        """
        pass

    @abc.abstractmethod
    def call(self, linked_item, ori_item=None):
        """
        执行过程，抽象方法
        :param linked_item: 处理的目标数据
        :param ori_item: 处理的原始数据
        :return: 处理的结果
        """
        pass
