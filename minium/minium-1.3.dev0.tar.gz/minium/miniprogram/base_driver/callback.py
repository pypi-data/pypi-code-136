"""
callback类, 供hook等需要callback的场景使用
"""
import types
import threading
import sys

from ...framework.exception import MiniTimeoutError
from ...utils.eventloop import event_loop
from ...utils.utils import async_wait, WaitTimeoutError, Future, EventLoop


class Callback(object):
    def __init__(self, callback: types.FunctionType = None) -> None:
        self.__callback = callback
        self.__called = threading.Semaphore(0)
        self.__is_called = False
        self.__callback_result = None

    def callback(self, args):
        self.__is_called = True
        self.__callback_result = args[0] if args and len(args) == 1 else args
        self.__called.release()
        if self.__callback:
            self.__callback(*args)

    @property
    def is_called(self):
        return self.__is_called

    def wait_called(self, timeout=10) -> bool:
        """
        等待回调调用, 默认等待最多10s
        """
        if self.__is_called:
            return True
        return self.__called.acquire(timeout=timeout)

    def get_callback_result(self, timeout=0) -> any:
        """
        获取回调结果, 超时未获取到结果报AssertionError
        1. 回调参数只有一个的情况会解构
        2. 回调参数中有多个的情况会直接返回参数list
        """
        if self.wait_called(timeout):
            return self.__callback_result
        assert self.__is_called, f"No callback received within {timeout} seconds"


class AsyncCallback(object):
    def __init__(self, loop: EventLoop = None) -> None:
        if loop is None:
            self._loop = event_loop
        else:
            self._loop = loop
        self._is_called = False
        self._waiter: Future = self._loop.create_future()

    async def set_result(self, args):
        if not self._waiter.done():
            self._is_called = True
            result = args[0] if args and len(args) == 1 else args
            if isinstance(result, BaseException):
                self._waiter.set_exception(result)
            else:
                self._waiter.set_result(result)

    def cancel(self):
        self._waiter.cancel()

    def callback(self, *args):
        if not self._waiter.done():
            self._loop.run_coroutine(self.set_result(args))

    @property
    def is_called(self):
        return self._waiter.done()

    def wait_called(self, timeout=10) -> bool:
        """
        等待回调调用, 默认等待最多10s
        """
        if timeout == 0:
            return self._waiter.done()
        if self._waiter.done():
            return True
        try:
            return self._loop.run_coroutine(async_wait(self._waiter, timeout, self._loop)).result()
        except WaitTimeoutError:
            return False
        except:
            return self._waiter.done()

    def get_callback_result(self, timeout=0) -> any:
        if self.wait_called(timeout):
            try:
                return self._waiter.result()
            except:
                return sys.exc_info()[1]
        assert self._is_called, f"No callback received within {timeout} seconds"

    def get_result(self, timeout=0):
        """
        获取回调结果, 结果如果为exception直接抛出, 超时未获取到则抛MiniTimeoutError
        """
        if self.wait_called(timeout):
            return self._waiter.result()
        raise MiniTimeoutError(f"No callback received within {timeout} seconds")
