import abc


class TrainableProcessState(metaclass=abc.ABCMeta):
    """
    训练过程的状态记录的处理类（抽象类）
    """
    @abc.abstractmethod
    def info_of_batch(self):
        """
        每个batch的训练数据处理过程
        :return: 无
        """
        pass

    @abc.abstractmethod
    def info_of_epoch(self):
        """
        每个epoch的训练数据的处理过程
        :return: 无
        """
        pass

    def event_finish_batch(self):
        """
        每个batch训练完成的Event
        :return: 无
        """
        pass

    def event_finish_epoch(self):
        """
        每个epoch训练完成的Event
        :return: 无
        """
        pass


class TrainableProcessModelBase(metaclass=abc.ABCMeta):
    """
    基于迭代训练模型的基类（抽象类）
    """
    def __init__(self, name: str):
        """
        初始化
        :param name: 模型名称
        """
        self._name = name

    @property
    def Name(self):
        """
        属性——模型名称
        :return: 返回名称
        """
        return self._name

    def __call__(self, *args, **kwargs):
        """
        同predict方法
        :param args: 参数
        :param kwargs: 参数
        :return: 结果
        """
        return self.predict(args[0], )

    @abc.abstractmethod
    def predict(self, input):
        """
        预测方法
        :param input: 输入数据
        :return:  结果
        """
        pass

    @abc.abstractmethod
    def train(self, input, lable) -> TrainableProcessState:
        """
        训练过程
        :param input: 训练集的batch
        :param lable: 训练集的label
        :return: 返回训练状态类 TrainableProcessState
        """
        pass

    @abc.abstractmethod
    def load(self, model_key: str):
        """
        模型的加载
        :param model_key: 模型的标识key
        :return: 无返回
        """
        pass

    @abc.abstractmethod
    def save(self, model_key: str):
        """
        模型的存储
        :param model_key: 存储的标识key
        :return: 无返回
        """
        pass
