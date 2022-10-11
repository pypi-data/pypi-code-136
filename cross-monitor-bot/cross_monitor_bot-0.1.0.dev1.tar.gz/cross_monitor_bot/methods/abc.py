import abc



class ABCMethod(abc.ABC):
    @abc.abstractmethod
    def isOk(self) -> bool:
        ...
