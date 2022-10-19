from python_framework import StaticConverter

try:
    import ModelConstant
except:
    from queue_manager_api.api.src.constant import ModelConstant


class MessageRequestDto:
    def __init__(self,
        key = None,
        queueKey = None,
        groupKey = None,
        headers = None,
        content = None
    ):
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey
        self.headers = headers
        self.content = content


class MessageResponseDto:
    def __init__(self,
        key = None,
        queueKey = None,
        groupKey = None,
        content = None,
        history = None
    ):
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey
        self.content = content
        self.history = history


class MessageCreationRequestDto:
    def __init__(self,
        key = None,
        queueKey = None,
        groupKey = None
    ):
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey

class MessageCreationResponseDto:
    def __init__(self,
        key = None,
        queueKey = None,
        groupKey = None
    ):
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey

class MessageQueryRequestDto:
    def __init__(self,
        key = None,
        queueKey = None,
        groupKey = None
    ):
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey


class MessageQueryResponseDto:
    def __init__(self,
        key = None,
        queueKey = None,
        groupKey = None,
        content = None,
        history = None,
        status = None,
        state = None
    ):
        self.key = key
        self.queueKey = queueKey
        self.groupKey = groupKey
        self.content = content
        self.history = history
        self.status = StaticConverter.getValueOrDefault(status, ModelConstant.DEFAULT_STATUS)
        self.state = StaticConverter.getValueOrDefault(state, ModelConstant.DEFAULT_STATE)
