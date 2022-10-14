
"""Utilities for Cavisson Python Agent code.

"""

from __future__ import unicode_literals
import errno

from logging import Formatter
import os

#mport _thread as thread
from .lang import thread

try:
    import greenlet
    try:
        get_ident = lambda: hash(greenlet.getcurrent())
#        print "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
        GREENLETS_ENABLED = True
    except:
 #      print "get_ident except "
        get_ident = thread.get_ident().ident

   # get_ident = lambda: hash(greenlet.getcurrent())
   # GREENLETS_ENABLED = True
except ImportError:
    get_ident = thread.get_ident
    GREENLETS_ENABLED = False

items = lambda d: d.items()


default_log_formatter = Formatter('%(asctime)s [%(levelname)s] %(funcName)s(%(lineno)d) <%(process)d>: %(message)s')

class LazyWsgiRequest(object):
    """Lazily read request line and headers from a WSGI environ.

    This matches enough of the Werkzeug Request API for the agent's needs: it
    only provides access to the information in the request line and the
    headers that is needed for the agent. (Since the agent doesn't inspect
    the request body, we don't touch any of that.)

    Parameters
    ----------
    environ : dict
        A WSGI environment.

    Attributes
    ----------
    headers : dict
        A dictionary of the HTTP headers. The headers are lowercase with
        dashes separating words.
    method : str
        The request method (e.g., GET).
    url : str
        The URL of the request (reconstructed according to PEP 333).
    cookies : dict
        The cookies passed in the request header (if any).
    path : str
        The path part of the request. Note that unlike raw WSGI, this will be
        just '/' if it would otherwise be empty.
    args : dict
        The query parameters. This is not a multi-dict: if a parameter is
        repeated multiple times, one of them wins.
    referer : str
        The HTTP Referer string.
    user_agent : str
        The HTTP User-Agent string.
    is_ajax : bool
        True if this request is AJAX.
    is_mobile : bool
        True if this request is from mobile.

    """
    DEFAULT_PORTS = {
        'http': 80,
        'https': 443,
    }

    def __init__(self, environ):
        super(LazyWsgiRequest, self).__init__()
        self.environ = environ.copy()

        self._headers = None
        self._host = None
        self._port = None
        self._http_host = None
        self._url = None
        self._path = None
        self._args = None
        self._cookies = None

def mkdir(path):
    """Create the directory in path, creating any intermediate directories.

    Does not complain if the directory already exists.

    """
    try:
        os.makedirs(path)
        #print("Logging path: ",path)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
