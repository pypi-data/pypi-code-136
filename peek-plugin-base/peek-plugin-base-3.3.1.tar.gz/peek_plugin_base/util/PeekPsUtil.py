import logging
import os

import psutil
from twisted.internet.task import LoopingCall
from vortex.DeferUtil import vortexLogFailure

from peek_plugin_base.LoopingCallUtil import peekCatchErrbackWithLogger

logger = logging.getLogger(__name__)


class PeekPsUtil:
    # For the CPU load, we should be polling regularly to get an accurate result
    __LOOPING_CALL_PERIOD = 1.0
    # Singleton
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PeekPsUtil, cls).__new__(cls)
            # Lazy load the instance
            cls._instance.__singleton_init__()

        return cls._instance

    def __singleton_init__(self):
        self.__process = psutil.Process(os.getpid())
        self.__cpuPercent = 0.0

        self.__loopingCall = LoopingCall(
            peekCatchErrbackWithLogger(logger)(self.__loopingCallTask)
        )

        d = self.__loopingCall.start(self.__LOOPING_CALL_PERIOD)
        d.addErrback(vortexLogFailure, logger)

    def __loopingCallTask(self):
        self.__cpuPercent = self.__process.cpu_percent()

    @property
    def cpuPercent(self):
        return self.__cpuPercent

    @property
    def memoryInfo(self):
        return self.__process.memory_info()
