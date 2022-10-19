#!/usr/bin/env python
# encoding: utf-8
from .helper import Helper
from .asyncWrapper import AsyncWrapper
import json
import asyncio
import sys
import logging
import pulsar
import contextvars
import uuid

logger = logging.getLogger(__name__)


class ConsumerHelper(Helper):
    """
    消费者辅助
    """

    def __init__(self):
        super(ConsumerHelper, self).__init__()

        self._offsetDict = {}
        self._loop = asyncio.get_event_loop()
        self._is_debug = False

        # 是否停止消费标记z
        self._stop_consume_dict = {}

        self._poll_tasks = []
        self._poll_task_running = False
        # self._loop.call_later(0.0001,self._loop.create_task,self._poll_task())
        self._client = None
        self._consumer_dict = {}

    def _init_client(self):
        self._client = pulsar.Client(self._config["url"])

    def open_debug(self):
        self._is_debug = True

    async def _poll_task(self):
        for task in self._poll_tasks:
            fn, params = task
            await fn(params)
        self._loop.call_later(0.000001, self._loop.create_task, self._poll_task())

    async def poll_task(self):
        for task in self._poll_tasks:
            fn, params = task
            await fn(params)

    def convert_properties_to_dict(self, properties):
        if isinstance(properties, dict):
            return properties
        d = {}
        for property in properties:
            key = property.key()
            value = properties[key]
            d[key] = value

        return d

    def receive_async(self, topic: str, subscription_name: str, work: callable):
        """
        订阅一系列主题，work 是处理接收到消息的方法
        此方法是异步执行
        """
        if not self.persistent:
            topic = "non-persistent://" + topic

        async def receive_message(t):
            consumer_async, work, topic = t
            if not self._stop_consume_dict[topic]:
                msg = None
                try:
                    msg = await consumer_async.receive(timeout_millis=5)
                except Exception as e:
                    return
                if msg:
                    try:
                        if self._is_debug:
                            logger.debug(
                                "Received message '{}' id='{}' properties='{}' ".format(
                                    msg.data(), msg.message_id(), msg.properties()
                                )
                            )

                        data = msg.data()
                        properties = self.convert_properties_to_dict(msg.properties())
                        if "sendTo" not in properties:
                            properties["sendTo"] = topic

                        # print(properties)
                        messageId = properties.get("messageId")
                        token = self.set_message_id(messageId)
                        if asyncio.iscoroutine(work) or asyncio.iscoroutinefunction(
                            work
                        ):
                            await work(data, properties)
                        else:
                            work(data, properties)
                        await consumer_async.acknowledge(msg)
                        self.reset_message_id(token)
                    except Exception as e:
                        logger.exception(e)

        if self._client is None:
            self._init_client()
        # if self._config['tenant'] not in topic:
        # topic =f"{self._config['tenant']}/{self._config['namespace']}/{topic}"
        consumer = self._client.subscribe(
            topic, subscription_name, consumer_type=pulsar.ConsumerType.Shared
        )
        self._consumer_dict[topic + "-" + subscription_name] = consumer
        c_async = AsyncWrapper(consumer, methods=["receive", "acknowledge"])
        self._stop_consume_dict[topic] = False
        self._poll_tasks.append((receive_message, (c_async, work, topic)))
        if not self._poll_task_running:
            self._loop.call_later(0.000001, self._loop.create_task, self._poll_task())
            self._poll_task_running = True

    def stop_consumer(self, topics: list):
        """
        停止接收信息
        """

        key = "_".join(topics)
        logger.info("{0} 停止接收信息".format(key))
        self._stop_consume_dict[key] = True

    def is_connected(self):

        for topic in self._consumer_dict:
            if not self._consumer_dict[topic].is_connected():
                return False

        return True
