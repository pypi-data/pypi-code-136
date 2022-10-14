"""Interceptor for Pyramid.

"""


from __future__ import unicode_literals
import sys

from pythonagent.agent.probes.frameworks.wsgi import WSGIInterceptor
from pythonagent.agent.probes.base import BaseInterceptor

class PyramidRouterInterceptor(BaseInterceptor):
    """
    Pyramid's interceptor class
    """
    def _handle_request(self, handle_request, router_instance, req):
        """

        Parameters
        ----------
        handle_request: original method pyramid.router.Router.handle_request
                        that is being overridden
        router_instance: pyramid.router.Router instance
        req: request object

        Returns
        -------
        Whatever pyramid.router.Router.handle_request returns

        """
        try:
            return handle_request(router_instance, req)
        except Exception:
            with self.log_exceptions():
                bt = self.bt
                if bt:
                    bt.add_exception(*sys.exc_info())
            raise


def intercept_pyramid(agent, mod):
    """

    Parameters
    ----------
    
    mod: pyramid.router module

    Returns
    -------
    None
    """
    #mod = '/home/cavisson/shop/my-shop/env/env/lib/python3.7/site-packages/pyramid/router.py'
    WSGIInterceptor(agent, mod.Router).attach('__call__')
    PyramidRouterInterceptor(agent, mod.Router).attach('handle_request') 
