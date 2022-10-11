import json
import socket
import logging
import traceback

from datetime import datetime


class Formatter(logging.Formatter):

    def __init__(self, label=None, tags=None):
        self.label = label if label else 'Main'
        self.tags = tags if tags else []
        self.host = socket.gethostname()

    def format(self, record):
        message = self.build_dict(record)
        message.update(self.add_extra_fields(record))
        message = self.check_for_exceptions(record, message)
        return self.serialize(message) + b'\n'

    def build_dict(self, record):
        return {
            '@timestamp': self.format_timestamp(record.created),
            'message': record.getMessage(),
            'level': record.levelname,
            'name': record.name,
            'host': self.host,
            'label': self.label,
            'tags': self.tags,
        }

    @staticmethod
    def format_timestamp(time):
        timestamp = datetime.utcfromtimestamp(time)
        return timestamp.isoformat()

    def add_extra_fields(self, record):
        known_skips = self.get_known_skips()
        fields = {}
        for key, value in record.__dict__.items():
            if key not in known_skips:
                fields[key] = self.add_field(value)
        return fields

    @staticmethod
    def get_known_skips():
        # The below contains all the attributes listed in
        # http://docs.python.org/library/logging.html#logrecord-attributes
        return (
            'args', 'asctime', 'created', 'exc_info', 'exc_text', 'filename',
            'funcName', 'id', 'levelname', 'levelno', 'lineno', 'module',
            'msecs', 'msecs', 'message', 'msg', 'name', 'pathname', 'process',
            'processName', 'relativeCreated', 'thread', 'threadName', 'extra',
            'auth_token', 'password', 'stack_info'
        )

    def add_field(self, value):
        easy_types = self.get_easy_types()
        return value if isinstance(value, easy_types) else repr(value)

    @staticmethod
    def get_easy_types():
        return str, bool, dict, float, int, list, type(None)

    def check_for_exceptions(self, record, message):
        if record.exc_info:
            message.update(self.get_debug_fields(record))
        return message

    def get_debug_fields(self, record):
        fields = {
            'stack_trace': self.format_exception(record.exc_info),
            'lineno': record.lineno,
            'process': record.process,
            'thread_name': record.threadName,
        }

        if getattr(record, 'funcName', None):
            fields['funcName'] = record.funcName

        if getattr(record, 'processName', None):
            fields['processName'] = record.processName

        return fields

    @staticmethod
    def format_exception(exc_info):
        return ''.join(traceback.format_exception(*exc_info)) if exc_info else ''

    @staticmethod
    def serialize(message):
        return bytes(json.dumps(message), encoding='u8')


# That's all folks...
