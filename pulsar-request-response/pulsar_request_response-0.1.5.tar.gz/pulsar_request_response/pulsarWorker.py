#!/usr/bin/env python
# encoding: utf-8
from .kafkapacket_pb2 import KafkaPacket
from .packagewrapper_pb2 import PackageWrapperRequest, PackageWrapperResponse
from . import packagewrapper_pb2
from .producer_helper import ProducerHelper
from .consumer_helper import ConsumerHelper
from .publishesMessage import PublishesMessage
from .workerDelegate import WorkerDelegate
from typing import Optional, Dict, List, Any
import asyncio
import traceback
import uuid
import time
import logging
import pulsar
import contextvars
import json
import sys
import os

# from loguru import logger

logger = logging.getLogger(__name__)


class PulsarWorker(object):
    """ """

    def __init__(
        self,
        host: str,
        tenant: str,
        namespace: str = "",
        private_topic: str = "",
        auth_token: str = "",
        is_debug=False,
    ):
        """

        :params host pulsar 集群节点
        :params private_topic 私人topic，用于发送信息后接收响应的信息
        """
        self._message_context = contextvars.ContextVar("message id")
        logger.info("pulsar worker init.")
        host = f"pulsar://{host}"
        self._tenant = tenant
        self._namespace = namespace
        if auth_token:
            from pulsar import AuthenticationToken

            self._client = pulsar.Client(
                host, authentication=AuthenticationToken(auth_token)
            )

        else:
            self._client = pulsar.Client(host)

        if private_topic != "":
            private_topic = f"{tenant}/{namespace}/{private_topic}"
        else:
            private_topic = f"{tenant}/{namespace}/{str(uuid.uuid4())}"

        self._producer = ProducerHelper()
        self._producer._client = self._client
        self._producer._message_context = self._message_context
        self._producer.config_servers(host)
        self._producer.config_tenant(tenant)
        self._producer.config_namespace(namespace)

        self._consumer = ConsumerHelper()
        self._consumer._client = self._client
        self._message_context = self._message_context
        self._consumer.config_servers(host)
        self._consumer.config_tenant(tenant)
        self._consumer.config_namespace(namespace)

        # 发出信息后，等待响应的信息列表
        self._wait_response_message: Dict[str, PublishesMessage] = {}
        # 注册接收指定topic 的消费者
        self._consumer_registers: Dict[str, callable] = {}
        # 如果指定routingKey，就使用topic+routingKey实现分发方法。(在这里routingKey和method都是用于分发调用业务方法，可认为是等价)
        self._method_registers: Dict[str, callable] = {}
        # 因为可能会往一些没有存在是topic发送信息，所以需要正式发送前发送hello 信息
        self._register_topic: Dict[str, int] = {}

        # 用于检测到pulsar 连接断掉后，重新订阅
        self._recover_register = {}
        # 失败次数
        self._fail_count = 0

        self._private_topic = private_topic
        # self._private_topic = str(uuid.uuid4())

        self.event_loop = asyncio.get_event_loop()

        # self._register_private_topic()
        self._open_private_topic()
        if is_debug:
            self._consumer.open_debug()

        self.event_loop.call_later(3, self.event_loop.create_task, self._health_check())

    def set_message_non_persistent(self):
        """配置消息非持久化"""
        self._producer.persistent = False
        self._consumer.persistent = False

    async def _on_message(
        self,
        message: KafkaPacket,
        request: PackageWrapperRequest,
    ):
        """
        当接收到kafka 信息的时候会触发调用这个方法
        分两种情况，1 发送的信息后收到的回复 2 接收到新信息
        """
        logger.debug(
            "_on_message, _wait_response_message length:{}".format(
                self._wait_response_message
            )
        )
        logger.debug(message)
        if message.correlationId in self._wait_response_message:
            # 发送信息后收到的回复
            publish_message = self._wait_response_message[message.correlationId]
            del self._wait_response_message[message.correlationId]
            logger.debug(
                "response msg.correlationId, msg.body: {0}, {1}".format(
                    message.correlationId, message.body
                )
            )
            # publish_message.callback(message)
            worker_delegate = WorkerDelegate(
                publish_message.callback, message, self._private_topic
            )
            await worker_delegate.executor()
        else:
            # 接收到新的信息后查询处理方法，如果没有注册，则丢弃
            if message.sendTo in self._consumer_registers:
                deal_function = self._consumer_registers[message.sendTo]
                if message.routingKey:
                    key = "{0}-{1}".format(message.sendTo, message.routingKey)
                    if key in self._method_registers:
                        deal_function = self._method_registers[key]

                worker_delegate = WorkerDelegate(
                    deal_function, message, self._private_topic
                )
                response_publish_message = await worker_delegate.executor()
                # 查询信息中包含的是否需要回复消息，没有replyTo即不需要，就不发送回复信息
                if message.replyTo:
                    self._send_message(response_publish_message, request)

    def _send_message(self, message, request=None):
        """
        发送信息
        """
        self._register_private_topic()
        if isinstance(message, PublishesMessage):
            if request is None:

                value = message.to_protobuf()
                is_reply = message.is_reply
                need_reply = True if message.reply_to else False
                if not message.send_to in self._register_topic:
                    self._register_topic[message.send_to] = 1
                if value.body:
                    self._producer.send(value, message.send_to)
                    logger.debug("_send_message: {}".format(message.to_dict()))
                    if not is_reply and need_reply:
                        self._wait_response_message[message.correlation_id] = message
            if request:
                body = message.payload
                response = PackageWrapperResponse()
                response.uid.append(request.uid)
                response.personid.append(request.personid)
                response.mode = packagewrapper_pb2.Unicast
                response.useragent = request.useragent
                response.bizcode = request.bizcode
                response.requestid = request.requestid
                response.client = request.client
                if isinstance(body, (dict)):
                    body["requestId"] = request.requestid
                    body = json.dumps(body).encode("utf-8")
                if isinstance(body, str):
                    body = body.encode("utf-8")

                response.payload = body

                logger.info(response)

                is_reply = message.is_reply
                need_reply = True if message.reply_to else False
                if not message.send_to in self._register_topic:
                    self._register_topic[message.send_to] = 1
                if response.payload:
                    self._producer.send(response, message.send_to)
                    logger.debug("_send_message: {}".format(message.to_dict()))
        else:

            if not message.sendTo in self._register_topic:
                self._open_topic(message.sendTo)
                self._register_topic[message.sendTo] = 1
            if message.body:

                self._producer.send(message, message.send_to)
                logger.debug("_send_message: {}".format(message))

    def gen_ws_reply_to(self, send_to, reply_to):
        """根据接收人的topic 来生产ws 接收消息的topic"""
        arr = str(send_to).split("/")
        arr[-1] = reply_to
        return "/".join(arr)

    async def _bind_to_on_message(self, value, properties=None):
        """
        绑定消费者收到信息后调用 _on_message
        """
        if value is None:
            return
        logger.debug("_bind_to_on_message: {}".format(value))
        # logger.info(properties)
        # print(properties)
        try:
            packet = None
            request = None
            if (
                properties
                and str(properties.get("ContentType","")).lower() in 
                [ "application/protobuf/packagewrapper","application/protobuf/packagewrapperrequest"]
            ):
                # 说明请求来自ws a110 ,需要用ws 的protobuf 加载数据
                request = PackageWrapperRequest()
                request.ParseFromString(value)
                reply_to = self.gen_ws_reply_to(
                    properties.get("sendTo"), properties.get("ReplyTo")
                )
                # reply_to = properties.get("ReplyTo")
                correlationId = str(uuid.uuid4())
                logger.info(request)
                packet = KafkaPacket()
                packet.body = request.payload
                packet.correlationId = correlationId
                packet.replyTo = reply_to
                packet.messageId = correlationId
                packet.sendTo = properties.get("sendTo")

            else:
                packet = KafkaPacket()
                packet.ParseFromString(value)
            await self._on_message(packet, request)
        except Exception as e:
            logger.exception(traceback.format_exc())
            logger.exception(e)
            logger.error(f"properties:{properties}")
            if properties is not None and properties.get("replyTo"):
                replyTo = properties.get("replyTo")
                error_response = {"code": -1, "message": str(e)}
                await self.send(
                    replyTo,
                    json.dumps(error_response).encode("utf-8"),
                    content_type=properties.get("contentType"),
                    message_id=properties.get("messageId"),
                )

    def subscribe(
        self, topic: str, subscription_name: str, work: callable, routingKey=""
    ):
        """
        订阅主题
        """
        if self._tenant not in topic:
            topic = f"{self._tenant}/{self._namespace}/{topic}"

        logger.debug("subscribe topic: {}".format(topic))
        if topic not in self._consumer_registers:
            self._consumer.receive_async(
                topic, subscription_name, self._bind_to_on_message
            )
            self._consumer._loop.call_later(
                0.01, self._consumer._loop.create_task, self._consumer._poll_task()
            )

            self._consumer_registers[topic] = work
            # 把订阅过的topic都存储起来，用于恢复
            self._recover_register[topic] = {
                "topic": topic,
                "subscription_name": subscription_name,
                "work": work,
                "routingKey": routingKey,
            }
        key = "{0}-{1}".format(topic, routingKey)

        if key not in self._method_registers:
            self._method_registers[key] = work

    def _open_topic(self, topic):
        """
        多次发送保障打开通道
        """

    def _open_private_topic(self):
        """
        多次发送保障打开通道
        """
        # asyncio.sleep(0.01)

    def _register_private_topic(self):
        """
        注册私密的topic,用于发送信息后接收到信息
        """
        if self._private_topic == "":
            return
        if self._private_topic not in self._consumer_registers:
            self._open_topic(self._private_topic)
        subscription_name = str(uuid.uuid4())
        self.subscribe(self._private_topic, subscription_name, lambda no_use: no_use)

    async def send(
        self,
        topic: str,
        message: bytes,
        content_type: str = None,
        content_encoding: str = "utf-8",
        group_id: str = "0",
        message_id: str = None,
        msg_type: str = None,
        user_id: str = None,
        app_id: str = None,
        headers: dict = None,
        need_reply: bool = True,
        routing_key: str = None,
    ):
        """
        发送信息
        """
        logger.info("send message: {}".format(message))
        waiter = self.event_loop.create_future()

        def for_callback(response):
            waiter.set_result(response)
            return waiter.result()

        reply_to = self._private_topic if need_reply else None

        publish_message = PublishesMessage(
            payload=message,
            reply_to=reply_to,
            send_to=topic,
            correlation_id="",
            content_type=content_type,
            content_encoding=content_encoding,
            group_id=group_id,
            message_id=message_id,
            msg_type=msg_type,
            user_id=user_id,
            app_id=app_id,
            headers=headers,
            callback=for_callback,
            routing_key=routing_key,
        )
        publish_message.new_correlation_id()
        self._send_message(publish_message)
        if not need_reply:
            return
        await self._consumer.poll_task()
        return await waiter

    def stop_consumer(self, topic: str):
        """
        停止接收数据
        """
        self._consumer.stop_consumer([topic])
        del self._consumer_registers[topic]

    async def _health_check(self):
        """
        健康检查
        """
        # logger.info("开始pulsar健康检测..")
        # print("开始pulsar健康检测..")

        if not self._producer.is_connected() or not self._consumer.is_connected():
            self._fail_count += 1
            logger.error(f"pulsar connection failed for the {self._fail_count} time")
            print(f"pulsar connection failed for the {self._fail_count} time")

        else:
            self._fail_count = 0

        if self._fail_count >= 30:
            # 通过退出程序来让k8s 重启
            logger.error(
                "pulsar connection detection failure, will exit by k8s to achieve reboot"
            )
            print(
                "pulsar connection detection failure, will exit by k8s to achieve reboot"
            )

            # sys.exit(10)
            os._exit(10)
        # logger.info("pulsar检测结束..")
        # print("pulsar检测结束..")

        self.event_loop.call_later(3, self.event_loop.create_task, self._health_check())
