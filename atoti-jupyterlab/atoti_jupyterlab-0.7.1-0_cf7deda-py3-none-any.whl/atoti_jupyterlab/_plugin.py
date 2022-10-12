from atoti_core import BaseSession, BaseSessionBound, Plugin
from atoti_query import QueryResult

from ._link import link
from ._visualize import visualize
from ._widget_conversion import create_query_result_repr_mimebundle_method_
from ._widget_manager import WidgetManager


class JupyterLabPlugin(Plugin):

    _widget_manager: WidgetManager = WidgetManager()

    def activate(self) -> None:
        # See https://github.com/python/mypy/issues/2427.
        BaseSession.link = link  # type: ignore[assignment]
        # See https://github.com/python/mypy/issues/2427.
        BaseSession.visualize = visualize  # type: ignore[assignment]

        # See https://github.com/python/mypy/issues/2427.
        QueryResult._repr_mimebundle_ = create_query_result_repr_mimebundle_method_(  # type: ignore[assignment]
            original_method=QueryResult._repr_mimebundle_
        )

    def init_session(self, session: BaseSessionBound, /) -> None:
        """Initialize the session."""
        session._widget_manager = self._widget_manager  # type: ignore
