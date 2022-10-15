from dataclasses import dataclass

from confluent_kafka import Consumer
import json
from abc import ABCMeta, abstractmethod
from typing import List

from ..common.kafka_config import BaseConfig


@dataclass
class ConfluentConsumerConfig(BaseConfig):
    bootstrap_servers: str
    security_protocol: str
    sasl_mechanisms: str
    sasl_username: str
    sasl_password: str
    session_timeout_ms: str
    group_id: str
    auto_offset_reset: str

    def get_config(self):
        return {
            "bootstrap.servers": self.bootstrap_servers,
            "security.protocol": self.security_protocol,
            "sasl.mechanisms": self.sasl_mechanisms,
            "sasl.username": self.sasl_username,
            "sasl.password": self.sasl_password,
            "session.timeout.ms": self.session_timeout_ms,
            "group.id": self.group_id,
            "auto.offset.reset": self.auto_offset_reset
        }


class ConfluentConsumer(metaclass=ABCMeta):
    def __init__(self, config: ConfluentConsumerConfig, topic: List[str] or str):
        self.config = config
        consumer = Consumer(self.config.get_config())
        self.consumer = consumer

        if isinstance(topic, str):
            topic = [topic]
        self.consumer.subscribe(topic)

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def process_error_data(self, error):
        pass

    def run_consumer(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                elif msg.error():
                    self.process_error_data(msg.error())
                else:
                    record_value = msg.value()
                    data = json.loads(record_value)
                    self.process_data(data)
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()


