import sys
import time

from socket_oneline import OnelineServer
from ver.core.ver_services import VerServices


# --------------------
## Verification Server that wraps the OnelineServer
class VerServer:
    # --------------------
    ## constructor
    def __init__(self):
        ## holds reference to the Oneline Server
        self.ols = OnelineServer()

    # --------------------
    ## initialize
    # Start the OnelineServer
    #
    # @return None
    def init(self):
        self._log('started')

        self.ols.callback = self._callback
        self.ols.ip_address = VerServices.ip_address
        self.ols.ip_port = VerServices.ip_port
        self.ols.logger = VerServices.logger
        self.ols.verbose = VerServices.verbose
        if not self.ols.start():
            self._log('ERR failed to set params')
            return False
        # TODO convert to wait_until... with timeout
        time.sleep(0.1)
        return True

    # --------------------
    ## terminate
    #
    # @return None
    def term(self):
        self.ols.term()

    # --------------------
    ## wait until the server stops running i.e. it is shutdown
    #
    # @return None
    def wait_until_done(self):
        while self.ols.is_running:
            time.sleep(0.5)

    # --------------------
    ## callback function used by OnelineServer to handle incoming commands
    #
    # @param cmd  the incoming command from the client
    # @return None
    def _callback(self, cmd):
        self._log(f'callback: cmd="{cmd}"')
        if cmd == 'cmd01':
            self.ols.send('ack')
        else:
            # unknown command, let client know
            self.ols.send('nak - unknown cmd')

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

        buf = f'ver_server  : {msg}'
        if VerServices.logger is None:
            print(buf)
            sys.stdout.flush()
        else:
            VerServices.logger.info(buf)
