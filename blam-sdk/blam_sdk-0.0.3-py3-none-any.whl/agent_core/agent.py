import json
import logging
import time
import warnings

import boto3

from blam_sdk.agent_core.agent_conf import AgentConf
from blam_sdk.services.action_service import ActionService


class Agent:
    def __init__(self, config: AgentConf = None, action_handlers={}):
        if config is None:
            config = AgentConf.from_file()
        self.config = config
        self.action_service = ActionService()
        self.action_handlers = action_handlers
        warnings.filterwarnings(
            "ignore", category=FutureWarning, module="botocore.client"
        )

    def _register(self):
        try:
            logging.info("Registering agent")
            self.action_service.register_agent(
                self.config.name, self.config.name, self.config.action_ids
            )
            logging.info("Agent registered")
        except Exception as e:
            if e.args[0]["message"] == "Agent already exists":
                logging.info("Agent already registered")
            else:
                logging.error("Failed to register agent: %s", e)
                raise e

    def _refresh_queue_data(self):
        logging.info(f"Refreshing queue data for {self.config.queue}")
        self._queue_data = self.action_service.queue_login(self.config.queue)[
            "creds"
        ]
        logging.info("Queue data refreshed successfully")
        self.sqs = boto3.resource(
            "sqs",
            "us-east-1",
            aws_access_key_id=self._queue_data["accessKeyId"],
            aws_secret_access_key=self._queue_data["secretAccessKey"],
            aws_session_token=self._queue_data["sessionToken"],
        )
        self.queue = self.sqs.get_queue_by_name(QueueName=self.config.queue)

    def _process_message(self, message):
        body = json.loads(message.body)
        logging.info(f"Processing message with exec id {body['id']}")
        message.delete()
        self.action_service.update_execution_status(body["id"], "processing")
        try:
            self.action_handlers[body["action_id"]].perform_action(body)
        except Exception as e:
            logging.error("Failed to process message: %s", e)
            self.action_service.update_execution_status(body["id"], "failed")
        logging.info(
            f"Message with exec id {body['id']} processed successfully"
        )
        self.action_service.update_execution_status(body["id"], "completed")

    def start(self, once=False):
        self._register()
        self._refresh_queue_data()
        self.start_handler_loop(once)

    def check_queue(self):
        return self.queue.attributes.get("ApproximateNumberOfMessages")

    def start_handler_loop(self, once=False):
        if once:
            logging.info("checking for messages one time")
        else:
            logging.info(
                f"Starting handler loop with a poll interval of {self.config.poll_interval} seconds"
            )
        while True:
            messages = self.queue.receive_messages(
                AttributeNames=["All"], MaxNumberOfMessages=1
            )
            if len(messages):
                self._process_message(messages[0])
            else:
                logging.info("No messages to process")
                logging.info(
                    f"Sleeping for {self.config.poll_interval} seconds"
                )
                time.sleep(self.config.poll_interval)

            if once:
                break

    def set_handlers(self, handlers):
        self.action_handlers = handlers
