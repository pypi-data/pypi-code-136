from redis.exceptions import ConnectionError
from threading import Thread
from queue import Queue, Empty
import typing
import redis
import time
import json


class IotRedisBasic:
    """Basic redis variable to set and retrieve data

    Base class for Redis variable"""

    def __init__(self):
        super().__init__()
        self.rdb = redis.Redis(
            host='localhost',
            port=6379,
            charset="utf-8",
            decode_responses=True,
            db=0
        )

    def get(self, var: str):
        try:
            return self.rdb.get(var)
        except ConnectionError as _:
            return

    def set(self, var_name: str, value: dict):
        try:
            if not isinstance(value, dict):
                raise TypeError()
            self.rdb.set(var_name, json.dumps(value))
        except ConnectionError as _:
            print("ConnetionError trying to set var")
        except TypeError as _:
            print("Value has to be a dictionary")


class IotRedisSubscriber(IotRedisBasic, Thread):
    """Class for consume info, inherits from Thread

    This class provides basic connetion to redis and consumes
    a list of channels to subscribe when is started.
    func_handler can be parsed to develop async distribution of data
    to a custom function.
    """

    def __init__(self, *channels_to_consume: str, func_handler=None) -> None:
        super().__init__()
        self.daemon = True
        self.data_list = Queue()
        self.init_channels = list(channels_to_consume)
        self.func_handler = func_handler
        # Create pubsub instance for subscribe
        self.pubsub = self.rdb.pubsub(ignore_subscribe_messages=True)

    @property
    def channels(self):
        return self.pubsub.channels

    def run(self) -> None:
        # Subscribe
        self._subscribe_channels(*self.init_channels)
        print("Run IotRedis Consumer: Init Consumer and channels")
        while True:
            try:
                self.pubsub.ping()
                self.listen()
            except ConnectionError as _:
                print("Problem trying to listen, relisten...")
            except AttributeError as _:
                print("None type of msg")

    def listen(self) -> None:
        for msg in self.pubsub.listen():
            if msg is not None and isinstance(msg, dict):
                # Save info in queue.
                data = self._convert_data(msg['data'])
                if self.func_handler is not None:
                    self.func_handler((msg['channel'], data))
                else:
                    self.data_list.put((msg['channel'], data))

    def _convert_data(self, data: str) -> typing.Any:
        try:
            return json.loads(data)
        except json.decoder.JSONDecodeError:
            return data
        except TypeError:
            return data

    def _subscribe_channels(self, *channels_to_consume: str) -> None:
        while True:
            try:  # Suscribe to every channel
                self.pubsub.subscribe(*channels_to_consume)
            except ConnectionError as err:
                print(f"Error trying to connect to server: {err}")
                time.sleep(1)
            else:  # If no error
                print("Connected to subscribe")
                break

    def data_available(self) -> bool:
        return not self.data_list.empty()

    def retrieve_data(self) -> tuple:
        try:
            return self.data_list.get_nowait()
        except Empty as _:
            return


class IotRedisPublisher(IotRedisBasic):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def publish(self, channel: str, data: dict) -> None:
        try:  # Publish data to channel
            if not isinstance(data, dict):
                raise TypeError("Type has to be a dictionary")
            return self.rdb.publish(channel, json.dumps(data))
        except ConnectionError as _:
            print("error trying to publish")


class IotRedisPubSub(IotRedisPublisher, IotRedisSubscriber):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    pubsub = IotRedisPubSub("hola", "opcua", func_handler=print)
    print(pubsub.channels)
    sample_consumer = IotRedisSubscriber('prueba1', 'prueba2')
    sample_consumer.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt as _:
            break
    print("Simulation ended")
