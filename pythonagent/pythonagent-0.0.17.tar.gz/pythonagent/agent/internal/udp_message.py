import struct
import binascii
import psutil
import os
import threading
import time

import logging
logger = logging.getLogger('pythonagent.agent')

class Header(object):

    def __init__(self, context, apiReqId, awsReqId, funcName):

        self.apiReqId = apiReqId
        self.awsReqId = awsReqId
        self.funcName = funcName
        self.tags = "tierName={};ndAppServerHost={};appName={}".format(context.tier_name, context.server_name, funcName)

        self.agentType = 0  # Python
        self.messageType = None

        self.apiReqLen = None
        self.awsReqLen = None
        self.funcNameLen = None
        self.tagslength = None
        self.whLen = None

    def encode(self, msg_type="default"):

        # 3 Defaults added in arguments for testing wsgi start fp for havoc inbound delay

        if self.apiReqId is None:
            self.apiReqId = "default_apiReqId"
        if self.awsReqId is None:
            self.awsReqId = "default_awsReqId"
        if self.funcName is None:
            self.funcName = "default_funcName"

        # Message Type

        if msg_type == "default":
            self.messageType = 0
        elif msg_type == "havoc":
            self.messageType = 1
        elif msg_type == "init":
            self.messageType = 2
        elif msg_type == "heartbeat":
            self.messageType = 3
        else:
            raise Exception("Invalid msg_type in wrap header")

        self.apiReqLen = len(self.apiReqId)
        self.awsReqLen = len(self.awsReqId)
        self.funcNameLen = len(self.funcName)
        self.tagslength = len(self.tags)

        self.whLen = (1                   # ^ (1c)
                      + 4                 # whLen(int)
                      + 4                 # apiReqLen(int)
                      + 4                 # awsReqLen(int)
                      + 4                 # funcNameLen(int)
                      + 4                 # tagslength(int)
                      + 2                 # agentType(short)
                      + 2                 # messageType(short)
                      + self.apiReqLen    # variable
                      + self.awsReqLen    # variable
                      + self.funcNameLen  # variable
                      + self.tagslength)  # variable

        header_struct = struct.Struct('=ciiiiihh{}s{}s{}s{}s'.format(self.apiReqLen, self.awsReqLen,
                                                                     self.funcNameLen, self.tagslength))

        header_values = (bytes('^', "utf-8"),
                         self.whLen,
                         self.apiReqLen,
                         self.awsReqLen,
                         self.funcNameLen,
                         self.tagslength,
                         self.agentType,
                         self.messageType,
                         self.apiReqId.encode('utf-8'),
                         self.awsReqId.encode('utf-8'),
                         self.funcName.encode('utf-8'),
                         self.tags.encode('utf-8'))

        header_packet = header_struct.pack(*header_values)

        return header_packet


class StartTransactionMessage(object):

    def __init__(self, url, flow_path_instance):
        self.fp_header = "dummy_fp_header"
        self.url = url
        self.btHeaderValue = "dummy_btHeaderValue"
        self.ndCookieSet = ""
        self.nvCookieSet = ""
        self.correlationHeader = "dummy_correlationHeader"
        self.flow_path_instance = flow_path_instance
        self.qTimeMS = 0  # DUMMY
        self.startTimeFP = 0  # DUMMY

    def encode(self):

        self.len_fp_header = len(self.fp_header)
        self.len_url = len(self.url)
        self.len_btHeaderValue = len(self.btHeaderValue)
        self.len_ndCookieSet = len(self.ndCookieSet)
        self.len_nvCookieSet = len(self.nvCookieSet)
        self.len_correlationHeader = len(self.correlationHeader)


        self.header_len = (4                            # header_len(int)
                           + 4                          # total_len(int)
                           + 4)                         # msg_type(int)

        self.total_len = (1                             # ^ (1c)
                          + 4                           # header_len(int)
                          + 4                           # total_len(int)
                          + 4                           # msg_type(int)
                          + 1                           # | (1c)
                          + 4                           # len_fp_header(int)
                          + 4                           # len_url(int)
                          + 4                           # len_btHeaderValue(int)
                          + 4                           # len_ndCookieSet(int)
                          + 4                           # len_nvCookieSet(int)
                          + 4                           # len_correlationHeader(int)
                          + 8                           # flow_path_instance(long long)
                          + 8                           # qTimeMS(long)
                          + 8                           # startTimeFP(long long)
                          + self.len_fp_header          # variable
                          + self.len_url                # variable
                          + self.len_btHeaderValue      # variable
                          + self.len_ndCookieSet        # variable
                          + self.len_nvCookieSet        # variable
                          + self.len_correlationHeader  # variable
                          + 1)                          # \n (1c)

        self.msg_type = 2  # START TRANSACTION

        format_str = "=ciiiciiiiiiqqq{}s{}s{}s{}s{}s{}sc".format(self.len_fp_header, self.len_url,
                                                                 self.len_btHeaderValue, self.len_ndCookieSet,
                                                                 self.len_nvCookieSet, self.len_correlationHeader)

        start_transaction_message_struct = struct.Struct(format_str)

        start_transaction_message_values = (bytes('^', "utf-8"),
                                            self.header_len,
                                            self.total_len,
                                            self.msg_type,
                                            bytes('|', "utf-8"),
                                            self.len_fp_header,
                                            self.len_url,
                                            self.len_btHeaderValue,
                                            self.len_ndCookieSet,
                                            self.len_nvCookieSet,
                                            self.len_correlationHeader,
                                            self.flow_path_instance,
                                            self.qTimeMS,
                                            self.startTimeFP,
                                            self.fp_header.encode('utf-8'),
                                            self.url.encode('utf-8'),
                                            self.btHeaderValue.encode('utf-8'),
                                            self.ndCookieSet.encode('utf-8'),
                                            self.nvCookieSet.encode('utf-8'),
                                            self.correlationHeader.encode('utf-8'),
                                            bytes('\n', "utf-8"))

        start_transaction_message_packet = start_transaction_message_struct.pack(*start_transaction_message_values)

        return start_transaction_message_packet


