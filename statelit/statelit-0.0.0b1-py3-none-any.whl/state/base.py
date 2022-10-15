from typing import TypeVar, List, Dict, Callable, Any, Optional, Generic, Iterable
import logging

import streamlit as st
from typing_extensions import Literal


__all__ = ["StatefulObjectBase"]


log = logging.getLogger(__name__)


T = TypeVar("T")


class StatefulObjectBase(Generic[T]):
    _value: T
    base_state_key: str
    replicated_state_keys: List[str]
    lazy_state_keys: List[str]
    to_statelit: Callable[[Any], Any]
    to_pydantic: Callable[[Any], Any]
    session_state: Dict[str, Any]

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self._value!r}, base_state_key={self.base_state_key!r})"

    def __init__(
            self,
            value: T,
            *,
            base_state_key: str,
            replicated_state_keys: Optional[List[str]] = None,
            lazy_state_keys: Optional[List[str]] = None,
            to_statelit: Optional[Callable[[Any], Any]] = None,
            to_pydantic: Optional[Callable[[Any], Any]] = None,
            session_state: Dict[str, Any] = None,
    ):
        self.base_state_key = base_state_key
        self.replicated_state_keys = replicated_state_keys or []
        self.lazy_state_keys = lazy_state_keys or []

        if to_statelit is not None:
            self.to_statelit = to_statelit

        if to_pydantic is not None:
            self.to_pydantic = to_pydantic

        if session_state is None:
            session_state = st.session_state
        self.session_state = session_state

        self._value = value
        if self.base_state_key not in self.session_state:
            self.session_state[self.base_state_key] = self.to_statelit(value)

    def to_pydantic(self, v: Any) -> Any:
        return v

    def to_statelit(self, v: Any) -> Any:
        return v

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, v: T) -> None:
        self._value = self.session_state[self.base_state_key] = v
        self.sync(update_lazy=True)

    def commit_key(
            self,
            key: str,
            *,
            state_type: Literal["base", "replicated", "lazy"] = "replicated"
    ) -> None:
        if state_type == "base":
            self.base_state_key = key
        elif state_type == "replicated":
            self.replicated_state_keys.append(key)
            self.session_state[key] = self.session_state[self.base_state_key]
        elif state_type == "lazy":
            self.lazy_state_keys.append(key)
            if key not in self.session_state:
                self.session_state[key] = self.session_state[self.base_state_key]
        else:
            raise ValueError

    @property
    def all_keys_generator(self) -> Iterable[str]:
        yield self.base_state_key
        for key in self.replicated_state_keys:
            yield key
        for key in self.lazy_state_keys:
            yield key

    def next_key(self) -> str:
        key_list = set(self.all_keys_generator)
        for i in range(100_000):
            candidate_key = f"{self.base_state_key}.{i}"
            if candidate_key not in key_list:
                return candidate_key
        else:
            raise ValueError

    def sync(self, update_lazy: bool = True):
        validated_value = self.to_statelit(self.value)

        log.debug(f"Syncing {self} with value {validated_value} and update_lazy={update_lazy}")

        for key in [self.base_state_key] + self.replicated_state_keys:
            self.session_state[key] = validated_value
        if update_lazy:
            for key in self.lazy_state_keys:
                self.session_state[key] = validated_value

    def gen_key(self, key_suffix: Optional[str] = None) -> str:
        """Stateless operation"""
        if not key_suffix:
            return self.next_key()
        else:
            return f"{self.base_state_key}.{key_suffix}"
