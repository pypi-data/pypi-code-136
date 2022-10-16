# coding=utf-8
"""looper-佛跳墙活套

[aslooper]
用来捕获 SIGINT, SIGTERM 信号后取消所有运行任务，
退出运行不引入asyncio报错。


[使用]
import asyncio
from aslooper import looper

# windows 系统不支持 uvloop，兼容 windows
try:
    import uvloop
except ImportError:
    class __Uvloop:
        @classmethod
        def install(cls):
            pass
    uvloop = __Uvloop


def youcall():
    pass


@looper(youcall)
async def main():
    while True:
        print("run something.")
        await asyncio.sleep(1)


uvloop.install()
asyncio.run(main())
"""

__version__ = "1.1.1b"
# 测试 task.cancel(msg="测试这个内容")

__all__ = ["looper"]


import asyncio
import functools
from signal import SIGINT, SIGTERM
from typing import Callable, Union, Awaitable
# from types import FunctionType


# def __cancel_all_tasks():
#     """取消所有任务
#
#     :return:
#     """
#     for task in asyncio.all_tasks():
#         if task is not asyncio.current_task():
#             print(f"Cancel Task {task}")
#             task.cancel()
#
#
# def __signal_cancel_run(call: Union[Callable, Awaitable] = None):
#     """取消所有任务，并执行自定义任务
#
#     :return:
#     """
#     loop = asyncio.get_running_loop()
#     for task in asyncio.all_tasks():
#         if task is not asyncio.current_task():
#             print(f"[Cancel Task] {task}")
#             task.cancel()
#     if call:
#         if asyncio.iscoroutinefunction(call):
#             loop.run_until_complete(call())
#         elif asyncio.iscoroutine(call):
#             loop.run_until_complete(call)
#         # elif isinstance(call, FunctionType):
#         #     call()
#         elif callable(call):
#             call()
#         else:
#             print(f"[Error Call] {call}")
#
#
# def looper(func, call: Union[Callable, Awaitable] = None):
#     """异步函数装饰器:
#     用来捕获 SIGINT, SIGTERM 信号后取消所有运行任务，退出运行不报错。
#     """
#     if not asyncio.iscoroutinefunction(func):
#         raise TypeError(f"{func} is not coroutinefunction.")
#
#     @functools.wraps(func)
#     async def loop_signal_handler(*args, **kwargs):
#         loop = asyncio.get_running_loop()
#         # Add signal
#         for signal in (SIGINT, SIGTERM):
#             try:
#                 loop.add_signal_handler(
#                     signal,
#                     # lambda: asyncio.create_task(__cancel_all_tasks(), name="signal_handler_call")
#                     # __cancel_all_tasks
#                     __signal_cancel_run,
#                     call
#                 )
#             except NotImplementedError:
#                 # logger.warning(
#                 #     "crawler tried to use loop.add_signal_handler "
#                 #     "but it is not implemented on this platform."
#                 # )
#                 pass
#         try:
#             return await func(*args, **kwargs)
#         except asyncio.CancelledError:
#             print("Exit!")
#
#     return loop_signal_handler


class Looper:
    """装饰器对象，用来装饰异步函数，用于取消异步任务。"""

    def __init__(self, call: Union[Callable, Awaitable] = None, *,
                 debug: bool = True):
        self.call = call
        self.debug = debug
        self.func = None  # 存放装饰的异步函数
        self.func_coroutine = None  # 存放装饰的异步函数协程对象

    def print(self, *args):
        if self.debug:
            print(*args)

    def __signal_cancel_run(self):
        """取消所有任务，并执行自定义任务"""
        loop = asyncio.get_running_loop()
        for task in asyncio.all_tasks():
            if task is not asyncio.current_task():
                self.print(f"[Cancel Task] {task}")
                task.cancel(msg=f"cancel task {task}")
        if self.call:
            if asyncio.iscoroutinefunction(self.call):
                loop.run_until_complete(self.call())
            elif asyncio.iscoroutine(self.call):
                loop.run_until_complete(self.call)
            # elif isinstance(self.call, FunctionType):
            #     self.call()
            elif callable(self.call):
                self.call()
            else:
                self.print(f"[Error Call] {self.call}")

    async def run_func(self):
        """用于__await__执行"""
        try:
            return await self.func_coroutine
        except asyncio.CancelledError:
            self.print("Exit!")

    def __await__(self):
        """
        必须定义这个方法才能直接 await 这个类的对象
        并且，返回值必须是一个 iterator，这里直接
        使用 async 函数的内置方法 __await__()
        """
        return self.run_func().__await__()

    def __call__(self, func):
        """异步函数装饰器:
        用来捕获 SIGINT, SIGTERM 信号后取消所有运行任务，退出运行不报错。
        """
        if not asyncio.iscoroutinefunction(func):
            raise TypeError(f"{func} is not coroutine function.")
        self.func = func

        @functools.wraps(func)
        async def loop_signal_handler(*args, **kwargs):
            loop = asyncio.get_running_loop()
            # Add signal
            for signal in (SIGINT, SIGTERM):
                try:
                    loop.add_signal_handler(
                        signal,
                        # lambda: asyncio.create_task(__cancel_all_tasks(), name="signal_handler_call")
                        self.__signal_cancel_run,
                    )
                except NotImplementedError:
                    # logger.warning(
                    #     "crawler tried to use loop.add_signal_handler "
                    #     "but it is not implemented on this platform."
                    # )
                    pass
            self.func_coroutine = self.func(*args, **kwargs)
            await self
        return loop_signal_handler


looper = Looper