class MethodEntryMessage(object):

    def __init__(self, methodName, query_string, url_parameter, flow_path_instance):
        self.methodName = methodName
        self.query_string = query_string
        self.urlParameter = url_parameter

        self.mid = 0  # DUMMY
        self.flow_path_instance = flow_path_instance
        self.threadId = 0  # DUMMY
        self.startTime = 0  # DUMMY

    def encode(self):

        self.len_methodName = len(self.methodName)
        self.len_query_string = len(self.query_string)
        self.len_urlParameter = len(self.urlParameter)

        self.header_len = (4                            # header_len(int)
                           + 4                          # total_len(int)
                           + 4)                         # msg_type(int)

        self.total_len = (1                             # ^ (1c)
                          + 4                           # header_len(int)
                          + 4                           # total_len(int)
                          + 4                           # msg_type(int)
                          + 1                           # | (1c)
                          + 4                           # mid(int)
                          + 8                           # flow_path_instance(long long)
                          + 8                           # threadId(long)
                          + 8                           # startTime(long long)
                          + 4                           # len_methodName(int)
                          + 4                           # len_query_string(int)
                          + 4                           # len_urlParameter(int)
                          + self.len_methodName         # variable
                          + self.len_query_string       # variable
                          + self.len_urlParameter       # variable
                          + 1)                          # \n (1c)

        self.msg_type = 0  # METHOD ENTRY

        format_str = "=ciiiciqqqiii{}s{}s{}sc".format(self.len_methodName, self.len_query_string, self.len_urlParameter)

        method_entry_message_struct = struct.Struct(format_str)

        method_entry_message_values = (bytes('^', "utf-8"),
                                       self.header_len,
                                       self.total_len,
                                       self.msg_type,
                                       bytes('|', "utf-8"),
                                       self.mid,
                                       self.flowpathinstance,
                                       self.threadId,
                                       self.startTime,
                                       self.len_methodName,
                                       self.len_query_string,
                                       self.len_urlParameter,
                                       self.methodName.encode('utf-8'),
                                       self.query_string.encode('utf-8'),
                                       self.urlParameter.encode('utf-8'),
                                       bytes('\n', "utf-8"))

        method_entry_message_packet = method_entry_message_struct.pack(*method_entry_message_values)

        return method_entry_message_packet


