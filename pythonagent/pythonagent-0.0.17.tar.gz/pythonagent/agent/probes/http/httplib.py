

"""Interceptor for httplib/http.client.

"""

from __future__ import unicode_literals
#from agent.internal.proxy import *
from . import HTTPConnectionInterceptor
#import agent


class HttplibConnectionInterceptor(HTTPConnectionInterceptor):
    

    def _putrequest(self, putrequest, connection, method, url, *args, **kwargs):
        #print("INSIDE PUT REQUEST")
        self.agent.get_transaction_context().http_request_type = method  # GET, PUT, POST or DELETE
        exit_call = None
        #self.agent.logger.info('Modulename: HttplibConnectionInterceptor class ')
        #self.agent.logger.info("url value is {0}".format(url))
        with self.log_exceptions():
            bt = self.bt

            #self.agent.logger.info("Modulename: HttplibConnectionInterceptor class inside _putrequest bt value is :{0}".format(bt))
            #self.agent.logger.info("Modulename: HttplibConnectionInterceptor class inside _putrequest method  is :{0}".format(method))
            #self.agent.logger.info("Modulename: HttplibConnectionInterceptor class inside _putrequest connection is :{0}".format(connection))
            #self.agent.logger.info("Modulename: HttplibConnectionInterceptor class inside _putrequest putrequest is :{0}".format(putrequest))
            host_port = str(connection.host) + "$" + str(connection.port)
            exit_call = self.http_call_begin(bt, host_port, url)
            #self.agent.logger.info("Modulename: HttplibConnectionInterceptor class inside _putrequest exit_call is :{0}".format(exit_call))

            if bt:
                scheme = 'https' if self._request_is_https(connection) else 'http'
                connection._pythonagent_exit_call = exit_call
                #backend = self.get_backend(connection.host, connection.port, scheme, url)
                #if backend:
                    #exit_call = self.start_exit_call(bt, backend, operation=url)
                    #connection._pythonagent_exit_call = exit_call
        return putrequest(connection, method, url, pythonagent_exit_call=exit_call, *args, **kwargs)

    def _endheaders(self, endheaders, connection, *args, **kwargs):
        #print("INSIDE END HEADERS")

        #self.agent.logger.info('Modulename: HttplibConnectionInterceptor class inside _endheaders ')

        exit_call = getattr(connection, '_pythonagent_exit_call', None)
        #self.agent.logger.info("Modulename: HttplibConnectionInterceptor class inside _endheaders exit_call is :{0}".format(exit_call))

        with self.log_exceptions():
            header = self.make_correlation_header(exit_call)
            if header is not None:
                connection.putheader(*header)
                #self.agent.logger.debug('Added correlation header to HTTP request: %s, %s' % header)
        return endheaders(connection, pythonagent_exit_call=exit_call, *args, **kwargs)

    def _getresponse(self, getresponse, connection, *args, **kwargs):
        #print("INSIDE GET RESPONSE")
        # CORE-40945 Catch TypeError as a special case for Python 2.6 and call getresponse with just the
        # HTTPConnection instance.
        #self.agent.logger.info('Modulename: HttplibConnectionInterceptor class inside _getresponse')

        exit_call = getattr(connection, '_pythonagent_exit_call', None)
        #self.agent.logger.info("Modulename: HttplibConnectionInterceptor class inside _getresponse exit_call is :{0}".format(exit_call))

        #self.agent.logger.info("exit_call value after getattr,".format(exit_call))
        bt = self.bt
        try:
            #print("inside try")
            with self.end_exit_call_and_reraise_on_exception(exit_call,
                                                             ignored_exceptions=(TypeError,)):
                #self.agent.logger.debug("inside with")
                self.agent.method_entry(bt, "getresponse")
                response = getresponse(connection, *args, **kwargs)
                self.agent.method_exit(bt, "getresponse")
                #print("RESPONSE STATUS CODE: ", response.status)
        except TypeError:
            #print("inside except")
            with self.end_exit_call_and_reraise_on_exception(exit_call):
                #self.agent.logger.debug("inside with")
                response = getresponse(connection)
                #print("RESPONSE STATUS CODE: ", response.status)

        self.http_call_end(self.bt, exit_call, response.status)
        #self.proxy.http_call_end(self.agent.bt,exit_call)
        try:
            del connection._pythonagent_exit_call
        except AttributeError:
            pass
        return response


def intercept_httplib(agent, mod):
    #print("intercept_httplib")
    HTTPConnectionInterceptor.https_connection_classes.add(mod.HTTPSConnection)
    interceptor = HttplibConnectionInterceptor(agent, mod.HTTPConnection)
    interceptor.attach(['putrequest', 'endheaders'])
    interceptor.attach('getresponse', wrapper_func=None)   # CORE-40945 Do not wrap getresponse in the default wrapper.
