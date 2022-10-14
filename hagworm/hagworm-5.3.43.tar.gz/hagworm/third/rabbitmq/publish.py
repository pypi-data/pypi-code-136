# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import asyncio
import aio_pika

from typing import List

from ...extend.base import Utils
from ...extend.asyncio.pool import ObjectPool


class RabbitMQProducer(aio_pika.RobustConnection):
    """RabbitMQ发布者
    """

    def __init__(self, url, **kwargs):

        super().__init__(url, **kwargs)

        self._channel: aio_pika.abc.AbstractRobustChannel = None

        self._lock: asyncio.Lock = asyncio.Lock()

    @property
    def current_channel(self) -> aio_pika.abc.AbstractRobustChannel:

        return self._channel

    async def connect(
            self, *,
            channel_number: int = None, publisher_confirms: bool = True, on_return_raises: bool = False,
            timeout: aio_pika.abc.TimeoutType = None
    ):

        await super().connect(timeout)

        await self.ready()

        if self._channel is None:
            self._channel = await self.channel(channel_number, publisher_confirms, on_return_raises)

    async def close(self):

        await self._channel.close()
        await super().close()

    async def publish(self, message, routing_key, **kwargs):

        async with self._lock:
            return await self._channel.default_exchange.publish(
                message if isinstance(message, aio_pika.Message) else aio_pika.Message(message),
                routing_key, **kwargs
            )


class RabbitMQProducerForExchange(RabbitMQProducer):
    """RabbitMQ交换机发布者
    """

    def __init__(self, url, **kwargs):

        super().__init__(url, **kwargs)

        self._exchange: aio_pika.abc.AbstractExchange = None

        self._exchange_name = None
        self._exchange_type = None
        self._exchange_config = None

    @property
    def current_exchange(self) -> aio_pika.abc.AbstractExchange:

        return self._exchange

    def config(
            self, exchange_name, exchange_type=aio_pika.ExchangeType.FANOUT,
            *, exchange_config=None
    ):

        self._exchange_name = exchange_name
        self._exchange_type = exchange_type
        self._exchange_config = exchange_config if exchange_config else {}

    async def connect(
            self, *,
            channel_number: int = None, publisher_confirms: bool = True, on_return_raises: bool = False,
            timeout: aio_pika.abc.TimeoutType = None
    ):

        await super().connect(
            channel_number=channel_number,
            publisher_confirms=publisher_confirms,
            on_return_raises=on_return_raises,
            timeout=timeout
        )

        if self._exchange is None:
            self._exchange = await self._channel.declare_exchange(
                self._exchange_name, self._exchange_type, **self._exchange_config
            )

    async def publish(self, message, routing_key=r'', **kwargs):

        async with self._lock:
            return await self._exchange.publish(
                message if isinstance(message, aio_pika.Message) else aio_pika.Message(message),
                routing_key, **kwargs
            )


class RabbitMQProducerPool(ObjectPool):
    """RabbitMQ发布者连接池
    """

    def __init__(self, url, pool_size, *, connection_config=None):

        self._mq_url = url

        self._connection_config = connection_config if connection_config else {}

        self._connections: List[RabbitMQProducer] = []

        super().__init__(pool_size)

    def _create_obj(self):

        connection = RabbitMQProducer(self._mq_url, **self._connection_config)

        self._connections.append(connection)

        return connection

    async def connect(
            self, *,
            publisher_confirms: bool = True, on_return_raises: bool = False,
            timeout: aio_pika.abc.TimeoutType = None
    ):

        for connection in self._connections:
            await connection.connect(
                publisher_confirms=publisher_confirms,
                on_return_raises=on_return_raises,
                timeout=timeout,
            )

        Utils.log.info(f'rabbitmq producer pool connected: {self._queue.qsize()}')

    async def close(self):

        for connection in self._connections:
            await connection.close()

    async def publish(self, message, routing_key=r'', **kwargs):

        async with self.get() as connection:
            return await connection.publish(
                message if isinstance(message, aio_pika.Message) else aio_pika.Message(message),
                routing_key, **kwargs
            )


class RabbitMQProducerForExchangePool(RabbitMQProducerPool):
    """RabbitMQ交换机发布者连接池
    """

    def __init__(
            self, url, pool_size, exchange_name,
            *, exchange_type=aio_pika.ExchangeType.FANOUT, exchange_config=None, connection_config=None
    ):

        self._exchange_name = exchange_name
        self._exchange_type = exchange_type
        self._exchange_config = exchange_config

        super().__init__(url, pool_size, connection_config=connection_config)

    def _create_obj(self):

        connection = RabbitMQProducerForExchange(self._mq_url, **self._connection_config)
        connection.config(self._exchange_name, self._exchange_type, exchange_config=self._exchange_config)

        self._connections.append(connection)

        return connection
