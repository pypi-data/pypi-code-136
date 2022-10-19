from python_framework import StaticConverter


class QueueRequestDto:
    def __init__(self,
        key = None,
        subscriptionList = None
    ):
        self.key = key
        self.subscriptionList = StaticConverter.getValueOrDefault(subscriptionList, [])


class QueueResponseDto:
    def __init__(self,
        key = None,
        subscriptionList = None
    ):
        self.key = key
        self.subscriptionList = StaticConverter.getValueOrDefault(subscriptionList, [])
