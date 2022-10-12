import json
from tkinter import E
import pika
import pika.exceptions
import time
from eon_logger import logging as rabbit_log

cls = rabbit_log.Logs_Manager('rabbit_mq', 'info')
_logger = cls.create_logger()


class ManageConsumers(): 
    def __init__(self, service_name, handler, rabbit_config_variables):
        # Getting Rabbit MQ user
        self.rabbit_user                = rabbit_config_variables['RABBIT_USER']
        # Getting Rabbit MQ password
        self.rabbit_password            = rabbit_config_variables['RABBIT_PASSWORD']
        # Getting Rabbit MQ server ip address
        self.rabbit_host                = rabbit_config_variables['RABBIT_HOST'] 
        # Getting Rabbit MQ server port
        self.rabbit_port                = rabbit_config_variables['RABBIT_PORT']     
        # Getting the exchange
        self.exchange_name              = rabbit_config_variables['EXCHANGE_NAME']
        # Getting the queue name for each service,  which is the name of the service followed by "_jobs"
        self.qeue_name                  = service_name + '_jobs'
        # Getting the routing key for the new jobs
        self.new_jobs_routing_key       = rabbit_config_variables['NEW_JOBS_ROUTING_KEY']  + service_name
        # Used for successful job
        self.successful_job_routing_key = service_name + rabbit_config_variables['SUCCESSFUL_JOB_ROUTING_KEY']
        # Used for faild jobs
        self.failed_job_routing_key     = service_name + rabbit_config_variables['FAILED_JOB_ROUTING_KEY']
        # Handler function from the service calling the class
        self.handler = handler
        # Used for storing connection
        self._conn = None
        # Used for storing channel
        self._channel = None
        # Calling connect function to establish connection 
        self.connect()
        # Calling start consume to start fetching message from the queue,
        # this function will take a message each time perform a process,
        # and remove the message from the queue 
        self.start_consume()
    
    def connect(self):
        try:
            # Setting Rabbit MQ Credentials taken from the __init__ function, takes user and password for Rabbit MQ server
            credentials   = pika.PlainCredentials(self.rabbit_user, self.rabbit_password)
            # Setting Rabbit MQ connection parametes, host, port, type and credintials (taken usiing plain credintials function above)
            parameters    = pika.ConnectionParameters(self.rabbit_host,
                                    int(self.rabbit_port),
                                    '/',
                                    credentials)
            # Using parametes to establish a connetion to Rabbit MQ
            self._conn    = pika.BlockingConnection(parameters)
            # Opening Rabbit MQ channel to send and recieve messages
            self._channel = self._conn.channel()
            # Logging successful connection
            _logger.info('connected to RabbitMQ Server')
        # Failing to connect exception
        except Exception as err:
            # Logging exceptions
            _logger.error(f'Could Not Establish Connection, Retrying in 5 Seconds...')
            # waiting for 10 seconds to try top recconnect to Rabit MQ server
            time.sleep(5)
            # Calling connect function to retry connecting to the server
            self.connect()
            
    def handle_new_message(self, channel, method, properties, body):
        try:
            # Getting the message from Rabbit MQ as json instead of string 
            message = json.loads(body)
        except Exception as err:
            # Sending ACK to the queue in cxase of an exception to remove message from the queue
            # takes delivery tag paramemeter
            channel.basic_ack(delivery_tag=method.delivery_tag)                
            return
        try:
            # Calling the handler from the service
            self.handler(message)
            # Logging after successful handelr prcess
            _logger.info(f"publishing at : { self.successful_job_routing_key}")
            # Publishing to the exchange with successful job routing key which is used to store the successfully done jobs,
            # takes exchange name to be pushed at, routing key and message body in json format
            channel.basic_publish(exchange=self.exchange_name, routing_key=self.successful_job_routing_key, body=json.dumps(message))
        except Exception as err:
            # logging exception in case of faild process
            _logger.error(f'Error processing job {err}')
            # Logging the recieved message from Rabbit MQ
            _logger.info(message)
            # Setting the error reason and storing it in the message
            message['reason'] = str(err)
            # Publishing to the exchange with faild job routing key which is used to store the faildjobs,
            # takes exchange name to be pushed at and
            channel.basic_publish(exchange=self.exchange_name, routing_key=self.failed_job_routing_key, body=json.dumps(message))
        # Sending ACK to the queue in after fininshing to remove message from the queue
        # takes delivery tag as a paramemeter
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consume(self):
        if not self._channel.connection:
            self.connect()
        else: 
            # Binding the qeue to a specific exchange
            self._channel.queue_bind(exchange=self.exchange_name, queue=self.qeue_name, routing_key=self.new_jobs_routing_key)
            # Setting the consuming call back function
            self._channel.basic_consume(self.qeue_name, self.handle_new_message)
            # Starting consuming from the queue 
            self._channel.start_consuming()