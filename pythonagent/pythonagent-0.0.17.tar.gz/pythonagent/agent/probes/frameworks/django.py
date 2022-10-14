"""Interceptor for Django.

"""


from __future__ import unicode_literals
import sys

from pythonagent.agent.probes.frameworks.wsgi import WSGIInterceptor
from pythonagent.agent.probes.base import BaseInterceptor
import logging
#from django.conf import settings



def add_exception(interceptor, exc_info):
    with interceptor.log_exceptions():
        bt = interceptor.bt
        if bt:
            bt.add_exception(*exc_info)

#from django.utils.deprecation import MiddlewareMixin






class DjangoBaseHandlerInterceptor(BaseInterceptor):
    def _load_middleware(self, load_middleware, base_handler):
        self.agent.logger.info("Loading middleware of django !")
        self.agent.logger.info('Modulename: DjangoBaseHandlerInterceptor class inside _load_middleware function : loading middleware of django !')
        #settings.MIDDLEWARE.append('agent.my_middleware.CustomMiddleware')
        load_middleware(base_handler)

        base_handler._exception_middleware.insert(0, pythonagentDjangoMiddleware(self).process_exception)
        #base_handler._request_middleware.insert(0, pythonagentDjangoMiddleware(self).process_request)
        #base_handler._response_middleware.insert(0, pythonagentDjangoMiddleware(self).process_response)
        #base_handler._template_response_middleware.insert(0, pythonagentDjangoMiddleware(self).process_template_response)
        #base_handler._view_middleware.insert(0, pythonagentDjangoMiddleware(self).process_view)



    def _handle_uncaught_exception(self, handle_uncaught_exception, base_handler, request, resolver, exc_info):
        add_exception(self, exc_info)
        return handle_uncaught_exception(base_handler, request, resolver, exc_info)


class DjangoExceptionInterceptor(BaseInterceptor):
    def _handle_uncaught_exception(self, handle_uncaught_exception, request, resolver, exc_info):
        add_exception(self, exc_info)
        return handle_uncaught_exception(request, resolver, exc_info)




class pythonagentDjangoMiddleware(object):
    def __init__(self, interceptor):
        self.interceptor = interceptor
        self.logger = logging.getLogger('pythonagent.agent')

    def process_exception(self, request, exception):
        add_exception(self.interceptor, sys.exc_info())
        #print("Django application process_request called and request as= ", request)


def intercept_django_wsgi_handler(agent, mod):
    WSGIInterceptor(agent, mod.WSGIHandler).attach('__call__')



def intercept_django_base_handler(agent, mod):
    base_handler_methods = ['load_middleware']

    try:
        import django.core.handlers.exception
        if hasattr(django.core.handlers.exception, 'handle_uncaught_exception'):
            DjangoExceptionInterceptor(agent, django.core.handlers.exception).attach('handle_uncaught_exception')
        else:
            base_handler_methods.append('handle_uncaught_exception')
    except ImportError:
        base_handler_methods.append('handle_uncaught_exception')

    DjangoBaseHandlerInterceptor(agent, mod.BaseHandler).attach(base_handler_methods)
