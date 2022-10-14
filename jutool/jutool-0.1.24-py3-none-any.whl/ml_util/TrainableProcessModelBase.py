import abc


class TrainableProcessState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info_of_batch(self):
        pass

    @abc.abstractmethod
    def info_of_epoch(self):
        pass

    def event_finish_batch(self):
        pass

    def event_finish_epoch(self):
        pass


class TrainableProcessModelBase(metaclass=abc.ABCMeta):

    def __init__(self, name: str):
        self._name = name

    @property
    def Name(self):
        return self._name

    def __call__(self, *args, **kwargs):
        return self.predict(args[0], )

    @abc.abstractmethod
    def predict(self, input):
        pass

    @abc.abstractmethod
    def train(self, input, lable) -> TrainableProcessState:
        pass

    @abc.abstractmethod
    def load(self, model_key: str):
        pass

    @abc.abstractmethod
    def save(self, model_key: str):
        pass
