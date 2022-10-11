from __future__ import annotations
import asyncio
from dataclasses import dataclass
from enum import Enum
from typing import Coroutine, Callable, Dict, Type, List, Set, Any
from typing import TypeVar

import loguru
from aioprocessing import AioEvent, AioLock, AioQueue  # type: ignore
from loguru import logger
from web_foundation import settings


class IMessage:
    message_type: str = "__all__"
    index: int
    inner_index: int
    sender: str
    destination: str = "__all__"
    exec_inner: bool = False

    def __init__(self):
        self.index = 0
        self.inner_index = 0
        self.sender = "None"

    def __str__(self):
        return f"{self.__class__.__name__}({self.message_type},{self.index=},{self.inner_index=}, {self.sender=})"


GenericIMessage = TypeVar("GenericIMessage", bound=IMessage, contravariant=True)


@dataclass
class IsolatePipes:
    queue: AioQueue
    event: AioEvent
    lock: AioLock

    async def write(self, msg: GenericIMessage):
        await self.queue.coro_put(msg)

    async def read(self) -> GenericIMessage:
        return await self.queue.coro_get()

    def empty(self):
        return self.queue.empty()


EventListener = Callable[[GenericIMessage], Coroutine]


class MessageWaitState(Enum):
    PENDING = "PENDING"
    DONE = "DONE"


class IMessageWaiter:
    event = asyncio.Event()
    result: Any = None
    call = None

    def __eq__(self, other):
        self.wait_for_index = other.wait_for_index


class IChannel:
    read_timeout = 0.01
    worker_name: str
    consume_pipe: IsolatePipes
    produce_pipe: IsolatePipes

    _listeners: Dict[str, List[EventListener]]
    _once_listeners: Dict[str, EventListener]
    _response_waiters: Dict[int, IMessageWaiter]

    _before_event_middlewares: Dict[str, EventListener]
    _after_event_middlewares: Dict[str, EventListener]
    _inner_index: int

    def __init__(self, isolate_name: str):
        self._inner_index = 0
        self.worker_name = isolate_name
        # self.debug = debug
        self._listeners = {}
        self._once_listeners = {}
        self._response_waiters = {}
        self.produce_pipe = IsolatePipes(AioQueue(), AioEvent(), AioLock())
        self.consume_pipe = IsolatePipes(AioQueue(), AioEvent(), AioLock())
        self._after_event_middlewares = {}
        self._before_event_middlewares = {}

    def __str__(self):
        return f"IChannel(name={self.worker_name})"

    async def produce(self, msg: IMessage):
        self._inner_index += 1
        msg.inner_index = self._inner_index
        msg.sender = self.worker_name
        before_middleware = self._before_event_middlewares.get(msg.message_type)
        if before_middleware:
            await before_middleware(msg)
        if msg.exec_inner:
            listeners = self._listeners.get(msg.message_type)
            for listener in listeners:
                asyncio.create_task(listener(msg))
        await self.produce_pipe.write(msg)

    async def sent_to_consume(self, msg: IMessage):
        await self.consume_pipe.write(msg)

    async def listen_produce(self, callback: Callable[[GenericIMessage], Coroutine]):
        while True:
            r: GenericIMessage = await self.produce_pipe.read()
            if settings.DEBUG:
                logger.info(
                    f"Channel {self.worker_name} send message: {r.message_type}")
            await callback(r)

    async def listen_consume(self):
        while True:
            r: IMessage = await self.consume_pipe.read()
            if settings.DEBUG:
                logger.info(
                    f"Channel {self.worker_name} receive message: {r.message_type}")
            once_callback = self._once_listeners.get(r.message_type)
            if once_callback:
                asyncio.create_task(self._exec_once(r, once_callback))
            after_middleware = self._after_event_middlewares.get(r.message_type)
            if after_middleware:
                asyncio.create_task(after_middleware(r))
            response_waiter = self._response_waiters.get(r.inner_index)
            if response_waiter:
                response_waiter.result = r
            callbacks = self._listeners.get(r.message_type)
            if not callbacks:
                continue
            for callback in callbacks:
                asyncio.create_task(callback(r))

    async def _exec_once(self, msg: GenericIMessage, callback: EventListener):
        await callback(msg)
        self._once_listeners.pop(msg.message_type)

    def add_event_middleware(self, event_type: str, callback: EventListener, assign_to: str = "after"):
        """
        :param callback: callback to call
        :param event_type: "event_message_type"
        :param assign_to: "before, after"
        :return: None
        """
        match assign_to:
            case 'before':
                self._before_event_middlewares.update({event_type: callback})
            case "after":
                self._after_event_middlewares.update({event_type: callback})

    async def produce_for_response(self, msg: GenericIMessage) -> Any:
        task = IMessageWaiter()
        await self.produce(msg)
        self._response_waiters.update({msg.inner_index: task})
        while not task.result:
            await asyncio.sleep(0.01)
        self._response_waiters.pop(msg.inner_index)
        return task.result

    def _add_event_listener(self, event_type: Type[IMessage] | str, callback: EventListener,
                            use_nested_classes: bool = False):
        if use_nested_classes and isinstance(event_type, str):
            raise AttributeError("Can't add_event_listener with use_nested_classes")

        def _add(event_name: str):
            nonlocal self
            nonlocal callback
            if event_name not in self._listeners:
                self._listeners[event_name] = []
            self._listeners[event_name].append(callback)

        if isinstance(event_type, str):
            _add(event_type)
        else:
            def _raise(cls_type):
                if not hasattr(cls_type, "message_type"):
                    raise AttributeError("Can't register listener cause message_type not found")

            if use_nested_classes:
                for cls in event_type.__subclasses__():
                    _raise(cls)
                    _add(cls.message_type)
            else:
                _raise(event_type)
                _add(event_type.message_type)

    def add_event_listener(self, event_type: List[Type[IMessage] | str] | Type[IMessage] | str,
                           callback: EventListener, use_nested_classes: bool = False):
        if isinstance(event_type, list):
            for i in event_type:
                self._add_event_listener(i, callback, use_nested_classes)
        else:
            self._add_event_listener(event_type, callback, use_nested_classes)

    def add_once_listener(self, event_type: str, callback: EventListener):
        self._once_listeners.update({event_type: callback})

    def remove_event_listeners(self, event_type: Type[IMessage] | str):
        if isinstance(event_type, str):
            self._listeners.pop(event_type)
        else:
            self._listeners.pop(event_type.message_type)

    @property
    def listeners(self):
        return self._listeners
