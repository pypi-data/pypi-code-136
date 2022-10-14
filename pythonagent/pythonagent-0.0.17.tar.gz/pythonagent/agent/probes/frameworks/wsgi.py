"""Interceptors and utilities for dealing with WSGI-based apps/frameworks"""
import os
import sys
import pstats 
from sys import settrace
from datetime import datetime, timedelta
import imp
import inspect
from functools import wraps
import threading
import pythonagent.agent
from ..base import EntryPointInterceptor
#from lib import LazyWsgiRequest
from pythonagent import config
ENTRY_WSGI =8
#from agent.internal.proxy import *
from werkzeug.wrappers import Request ,Response
from pyclbr import readmodule
import os
import inspect
import cProfile
import pstats
from pythonagent.agent.probes.frameworks.test import dumpstacks
from pythonagent.agent.probes.frameworks.aisess import Aisession
#import AIsession
#import aisess
#aisess
#import importlib.util
#spec = importlib.util.spec_from_file_location("aisess", "/home/cavisson/my-shop/env/env/lib/python3.7/site-packages/pythonagent/agent/probes/frameworks/aisess.py")
#foo = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(foo)

#os.environ['Aisession_flag'] = 'True'

#profiler = None
def aiflagset(s,st,d,sname):
    os.environ['Aisession_flag'] = 'True'   
    global duration
    duration = d
    global starttime
    starttime = st
    global istart
    istart = s 
    global sess
    sess = sname

class WSGIInterceptor(EntryPointInterceptor):

    def attach(self, application):
        super(WSGIInterceptor, self).attach(application, patched_method_name='application_callable')

    def application_callable(self, application, instance, environ, start_response):
        # bt = self.start_transaction(ENTRY_WSGI, LazyWsgiRequest(environ))
        stack = inspect.stack()
        temp = {}
        the_method_called = stack[3][0].f_code.co_name
        print("the_method in wsgi.py ------------------>>>>>>>>>>>>>>>>>>>>>>",the_method_called)

        request = Request(environ)
        
        #thread dump captured
        #dumpstacks()

        # local trace function which returns itself
        # local trace function which returns itselfi

        
        if os.environ.get('Aisession_flag', 'None') == 'True' and os.environ.get('aisess_status', 'False') != 'True':
            profiler = Aisession(istart, starttime, duration, sess)
            profiler.enableprof()
            profiler.disableprof()

        bt = self.start_business_transaction(request.full_path, '')
        req_headers = self.parse_headers(request.headers.items())
        self.agent.http_req_resp_wrapper(bt, req_headers, "req", 200)

        self.agent.logger.debug("Modulename: WSGI interceptor class || bt value is :{0}".format(bt)) 


        try:
            self.agent.logger.info("Modulename: WSGI interceptor class || request is :{0} || request path is {1} || query_string: {2} || host: {3} ".format(request,(request.path,request.query_string,request.host)))
        except:
            pass

        try:
            response = application(instance, environ, self._make_start_response_wrapper(start_response))
            self.agent.logger.info("Modulename: WSGI interceptor class || response is :{0}".format(response))

        except:
            with self.log_exceptions():
                if bt:
                    bt.add_exception(*sys.exc_info())

            raise
        finally:

            method = the_method_called
            self.end_business_transaction(bt)

        return response

    def _make_start_response_wrapper(self, start_response):
        @wraps(start_response)
        def start_response_wrapper(status, headers, exc_info=None):
            #Deal with HTTP status codes, errors and EUM correlation.
            #See https://www.python.org/dev/peps/pep-0333/#the-start-response-callable for more information.
            with self.log_exceptions():
                bt = self.bt
                resp_headers = self.parse_headers(headers.copy())

                #traceparent_bytes, tracestate_bytes = self.agent.get_trace_headers(bt)
                #telemetry_headers = "|Traceparent$" + traceparent_bytes.decode() + "|Tracestate$" + tracestate_bytes.decode()
                #resp_headers = resp_headers + telemetry_headers

                self.agent.http_req_resp_wrapper(bt, resp_headers, "resp", 200)
                self.agent.logger.info("Modulename: WSGI interceptor class || bt value is :{0}".format(bt))

                if bt:
                    # Store the HTTP status code and deal with errors.
                    status_code, msg = status.split(' ', 1)
                    self.handle_http_status_code(bt, int(status_code), msg)

                    # Inject EUM metadata into the response headers.
                    # inject_eum_metadata(self.agent.eum_config, bt, headers)

            return start_response(status, headers, exc_info)

        return start_response_wrapper


    def parse_headers(self, input_list):
        output_str = ""
        for key, value in input_list:
            new_str = key + "$" + value + "|"
            output_str += new_str
        output_str = output_str[:-1]  # Remove last |
        output_str = output_str.replace("=", "$")
        # output_str = output_str.replace("&", "|")

        return output_str


class WSGIMiddleware(object):
    #self.agent.logger.info('Modulename: WSGIMiddleware class ')
    def __init__(self, application=None):
        self._application = application
        self._configured = False
        self._interceptor = WSGIInterceptor(pythonagent.agent.get_agent_instance(), None)
        self._load_application_lock = threading.Lock()
        #get_script()
        #from pythonagent import config
        #config.WSGI_SCRIPT_ALIAS = input("Enter the absolute path of WSGI application script. (command to get 'readlink -f <script_path.py>') : ")

    def load_application(self):
        wsgi_callable = config.WSGI_CALLABLE_OBJECT or 'application'

        config.WSGI_SCRIPT_ALIAS = os.environ.get('WSGI_SCRIPT_ALIAS')
        if not config.WSGI_SCRIPT_ALIAS and not config.WSGI_MODULE:
            raise AttributeError(
                'Cannot get WSGI application: the agent cannot load your '
                'application. You must set either CAV_WSGI_SCRIPT_ALIAS'
                'in order to load your application.')

        if config.WSGI_MODULE:
            module_name = config.WSGI_MODULE

            if ':' in module_name:
                module_name, wsgi_callable = module_name.split(':', 1)

            __import__(module_name)
            wsgi_module = sys.modules[module_name]
        else:
            wsgi_module = imp.load_source('wsgi_module', config.WSGI_SCRIPT_ALIAS)

        if wsgi_callable.endswith('()'):  # "Quick" callback
            app = getattr(wsgi_module, wsgi_callable[:-2])
            app = app()
        else:
            app = getattr(wsgi_module, wsgi_callable)

        self._application = app

    def wsgi_application(self, environ, start_response):
        return self._application(environ, start_response)

    def __call__(self, environ, start_response):
        #config.WSGI_SCRIPT_ALIAS = input("Enter the absolute path of WSGI application script. (command to get 'readlink -f <script_path.py>') : ")
        if not self._configured:
            pythonagent.agent.configure(environ)
            self._configured = True

        if not self._application:
            # CORE-60212 - We are deadlocking inside imp.load_source when
            # WSGI_SCRIPT_ALIAS is used and uwsgi workers are restarted. We
            # actually don't need to go inside `load_application` multiple
            # times, which should prevent the imp.load_source deadlock while
            # improving initial request performance a bit. (We do double-
            # checked locking so we don't take the lock on every __call__,
            # only the initial burst of concurrent ones.)
            with self._load_application_lock:
                if not self._application:
                    self.load_application()

        # The interceptor expects an unbound function to call, hence why this function is called like this.
        return self._interceptor.application_callable(WSGIMiddleware.wsgi_application, self, environ, start_response)

    def get_script():
        config.WSGI_SCRIPT_ALIAS = input("Enter the absolute path of WSGI application script. (command to get 'readlink -f <script_path.py>') : ")
        