class MethodExitMessage(object):

    def __init__(self, methodName, backend_header, status, duration):

        self.methodName = methodName
        self.backend_header = backend_header
        self.requestNotificationPhase = "dummy_requestNotificationPhase"
        self.statusCode = status
        self.duration = duration
        self.mid = 0  # DUMMY
        self.eventType = 0  # DUMMY
        self.isCallout = 1  # DUMMY 1
        self.threadId = 0  # DUMMY threading.get_ident()
        self.flowpathinstance = 0  # DUMMY
        self.cpuTime = 0  # DUMMY

        self.len_methodName = None
        self.len_backend_header = None
        self.len_requestNotificationPhase = None

        self.tierCallOutSeqNum = 1  # DUMMY
        self.endTime = 0  # DUMMY

        self.header_len = None
        self.total_len = None

        self.msg_type = 1  # METHOD EXIT


    def encode(self):
        self.len_methodName = len(self.methodName)
        self.len_backend_header = len(self.backend_header)
        self.len_requestNotificationPhase = len(self.requestNotificationPhase)

        self.header_len = (4                                       # header_len(int)
                           + 4                                     # total_len(int)
                           + 4)                                    # msg_type(int)

        #self.total_len = 3 + 12 + 80 + self.len_methodName + self.len_backend_header + self.len_requestNotificationPhase

        self.total_len = (1                                        # ^ (1c)
                          + 4                                      # header_len(int)
                          + 4                                      # total_len(int)
                          + 4                                      # msg_type(int)
                          + 1                                      # | (1c)
                          + 4                                      # status_code(int)
                          + 4                                      # mid(int)
                          + 4                                      # eventType(int)
                          + 4                                      # isCallout(int)
                          + 8                                      # threadId(long)
                          + 8                                      # duration(long)
                          + 8                                      # flow_path_instance(long long)
                          + 8                                      # cpuTime(long long)
                          + 4                                      # len_methodName(int)
                          + 4                                      # len_backend_header(int)
                          + 4                                      # len_requestNotificationPhase(int)
                          + 8                                      # tierCallOutSeqNum(long long)
                          + 8                                      # endTime(long long)
                          + self.len_methodName                    # variable
                          + self.len_backend_header                # variable
                          + self.len_requestNotificationPhase      # variable
                          + 1)                                     # \n (1c)


        format_str = "=ciiiciiiiqqqqiiiqq{}s{}s{}sc".format(self.len_methodName, self.len_backend_header, self.len_requestNotificationPhase)

        method_exit_message_struct = struct.Struct(format_str)

        method_exit_message_values = (bytes('^', "utf-8"),
                                      self.header_len,
                                      self.total_len,
                                      self.msg_type,
                                      bytes('|', "utf-8"),
                                      self.statusCode,
                                      self.mid,
                                      self.eventType,
                                      self.isCallout,
                                      self.threadId,
                                      self.duration,
                                      self.flow_path_instance,
                                      self.cpuTime,
                                      self.len_methodName,
                                      self.len_backend_header,
                                      self.len_requestNotificationPhase,
                                      self.tierCallOutSeqNum,
                                      self.endTime,
                                      self.methodName.encode('utf-8'),
                                      self.backend_header.encode('utf-8'),
                                      self.requestNotificationPhase.encode('utf-8'),
                                      bytes('\n', "utf-8"))

        method_exit_message_packet = method_exit_message_struct.pack(*method_exit_message_values)
        logger.debug("status {} duration {}".format(self.statusCode, self.duration))

        return method_exit_message_packet


class EndTransactionMessage(object):

    def __init__(self, status_code, flow_path_instance):

        self.status_code = status_code
        self.flow_path_instance = flow_path_instance
        self.endTime = 0  # DUMMY
        self.cpuTime = 0  # DUMMY
        self.header_len = None
        self.total_len = None
        self.msg_type = 3  # END TRANSACTION

    def encode(self):

        self.header_len = (4                                       # header_len(int)
                           + 4                                     # total_len(int)
                           + 4)                                    # msg_type(int)

        #self.total_len = 3 + 12 + 32

        self.total_len = (1                                        # ^ (1c)
                          + 4                                      # header_len(int)
                          + 4                                      # total_len(int)
                          + 4                                      # msg_type(int)
                          + 1                                      # | (1c)
                          + 4                                      # status_code(int)
                          + 8                                      # flow_path_instance(long long)
                          + 8                                      # endTime(long long)
                          + 8                                      # cpuTime(long long)
                          + 1)                                     # \n (1c)

        end_transaction_message_struct = struct.Struct("=ciiiciqqqc")

        end_transaction_message_values = (bytes('^', "utf-8"),
                                          self.header_len,
                                          self.total_len,
                                          self.msg_type,
                                          bytes('|', "utf-8"),
                                          self.status_code,
                                          self.flow_path_instance,
                                          self.endTime,
                                          self.cpuTime,
                                          bytes('\n', "utf-8"))

        end_transaction_message_packet = end_transaction_message_struct.pack(*end_transaction_message_values)

        return end_transaction_message_packet


class TransactionEncodeHttpMessage(object):

    def __init__(self, bt, rbuffer, rtype, statuscode, flow_path_instance):

        # bt = 140544547110928
        # http_host = "www.google.com"
        # url = "/"
        self.buffer = rbuffer
        self.type = rtype
        self.statuscode = statuscode
        self.flow_path_instance = flow_path_instance

    def encode(self):
        self.buffer_len = len(self.buffer)
        self.type_len = len(self.type)

        self.header_len = 12
        self.total_len = 12 + 20 + self.buffer_len + self.type_len + 3
        self.msg_type = 6  # HTTP CALLOUT BEGIN, 7 FOR END

        format_str = "=ciiiciiiq{}s{}sc".format(self.buffer_len, self.type_len)

        transaction_encode_http_message_struct = struct.Struct(format_str)

        transaction_encode_http_message_values = (bytes('^', "utf-8"),
                                                  self.header_len,
                                                  self.total_len,
                                                  self.msg_type,
                                                  bytes('|', "utf-8"),
                                                  self.statuscode,
                                                  self.buffer_len,
                                                  self.type_len,
                                                  self.flow_path_instance,
                                                  self.buffer.encode('utf-8'),
                                                  self.type.encode('utf-8'),
                                                  bytes('\n', "utf-8"))

        transaction_encode_http_message_packet = transaction_encode_http_message_struct.pack(*transaction_encode_http_message_values)


        return transaction_encode_http_message_packet


