from functools import wraps
from typing import Awaitable
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

from .http import MetroHTTP
from .models import Bot, ListUpdate

DEFAULT_TAGS = ["Metro (Integrase)"]
"""Default tags for the integrase routes"""

class Metro():
    """
    This is the actual main client you should initialize and then use

    To use the server bit, you should do something like this:

    .. code-block:: python

        from metro_integrase import Metro
        from fastapi import FastAPI, Request

        app = FastAPI()
        metro = Metro(...)

        @metro.claim()
        async def claim(bot: Bot):
            ...

        @metro.unclaim()
        async def unclaim(bot: Bot):
            ...

        @metro.approve()
        async def approve(bot: Bot):
            ...

        @metro.deny()
        async def deny(bot: Bot):
            ...

        @app.on_event("startup")
        async def startup():
            await metro.register_api_urls()

    If you wish to use a HTTP method, use ``self.http`` or manually initialize ``MetroHTTP`` with the list ID and secret key.
    """

    def __init__(self, *, domain: str, list_id: str, secret_key: str, app: FastAPI = None):
        self.http = MetroHTTP(list_id=list_id, secret_key=secret_key)
        self.domain = domain
        self._urls = {}
        self._app = app
    
    async def paginate(self, func: Awaitable, *, limit: int = 50):
        """
        Simple helper that can be combined with a ``self.http`` paginated function to paginate a function

        Example:

        .. code-block:: python

            async for act in metro.paginate(metro.http.get_actions):
                print(act)
        """
        offset = 0
        while True:
            ret = await func(offset=offset, limit=limit)

            json: list[dict] = ret[0]
            model: BaseModel = ret[1]

            if not json:
                break
            for item in json:
                yield model(**item)
            offset += limit

    async def register_api_urls(self):
        """Register all decorated API endpoints with Metro Reviews using ``MetroHTTP.update_list``"""
        res, json = await self.http.update_list(
            ListUpdate(
                domain=self.domain,
                claim_bot_api=self._urls.get("claim"),
                unclaim_bot_api=self._urls.get("unclaim"),
                approve_bot_api=self._urls.get("approve"),
                deny_bot_api=self._urls.get("deny")
            )
        )

        if not res.ok:
            try:
                if json["detail"][0]["loc"][1] == "list_id":
                    raise ValueError("Invalid list ID")
            except (KeyError, IndexError):
                ...

            raise RuntimeError(f"Metro setup failed: {res.status}. Ensure proper list ID and secret key...")
    
    # HTTP Server Code
    def _wrapper(self, *, url: str, name: str, func: Awaitable, tags: list[str]):
        if not self._app:
            raise ValueError("App must be passed in order to use this method")

        @wraps(func)
        async def metro_f(request: Request, response: Response, bot: Bot, *args, **kwargs):
            if request.headers.get("Authorization") != self.http.secret_key:
                response.status_code = 401
                return {"detail": "Invalid secret key"}

            return await func(bot, *args, **kwargs)

        self._app.post(url, tags=tags)(metro_f)

        self._urls[name] = url

    def claim(self, *, tags: list[str] = DEFAULT_TAGS, url: str = "/metro/claim"):
        """Claim API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="claim", func=func, tags=tags)
        
        return wrapper

    def unclaim(self, *, tags: list[str] = DEFAULT_TAGS, url: str = "/metro/unclaim"):
        """Unclaim API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="unclaim", func=func, tags=tags)
        
        return wrapper

    def approve(self, *, tags: list[str] = DEFAULT_TAGS, url: str = "/metro/approve"):
        """Approve API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="approve", func=func, tags=tags)
        
        return wrapper

    def deny(self, *, tags: list[str] = DEFAULT_TAGS, url: str = "/metro/deny"):
        """Deny API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="deny", func=func, tags=tags)
        
        return wrapper
    
