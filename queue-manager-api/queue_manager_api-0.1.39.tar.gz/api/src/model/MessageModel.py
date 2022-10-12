from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper
from python_framework import StaticConverter, Serializer
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import MESSAGE, EMISSION, MODEL
from constant import ModelConstant
from util import ModelUtil
from helper.static import HistoryStaticHelper


class MessageModel(MODEL):
    __tablename__ = MESSAGE

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, unique=True)
    queueKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    groupKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    originKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    content = sap.Column(sap.String(65_536))
    status = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=ModelConstant.DEFAULT_STATUS)
    state = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=ModelConstant.DEFAULT_STATE)

    history = sap.Column(sap.String(65_536))

    createdAt = sap.Column(sap.DateTime, nullable=False)
    updatedAt = sap.Column(sap.DateTime, nullable=False)


    def __init__(self,
        id = None,
        key = None,
        queueKey = None,
        groupKey = None,
        originKey = None,
        content = None,
        status = None,
        state = None,
        emissionList = None,
        history = None,
        createdAt = None,
        updatedAt = None
    ):
        self.id = id
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey
        self.originKey = originKey
        self.content = Serializer.jsonifyIt(content)
        self.status = StaticConverter.getValueOrDefault(status, ModelConstant.DEFAULT_STATUS)
        self.state = StaticConverter.getValueOrDefault(state, ModelConstant.DEFAULT_STATE)
        self.setHistory(history) ###- ModelUtil.getOneToManyData(history)

        self.createdAt = createdAt
        self.updatedAt = updatedAt
        StaticConverter.overrideDateData(self)


    def setHistory(self, history):
        HistoryStaticHelper.overrideModelHistory(self, history)


    def addHistory(self, history):
        HistoryStaticHelper.addModelHistory(self, history)


    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, key={self.key}, queueKey={self.queueKey}, status={self.status}, state={self.state})'
