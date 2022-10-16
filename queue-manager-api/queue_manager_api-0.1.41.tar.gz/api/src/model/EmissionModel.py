from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper
from python_framework import StaticConverter
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import EMISSION, MESSAGE, MODEL
from util import ModelUtil
from constant import EmissionConstant, ModelConstant
from helper.static import EmissionModelHelperStatic, HistoryStaticHelper


class EmissionModel(MODEL):
    __tablename__ = EMISSION

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(3*sap.MEDIUM_STRING_SIZE), nullable=False, unique=True)
    queueKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    subscriptionKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    groupKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    messageKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    originKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)

    url = sap.Column(sap.String(sap.LARGE_STRING_SIZE), nullable=False)
    tries = sap.Column(sap.Integer(), nullable=False, default=EmissionConstant.ZERO_TRIES)
    onErrorUrl = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE))
    onErrorTries = sap.Column(sap.Integer(), nullable=False, default=EmissionConstant.ZERO_TRIES)
    maxTries = sap.Column(sap.Integer(), nullable=False, default=EmissionConstant.DEFAULT_MAX_TRIES)
    backOff = sap.Column(sap.Float(precision=3), nullable=False, default=EmissionConstant.DEFAULT_BACKOFF)
    status = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=ModelConstant.DEFAULT_STATUS)
    state = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=ModelConstant.DEFAULT_STATE)

    history = sap.Column(sap.String(65_536))

    createdAt = sap.Column(sap.DateTime, nullable=False)
    updatedAt = sap.Column(sap.DateTime, nullable=False)


    def __init__(self,
        id = None,
        key = None,
        queueKey = None,
        subscriptionKey = None,
        groupKey = None,
        messageKey = None,
        originKey = None,
        url = None,
        tries = None,
        onErrorUrl = None,
        onErrorTries = None,
        maxTries = None,
        backOff = None,
        status = None,
        state = None,
        history = None,
        createdAt = None,
        updatedAt = None
    ):
        self.id = id
        self.queueKey = queueKey
        self.subscriptionKey = subscriptionKey
        self.groupKey = groupKey
        self.messageKey = messageKey
        self.originKey = originKey
        self.url = url
        self.tries = StaticConverter.getValueOrDefault(tries, EmissionConstant.ZERO_TRIES)
        self.onErrorUrl = onErrorUrl
        self.onErrorTries = StaticConverter.getValueOrDefault(onErrorTries, EmissionConstant.ZERO_TRIES)
        self.maxTries = StaticConverter.getValueOrDefault(maxTries, EmissionConstant.DEFAULT_MAX_TRIES)
        self.backOff = StaticConverter.getValueOrDefault(backOff, EmissionConstant.DEFAULT_BACKOFF)
        self.status = StaticConverter.getValueOrDefault(status, ModelConstant.DEFAULT_STATUS)
        self.state = StaticConverter.getValueOrDefault(state, ModelConstant.DEFAULT_STATE)
        self.setHistory(history)
        self.updateKey(key=key)

        self.createdAt = createdAt
        self.updatedAt = updatedAt
        StaticConverter.overrideDateData(self)


    def updateKey(self, key=None):
        self.key = StaticConverter.getValueOrDefault(key, EmissionModelHelperStatic.buildKey(
            queueKey = self.queueKey,
            subscriptionKey = self.subscriptionKey,
            messageKey = self.messageKey
        ))


    def setHistory(self, history):
        HistoryStaticHelper.overrideModelHistory(self, history)


    def addHistory(self, history):
        HistoryStaticHelper.addModelHistory(self, history)


    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, key={self.key}, queueKey={self.queueKey}, subscriptionKey={self.subscriptionKey}, messageKey={self.messageKey}, tries={self.tries}, onErrorTries={self.onErrorTries}, maxTries={self.maxTries}, backOff={self.backOff}, status={self.status}, state={self.state})'
