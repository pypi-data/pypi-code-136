from __future__ import annotations

from typing import Iterator
from urllib.parse import urlparse, parse_qsl

import uuid
import redis
import orjson

from powerful_pipes import read_json, dump_json

from .interface import BusInterface


class RedisBusSimpleQueue(BusInterface):

    def __init__(self, connection, queue_name: str = None):
        self.queue = queue_name
        self._connection: redis.Redis = connection

    def read_json_messages(self, queue_name: str = None) -> Iterator[dict]:

        queue = queue_name or self.queue

        while True:
            try:
                queue_name, message = self._connection.blpop(queue)
            except KeyboardInterrupt:
                return

            except:
                continue

            if message == "QUIT":
                break

            yield read_json(message)

    def send_json_message(self, data: dict, queue_name: str = None):
        queue = queue_name or self.queue

        self._connection.rpush(queue, orjson.dumps(data))

    @classmethod
    def open(cls, connection_string: str) -> RedisBusSimpleQueue:
        parsed = urlparse(connection_string)

        query = dict(parse_qsl(parsed.query))

        port = parsed.port or 6379
        host = parsed.hostname or "localhost"
        db = query.get("db", 0)
        queue = query.get("queue", None)

        o = cls(
            connection=redis.Redis(host, port, db),
            queue_name=queue
        )

        return o


class RedisBusPubSub(BusInterface):

    def __init__(self, connection, channel: str = None):
        self.channel = channel
        self._connection: redis.Redis = connection
        self.pubsub = self._connection.pubsub()

    def read_json_messages(self, channel: str = None) -> Iterator[dict]:
        channel = channel or self.channel

        if "*" in channel:
            self.pubsub.psubscribe(channel)
        else:
            self.pubsub.subscribe(channel)

        while True:

            try:
                raw_message = self.pubsub.get_message()

                if raw_message.get("type") not in ("pmessage", "message"):
                    continue

                message = raw_message.get("data")
            except KeyboardInterrupt:
                return

            except:
                continue

            if message == "QUIT":
                break

            yield read_json(message)

    def send_json_message(self, data: dict, channel: str = None):
        channel = channel or self.channel

        self._connection.publish(channel, orjson.dumps(data))

    @classmethod
    def open(cls, connection_string: str) -> RedisBusPubSub:
        parsed = urlparse(connection_string)

        query = dict(parse_qsl(parsed.query))

        port = parsed.port or 6379
        host = parsed.hostname or "localhost"
        db = query.get("db", 0)
        channel = query.get("channel", None)

        o = cls(
            connection=redis.Redis(host, port, db),
            channel=channel
        )

        return o


class RedisStreams(BusInterface):

    def __init__(
            self,
            connection,
            stream_name: str = None,
            group_name: str = None,
            consumer_name: str = None,
            timeout: int = 5000,
            batch_size: int = 1
    ):
        """Timeout is in milliseconds"""
        self.timeout = timeout
        self.batch_size = batch_size
        self.group_name = group_name
        self.stream_name = stream_name
        self.consumer_name = consumer_name

        self._groups = set()
        self._connection: redis.Redis = connection

    def read_json_messages(self, channel: str = None, group: str = None) -> Iterator[dict]:

        #
        # If Group or consumer is set, then it's a consumer
        #
        if self.group_name or self.consumer_name:
            self._create_group(self.group_name)

            while True:
                if message := self._connection.xreadgroup(
                    self.group_name,
                    self.consumer_name,
                    {self.stream_name: ">"},
                    count=self.batch_size,
                    block=self.timeout
                ):
                    for message_id, message_data in self._extract_message(message, "xreadgroup"):
                        yield message_data

                        self._connection.xack(self.stream_name, self.group_name, message_id)

                else:
                    # If the worker has not received any messages for a while,
                    # it claims pending messages that were delivered to it but not yet acknowledged.
                    if message := self._connection.xautoclaim(
                        self.stream_name,
                        self.group_name,
                        self.consumer_name,
                        min_idle_time=self.timeout,
                        start_id=1,
                        count=self.batch_size
                    ):

                        for message_id, message_data in self._extract_message(message, "claimed"):
                            yield message_data

                            self._connection.xack(self.stream_name, self.group_name, message_id)


    def send_json_message(self, data: dict, stream: str = None):
        stream = stream or self.stream_name

        self._connection.xadd(stream,  data)

    @classmethod
    def open(cls, connection_string: str) -> RedisStreams:
        parsed = urlparse(connection_string)

        query = dict(parse_qsl(parsed.query))

        port = parsed.port or 6379
        host = parsed.hostname or "localhost"
        db = query.get("db", 0)
        stream = query.get("stream", None)
        group = query.get("group", None)
        consumer = query.get("consumer", None)
        timeout = query.get("timeout", 5000)
        batch_size = query.get("batch_size", 1)

        if not stream:
            raise ValueError("Stream name is required")

        if group or not consumer:
            consumer = consumer or uuid.uuid4().hex

        o = cls(
            connection=redis.Redis(host, port, db, decode_responses=True),
            stream_name=stream,
            group_name=group,
            consumer_name=consumer,
            timeout=timeout,
            batch_size=batch_size
        )

        return o

    def _create_group(self, group_name: str):
        try:
            if group_name not in self._groups:
                self._connection.xgroup_create(self.stream_name, group_name, mkstream=True)
                self._groups.add(group_name)
        except redis.exceptions.ResponseError:
            pass

    def _delete_group(self, group_name: str):
        try:
            if group_name in self._groups:
                self._connection.xgroup_destroy(self.stream_name, group_name)
                self._groups.remove(group_name)
        except redis.exceptions.ResponseError:
            pass

    def _extract_message(self, message, source: str):
        if not message:
            return

        if source == "claimed":
            try:
                for message_id, message_data in message[1]:
                    yield message_id, message_data
            except IndexError:
                return

        elif source == "xreadgroup":
            try:
                for message_id, message_data in message[0][1]:
                    yield message_id, message_data
            except IndexError:
                return

        else:
            raise Exception("Invalid source")

