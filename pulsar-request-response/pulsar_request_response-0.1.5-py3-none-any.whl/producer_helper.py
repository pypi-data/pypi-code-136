#!/usr/bin/env python
# encoding: utf-8
from .helper import Helper
from .asyncWrapper import AsyncWrapper
import pulsar
import json
import logging

from .kafkapacket_pb2 import KafkaPacket
from .packagewrapper_pb2 import PackageWrapperResponse

# from loguru import logger

logger = logging.getLogger(__name__)


class ProducerHelper(Helper):
    """
    生产者辅助
    """

    def __init__(self):
        super(ProducerHelper, self).__init__()
        self._producers = {}
        self._client = None

    def _init_client(self):
        self._client = pulsar.Client(self._config["url"])

    def send(self, msg: bytes, topic: str):
        """
        发送消息
        :param msg:
        :param topic:
        :return:
        """
        # if self._config['tenant'] not in topic:
        # topic =f"{self._config['tenant']}/{self._config['namespace']}/{topic}"
        if self._client is None:
            self._init_client()
        if not self.persistent:
            topic = "non-persistent://" + topic
        producer = self._producers.get(topic)
        if producer is None:
            producer = self._client.create_producer(topic)
            self._producers[topic] = producer
        if isinstance(msg, bytes):
            producer.send(msg)
        if isinstance(msg, str):
            producer.send(msg.encode("utf-8"))
        if isinstance(msg, dict):
            producer.send(json.dumps(msg))
        if isinstance(msg, KafkaPacket):
            properties = {
                "contentType": msg.contentType,
                "contentEncoding": msg.contentEncoding,
                "sendTo": msg.sendTo,
                "groupId": msg.groupId,
                "correlationId": msg.correlationId,
                "replyTo": msg.replyTo,
                "messageId": msg.messageId,
                "timestamp": str(msg.timestamp),
                "type": msg.type,
                "userId": msg.userId,
                "appId": msg.appId,
            }
            if msg.messageId is None:
                properties["messageId"] = self.get_message_id()

            if str(msg.contentType).lower() == "json":
                data = {
                    "contentType": msg.contentType,
                    "contentEncoding": msg.contentEncoding,
                    "sendTo": msg.sendTo,
                    "groupId": msg.groupId,
                    "correlationId": msg.correlationId,
                    "replyTo": msg.replyTo,
                    "messageId": msg.messageId,
                    "timestamp": msg.timestamp,
                    "type": msg.type,
                    "userId": msg.userId,
                    "appId": msg.appId,
                    "statusCode": msg.statusCode,
                    "errorMessage": msg.errorMessage,
                    "body": msg.body.decode(),
                    "routingKey": msg.routingKey,
                    "consumerTag": msg.consumerTag,
                    "exchange": msg.exchange,
                }
                producer.send(json.dumps(data).encode("utf-8"), properties=properties)
            else:
                producer.send(msg.SerializeToString(), properties=properties)

        if isinstance(msg, PackageWrapperResponse):
            # logger.info(msg.SerializeToString())
            producer.send(msg.SerializeToString(), properties={"a": "b"})

    def is_connected(self):

        for topic in self._producers:
            if not self._producers[topic].is_connected():
                return False

        return True
