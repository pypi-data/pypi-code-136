import uuid
import os
import socket

import sys
import threading
import json
from .udp_message import create_start_transaction_message, create_end_transaction_message
from .udp_message import create_method_entry_message, create_method_exit_message
from .udp_message import create_transaction_encode_http_message
from .udp_message import create_havoc_message
from .udp_message import create_init_message
from .udp_message import create_heartbeat_message
import time
import logging

udp_connection = None

logger = logging.getLogger('pythonagent.agent')


class UDPConnection(object):
    def __init__(self, agent_obj):

        if 'CAV_APP_AGENT_PROXYIP' in os.environ:
            self.cav_proxy_ip = os.environ['CAV_APP_AGENT_PROXYIP']
        else:
            self.cav_proxy_ip = "127.0.0.1"

        if 'CAV_APP_AGENT_PROXYPORT' in os.environ:
            self.cav_proxy_port = int(os.environ['CAV_APP_AGENT_PROXYPORT'])

        else:
            self.cav_proxy_port = 10000

        self.server_address_port = (self.cav_proxy_ip, self.cav_proxy_port)

        # Create a UDP socket at client side
        try:

            self.UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            logger.debug("Server Port {}".format(self.server_address_port))

            havoc_thread = threading.Thread(target=incoming_message_processor, name="havoc_thread",
                                            args=(self.UDPClientSocket,), daemon=True)
            havoc_thread.start()

            heartbeat_thread = threading.Thread(target=heartbeat_sender, name="heartbeat_thread",
                                                args=(self.UDPClientSocket, self.server_address_port, agent_obj),
                                                daemon=True)
            heartbeat_thread.start()


        except:
            logger.warning("Unable to create UDP Connection")

    def send(self, message, tx_type="non_start_fp"):

        # Send to server using created UDP socket
        try:
            self.UDPClientSocket.sendto(message, self.server_address_port)

        except:
            logger.warning("Unable to send UDP packet")


def heartbeat_sender(udp_socket, address_port, ag_obj):
    logger.info("heartbeat sender started")
    context = ag_obj.get_transaction_context()
    message = create_heartbeat_message(context)
    logger.info("heartbeat message {}".format(message))
    while True:
        try:
            logger.debug("heartbeat about to send")
            udp_socket.sendto(message, address_port)
            logger.info("heartbeat sent")
            time.sleep(10)
            logger.debug("heartbeat sleep completed")
        except Exception as e:
            logger.error("heartbeat exception", e)


def incoming_message_processor(udp_socket):
    logger.debug("New thread started")

    from pythonagent.agent.probes.havoc.havoc_manager import NDNetHavocMonitor  # Don't shift to top, it will cause circular import
    havoc_monitor = NDNetHavocMonitor.get_instance()
    # logger.debug("udp.py havoc id {}".format(id(havoc_monitor)))
    udp_socket.settimeout(2.0)
    buffer_size = 4096
    counter = 0

    while True:

        try:  # timeout (non-blocking behaviour) added because in warm-start, listener is not working sometimes
            counter += 1
            logger.debug("counter: {}".format(counter))
            logger.debug("Going to call recv from api for {} time".format(counter))
            logger.debug("Going to call recv from api")
            data, address = udp_socket.recvfrom(buffer_size)
            logger.debug("incoming received message = {} from address {}".format(data, address))
            logger.debug("after gettting message")

            output = str(data)

            if output == "b'Heart Beat Received'":
                logger.debug("ignoring heartbeat acknowledgement")
                continue
            try:

                output = output[2:-1]  # Remove b' from beginning and ' from end
                split_arr = output.split("\\n")

                header = split_arr[0]
                body = split_arr[1]

                body = body.replace("-", ":")

                header = header[:-1]  # Trim ; from end
                header_dict = {}

                header_split = header.split(";")

                count = 0
                for element in header_split:
                    if count == 0:
                        count += 1
                        continue  # Ignore first value: NetDiagnosticMessage2.0
                    else:
                        element_split = element.split(":")
                        key = element_split[0].strip()
                        value = element_split[1].strip()
                        header_dict[key] = value
                        count += 1
                havoc_monitor.parse_nethavoc_config(body, header_dict)

            except Exception as e:
                logger.warning("Unable to parse config: {}", e)
                logger.warning("unable to parse message except")

        except socket.timeout:
            logger.debug("recv timed out")  # This is not an exception, but a mechanism to implement timeout


def generate_bt():
    id = uuid.uuid4()
    id_int = id.int
    return id_int


def sdk_init(agent_obj):
    agent_obj.udp_connection = UDPConnection(agent_obj)
    logger.debug("called sdk init")
    context = agent_obj.get_transaction_context()
    logger.debug("transaction context dictionary inside sdk init in udp.py {}".format(context.function_name))
    message = create_init_message(context)
    logger.debug("first message to be sent to proxy {}".format(message))
    agent_obj.udp_connection.send(message)
    logger.debug("init sent")
    return udp_connection


def sdk_free(agent_obj):
    pass


def method_entry(agent_obj, bt, method, query_string, url_parameter):
    context = agent_obj.get_transaction_context()
    message = create_method_entry_message(context, bt, method, query_string, url_parameter)
    logger.info("method_entry {}".format(message))
    agent_obj.udp_connection.send(message)


def method_exit(agent_obj, bt, method, backend_header, status, duration):
    context = agent_obj.get_transaction_context()
    # message = create_method_exit_message(context, bt, method)
    message = create_method_exit_message(context, bt, method, backend_header, status, duration)
    logger.info("method_exit: status {}, duration {}, message {}".format(status, duration, message))
    agent_obj.udp_connection.send(message)


def start_business_transaction(agent_obj, bt_name, correlation_header):
    if os.environ['nd_init_done'] == '0':
        agent_obj.sdk_init()

    context = agent_obj.get_transaction_context()
    # message = udp_message.create_start_transaction_message(context, bt_name, correlation_header)
    message = create_start_transaction_message(context, bt_name, correlation_header)
    logger.info("start_business_transaction {}".format(message))
    agent_obj.udp_connection.send(message, "start_fp")

    bt = generate_bt()

    agent_obj.active_bts.add(bt)
    agent_obj.set_current_bt(bt)

    return bt


def end_business_transaction(agent_obj, bt):
    status_code = agent_obj.get_current_status_code()
    context = agent_obj.get_transaction_context()
    message = create_end_transaction_message(context, bt, status_code)
    agent_obj.logger.info("status_code {}, message {}".format(status_code, message))

    agent_obj.udp_connection.send(message)
    rc = 0  # DUMMY VALUE FOR SUCCESS
    agent_obj.reset_transaction_context()

    return rc


def store_business_transaction(agent_obj, bt, unique_bt_id):
    pass


def db_call_begin(agent_obj, bt, db_host, db_query):
    pass


def db_call_end(agent_obj, bt, ip_handle):
    pass


def http_call_begin(agent_obj, bt, http_host, url):
    handle = 1  # DUMMY NON ZERO VALUE
    return handle


def http_call_end(agent_obj, bt, ip_handle):
    pass

def http_req_resp_wrapper(agent_obj, bt, rbuffer, rtype, statuscode):
    context = agent_obj.get_transaction_context()
    message = create_transaction_encode_http_message(context, bt, rbuffer, rtype, statuscode)
    logger.info("transaction_encode_http message {}".format(message))
    agent_obj.udp_connection.send(message)

def havoc_message(agent_obj, havoc_header):
    context = agent_obj.get_transaction_context()
    message = create_havoc_message(context, havoc_header)
    logger.debug("havoc_message: {}".format(message))
    agent_obj.udp_connection.send(message)
