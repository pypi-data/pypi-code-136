import json
from kafka import KafkaProducer


class MessageQueue:
    def __init__(self, bootstrap_servers, customer_id, model_id, training_id, topic):
        self.bootstrap_servers = bootstrap_servers
        self.customer_id = customer_id
        self.model_id = model_id
        self.training_id = training_id
        self.topic = topic
        self.startup_key = "MQ0003"
        self.status_key = "MQ0004"

    def _produce(self, key, value):
        print("MQ Send:", value)
        print()

        # send MQ for service start successfully
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

        data = json.dumps(value).encode('utf-8')
        producer.send(self.topic, key=key.encode('utf-8'), value=data)
        producer.flush()
        producer.close()

    def startup(self, return_code, reason):
        value = {
            "return_code": return_code,
            "payload": {
                "customer_id": self.customer_id,
                "model_id": self.model_id,
                "training_id": self.training_id,
                "progress": "0",
                "reason": reason,
            }
        }
        self._produce(self.startup_key, value)

    def send(self, return_code, progress, reason):
        value = {
            "return_code": return_code,
            "payload": {
                "customer_id": self.customer_id,
                "model_id": self.model_id,
                "training_id": self.training_id,
                "progress": progress,
                "reason": reason,
            }
        }
        self._produce(self.status_key, value)

    def finish(self, return_code, progress, kg_list, val_report, reason):
        value = {
            "return_code": return_code,
            "payload": {
                "customer_id": self.customer_id,
                "model_id": self.model_id,
                "training_id": self.training_id,
                "progress": progress,
                "kg_list": kg_list,
                "val_report": val_report,
                "reason": reason,
            }
        }
        self._produce(self.status_key, value)
