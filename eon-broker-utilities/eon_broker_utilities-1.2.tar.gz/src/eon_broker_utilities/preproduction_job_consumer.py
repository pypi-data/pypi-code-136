import json
from tkinter import E
import pika
import pika.exceptions
import time
from eon_logger import logging as rabbit_log

cls = rabbit_log.Logs_Manager('rabbit_mq', 'debug')
_logger = cls.create_logger()


class ManageConsumers(): 
    def __init__(self, service_name, handler, config):
        self.rabbit_user                = config['RABBIT_USER']
        self.rabbit_password            = config['RABBIT_PASSWORD']
        self.rabbit_host                = config['RABBIT_HOST'] 
        self.rabbit_port                = config['RABBIT_PORT']     
        self.exchange_name              = config['EXCHANGE_NAME']
        self.qeue_name                  = service_name + '_jobs'
        self.new_jobs_routing_key       = config['NEW_JOBS_ROUTING_KEY']  + service_name
        self.successful_job_routing_key = service_name + config['SUCCESSFUL_JOB_ROUTING_KEY']
        self.failed_job_routing_key     = service_name + config['FAILED_JOB_ROUTING_KEY']
        self.handler = handler
        self._conn = None
        self._channel = None
        self.connect()
        self.start_consume()
    
    def connect(self):
        try:
            credentials   = pika.PlainCredentials(self.rabbit_user, self.rabbit_password)
            parameters    = pika.ConnectionParameters(self.rabbit_host,
                                    int(self.rabbit_port),
                                    '/',
                                    credentials)
            self._conn    = pika.BlockingConnection(parameters)
            self._channel = self._conn.channel()
            _logger.info('connected to RabbitMQ Server')

        except Exception as err:
            _logger.error(f'Error processing job {err}')
            time.sleep(10)
            self.connect()
            
    def handle_new_message(self, channel, method, properties, body):
        try:
            message = json.loads(body)
        except Exception as err:
            channel.basic_ack(delivery_tag=method.delivery_tag)                
            return
        try:
            self.handler(message)
            _logger.info(f"publishing at : { self.successful_job_routing_key}")
            channel.basic_publish(exchange=self.exchange_name, routing_key=self.successful_job_routing_key, body=json.dumps(message))
        except Exception as err:
            _logger.error(f'Error processing job {err}')
            _logger.info(message)
            message['reason'] = str(err)
            channel.basic_publish(exchange=self.exchange_name, routing_key=self.failed_job_routing_key, body=json.dumps(message))
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consume(self):
        self._channel.queue_bind(exchange=self.exchange_name, queue=self.qeue_name, routing_key=self.new_jobs_routing_key)
        self._channel.basic_consume(self.qeue_name, self.handle_new_message)
        self._channel.start_consuming()


