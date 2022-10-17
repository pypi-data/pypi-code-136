class SignalDetector:
    def __init__(self, identifier, name):
        self.__id = identifier
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def is_valid(self, stock_market):
        return True
