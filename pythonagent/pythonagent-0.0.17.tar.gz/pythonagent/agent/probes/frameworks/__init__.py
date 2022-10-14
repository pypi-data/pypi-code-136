
"""Entry-point interceptors for various web/application frameworks.

"""

from __future__ import unicode_literals

from .django import intercept_django_wsgi_handler, intercept_django_base_handler
from .flask import intercept_flask
from .bottle import intercept_bottle
from .tornado_web import intercept_tornado_web
from .cherry import intercept_cherrypy
from .pyramid import intercept_pyramid
from .falcon import intercept_falcon
#__all__ = [
#    'intercept_flask',
#    'intercept_django_wsgi_handler',
#    'intercept_django_base_handler',
#    'intercept_bottle',
#    'intercept_tornado_web',
#]
