import time
import logging
from os import linesep
from telnetlib import Telnet
from threading import Thread
from typing import List, Tuple, Dict

class Videohub:    
    """Blackmagic Design Smart Videohub Control Interface

    Parameters
    ----------
    ip : str
        Local IP Address of the Smart Videohub
    """
    def __init__(self, ip: str) -> None:     
        self.ip = ip
        self.connection = Telnet(ip, 9990)
        self.logger = logging.getLogger(__name__)

        self._reader_thread = Thread(target=self._reader)
        self._reader_thread.start()

        # Device Info
        self.protocol_version = None # type: str
        """Videohub Ethernet Protocol Version (ex. '2.7')
        """
        self.model = None # type: str
        """Model of Videohub (ex. 'Blackmagic Smart Videohub 20 x 20')
        """
        self.unique_id = None # type: str
        """Generated unique identifier for each Videohub, persists across boots and network changes. (ex. '7C2E0DA4BFC0' )
        """
        self.inputs = 0 # type: int
        """Number of Video Inputs (sources)
        """
        self.outputs = 0 # type: int
        """Number of Video Outputs (destinations)
        """

        # Routing Elements
        self.input_labels = None # type: List[str]
        """Custom labels for inputs, keyed by source (input).
        """
        self.output_labels = None # type: List[str]
        """Custom labels for outputs, keyed by destination (output).
        """
        self.routing = None # type: List[int]
        """Videohub routing keyed by destination (output)
        """

    def _reader(self) -> None:
        while True:
            try:
                message = self.connection.read_until(bytes('\n', 'ascii'))
                # self.logger.debug(message.decode('ascii'))
                try:
                    if message.decode('ascii')[-2] == ':':
                        message += self.connection.read_until(bytes('\n\n', 'ascii'))
                        self._decode_message(message)
                    else:
                        self._decode_response(message)
                except IndexError as e:
                    self._decode_response(message)
            except Exception as e:
                self.logger.error(e)
                time.sleep(3)
                self.connection = Telnet(self.ip, 9990)

    
    def _send(self, command: str) -> None:
        self.logger.debug(f'Sending Message: [{command.replace(linesep, "-")}]')
        self.connection.write(bytes(command + '\n\n', 'ascii'))

    def _decode_message(self, message: bytes) -> None:
        msg = message.decode('ascii').rstrip('\n\n')
        lines = msg.split('\n')
        self.logger.debug(f'Recieved Message: [{msg.replace(linesep, "//")}]')
        self._response_processor(lines)
    
    def _decode_response(self, message: bytes) -> None:
        response = message.decode('ascii').rstrip('\n')
        self.logger.debug(f'Recieved Response: [{response.replace(linesep, "//")}]')

    def _response_processor(self, message: List[str]) -> None:
        message_type = message[0].rstrip(':')
        contents = message[1:]
        if message_type == 'PROTOCOL PREAMBLE':
            self._process_protocol_preamble(contents)
        elif message_type == 'VIDEOHUB DEVICE':
            self._process_videohub_device(contents)
        elif message_type == 'INPUT LABELS':
            self._process_input_labels(contents)
        elif message_type == 'OUTPUT LABELS':
            self._process_output_labels(contents)
        elif message_type == 'VIDEO OUTPUT LOCKS':
            pass
        elif message_type == 'VIDEO OUTPUT ROUTING':
            self._process_output_routing(contents)
        elif message_type == 'CONFIGURATION':
            pass
    
    def _process_protocol_preamble(self, message_contents: List[str]) -> None:
        for item in message_contents:
            key, value = item.split(': ')
            if key == 'Version':
                self.protocol_version = value

    def _process_videohub_device(self, message_contents: List[str]) -> None:
        for item in message_contents:
            key, value = item.split(': ')
            if key == 'Model name':
                self.model = value
            elif key == 'Unique ID':
                self.unique_id = value
            elif key == 'Video inputs':
                self.inputs = int(value)
                self.input_labels = [''] * self.inputs
            elif key == 'Video outputs':
                self.outputs = int(value)
                self.output_labels = [''] * self.outputs
                self.routing = [-1] * self.outputs
    
    def _process_input_labels(self, message_contents: List[str]) -> None:
        for item in message_contents:
            i, label = item.split(' ', 1)
            self.input_labels[int(i)] = label
    
    def _process_output_labels(self, message_contents: List[str]) -> None:
        for item in message_contents:
            o, label = item.split(' ', 1)
            self.output_labels[int(o)] = label

    def _process_output_routing(self, message_contents: List[str]) -> None:
        for item in message_contents:
            destination, source = item.split(' ')
            self.routing[int(destination)] = int(source)

    def route(self, destination: int, source: int) -> None:
        """Re-route a single input to a single output.

        Parameters
        ----------
        destination : int
            Output Destination Identifier
        source : int
            Input Source Identifier
        """
        self._send(f'VIDEO OUTPUT ROUTING:\n{destination} {source}')
    
    def bulk_route(self, routes: List[Tuple[int, int]]) -> None:
        """Re-route multiple outputs at once, new routes take effect simultaneously.  An error in any route change may fail all otherwise valid changes. 

        Parameters
        ----------
        routes : List[Tuple[int, int]]
            A list of (destination, source) video output/input identifiers.
        """
        command = ''
        for route in routes:
            command += '\n' + str(route[0]) + ' ' + str(route[1])
        self._send('VIDEO OUTPUT ROUTING:' + command)

    def input_label(self, source: int, label: str) -> None:
        """Re-label a video input source.

        Parameters
        ----------
        source : int
            Input Video Source Identifier
        label : str
            New Label
        """
        self._send(f'INPUT LABELS:\n{source} {label}')
    
    def output_label(self, destination: int, label: str) -> None:
        """Re-label a video input source.

        Parameters
        ----------
        destination : int
            Output Video Destination Identifier
        label : str
            New Label
        """
        self._send(f'OUTPUT LABELS:\n{destination} {label}')