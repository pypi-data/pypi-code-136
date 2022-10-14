#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Author:         yopofeng
Filename:       utils.py
Create time:    2021/9/24 21:21
Description:

"""
import time
from functools import wraps
import typing
import types
import platform
import re
import sys
import inspect
import threading
import logging
import os
import asyncio
import functools
import concurrent.futures

logger = logging.getLogger("minium")


def timeout(duration, interval=1):
    """
    重试超时装饰器,在超时之前会每隔{interval}秒重试一次
    注意：被修饰的函数必须要有非空返回,这是重试终止的条件！！！
    :param duration: seconds
    :return:
    """

    def spin_until_true(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timeout = time.time() + duration
            execed = False
            r = None
            while not (r or timeout < time.time() and execed):
                r = func(*args, **kwargs)
                execed = True
                if r or timeout < time.time():
                    return r
                time.sleep(interval)
            return r

        return wrapper

    return spin_until_true


def retry(cnt, expected_exception=None):
    """
    重试固定次数装饰器, 被修饰函数没有raise error则直接返回，有则最多执行${cnt}次
    :cnt: 重试次数，函数最多被执行 ${cnt} 次
    :expected_exception: 命中预期的错误才重试，None为所有错误
    """

    def try_until_no_error(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _cnt = 0
            while _cnt < cnt:
                try:
                    _cnt += 1
                    # print("try %d" % _cnt)
                    return func(*args, **kwargs)
                except:
                    if _cnt >= cnt:
                        raise
                    e = sys.exc_info()[1]
                    if expected_exception and isinstance(
                        expected_exception, (tuple, list)
                    ):
                        if e.__class__ in expected_exception:
                            continue
                    elif expected_exception:
                        if e.__class__ == expected_exception:
                            continue
                    else:
                        continue
                    raise

        return wrapper

    return try_until_no_error


def catch(*args):
    """
    抓获指定/所有exception
    :wrapped: 被修饰的函数, 如果为空则作为修饰器使用
    :expected_exception: 指定/所有exception
    :return: Exception/None
    """
    wrapped = None
    expected_exception = None
    if len(args) == 0:
        expected_exception = None
    elif len(args) == 1:
        if inspect.isfunction(args[0]) or inspect.ismethod(args[0]):
            wrapped = args[0]
        else:
            expected_exception = args[0]
    elif len(args) == 2:
        wrapped, expected_exception = args
    else:
        raise TypeError(f"catch takes at most 2 argument but {len(args)} were given")

    def try_catch(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                e = sys.exc_info()[1]
                if expected_exception and isinstance(expected_exception, (tuple, list)):
                    if e.__class__ in expected_exception:
                        return e
                elif expected_exception:
                    if e.__class__ == expected_exception:
                        return e
                else:
                    return e
                raise

        return wrapper

    if wrapped:
        return try_catch(wrapped)
    # 修饰器用法
    return try_catch


class WaitTimeoutError(TimeoutError):
    pass


TimeoutErrors = (TimeoutError, WaitTimeoutError, asyncio.exceptions.TimeoutError)


class WaitThread(threading.Thread):
    def __init__(
        self,
        group=None,
        target=None,
        name=None,
        args=(),
        kwargs=None,
        daemon=None,
        semaphore=None,
    ):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self._result = None
        self._exception = None
        self._semaphore: threading.Semaphore = semaphore

    def run(self):
        try:
            if self._target:
                self._result = self._target(*self._args, **self._kwargs)
        except:
            self._exception = sys.exc_info()[1]
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
            if self._semaphore:
                self._semaphore.release()

    def get_result(self, timeout=None, block=True):
        if block:
            self.join(timeout=timeout)
        if self._exception:
            raise self._exception
        if block and self.is_alive():
            raise WaitTimeoutError("wait [%s] seconds timeout" % timeout)
        return self._result


def wait(timeout, default=None):
    """
    等待修饰器
    等待timeout时间, 如果函数没有返回则返回default
    """

    def spin_until_true(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t = WaitThread(target=func, args=args, kwargs=kwargs)
            t.setDaemon(True)
            t.start()
            try:
                return t.get_result(timeout)
            except WaitTimeoutError:
                logger.error("wait %s %ss timeout" % (func.__name__, timeout))
                return default

        return wrapper

    return spin_until_true


_platform = platform.platform()
isWindows = "Windows" in _platform
isMacOS = "Darwin" in _platform or "macOS" in _platform


class Version(object):
    def __init__(self, version: str) -> None:
        m = re.match(r"^([0-9\.]+|latest|dev)", version or "")
        if not m:
            raise ValueError(f"{version} format not collect")
        self.version = "latest" if m.group(1) in ("latest", "dev") else m.group(1)

    def __str__(self) -> str:
        return self.version

    def __comp_version(self, a: str, b: str) -> int:
        """
        description: 对比基础库版本
        param {*} self
        param {str} a
        param {str} b
        return {int} 1 if a > b, 0 if a == b ,-1 if a < b
        """
        latest = ("latest", "dev")  # latest, dev版本看作是最大的版本号
        if a in latest:
            return 0 if b in latest else 1
        if b in latest:
            return 0 if a in latest else 1
        i = 0
        a = a.split(".")
        b = b.split(".")
        while i < len(a) and i < len(b):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(a[i]) < int(b[i]):
                return -1
            i += 1
        return 0

    def __lt__(self, version):
        if isinstance(version, str):
            version = Version(version)
        if self.__comp_version(self.version, version.version) == -1:
            return True
        return False

    def __gt__(self, version):
        if isinstance(version, str):
            version = Version(version)
        if self.__comp_version(self.version, version.version) == -1:
            return False
        return True

    def __le__(self, version):
        if isinstance(version, str):
            version = Version(version)
        if self.__comp_version(self.version, version.version) != 1:
            return True
        return False

    def __ge__(self, version):
        if isinstance(version, str):
            version = Version(version)
        if self.__comp_version(self.version, version.version) != -1:
            return True
        return False

    def __eq__(self, version):
        if isinstance(version, str):
            version = Version(version)
        return self.version == version.version


def add_path_to_env(path: str):
    """
    把路径添加到PATH环境变量中
    """
    SPLIT = ":" if isMacOS else ";"
    _path = path if os.path.isdir(path) else os.path.dirname(path)
    env_paths = (os.environ["PATH"] or "").split(SPLIT)
    if _path not in env_paths:
        env_paths.append(_path)
    os.environ["PATH"] = SPLIT.join(env_paths)


class ProcessSafeEventLoop(object):
    def __init__(self) -> None:
        self.pid = os.getpid()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.run_loop()

    def run_loop(self):
        threading.Thread(target=self.loop.run_forever, daemon=True).start()

    def stop_loop(self):
        self.loop.stop()

    def run_coroutine(self, coro):
        """Submit a coroutine object to a given event loop.

        Return a concurrent.futures.Future to access the result.
        """
        if os.getpid() != self.pid:
            self.pid = os.getpid()
            self.loop = asyncio.new_event_loop()
            self.run_loop()
        return asyncio.run_coroutine_threadsafe(coro, loop=self.loop)

    def is_running(self):
        return self.loop.is_running()

    def __getattr__(self, name):
        return getattr(self.loop, name)


async def _cancel_and_wait(fut, loop):
    """Cancel the *fut* future or task and wait until it completes."""

    waiter = loop.create_future()
    cb = functools.partial(_release_waiter, waiter)
    fut.add_done_callback(cb)

    try:
        fut.cancel()
        # We cannot wait on *fut* directly to make
        # sure _cancel_and_wait itself is reliably cancellable.
        await waiter
    finally:
        fut.remove_done_callback(cb)


def _release_waiter(waiter, *args):
    if not waiter.done():
        waiter.set_result(None)


async def async_wait(
    fut, timeout, loop: ProcessSafeEventLoop or asyncio.AbstractEventLoop = None
):
    """
    reference asyncio.wait_for
    wait fut done, when timeout, raise 
    """
    if loop is None:
        loop = asyncio.get_running_loop()
    elif isinstance(loop, ProcessSafeEventLoop):
        loop = loop.loop
    else:
        loop = loop
    waiter = loop.create_future()
    cb = functools.partial(_release_waiter, waiter)
    fut = asyncio.ensure_future(fut, loop=loop)
    fut.add_done_callback(cb)
    timeout_handle = loop.call_later(timeout, _release_waiter, waiter)

    try:
        # wait until the future completes or the timeout WaitTimeoutError
        try:
            await waiter
        except asyncio.exceptions.CancelledError:
            if fut.done():
                return fut.result()
            else:
                fut.remove_done_callback(cb)
                # We must ensure that the task is not running
                # after wait_for() returns.
                # See https://bugs.python.org/issue32751
                await _cancel_and_wait(fut, loop=loop)
                raise

        if fut.done():
            return fut.result()
        else:
            fut.remove_done_callback(cb)
            # We must ensure that the task is not running
            # after wait_for() returns.
            # See https://bugs.python.org/issue32751
            await _cancel_and_wait(fut, loop=loop)
            # In case task cancellation failed with some
            # exception, we should re-raise it
            # See https://bugs.python.org/issue40607
            try:
                fut.result()
            except asyncio.exceptions.CancelledError as exc:
                raise WaitTimeoutError() from exc
            else:
                raise WaitTimeoutError()
    finally:
        timeout_handle.cancel()


class AsyncCondition(asyncio.Condition):
    def __init__(
        self, lock: asyncio.Lock = None, *, loop: asyncio.AbstractEventLoop or ProcessSafeEventLoop = None
    ) -> None:
        if isinstance(loop, ProcessSafeEventLoop):
            loop = loop.loop
        if sys.version_info < (3, 10):
            super().__init__(lock, loop=loop)
        else:  # loop参数将在3.10废除
            asyncio.set_event_loop(loop)
            super().__init__(lock)

    async def wait(self, timeout=None):
        loop = self._loop
        coro = super().wait()
        if timeout is None:
            return await coro
        try:
            return await async_wait(coro, timeout=timeout, loop=loop)
        except WaitTimeoutError:
            return False

Future = typing.Union[asyncio.futures.Future, concurrent.futures.Future]
EventLoop = typing.Union[ProcessSafeEventLoop, asyncio.BaseEventLoop]

def get_result(
    fut: Future,
    timeout=None,
    default=None,
):
    # asyncio.futures.Future.result 去掉了timeout参数
    if isinstance(fut, concurrent.futures.Future):
        try:
            return fut.result(timeout)
        except concurrent.futures.TimeoutError as ext:
            if default is not None:
                return default
            raise WaitTimeoutError() from ext
    loop = fut.get_loop()
    try:
        return asyncio.run_coroutine_threadsafe(
            async_wait(fut, timeout=timeout, loop=loop), loop=loop
        ).result()
    except WaitTimeoutError as ext:
        if default is not None:
            return default
        raise WaitTimeoutError() from ext
