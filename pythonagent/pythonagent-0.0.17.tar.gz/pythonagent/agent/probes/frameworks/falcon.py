
from __future__ import unicode_literals
import sys

from pythonagent.agent.probes.frameworks.wsgi import WSGIInterceptor
from pythonagent.agent.probes.base import BaseInterceptor

class FalconExceptionAdder(BaseInterceptor):
    def add_exception(self, func, *args, **kwargs):
        with self.log_exceptions():
            bt = self.bt
            if bt:
                bt.add_exception(*sys.exc_info())
        return func(*args, **kwargs)


def intercept_falcon(agent, mod):
    WSGIInterceptor(agent, mod.App).attach('__call__')
    FalconExceptionAdder(agent, mod.App).attach('_handle_exception', patched_method_name='add_exception')
    #FalconExceptionAdder(agent, mod.Request).attach('set_response', patched_method_name='add_exception')
