
from __future__ import unicode_literals
import contextlib
import sys
#import threading

#from lib import LazyWsgiRequest
#from appdynamics.agent.core.eum import inject_eum_metadata
#from appdynamics.agent.models.transactions import ENTRY_TORNADO
from ..base import EntryPointInterceptor
#from agent.internal.proxy import *
#import agent
#ENTRY_PYTHON_WEB = pb.PYTHON_WEB # need to ask ENTRY_PYTHON_WEB value
#ENTRY_TORNADO = ENTRY_PYTHON_WEB
try:
    import tornado.httputil
    import tornado.ioloop
   # import tornado.stack_context
   # import tornado.stack_context.StackContext
    import tornado.web
    import tornado.wsgi

    class TornadoFallbackHandlerInterceptor(EntryPointInterceptor):
        #proxy = Proxy.getInstance()
       # print("framework tornado_web: TornadoFallbackHandlerInterceptor function proxy instance inside  tornado_web.py : ", proxy)
       # print("framework tornado_web: TornadoFallbackHandlerInterceptor function proxy.lib inside class level variable inside tornado_web module : ", proxy.lib)
        # When using FallbackHandler, the RequestHandler's finish method is
        # never called.  Wrap the custom fallback callable to end the bt here.
        def _initialize(self, initialize, handler, fallback):
            self.agent.logger.info('Modulename: TornadoFallbackHandlerInterceptor class') 
            def _fallback(request):
                fallback(request)
                bt = self.bt
                self.agent.logger.debug("Modulename: TornadoFallbackHandlerInterceptor class || bt value is :{0}".format(bt))
                if bt:
                    #self.end_transaction(bt)
                    self.end_business_transaction(bt)
            initialize(handler, _fallback)

    class TornadoRequestHandlerInterceptor(EntryPointInterceptor):
        def __execute(self, _execute, handler, *args, **kwargs):
           # bt = self.proxy.start_business_transaction(ENTRY_TORNADO,
           #                             LazyWsgiRequest(tornado.wsgi.WSGIContainer.environ(handler.request)))
           # bt = self.start_business_transaction(handler.request,correlation_header=None)
            requests = handler.request
            bt = self.start_business_transaction(requests.path,'')
            #self.agent.logger.info("framework tornado_web: TornadoRequestHandlerInterceptor function print value of bt " .format(bt))
            self.agent.logger.debug("Modulename: TornadoRequestHandlerInterceptor class || bt value is :{0}".format(bt))

            #local_thread = threading.local()
            #local_thread.context = bt

            try:
                #print("framework tornado_web: TornadoRequestHandlerInterceptor  request in  ===>: ", handler.request)
                                                                                                                   
                #self.agent.logger.info("Modulename: TornadoRequestHandlerInterceptor class insinde __execute function request is :{0}".format(handler.request))
                # requests =handler.request
                #print("framework tornado_web: TornadoRequestHandlerInterceptor  request.PATH_INFO ===>: ", requests.path)
                #self.agent.logger.info("Modulename: TornadoRequestHandlerInterceptor class insinde __execute function request.PATH_INFO is :{0}".format(requests.path))
                #print("framework tornado_web: TornadoRequestHandlerInterceptor  request.QUERY_STRING ===>: ", requests.query_string)
                #self.agent.logger.info("Modulename: TornadoRequestHandlerInterceptor class insinde __execute function request.QUERY_STRING is :{0}".format(requests.query_string))
                # print("WSGI interceptor request.data ===>: ", request.data)
                #print("framework tornado_web: TornadoRequestHandlerInterceptor  request.host ===>: ", requests.host)
                self.agent.logger.info("Modulename: TornadoRequestHandlerInterceptor class insinde __execute function requests.host is :{0}".format(requests.host))
            except:
                pass

            if bt:
                @contextlib.contextmanager
                def current_bt_manager():
                    """Set and unset current_bt as tornado moves between execution contexts.

                    By wrapping the handler's execution with this we can ensure that whenever the
                    IOLoop is executing code for a particular BT, that BT is the 'current_bt'.
                    For more information see http://www.tornadoweb.org/en/stable/stack_context.html.

                    """
                    self.agent.set_current_bt(bt)
                    try:
                        yield
                    except:
                        # Currently can't figure out how to get here, so this code is untested.
                        #bt.add_exception(*sys.exc_info())
                        self.agent.logger.debug("Modulename: TornadoRequestHandlerInterceptor class || Exception is :{0}".format(*sys.exc_info()))
                        raise
                    finally:
                        self.agent.unset_current_bt()

               # with tornado.stack_context.StackContext(current_bt_manager):
                result = _execute(handler, *args, **kwargs)
            else:
                result = _execute(handler, *args, **kwargs)

            return result

        def _finish(self, finish, handler, *args, **kwargs):
            result = finish(handler, *args, **kwargs)
            bt = self.bt
            if bt:
                with self.log_exceptions():
                    self.handle_http_status_code(bt, handler._status_code, handler._reason)
                    #self.end_transaction(bt)
                    self.end_business_transaction(bt)
            return result

        def _flush(self, flush, handler, *args, **kwargs):
            with self.log_exceptions():
                if not handler._headers_written:
                    bt = self.bt
                    if bt:
                        headers = list(handler._headers.get_all())
                       # inject_eum_metadata(self.agent.eum_config, bt, headers)
                        handler._headers = tornado.httputil.HTTPHeaders(headers)
            return flush(handler, *args, **kwargs)

        def __handle_request_exception(self, _handle_request_exception, handler, e, *args, **kwargs):
            with self.log_exceptions():
                bt = self.bt
                if bt and not (hasattr(tornado.web, 'Finish') and isinstance(e, tornado.web.Finish)):
                    #bt.add_exception(*sys.exc_info())
                    self.agent.logger.debug("Modulename: TornadoRequestHandlerInterceptor class || Exception is :{0}".format(*sys.exc_info()))
            return _handle_request_exception(handler, e, *args, **kwargs)

    def intercept_tornado_web(agent, mod):
        #print("framework torando_web :  intercept_torando_web")
        TornadoRequestHandlerInterceptor(agent, mod.RequestHandler).attach(
            ['_execute', 'flush', '_handle_request_exception', 'finish'])
        TornadoFallbackHandlerInterceptor(agent, mod.FallbackHandler).attach('initialize')

except ImportError:
    def intercept_tornado_web(agent, mod):
        pass

