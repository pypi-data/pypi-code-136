"""Interceptor for Cherry framework.

"""
from __future__ import unicode_literals
import sys

from pythonagent.agent.probes.frameworks.wsgi import WSGIInterceptor
from pythonagent.agent.probes.base import BaseInterceptor

class CherrypyExceptionAdder(BaseInterceptor):
    def add_exception(self, func, *args, **kwargs):
        with self.log_exceptions():
            bt = self.bt
            self.agent.logger.info("Modulename: cherry exception  class || bt  value is {0} :".format(bt))
            if bt:
                bt.add_exception(*sys.exc_info())
                self.agent.logger.debug("Exception occured as  !!! {0}".format(sys.exc_info()))
        return func(*args, **kwargs)


def intercept_cherrypy(agent, mod):
    WSGIInterceptor(agent, mod.Application).attach('__call__')
    CherrypyExceptionAdder(agent, mod._cprequest.Request).attach('handle_error', patched_method_name='add_exception')
    CherrypyExceptionAdder(agent, mod.HTTPError).attach('set_response', patched_method_name='add_exception')
