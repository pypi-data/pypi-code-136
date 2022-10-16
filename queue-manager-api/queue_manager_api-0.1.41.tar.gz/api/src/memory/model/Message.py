from python_helper import Constant as c
from python_helper import ObjectHelper
from python_framework import StaticConverter, Serializer
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import MESSAGE, EMISSION
from constant import ModelConstant
from helper.static import HistoryStaticHelper


class Message:
    __memoryname__ = MESSAGE.replace(Serializer.MODEL_SUFIX, c.BLANK)

    def __init__(self,
        key = None,
        queueKey = None,
        groupKey = None,
        originKey = None,
        headers = None,
        content = None,
        status = None,
        state = None,
        emissionList = None,
        history = None
    ):
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey
        self.originKey = originKey
        self.headers = headers
        self.content = content
        self.status = StaticConverter.getValueOrDefault(status, ModelConstant.DEFAULT_STATUS)
        self.state = StaticConverter.getValueOrDefault(state, ModelConstant.DEFAULT_STATE)
        self.setEmissionList(emissionList)
        self.setHistory(history)


    def setEmissionList(self, emissionList):
        self.emissionList = StaticConverter.getValueOrDefault(emissionList, [])


    def addEmissionList(self, emissionList):
        for emission in emissionList:
            self.addEmission(emission)


    def addEmission(self, emission):
        if not EmissionModelHelperStatic.containsEmission(self.emissionList, emission):
            self.emissionList.append(emission)


    def setHistory(self, history):
        HistoryStaticHelper.overrideMemoryHistory(self, history)


    def addHistory(self, history):
        HistoryStaticHelper.addMemoryHistory(self, history)


    def __repr__(self):
        return f'{self.__memoryname__}(key={self.key}, queueKey={self.queueKey}, groupKey={self.groupKey}, originKey={self.originKey}, status={self.status}, state={self.state})'
