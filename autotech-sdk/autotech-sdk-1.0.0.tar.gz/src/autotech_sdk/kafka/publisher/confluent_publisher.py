from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from confluent_kafka import Producer
import json

from ..common import confluent_ccloud_lib as ccloud_lib
from ..common.kafka_config import BaseConfig


@dataclass
class ConfluentPublisherConfig(BaseConfig):
    bootstrap_servers: str
    security_protocol: str
    sasl_mechanisms: str
    sasl_username: str
    sasl_password: str

    def get_config(self):
        return {
            "bootstrap.servers": self.bootstrap_servers,
            "security.protocol": self.security_protocol,
            "sasl.mechanisms": self.sasl_mechanisms,
            "sasl.username": self.sasl_username,
            "sasl.password": self.sasl_password,
        }


class ConfluentPublisher(metaclass=ABCMeta):
    def __init__(self, config: ConfluentPublisherConfig):
        self.config = config
        self.producer = Producer(self.config.get_config())

    @abstractmethod
    def acked(self, err, msg):
        pass

    def push_message_to_confluent_kafka(self, data, topic, auto_create_topic=False, record_key=""):
        if auto_create_topic:
            ccloud_lib.create_topic(self.config.get_config(), topic)

        record_value = json.dumps(data)
        self.producer.produce(topic, key=record_key, value=record_value, on_delivery=self.acked)
        self.producer.poll(0)
        self.producer.flush()
