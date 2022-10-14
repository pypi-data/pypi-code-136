from __future__ import unicode_literals
import functools

from pythonagent.lang import get_args, urlparse
from . import HTTPConnectionInterceptor
#from agent.internal.proxy import *
#import agent

try:
    import tornado.httpclient
   # import tornado.stack_context

    class AsyncHTTPClientInterceptor(HTTPConnectionInterceptor):
        #print("going to get  instance of AsyncHTTPClientInterceptor(HttpConnection Interceptor)")
        #self.agent.logger.debug('Modulename: AsyncHTTPClientInterceptor class') 
        #proxy = Proxy.getInstance()
        #print("proxy handle = ", proxy)
        def http_call_begin(self,url):
            #bt = self.bt
            bt =self.bt
           # bt =140138019344400
            self.agent.logger.info("Modulename: AsyncHTTPClientInterceptor class inside http_call_begin function bt is :{0}".format(bt))

            self.agent.logger.info("http tornado_http client module bt value .....{0} ".format(bt))
            #bt = self.agent.get_current_bt
            if not bt:
                return None

            parsed_url = urlparse(url)
            self.agent.logger.info("Modulename: AsyncHTTPClientInterceptor class inside http_call_begin function parsed_url is :{0}".format(parsed_url))

            port = parsed_url.port or ('443' if parsed_url.scheme == 'https' else '80')
            self.agent.logger.info("Modulename: AsyncHTTPClientInterceptor class inside http_call_begin function port is :{0}".format(port))
            #print("http tornado_httpclient module :AsyncHTTPClientInterceptor host",type(parsed_url.hostname))
            self.agent.logger.info("Modulename: AsyncHTTPClientInterceptor class inside http_call_begin function parsed_url.hostname is :{0}".format(parsed_url.hostname))
            #print("http tornado_httpclient module :AsyncHTTPClientInterceptor url",type( parsed_url.path))
            self.agent.logger.info("Modulename: AsyncHTTPClientInterceptor class inside http_call_begin function parsed_url.path is :{0}".format(parsed_url.path))
            #print("http tornado_httpclient module :AsyncHTTPClientInterceptor type of bt", type(bt))
            #backend = self.get_backend(parsed_url.hostname, port, parsed_url.scheme, url)
            #if not backend:
             #   return None

           # return super(AsyncHTTPClientInterceptor, self).http_call_begin(bt, parsed_url.hostname,url)
            return super().http_call_begin(bt,parsed_url.hostname,parsed_url.path)
        def http_call_end(self, exit_call, future):
            #super(AsyncHTTPClientInterceptor, self).http_call_end(exit_call, exc_info=future.exc_info())
            super().http_call_end(exit_call,exc_info=future.exc_info())
        def _fetch(self, fetch,client,request, raise_error=True, **kwargs):
            self.agent.logger.info('Modulename: AsyncHTTPClientInterceptor class inside _fetch function')
            exit_call = None
            with self.log_exceptions():
                is_request_object = isinstance(request, tornado.httpclient.HTTPRequest)
                url = request.url if is_request_object else request
                self.agent.logger.info("http tornado_httpclient module : _fetch method  url value {0}".format(url))
               # parsed_url = urlparse(url)         
                exit_call = self.http_call_begin(url)
                self.agent.logger.info("Modulename: AsyncHTTPClientInterceptor class inside _fetch function exit_call is :{0}".format(exit_call))

                self.agent.logger.info("http tornado_httpclient module : exit_call value ..........{0}".format(exit_call))
                if exit_call:
                    #self.agent.logger.info("http tornado_httpclient module : _fetch method  exit_call value", exit_call)
                    correlation_header = self.make_correlation_header(exit_call)
                    #print("http tornado_httpclient module : _fetch method  correlation_header value", correlation_header)
                    self.agent.logger.info("Modulename: AsyncHTTPClientInterceptor class inside _fetch function correlation_header is :{0}".format(correlation_header))
                    if correlation_header:
                        headers = request.headers if is_request_object else kwargs.setdefault('headers', {})
                        headers[correlation_header[0]] = correlation_header[1]
                        self.agent.logger.info("http tornado_httpclient module : _fetch method  headers[correlation_header[0]]".format(headers[correlation_header[0]]))

            # The `raise_error` kwarg was added in tornado 4.1.  Passing it by name on versions
            # prior to this cause it to be included in the `**kwargs` parameter to `fetch`.  This
            # dict is passed directly to the `HTTPRequest` constructor, which does not have
            # `raise_error` in its signature and thus raises a TypeError.
            if 'raise_error' in get_args(fetch):
                self.agent.logger.info("raise error.........".format(get_args(fetch)))
                future = fetch(client, request, raise_error=raise_error, **kwargs)
                #print(".............>",future)
                self.agent.logger.info('Modulename: AsyncHTTPClientInterceptor class inside _fetch function future is :'.format(future))
            else:
                future = fetch(client, request, **kwargs)
                #print("else future.......",future)
           # future._callbacks.insert(0, functools.partial(tornado.stack_context.wrap(self.http_call_end), exit_call))
            future._callbacks.insert(0, functools.partial(self.http_call_end, exit_call))
            return future

    def intercept_tornado_httpclient(agent, mod):
        # these methods don't normally return anything, but to be able to test that
        # the 'empty' interceptor defined below works properly, return a value here.
        #print("http torando_httpclient module : intercept_tornado_httpclient")
        return AsyncHTTPClientInterceptor(agent, mod.AsyncHTTPClient).attach('fetch', wrapper_func=None)
except ImportError:
    def intercept_tornado_httpclient(agent, mod):
        pass

