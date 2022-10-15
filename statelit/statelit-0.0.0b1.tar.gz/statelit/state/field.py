from typing import TypeVar, List, Dict, Callable, Any, Optional

from statelit.state.base import StatefulObjectBase


T = TypeVar("T")


class StatelitField(StatefulObjectBase[T]):

    def __init__(
            self,
            value: T,
            *,
            base_state_key: str,
            replicated_state_keys: Optional[List[str]] = None,
            lazy_state_keys: Optional[List[str]] = None,
            to_statelit: Optional[Callable[[Any], Any]] = None,
            widget_callback: callable = None,
            to_pydantic: Optional[Callable[[Any], Any]] = None,
            session_state: Dict[str, Any] = None,
    ):
        super().__init__(
            value=value,
            base_state_key=base_state_key,
            replicated_state_keys=replicated_state_keys,
            lazy_state_keys=lazy_state_keys,
            to_statelit=to_statelit,
            to_pydantic=to_pydantic,
            session_state=session_state,
        )
        self.widget_callback = widget_callback
