#!/usr/bin/env python
# encoding: utf-8
from .publishesMessage import PublishesMessage
from .kafkapacket_pb2 import KafkaPacket
import json
import asyncio
import logging

logger = logging.getLogger(__name__)


class WorkerDelegate(object):
    """
    用于执行 回调函数以及对应的参数
    """

    def __init__(self, callback: callable, message: KafkaPacket, private_topic: str):
        self.callback = callback
        self.message = message
        self.private_topic = private_topic

    async def executor(self):
        """
        用于执行回调函数，返回PublishesMessage
        """
        headers = self.message.headers
        response_headers = dict()
        for item in headers:
            response_headers[item.name] = item.value
        publish_message = PublishesMessage(
            payload="",
            reply_to=self.private_topic,
            send_to=self.message.replyTo,
            correlation_id=self.message.correlationId,
            is_reply=True,
            content_type=self.message.contentType,
            content_encoding=self.message.contentEncoding,
            group_id=self.message.groupId,
            message_id=self.message.messageId,
            msg_type=self.message.type,
            user_id=self.message.userId,
            app_id=self.message.appId,
            headers=response_headers,
            callback=None,
        )
        if callable(self.callback):
            result = ""
            try:
                # 为保持pulsar 的连接而进行ping 操作，在这里进行pong 的回复
                try:
                    payload = json.loads(self.message.body)
                    if payload.get("bizCode") == "ping":
                        reply = {"code": 0, "message": "success", "data": "pong"}
                        publish_message.payload = json.dumps(reply)
                        return publish_message
                except Exception as te:
                    pass
                if asyncio.iscoroutinefunction(self.callback):
                    result = await self.callback(self.message)
                else:
                    result = self.callback(self.message)
                if isinstance(result, (list, dict)):
                    try:
                        result = json.dumps(result)
                    except Exception as ee:
                        logger.exception(ee)
                        logger.error(
                            "json serialize %s failed with error:%s",
                            str(result),
                            str(ee),
                        )
                        result = ""
                        publish_message.status_code = 500
                        publish_message.error_message = str(ee)
                elif isinstance(result, (bytes, str)):
                    pass
                else:
                    result = ""
            except Exception as e:
                logger.exception(e)
                publish_message.status_code = 500
                publish_message.error_message = str(e)
            publish_message.payload = result
        return publish_message
