import atexit
import logging
import re
from threading import Thread

import httpx
from httpx import Limits
import requests

from cornflakes import default_ca_path


class ElkHandler(logging.Handler):
    """ElkHandler for the default python logger."""

    def __init__(
        self,
        hosts: str,
        index: str,
        port: int = 443,
        auth: str = "",
        silent: bool = True,
        ssl_enabled: bool = True,
        verify: str or bool = None,
        bulk_records_size=15,
    ):
        """Initializes the custom http handler.

        :param hosts (str): The URL that the logs will be sent to
        :param auth (str): The Authorization token being used
        :param silent (bool): If False the http response and logs will be sent to STDOUT for debug
        :param verify (bool or str): ca file or False
        :param ssl_enabled (bool): use https
        """
        self.__bulk_records_size = bulk_records_size
        self.__bulk_queue = bytearray()
        self.__records_size = 0
        self.protocol = "https://" if ssl_enabled else "http://"

        transport = httpx.HTTPTransport(retries=5, http2=True)
        self.client = httpx.Client(
            transport=transport,
            verify=verify if bool(verify) else default_ca_path(),
            limits=Limits(max_connections=self.max_poolsize, max_keepalive_connections=self.max_poolsize),
        )

        hosts = hosts.split(",")
        for host in hosts:
            try:
                self.url = f'{self.protocol}{re.sub("/$", "", host)}'
                if port:
                    self.url = f"{self.url}:{port}"
                self.client.get(self.url, timeout=10)
            except (requests.ConnectionError, requests.Timeout) as e:
                logging.error(f"No connection to {self.url}, {e}")
                self.url = None
            if self.url:
                break

        if index:
            self.url = f'{self.url}/{re.sub("^/", "", index)}/_bulk'
        self.auth = auth
        self.silent = silent

        # sets up a session with the server
        self.max_poolsize = 1000
        self.client.headers.update({"Content-Type": "application/json", "Authorization": f"Basic {self.auth}"})

        atexit.register(self._atexit_emit)
        super().__init__()

    def _atexit_emit(self):
        logging.debug("finish logstash bulk logs")
        if len(self.__bulk_queue) and self.url:
            response = self.client.post(self.url, data=self.__bulk_queue)
            if not self.silent:
                logging.info(response.content)
            self.client.close()

    def emit(self, record):
        """This function gets called when a log event gets emitted.

        It recieves a record, formats it and sends it to the url
        :param record: a log record
        """
        self.__bulk_queue.extend(b'{ "index": {} }\n')
        self.__bulk_queue.extend(self.format(record).encode("utf-8"))
        self.__bulk_queue.extend(b"\n")
        self.__records_size += 1
        if self.__records_size >= self.__bulk_records_size:
            response = self.client.post(self.url, data=self.__bulk_queue)
            self.__records_size = 0
            if not self.silent:
                logging.info(record)
                logging.info(response.content)


class AsyncElkHandler(ElkHandler):
    """AsyncElkHandler for the default python logger."""

    def __init__(self, *args, **kwargs):
        """Init Function for AsyncElkHandler."""
        super().__init__(*args, **kwargs)
        self.__queue = []
        self.__thread = Thread(target=self.__loop)
        self.__thread.daemon = True
        self.__thread.start()

    def emit(self, record):
        """This function gets called when a log event gets emitted.

        It recieves a record, formats it and sends it to the url
        :param record: a log record
        """
        self.__queue.append(record)

    def __loop(self):
        while True:
            if len(self.__queue):
                try:
                    super().emit(self.__queue.pop())
                except Exception as e:
                    raise e
