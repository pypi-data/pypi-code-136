
"""Interceptor for Flask framework.

"""

from __future__ import unicode_literals
import sys

from pythonagent.agent.probes.frameworks.wsgi import WSGIInterceptor
from pythonagent.agent.probes.base import BaseInterceptor


class FlaskInterceptor(BaseInterceptor):
    def _handle_user_exception(self, handle_user_exception, flask, e):
        self.agent.logger.info('Modulename: FlaskInterceptor  class')
        with self.log_exceptions():
            bt = self.bt
            self.agent.logger.info("Modulename: FlaskInterceptor  class || bt  value is {0} :".format(bt))
            if bt:
                #bt.add_exception(*sys.exc_info())
                self.agent.logger.debug("Exception occured as  !!! {0}".format(sys.exc_info()))
        #print('returning from _handle method !!')
        return handle_user_exception(flask, e)


def intercept_flask(agent, mod):
    #print('=============inside flask instrumentation==========')
    WSGIInterceptor(agent, mod.Flask).attach('wsgi_app')
    FlaskInterceptor(agent, mod.Flask).attach('handle_user_exception')
