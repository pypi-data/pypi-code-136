#  Copyright (c) 2021-2022 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Socket to mime a Telnet server for the tests
"""
import logging
import socket
import threading
from abc import abstractmethod
from time import sleep
from typing import Optional

logging.basicConfig(level=logging.DEBUG)


class LocalTelnetTestServer:
    """
    Local Telnet Sever for testing
    """

    def __init__(self, port=23, timeout=1):
        self._host = ""  # "127.0.0.1"
        self._port = port
        self._timeout = timeout
        self._socket = socket.socket()
        self._client = None
        self._addr = None
        logging.debug("LocalTelnetTestServer created")
        logging.debug("Bind...")
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self._host, self._port))
        logging.debug("Start listen")
        self._socket.listen()

    def __del__(self):
        _socket = getattr(self, "_socket", None)
        if _socket is not None:
            _socket.close()
            del _socket

    def open(self):
        logging.debug("Accepting?")
        self._socket.settimeout(self._timeout)
        self._client, self._addr = self._socket.accept()
        logging.debug(f"Accepted: {self._client} with {self._addr}")
        self._client.settimeout(self._timeout)

    def close(self):
        if self._client is not None:
            self._client.close()
            self._client = None

    def put_text(self, text: str, encoding=None):
        if encoding is None:
            self._client.send(text.encode())
        else:
            self._client.send(text.encode(encoding=encoding))

    def get_written(self):
        # logging.debug("Receiving")
        try:
            data = self._client.recv(1024)
            # logging.debug(f"Received: {data}")
            return data.decode().strip()
        except socket.timeout:
            return None


class RunningDeviceMockup:
    def __init__(self, port, timeout=1, polling_interval=0.01):
        self._ts = LocalTelnetTestServer(port=port, timeout=timeout)

        self.polling_interval: float = polling_interval
        self.keep_running: bool = True

        self.last_request = ""
        self.custom_answer = ""

        self._starting = threading.Thread(target=self.open)
        self._automatic_answer_thread = threading.Thread(target=self._listen_and_answer)

    def __enter__(self):
        self._starting.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def open(self):
        self._ts.open()
        self._automatic_answer_thread.start()

    def close(self):
        self.keep_running = False
        self._automatic_answer_thread.join()
        self._ts.close()

    def get_written(self):
        return self._ts.get_written()

    def put_text(self, request, encoding=None):
        self._ts.put_text(text=request, encoding=encoding)

    def _listen_and_answer(self):
        while self.keep_running:
            request = self.get_written()
            if not request:
                continue

            logging.debug(f"{self.__class__} got: {request}")
            self.listen_and_answer(request)

            sleep(self.polling_interval)

    @abstractmethod
    def listen_and_answer(self, request):
        pass


class LocalTechnixServer(RunningDeviceMockup):
    def __init__(self, port=4660, timeout=1):
        super().__init__(port, timeout)

        self.listen_and_repeat = (
            "P5,0",  # HV on
            "P5,1",
            "P6,0",  # HV off
            "P6,1",
            "P7,0",  # Local/remote mode
            "P7,1",
            "P8,0",  # Inhibit
            "P8,1",
        )

        self.status: int = 0
        self.voltage: Optional[int] = None
        self.current: Optional[int] = None

    def listen_and_answer(self, request):
        if request == "E":
            self.put_text(f"E{self.status}")
        elif request in self.listen_and_repeat:
            self.put_text(request)
            logging.debug(f"TechnixMockup returned the request: {request}")
        elif self.voltage is not None and request == "a1":
            self.put_text(f"a1{self.voltage}")
        elif self.current is not None and request == "a2":
            self.put_text(f"a2{self.current}")
        else:
            self.last_request = request
            self.put_text(self.custom_answer)


class LocalT560Server(RunningDeviceMockup):
    def __init__(self, port=9999, timeout=1):
        super().__init__(port, timeout)

        self.response = "OK"

        self.response_dict = {
            "AU": "0",
            "AS": "Ch A  POS  OFF  Dly  00.000,001  Wid  00.000,002",
            "BS": "Ch B  NEG  ON  Dly  00.000,000  Wid  00.000,002",
            "CS": "Ch C  POS  ON  Dly  00.000,000  Wid  00.000,002",
            "DS": "Ch D  POS  OFF  Dly  00.000,000  Wid  00.000,002",
            "GA": "Gate INP POS HIZ Shots 0000000066",
            "TR": "Trig REM HIZ Level 1.250 Div 00 SYN 00010000.00",
            "Throw an error": "??",
        }

    def listen_and_answer(self, request):
        if request in self.response_dict.keys():
            self.put_text(self.response_dict[request])
        else:
            self.put_text(self.response)


class LocalFluke8845aServer(RunningDeviceMockup):
    def __init__(self, port=3490, timeout=1):
        super().__init__(port, timeout)

    def listen_and_answer(self, request):
        logging.debug(f"Fluke8845aMockup got: {request}")
        if "*IDN?" in request:
            self.put_text("FLUKE,8845A,2540017,08/02/10-11:53")
        elif "FETC?" in request:
            self.put_text("1.234")
        elif "?" in request:
            self.last_request = request
            self.put_text(self.custom_answer)
