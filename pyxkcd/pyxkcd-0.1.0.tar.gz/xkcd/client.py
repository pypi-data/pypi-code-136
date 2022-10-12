from .comic import Comic
from .errors import InvalidComicError

import asyncio
import weakref
import random
import json

import httpx


class Client:
    """
    Represents a client that can be used to interact with the xkcd API.
    This class is used to interact with the xkcd API.

    Attributes
    ----------
    session: httpx.Client
        The session used to make requests to the xkcd API.
    current: int
        The current comic number.
    """

    def __init__(self):
        self.session = httpx.Client()
        self.current = self.latest().num

        weakref.finalize(self, self.session.close)

    def get(self, comic: int) -> Comic:
        """
        Gets a comic from the xkcd API.

        Parameters
        ----------
        comic: int
            The comic number to get.

        Returns
        -------
        Comic
        """
        raw_data = self.session.get(f"https://xkcd.com/{comic}/info.0.json")
        try:
            return Comic(raw_data.json())
        except json.decoder.JSONDecodeError:
            raise InvalidComicError("Invalid comic number.")

    def latest(self) -> Comic:
        """
        Gets the latest comic from the xkcd API.

        Returns
        -------
        Comic
        """
        raw_data = self.session.get("https://xkcd.com/info.0.json")
        return Comic(raw_data.json())

    def random(self) -> Comic:
        """
        Gets a random comic from the xkcd API.
        
        Returns
        -------
        Comic
        """
        return self.get(random.randint(1, self.current))


class AsyncClient:
    """
    An asynchronous version of the Client class.
    
    Attributes
    ----------
    session: httpx.AsyncClient
        The session used to make requests to the xkcd API.
    current: int
        The current comic number.
    """

    def __init__(self):
        self.session = httpx.AsyncClient()
        self.current = asyncio.run(self.latest()).num

        weakref.finalize(self, self.close)

    async def get(self, comic: int) -> Comic:
        """
        Gets a comic from the xkcd API.

        Parameters
        ----------
        comic: int
            The comic number to get.

        Returns
        -------
        Comic
        """
        raw_data = await self.session.get(f"https://xkcd.com/{comic}/info.0.json")
        try:
            return Comic(raw_data.json())
        except json.decoder.JSONDecodeError:
            raise InvalidComicError("Invalid comic number.")

    async def latest(self) -> Comic:
        """
        Gets the latest comic from the xkcd API.

        Returns
        -------
        Comic
        """
        raw_data = await self.session.get("https://xkcd.com/info.0.json")
        return Comic(raw_data.json())

    async def random(self) -> Comic:
        """
        Gets a random comic from the xkcd API.
        
        Returns
        -------
        Comic
        """
        return await self.get(random.randint(1, self.current))

    def close(self):
        """
        Closes the http session. Can be called manually, but is also called when the object is garbage collected.
        """
        asyncio.run(self.session.aclose())