class HavocMessage(object):

    def __init__(self, havoc_header):
        self.havoc_header = havoc_header
        self.len_havoc_header = None

    def encode(self):

        self.len_havoc_header = len(self.havoc_header)

        format_str = "=c{}s".format(self.len_havoc_header)

        havoc_message_struct = struct.Struct(format_str)

        havoc_message_values = (bytes('^', "utf-8"),
                                self.havoc_header.encode('utf-8'))

        havoc_message_packet = havoc_message_struct.pack(*havoc_message_values)

        return havoc_message_packet


def create_start_transaction_message(context, bt_name, correlation_header):
    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    header_packet = header.encode()

    start_transaction_message = StartTransactionMessage(bt_name, context.flow_path_id)
    start_transaction_message_packet = start_transaction_message.encode()

    full_packet = header_packet + start_transaction_message_packet

    return full_packet


def create_method_entry_message(context, bt, method, query_string, url_parameter):

    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    header_packet = header.encode()

    method_entry_message = MethodEntryMessage(method, query_string, url_parameter, context.flow_path_id)
    method_entry_message_packet = method_entry_message.encode()

    full_packet = header_packet + method_entry_message_packet

    return full_packet


def create_method_exit_message(context, bt, method, backend_header, status, duration):
    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    header_packet = header.encode()

    method_exit_message = MethodExitMessage(method, backend_header, status, duration, context.flow_path_id)
    method_exit_message_packet = method_exit_message.encode()

    full_packet = header_packet + method_exit_message_packet

    return full_packet


def create_end_transaction_message(context, bt, statuscode):
    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    header_packet = header.encode()

    end_transaction_message = EndTransactionMessage(statuscode, context.flow_path_id)
    end_transaction_message_packet = end_transaction_message.encode()

    full_packet = header_packet + end_transaction_message_packet

    return full_packet


def create_havoc_message(context, havoc_header):

    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    msg_type = "havoc"
    header_packet = header.encode(msg_type)

    havoc_message = HavocMessage(havoc_header)
    havoc_message_packet = havoc_message.encode()

    full_packet = header_packet + havoc_message_packet

    return full_packet


def create_transaction_encode_http_message(context, bt, rbuffer, rtype, statuscode):
    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    header_packet = header.encode()

    transaction_encode_http_message = TransactionEncodeHttpMessage(bt, rbuffer, rtype, statuscode, context.flow_path_id)
    transaction_encode_http_message_packet = transaction_encode_http_message.encode()

    full_packet = header_packet + transaction_encode_http_message_packet

    return full_packet


class InitMessage(object):

    def __init__(self):
        self.buffer = "dummy_buffer"

    def encode(self):
        init_message_struct = struct.Struct("=c")
        init_message_values = (bytes('^', "utf-8"),)
        init_message_packet = init_message_struct.pack(*init_message_values)
        return init_message_packet

def create_init_message(context):
    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    logger.debug('function name inside wrap header {}'.format(context.function_name))
    msg_type = "init"
    header_packet = header.encode(msg_type)

    init_message = InitMessage()
    init_message_encode_packet = init_message.encode()

    full_packet = header_packet + init_message_encode_packet

    return full_packet


class HeartbeatMessage(object):

    def __init__(self):
        self.buffer = "dummy_buffer"

    def encode(self):

        heartbeat_message_struct = struct.Struct("=c")
        heartbeat_message_values = (bytes('^', "utf-8"),)
        heartbeat_message_packet = heartbeat_message_struct.pack(*heartbeat_message_values)
        return heartbeat_message_packet


def create_heartbeat_message(context):
    header = Header(context, context.api_request_id, context.aws_request_id, context.function_name)
    logger.debug('function name inside wrap header {}'.format(context.function_name))
    msg_type = "heartbeat"
    header_packet = header.encode(msg_type)

    heartbeat_message = HeartbeatMessage()
    heartbeat_message_encode_packet = heartbeat_message.encode()

    full_packet = header_packet + heartbeat_message_encode_packet

    return full_packet
