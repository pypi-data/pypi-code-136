from functools import wraps
from inspect import signature
import traceback
from typing import Awaitable, List as ListT
from fastapi import FastAPI, Request
from pydantic import BaseModel

from .http import MetroHTTP
from .models import Bot, ListUpdate

try:
    from fastapi.responses import ORJSONResponse as JSONResp
except:
    from fastapi.responses import JSONResponse as JSONResp

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
        async def claim(request: Request, bot: Bot):
            ...

        @metro.unclaim()
        async def unclaim(request: Request, bot: Bot):
            ...

        @metro.approve()
        async def approve(request: Request, bot: Bot):
            ...

        @metro.deny()
        async def deny(request: Request, bot: Bot):
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
        self.wrapped = {}
    
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

            json: ListT[dict] = ret[0]
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
    def _wrapper(self, *, url: str, name: str, func: Awaitable, tags: ListT[str]):
        if not self._app:
            raise ValueError("App must be passed in order to use this method")

        # Check the args of func
        func_sig = signature(func)

        if not func_sig.parameters.get("request"):
            raise ValueError("Function must take request")

        @wraps(func)
        async def metro_f(request: Request, bot: Bot, *args, **kwargs):
            try:
                if request.headers.get("Authorization") != self.http.secret_key:
                    return JSONResp({"detail": "Invalid secret key"}, status_code=401)

                return await func(request, bot, *args, **kwargs)
            except:
                return JSONResp({"detail": traceback.format_exc()}, status_code=500)

        self._app.post(url, tags=tags)(metro_f)

        self._urls[name] = f"{self.domain}{url}"

        self.wrapped[name] = metro_f

    def claim(self, *, tags: ListT[str] = DEFAULT_TAGS, url: str = "/metro/claim"):
        """Claim API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="claim", func=func, tags=tags)
        
        return wrapper

    def unclaim(self, *, tags: ListT[str] = DEFAULT_TAGS, url: str = "/metro/unclaim"):
        """Unclaim API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="unclaim", func=func, tags=tags)
        
        return wrapper

    def approve(self, *, tags: ListT[str] = DEFAULT_TAGS, url: str = "/metro/approve"):
        """Approve API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="approve", func=func, tags=tags)
        
        return wrapper

    def deny(self, *, tags: ListT[str] = DEFAULT_TAGS, url: str = "/metro/deny"):
        """Deny API Decorator"""

        def wrapper(func: Awaitable):
            self._wrapper(url=url, name="deny", func=func, tags=tags)
        
        return wrapper
    
