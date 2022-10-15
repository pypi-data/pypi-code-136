from typing import List, Type
from urllib import request
import json

from starlette.responses import JSONResponse
from starlette.routing import Route

from arc.serve.server import Client, Server


class Foo(Server):
    """A Foo"""

    pass


class Bar(Server):
    """A Bar"""

    @classmethod
    def client_cls(cls) -> Type[Client]:
        """Class of the client for the server

        Returns:
            Type[Client]: A client class for the server
        """
        return BarClient

    @classmethod
    def routes(cls) -> List[Route]:
        """Routes to add to the server

        Returns:
            List[Route]: List of routes to add to the server
        """
        return [
            Route("/echo", endpoint=cls._echo_req),
        ]

    def _echo_req(self, request):
        return JSONResponse({"message": self.echo()})

    def echo(self, txt: str) -> str:
        """Echo a string back

        Args:
            txt (str): String to echo

        Returns:
            str: String echoed with a hello
        """
        return txt + " -- hello!"


class BarClient(Client):
    """A Bar client"""

    def echo(self, txt: str) -> str:
        """Echo the message

        Args:
            txt (str): Message to echo

        Returns:
            str: Echoed message with a hello
        """
        req = request.Request(f"{self.server_addr}/echo")
        resp = request.urlopen(req)
        data = resp.read().decode("utf-8")
        dict = json.loads(data)
        return dict["message"]


if __name__ == "__main__":
    foo = Foo()

    client = foo.develop()

    print(client.info())
