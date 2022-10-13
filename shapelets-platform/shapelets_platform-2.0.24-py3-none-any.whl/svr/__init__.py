# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from requests import Session
from requests.auth import AuthBase
from rodi import Container, Services
from typing import Optional
from urllib.parse import urljoin

from . import app
from . import authn
from . import dataapps
from . import db
from . import execution
from . import groups
from . import mustang
from . import settings
from . import users

from .authn import *
from .dataapps import *
from .execution import *
from .groups import *
from .server import InProcServer, launch_in_process, run_dedicated
from .settings import *
from .users import *


class BearerAuth(AuthBase):
    def __init__(self, token):
        self.token = f"Bearer {token}"

    def __call__(self, r):
        r.headers["Authorization"] = self.token
        return r


class PrefixedSession(Session):
    def __init__(self, prefix_url: str, *args, **kwargs):
        self.prefix_url = prefix_url
        super(PrefixedSession, self).__init__(*args, **kwargs)

    def set_authorization(self, token: str):
        self.auth = BearerAuth(token)

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(PrefixedSession, self).request(method, url, verify=False, *args, **kwargs)


def setup_http_server(cfg: Settings, blocking: bool) -> Optional[InProcServer]:
    """
    Creates an HTTP server capable of hosting the UI and the APIs
    
    Parameters
    ----------
    cfg: Settings
        Configuration settings 
    
    blocking: bool
        Should the server block the main thread or run on the background
    
    Returns
    -------
    When the server is run in blocking mode, this code never returns.  However,
    when the server is not run in blocking mode, an instance of `InProcServer`
    is returned to stop gracefully the background instance.
    """
    # create the database
    db.setup_database(cfg.database)
    # create the application
    application = app.setup_app(cfg)
    # add settings to D.I. container
    application.services.add_instance(cfg, Settings)
    # full services for authn
    authn.setup_services(application.services)
    # users services
    users.setup_services(application.services)
    # groups services
    groups.setup_services(application.services)
    # dataapps services
    dataapps.setup_services(application.services)
    # execution services
    execution.setup_services(application.services)
    # run in process, non main thread blocking
    if blocking:
        run_dedicated(application, cfg)

    # return a instance of InProcServer
    return launch_in_process(application, cfg)


def setup_remote_client(cfg: Settings) -> Services:
    """
    Creates a stack of services required to connect to an
    HTTP API front end.
    """
    container = Container()
    container.add_instance(cfg, Settings)
    container.add_instance(PrefixedSession(cfg.client.server_url), Session)
    authn.setup_remote_client(container)
    users.setup_remote_client(container)
    groups.setup_remote_client(container)
    dataapps.setup_remote_client(container)
    execution.setup_remote_client(container)
    return container.build_provider()


def setup_headless(cfg: Settings) -> Services:
    """
    Creates a headless environment, where the services are running 
    fully in process, without going through an HTTP comms stack.
    """
    db.setup_database(cfg.database)
    container = Container()
    container.add_instance(cfg, Settings)
    authn.setup_services(container)
    users.setup_services(container)
    groups.setup_services(container)
    return container.build_provider()


__all__ = ['setup_http_server', 'setup_remote_client', 'setup_headless']
__all__ += ['InProcServer']
__all__ += ['mustang']
__all__ += settings.__all__
__all__ += authn.__all__
