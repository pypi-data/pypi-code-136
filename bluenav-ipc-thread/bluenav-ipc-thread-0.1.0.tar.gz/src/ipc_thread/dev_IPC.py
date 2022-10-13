import json
import logging
import threading
import time
from typing import Any, Callable

import redis

logger = logging.getLogger("ipc_thread.IPC")


class MockIoTCore:
    def __init__(self) -> None:
        pass

    def set_handler(self) -> None:
        pass


class MessageHandler(threading.Thread):
    def __init__(self, sub) -> None:
        super().__init__()
        self.sub = sub
        self.__handler = None
        self.start()

    def set_handler(self, callback: Callable[[str, str], None]) -> None:
        self.__handler = callback

    def run(self):
        for msg in self.sub.listen():
            if msg and msg['type'] == 'message':
                self.__handler(json.loads(msg['data']), msg['channel'].decode())


class dev_IPC:
    def __init__(self):
        self.__ipc_client = None
        self.connect()
        self.__TIMEOUT = 10

    #------------------------------------------------------------------------

    def connect(self) -> bool:
        try:
            self.__ipc_client = redis.Redis(host='localhost', port=6379, db=0)
            return True
        except InterruptedError:
            self.__ipc_client = None
            time.sleep(10)
            return self.connect()
        except Exception as e:
            self.__ipc_client = None
            time.sleep(10)
            return self.connect()

    def disconnect(self):
        if self.__ipc_client is not None:
            self.__ipc_client.close()
            self.__ipc_client = None

    def subscribe(self, topic: str) -> MessageHandler:
        sub = self.__ipc_client.pubsub()
        sub.subscribe(topic)
        return MessageHandler(sub)

    def publish(self, topic: str, data: Any) -> None:
        self.__ipc_client.publish(topic, json.dumps(data))

    def publish_to_core(self, topic: str, data: Any) -> None:
        pass

    def subscribe_to_core(self, topic) -> MockIoTCore:
        return MockIoTCore()

    def subscribe_to_component_update(self) -> MockIoTCore:
        return MockIoTCore()

    def acknowledge_update(self) -> None:
        pass

    def defer_update(self) -> None:
        pass
