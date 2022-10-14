

"""Definition of base entry and exit point interceptors.

"""


import sys
from functools import wraps
from contextlib import contextmanager
import time
from pythonagent.utils import get_current_timestamp_in_ms


class BaseInterceptor(object):
    def __init__(self, agent, cls):
        self.agent = agent
        self.cls = cls

    @property
    def bt(self):
        # add a docstring here about what current bt means now.
        return self.agent.get_current_bt()

    def __setitem__(self, key, value):
        bt = self.bt
        if bt:
            bt._properties[key] = value

    def __getitem__(self, key):
        bt = self.bt
        if bt:
            return bt._properties.get(key)

    def __delitem__(self, key):
        bt = self.bt
        if bt:
            bt._properties.pop(key, None)


    @staticmethod
    def _fix_dunder_method_name(method, class_name):
        # If `method` starts with '__', then it will have been renamed by the lexer to '_SomeClass__some_method'
        # (unless the method name ends with '__').
        if method.startswith('__') and not method.endswith('__'):
            method = '_' + class_name + method
        return method

    def _attach(self, method, wrapper_func, patched_method_name):
        patched_method_name = patched_method_name or '_' + method

        # Deal with reserved identifiers.
        # https://docs.python.org/2/reference/lexical_analysis.html#reserved-classes-of-identifiers
        method = self._fix_dunder_method_name(method, self.cls.__name__)
        patched_method_name = self._fix_dunder_method_name(patched_method_name, self.__class__.__name__)

        # Wrap the original method if required.
        original_method = getattr(self.cls, method)

        # Do not intercept the same method more than once.
        if hasattr(original_method, '_pythonagent_intercepted'):
            return

        if wrapper_func:
            @wraps(original_method)
            def wrapped_method(*args, **kwargs):
                return wrapper_func(original_method, *args, **kwargs)
            real_method = wrapped_method
        else:
            real_method = original_method

        # Replace `self.cls.method` with a call to the patched method.
        patched_method = getattr(self, patched_method_name)

        @wraps(original_method)
        def call_patched_method(*args, **kwargs):
            return patched_method(real_method, *args, **kwargs)

        call_patched_method._pythonagent_intercepted = True

        setattr(self.cls, method, call_patched_method)

    def attach(self, method_or_methods, wrapper_func=None, patched_method_name=None):
        if not isinstance(method_or_methods, list):
            method_or_methods = [method_or_methods]
        for method in method_or_methods:
            self._attach(method, wrapper_func, patched_method_name)

    def log_exception(self, level=1):
        self.agent.logger.exception('Exception in {klass}.{function}.'.format(klass=self.__class__.__name__, function=level))

    @contextmanager
    def log_exceptions(self):
        try:
            yield
        except:
            self.log_exception(level=3)


NO_WRAPPER = object()


class ExitCallInterceptor(BaseInterceptor):
    def attach(self, method_or_methods, wrapper_func=NO_WRAPPER, patched_method_name=None):
        if wrapper_func is NO_WRAPPER:
            wrapper_func = self.run
        super(ExitCallInterceptor, self).attach(method_or_methods, wrapper_func=wrapper_func,
                                                patched_method_name=patched_method_name)

    def make_correlation_header(self, exit_call):
        header = None
        if exit_call and header is not None:
            exit_call.optional_properties['CorrelationHeader'] = header[1]
        return header

    def http_call_begin(self, bt, http_host, url):
        """Start an exit call.
        """
        print("HTTP CALL BEGIN")
        current_time = get_current_timestamp_in_ms() 
        self.agent.get_transaction_context().tier_callout_start_time = current_time
        self.agent.get_transaction_context().tier_callout_type = "http"
        self.agent.get_transaction_context().backend_header = http_host
        method_name = "request" + "." + self.agent.get_transaction_context().http_request_type.lower()
        zero_bt = 0

        with self.log_exceptions():

            self.agent.method_entry_http_callout(zero_bt, method_name, http_host, url)  # METHOD ENTRY FOR PROXY
            return self.agent.http_call_begin(bt, http_host, url)

    def db_call_begin(self, bt, db_host, db_query):
        """Start an exit call.
        """
        with self.log_exceptions():
            return self.agent.db_call_begin(bt, db_host, db_query)

    def run(self, func, *args, **kwargs):
        """Run the function.  If it raises an exception, end the exit call started from func
           and raise the exception.

           The exit call that needs to be managed should be passed as key word argument pythonagent_exit_call.

        """
        exit_call = kwargs.pop('pythonagent_exit_call', None)
        with self.end_exit_call_and_reraise_on_exception(exit_call):
            return func(*args, **kwargs)

    def http_call_end(self, bt, exit_call, status=200):
        """End the exit call.
        """
        print("HTTP CALL END")
        current_time = get_current_timestamp_in_ms() 
        start_time = self.agent.get_transaction_context().tier_callout_start_time
        duration = current_time - start_time
        method_name = "request" + "." + self.agent.get_transaction_context().http_request_type.lower()
        zero_bt = 0

        try:
            from pythonagent.agent.probes.havoc.havoc_manager import NDNetHavocMonitor, NDHavocException
            havoc_monitor = NDNetHavocMonitor.get_instance()
            http_host = self.agent.get_transaction_context().backend_header
            havoc_monitor.apply_outbound_service_failure(http_host)

        except Exception as e:
            if isinstance(e, NDHavocException):
                self.agent.logger.info("Havoc Exception {}".format(e))
                zero_bt = 0
                backend_header = self.agent.get_transaction_context().backend_header
                status = 503
                self.agent.method_exit_http_callout(zero_bt, method_name, backend_header, status, duration)
                self.agent.set_current_status_code(503)
                raise e
            else:
                self.agent.logger.info("Non-Havoc Exception {}".format(e))

        with self.log_exceptions():
            if exit_call:
                print("Inside with self.log_exceptions(); if exit_call")
                backend_header = self.agent.get_transaction_context().backend_header
                self.agent.method_exit_http_callout(zero_bt, method_name, backend_header, status, duration)  # METHOD EXIT FOR PROXY
                self.agent.http_call_end(bt, exit_call)


    def db_call_end(self, bt, ip_handle):
        """End the exit call.
        """
        with self.log_exceptions():
            if bt:
                self.agent.db_call_end(bt, ip_handle)

    @contextmanager
    def end_exit_call_and_reraise_on_exception(self, exit_call, ignored_exceptions=()):
        try:
            yield
        except ignored_exceptions:
            raise
        except:
            self.agent.logger.exception("Exception raised in end exit call !!! {0}".format(sys.exc_info()))
            raise


class EntryPointInterceptor(BaseInterceptor):
    HTTP_ERROR_DISPLAY_NAME = 'HTTP {code}'

    def start_business_transaction(self, bt_name, correlation_header):
        with self.log_exceptions():
            return self.agent.start_business_transaction(bt_name, correlation_header)

    def end_business_transaction(self, bt):
        with self.log_exceptions():
            self.agent.end_business_transaction(bt)

    def handle_http_status_code(self, bt, status_code, msg):
        """Add the status code to the BT and deal with error codes.

        If the status code is in the error config and enabled, or the status
        code is >= 400, create an ErrorInfo object and add it to the BT.

        """
        self.agent.set_current_status_code(status_code)
        if status_code >= 400:
            self.agent.logger.info('Message is '.format(msg))
        else:
            return



