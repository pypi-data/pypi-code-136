#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys
import logging
import tornado.web
from lcyframe.libs import utils

class route(object):
    _uris = []
    _names = []
    _handlers = []
    _routes = []

    def __init__(self, uri, name=None):
        self.uri = uri
        self.name = name

    def __call__(self, _handler):
        """gets called when we class decorate"""
        self.name = self.name and self.name or _handler.__name__
        if self.uri in self._uris:
            logging.error("Multiple uri: %s in %s; replacing previous value" % (self.uri, _handler))
            sys.exit(0)
        if _handler.__name__ in self._handlers:
            logging.error("Multiple handlers named: %s; replacing previous value" % _handler)
            sys.exit(0)
        if self.name in self._names:
            logging.error("Multiple api named: %s in %s; replacing previous value" % (self.name, _handler))
            sys.exit(0)

        self._uris.append(self.uri)
        self._names.append(self.name)
        self._handlers.append(_handler.__name__)
        self._routes.append(tornado.web.url(self.uri, _handler, name=self.name))
        return _handler

    @classmethod
    def get_routes(cls, ROOT, handler_dir):
        if not isinstance(handler_dir, list):
            handler_dir = [handler_dir]

        for work in handler_dir:
            for root, dirs, files in os.walk(utils.fix_path(os.path.join(ROOT, work))):
                for file in files:
                    if file.startswith("__"):
                        continue
                    if file.endswith(".pyc"):
                        continue
                    if not file.endswith(".py"):
                        continue
                    model_name = root.replace(ROOT, "").lstrip("/").replace("/", ".") + "." + file.rstrip(".py")
                    __import__(model_name, globals(), locals(), [model_name], 0)
                    logging.debug("handler [%s] register success!" % model_name)
        return cls._routes

def route_redirect(from_, to, name=None):
    route._routes.append(tornado.web.url(from_, tornado.web.RedirectHandler, dict(url=to), name=name))



