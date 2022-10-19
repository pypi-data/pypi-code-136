import sys
import time

from socket_oneline import OnelineClient
from ver.core.ver_services import VerServices


# --------------------
## sample Client that wraps the OnelineClient
class VerClient:
    # --------------------
    ## constructor
    def __init__(self):
        ## holds reference to Oneline Client
        self.olc = OnelineClient()

    # --------------------
    ## initialize the OnelineClient and connect to the server
    #
    # @return None
    def init(self):
        self._log('started')

        self.olc.ip_address = VerServices.ip_address
        self.olc.ip_port = VerServices.ip_port
        self.olc.logger = VerServices.logger
        self.olc.verbose = VerServices.verbose
        if not self.olc.init():
            self._log('ERR failed to set params')
            return

        self.olc.connect()
        # TODO replace with wait_until... with timeout
        time.sleep(0.1)

    # --------------------
    ## terminate
    #
    # @return None
    def term(self):
        if self.olc is not None:
            self.olc.disconnect()
            self.olc.term()
            self.olc = None

    # --------------------
    ## ping the Server
    #
    # @return the response (should be 'pong')
    def ping(self):
        return self.send_recv('ping')

    # --------------------
    ## send a command to the Server, wait for a response
    #
    # @param cmd  the command to send
    # @return the response
    def send_recv(self, cmd):
        self.send(cmd)
        rsp = self.recv()
        return rsp

    # --------------------
    ## send a cmd01 command to the Server
    #
    # @return the response (should be 'ack')
    def cmd01(self):
        return self.send_recv('cmd01')

    # --------------------
    ## send a disconnect ocmmand to the Server
    #
    # @return None
    def disconnect(self):
        self.olc.disconnect()

    # --------------------
    ## send a shutdown command to the Server
    #
    # @return None
    def shutdown(self):
        self.olc.shutdown()

    # --------------------
    ## send a command to the Server
    #
    # @param cmd  the command to send
    # @return None
    def send(self, cmd):
        self._log(f'tx: {cmd}')
        self.olc.send(cmd)

    # --------------------
    ## wait for a response from the Server
    #
    # @return the response
    def recv(self):
        rsp = self.olc.recv()
        self._log(f'rx: {rsp}')
        return rsp

    # --------------------
    ## log the message
    # if verbose is False, then nothing is logged
    # if verbose is True, and logger is defined, the msg is logged
    # if verbose is True, and logger is not defined, the msg is printed to stdout
    #
    # @param msg  the message to log
    # @return None
    def _log(self, msg):
        # handle verbose/quiet
        if not VerServices.verbose:
            return

        buf = f'ver_client  : {msg}'
        if VerServices.logger is None:
            print(buf)
            sys.stdout.flush()
        else:
            VerServices.logger.info(buf)
