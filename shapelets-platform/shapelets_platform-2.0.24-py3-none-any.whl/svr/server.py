from typing import TYPE_CHECKING, Callable, Optional, Union
import functools
import asyncio
import threading

from .settings import Settings, update_uvicorn_settings
from uvicorn import Config as UviConfig, Server as UviServer

if TYPE_CHECKING:
    from asgiref.typing import ASGIApplication

try:
    # ensure we are running with uvloop if possible
    import uvloop
    # by registering it as the engine behind asyncio
    uvloop.install()
except ModuleNotFoundError:
    # TODO: Log this message, rather than print it.
    print("Running without `uvloop`")

class InProcServer:
    """
    Class handling a in-process ASGI web server based on uvicorn
    
    Notes
    -----
    The server runs on a separated thread, on its own event loop.
    """
    __slots__ = ['__daemon', '__server', '__loop']

    def __init__(self) -> None:
        self.__daemon = None 
        self.__server = None 
        self.__loop = None

    def __run(self, config: UviConfig):
        self.__server = UviServer(config)
        self.__loop = asyncio.new_event_loop()
        try:
            asyncio.set_event_loop(self.__loop)
            return self.__loop.run_until_complete(self.__server.serve())
        finally:
            self.__loop.close()   
            self.__loop = None 
            self.__server = None 

    @staticmethod
    def __stop(server:UviServer):
        server.should_exit = True

    def start(self, config: UviConfig):
        """
        Starts a new server 
        
        Parameters
        ----------
        config: uvicorn configuration object
            Configuration settings
        """
        if config is None:
            raise ValueError("Configuration is required.")

        if self.__daemon is not None:
            raise RuntimeError("Daemon thread already exists.")

        self.__daemon = threading.Thread(target=self.__run, daemon=True, name="api-thread", args=(config,))    
        self.__daemon.start()    

    def join(self, timeout: Optional[float] = None):
        """
        Asks the server to stop and waits until termination
        
        Parameters
        ----------
        timeout: float, optional, defaults to None
            Time in seconds to wait for the background thread 
            to terminate.  When set to None, it waits 
            forever until termination.
            
        """
        loop = self.__loop 
        if loop is None:
            raise RuntimeError("No event loop")

        server = self.__server 
        if server is None:
            raise RuntimeError("No server")

        callback = functools.partial(InProcServer.__stop, server)
        handle = loop.call_soon_threadsafe(callback)

        self.__daemon.join(timeout)
        if self.__daemon.is_alive():
            handle.cancel()
            raise RuntimeError("Unable to stop event loop thread in a timely manner.")

        self.__daemon = None


def launch_in_process(app: Union["ASGIApplication", Callable, str], cfg: Settings) -> InProcServer:
    """
    Starts an in-process server
    """
    in_proc = InProcServer()
    in_proc.start(update_uvicorn_settings(cfg.server, UviConfig(app)))
    return in_proc

def run_dedicated(app: Union["ASGIApplication", Callable, str], cfg: Settings):
    """
    Runs a Uvicorn server in a dedicated manner, blocking the process.
    """
    server = UviServer(update_uvicorn_settings(cfg.server, UviConfig(app)))
    server.run()
    
__all__ = ['launch_in_process', 'stop_in_process', 'run_dedicated']