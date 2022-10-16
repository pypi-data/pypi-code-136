from typing import Any

from sanic.router import Route

from insanic.commands import SyncCommand
from insanic.utils import load_application

def sort_routes(route: Route) -> str:
    is_app_route = len(route.segments) != 1
    route_first_letter = route.segments[0][0]  # First letter of first segments

    return (is_app_route, route_first_letter,)

class RoutesCommand(SyncCommand):
    help = 'Prints all registered routes'

    def execute(self, **kwargs: Any) -> None:
        application = load_application()

        sorted_routes = sorted(application.router.routes_all.values(), key=sort_routes)
        for route in sorted_routes:
            print(route.uri)
