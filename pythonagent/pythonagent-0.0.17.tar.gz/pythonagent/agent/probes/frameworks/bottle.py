"""Interceptor for Bottle.

"""

import sys

from pythonagent.agent.probes.frameworks.wsgi import WSGIInterceptor
from pythonagent.agent.probes.base import BaseInterceptor


class BottleInterceptor(BaseInterceptor):
    def add_exception(self, func, *args, **kwargs):
        self.agent.logger.info('Modulename: BottleInterceptor class')
        with self.log_exceptions():
            bt = self.bt
            self.agent.logger.info("Modulename: BottleInterceptor class inside add_exception function bt value is :{0}".format(bt))
            if bt:
                bt.add_exception(*sys.exc_info())
        return func(*args, **kwargs)



def intercept_bottle(agent, mod):
    WSGIInterceptor(agent, mod.Bottle).attach('__call__')
    #print("framework.bottle.intercept_bottle: intercepting bottle ......")
    BottleInterceptor(agent, mod.HTTPError).attach('__init__', patched_method_name='add_exception')
