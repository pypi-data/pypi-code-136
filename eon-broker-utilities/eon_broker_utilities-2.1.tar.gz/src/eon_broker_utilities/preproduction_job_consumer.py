import asyncio
from crypt import methods
import queue
from aio_pika import connect_robust
import json
import aio_pika
from eon_logger import logging as rabbit_log

cls = rabbit_log.Logs_Manager('rabbit_mq', 'info')
_logger = cls.create_logger()


consumer = None

class ManageConsumers():
    def __init__(self, service_name, rabbit_config_variables):
        self.service_name = service_name
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
        self.queue_name                 = service_name + '_jobs'
        # Getting the routing key for the new jobs
        self.new_jobs_routing_key       = rabbit_config_variables['NEW_JOBS_ROUTING_KEY']  + service_name
        # Used for successful job
        self.successful_job_routing_key = service_name + rabbit_config_variables['SUCCESSFUL_JOB_ROUTING_KEY']
        # Used for faild jobs
        self.failed_job_routing_key     = service_name + rabbit_config_variables['FAILED_JOB_ROUTING_KEY']
        
        self.started_job_routing_key     = service_name + rabbit_config_variables['STARTED_JOB_ROUTING_KEY']
        # Handler function from the service calling the class
        self.handler = None
        # Used for storing connection
        self.connection = None
        # Used for storing channel
        self.channel = None

    def set_connection(self, new_channel):
        self.connection = new_channel

    def get_connection(self):
        return self.connection

    def set_channel(self, new_channel):
        self.channel = new_channel

    def get_channel(self):
        return self.channel

    def set_handler(self, new_handler):
        self.handler = new_handler

    def get_handler(self):
        return self.handler  
          
    def set_exchange(self, new_exchange):
        self.exchange = new_exchange

    def get_exchange(self):
        return self.exchange  

def set_consumer(new_consumer):
    global consumer
    consumer = new_consumer

def get_consumer():
    return consumer

async def service_publish(new_message, routing_key):
    consumer = get_consumer()
    exchange = consumer.get_exchange()
    try:
        await exchange.publish(aio_pika.Message(body=json.dumps(new_message).encode("utf-8")),
        routing_key=routing_key)
    except Exception as err:
        print(err)

async def callback(message: aio_pika.abc.AbstractIncomingMessage,) -> None:
    consumer = get_consumer()
    new_message = json.loads(message.body)
    print(str(json.loads(message.body)))
    await service_publish((new_message), consumer.started_job_routing_key)
    handler = consumer.get_handler()
    _response, _status = handler(new_message)
    if _status == True:
        _logger.info(f"publishing at1 : { consumer.successful_job_routing_key} {new_message}")
        await service_publish((new_message), consumer.successful_job_routing_key)
    elif _status == False:
        _logger.info(f"publishing at : { consumer.failed_job_routing_key}")
        new_message['error'] = {"message": f"{_response}"}
        await service_publish((new_message), consumer.failed_job_routing_key)
    await message.ack(False)
    
async def main(consumer) -> None:
    connection = await connect_robust(
    f"amqp://{consumer.rabbit_user}:{consumer.rabbit_password}@{consumer.rabbit_host}/?name=aio-pika%20worker",
    )
    created_channel = await connection.channel()
    consumer.set_channel(created_channel)
    await created_channel.set_qos(prefetch_count=1)
    queue = await created_channel.declare_queue(consumer.queue_name, durable=True)
    exchange = await created_channel.declare_exchange(name = consumer.exchange_name, type = 'topic', durable=True)
    consumer.set_exchange(exchange)
    await queue.bind(exchange, consumer.new_jobs_routing_key)
    await queue.consume(callback)
    await asyncio.Future()
    
def start_consumer(service_name, handler, rabbit_config):
    consumer = ManageConsumers(service_name, rabbit_config)
    consumer.set_handler(handler)
    set_consumer(consumer)
    asyncio.run(main(consumer))