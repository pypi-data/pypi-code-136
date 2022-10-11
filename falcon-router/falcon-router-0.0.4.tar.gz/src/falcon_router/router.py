import importlib
from enum import Enum
from types import ModuleType
from typing import List, Optional, Tuple, Union

from falcon import App as WApp
from falcon.asgi import App as AApp


class AppType(str, Enum):
    ASGI: str = "asgi"
    WSGI: str = "wsgi"


class FalconRouter:
    def __init__(
        self,
        app_type: str = AppType.ASGI,
        route_groups: Union[List[str], str, None] = None,
        add_trailing_slash: bool = False,
        **kwargs,
    ) -> None:
        self.app: Union[WApp, AApp] = self._create_app(app_type, **kwargs)
        self.app.req_options.strip_url_path_trailing_slash = add_trailing_slash
        self._route_groups: Union[List[str], str, None] = route_groups
        self._add_routes()

    @staticmethod
    def _create_app(app_type: str, **kwargs) -> Union[WApp, AApp]:
        app_type = app_type.lower()
        if app_type not in [AppType.ASGI, AppType.WSGI]:
            raise ValueError("Invalid application type specified!")
        return WApp(**kwargs) if app_type == AppType.WSGI else AApp(**kwargs)

    def _add_routes(self) -> None:
        if not self._route_groups:
            return
        if isinstance(self._route_groups, str):
            self._route_groups = [self._route_groups]
        for route_group in self._route_groups:
            route_module: ModuleType = importlib.import_module(route_group)
            routes: Optional[List[Tuple]] = getattr(route_module, "routes", [])
            if not routes:
                continue
            for route, handler in routes:
                self.app.add_route(f"/{route.strip().strip('/')}", handler)
