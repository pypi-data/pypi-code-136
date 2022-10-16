from typing import Awaitable, Callable, List, Optional

from dependency_injector.containers import Container
from fastapi import FastAPI, Request, Response
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

from dropland.app.application import Application


class FastAPIApplication(Application):
    def __init__(self, container: Container, name: str, debug: bool, version: str,
                 title: str, api_root: str, cors: Optional[List[str]] = None):
        super().__init__(container, name, debug, version)

        self._server = self._create_server(title, debug, self.version, api_root, cors)
        self._server.state.application = self

    @property
    def server(self):
        return self._server

    def _create_server(self, title: str, debug: bool, version: str,
                       api_root: str, cors: Optional[List[str]] = None):
        from fastapi.responses import UJSONResponse
        from starlette.authentication import AuthenticationBackend, AuthCredentials, UnauthenticatedUser
        from starlette.middleware.authentication import AuthenticationMiddleware
        from fastapi.middleware.cors import CORSMiddleware

        class AuthBackend(AuthenticationBackend):
            async def authenticate(self, request):
                return AuthCredentials(), UnauthenticatedUser()

        middlewares = [
            Middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in cors] if cors else ['*'],
                allow_credentials=True, allow_methods=['*'], allow_headers=['*'],
            ),
            Middleware(AuthenticationMiddleware, backend=AuthBackend()),
        ]

        server = FastAPI(
            title=title, version=version, debug=debug,
            default_response_class=UJSONResponse, root_path=api_root,
            on_startup=[self.startup, self.sync_startup],
            on_shutdown=[self.shutdown, self.sync_shutdown],
            middleware=middlewares
        )

        server.add_middleware(BaseHTTPMiddleware, dispatch=self._server_entrypoint)

        return server

    async def _server_entrypoint(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]):
        async with self.with_app_sessions():
            return await call_next(request)
