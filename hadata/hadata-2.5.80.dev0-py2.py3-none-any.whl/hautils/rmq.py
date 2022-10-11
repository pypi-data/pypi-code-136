import os

import pika
from dotenv import load_dotenv
from pika import PlainCredentials

from hautils.logger import logger

load_dotenv(override=False)

RABBIT_MQ_HOST = os.getenv('RABBIT_MQ_HOST')
RABBIT_MQ_USER = os.getenv("RABBIT_MQ_USER")
RABBIT_MQ_PASS = os.getenv("RABBIT_MQ_PASS")


def get_rmq_connection():
    """
    The get_rmq_connection function connects to the RabbitMQ server using the host, user and password
    provided in the environment variables. The function returns a connection object that can be used
    to send messages to or receive messages from any of RabbitMQ's queues.

    :return: A connection to rabbitmq
    :doc-author: Trelent
    """
    logger.info("connecting to rmq %s - %s - %s" % (RABBIT_MQ_HOST, RABBIT_MQ_USER, RABBIT_MQ_PASS))
    return pika.BlockingConnection(
        pika.ConnectionParameters(heartbeat=1000, host=RABBIT_MQ_HOST,
                                  credentials=PlainCredentials
                                  (RABBIT_MQ_USER, RABBIT_MQ_PASS)))


def publish_rmq(exchange, body, ex_type="direct"):
    """
    The publish_rmq function publishes a message to an exchange.
    The publish_rmq function accepts three parameters:
        1) exchange - the name of the exchange to publish to (string)
        2) body - the message that will be published (string or JSON object/array)
        3) ex_type - optional parameter specifying what type of exchange this is.  Default is direct.

    :param exchange: Specify the exchange to publish to
    :param body: Send the message to the exchange
    :param ex_type=&quot;direct&quot;: Specify the type of exchange
    :return: The channel object
    :doc-author: Trelent
    """
    connection = get_rmq_connection()
    channel = connection.channel()
    logger.info("publishing to exchange %s with data %s" % (exchange, body))
    channel.exchange_declare(exchange=exchange, exchange_type=ex_type)
    channel.basic_publish(exchange=exchange, routing_key=exchange, body=body)
    connection.close()
    logger.info("closing connection")


def rmq_bind(exchange="ha", queue="ha"):
    """
    The rmq_bind function binds two queues together.



    :param exchange=&quot;ha&quot;: Specify the exchange to which the
    :param queue=&quot;ha&quot;: Specify the queue name
    :return: The channel that was created
    :doc-author: Trelent
    """
    logger.info("binding queues together %s to %s" % (exchange, queue))
    connection = get_rmq_connection()
    channel = connection.channel()
    result = channel.queue_declare(queue=queue, exclusive=False, durable=True)
    logger.info("queue declare result %s" % (result,))
    result = channel.queue_bind(exchange=exchange,
                                queue=queue, routing_key=exchange)
    logger.info("queue bind result %s" % (result,))
    return channel


def rmq_consume(queue, callback, durable=True, ack=True):
    """
    The rmq_consume function creates a connection to the RabbitMQ server,
    and then creates a channel on that connection. It then declares the queue
    on that channel and binds it to the exchange (which is also declared). The
    channel is returned so that it can be used in other functions.

    :param queue: Specify the queue to which the message should be sent
    :param callback: Specify the function that is called whenever a new message arrives on the queue
    :param durable=True: Ensure that the queue is not deleted if it
    :param ack=True: Acknowledge that a message has been received and processed
    :return: A channel object
    :doc-author: Trelent
    """
    logger.info("rmq consumer getting ready")
    connection = get_rmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=durable)
    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=ack)
    logger.info("consumer bound to %s " % (queue,))
    return channel
