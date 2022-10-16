from python_framework import StaticConverter

from constant import EmissionConstant, ModelConstant


class EmissionRequestDto:
    def __init__(self,
        queueKey = None,
        subscriptionKey = None,
        url = None,
        tries = None,
        onErrorUrl = None,
        onErrorTries = None,
        maxTries = None,
        backOff = None,
        message = None
    ):
        self.queueKey = queueKey
        self.subscriptionKey = subscriptionKey
        self.url = url
        self.tries = StaticConverter.getValueOrDefault(tries, EmissionConstant.ZERO_TRIES)
        self.onErrorUrl = onErrorUrl
        self.onErrorTries = StaticConverter.getValueOrDefault(onErrorTries, EmissionConstant.ZERO_TRIES)
        self.maxTries = StaticConverter.getValueOrDefault(maxTries, EmissionConstant.DEFAULT_MAX_TRIES)
        self.backOff = StaticConverter.getValueOrDefault(backOff, EmissionConstant.DEFAULT_BACKOFF)
        self.message = message


class EmissionResponseDto:
    def __init__(self,
        queueKey = None,
        subscriptionKey = None,
        url = None,
        tries = None,
        onErrorUrl = None,
        onErrorTries = None,
        maxTries = None,
        backOff = None,
        message = None,
        history = None
    ):
        self.queueKey = queueKey
        self.subscriptionKey = subscriptionKey
        self.url = url
        self.tries = StaticConverter.getValueOrDefault(tries, EmissionConstant.ZERO_TRIES)
        self.onErrorUrl = onErrorUrl
        self.onErrorTries = StaticConverter.getValueOrDefault(onErrorTries, EmissionConstant.ZERO_TRIES)
        self.maxTries = StaticConverter.getValueOrDefault(maxTries, EmissionConstant.DEFAULT_MAX_TRIES)
        self.backOff = StaticConverter.getValueOrDefault(backOff, EmissionConstant.DEFAULT_BACKOFF)
        self.message = message
        self.history = StaticConverter.getValueOrDefault(history, [])


class EmissionQueryRequestDto:
    def __init__(self,
        key = None,
        messageKey = None,
        queueKey = None,
        groupKey = None
    ):
        self.key = key
        self.messageKey = messageKey
        self.queueKey = queueKey
        self.groupKey = groupKey


class EmissionQueryResponseDto:
    def __init__(self,
        queueKey = None,
        subscriptionKey = None,
        url = None,
        tries = None,
        onErrorUrl = None,
        onErrorTries = None,
        maxTries = None,
        backOff = None,
        message = None,
        status = None,
        state = None,
        history = None
    ):
        self.queueKey = queueKey
        self.subscriptionKey = subscriptionKey
        self.url = url
        self.tries = StaticConverter.getValueOrDefault(tries, EmissionConstant.ZERO_TRIES)
        self.onErrorUrl = onErrorUrl
        self.onErrorTries = StaticConverter.getValueOrDefault(onErrorTries, EmissionConstant.ZERO_TRIES)
        self.maxTries = StaticConverter.getValueOrDefault(maxTries, EmissionConstant.DEFAULT_MAX_TRIES)
        self.backOff = StaticConverter.getValueOrDefault(backOff, EmissionConstant.DEFAULT_BACKOFF)
        self.message = message
        self.status = StaticConverter.getValueOrDefault(status, ModelConstant.DEFAULT_STATUS)
        self.state = StaticConverter.getValueOrDefault(state, ModelConstant.DEFAULT_STATE)
        self.history = StaticConverter.getValueOrDefault(history, [])
