from functools import partial
from typing import TypeVar, Type, List, Dict, Any, Optional, Generic

import streamlit as st
from pydantic import BaseModel

from statelit.state.model import StatelitModel
from statelit.utils.misc import chain_two_callables


ModelInstanceType = TypeVar("ModelInstanceType", bound=BaseModel)
T = TypeVar("T")


class StateManager(Generic[ModelInstanceType]):
    statelit_model_class: Type[StatelitModel] = StatelitModel
    statelit_model: StatelitModel
    session_state: Dict[str, Any]

    def __init__(
            self,
            pydantic_model: Type[ModelInstanceType],
            *,
            session_state: Dict[str, Any] = None,
            base_state_key: str = None,
    ):
        if base_state_key is None:
            base_state_key = f"statelit.{pydantic_model.__name__}"
        if session_state is None:
            session_state = st.session_state

        if base_state_key in session_state:
            pydantic_obj = pydantic_model.parse_raw(session_state[base_state_key])
        else:
            pydantic_obj = pydantic_model()

        self.statelit_model = self.statelit_model_class(
            value=pydantic_obj,
            base_state_key=base_state_key,
            session_state=session_state
        )

    @property
    def session_state(self) -> Dict[str, Any]:
        return self.statelit_model.session_state

    @property
    def base_state_key(self) -> str:
        return self.statelit_model.base_state_key

    @property
    def pydantic_obj(self) -> ModelInstanceType:
        return self.statelit_model.value

    @pydantic_obj.setter
    def pydantic_obj(self, v: Any):
        self.statelit_model.value = v

    def sync(self, update_lazy: bool = True):
        self.statelit_model.sync(update_lazy=update_lazy)

    def apply_session_state_delta(self, key: str):
        if key in self.statelit_model.all_keys_generator:
            self.apply_obj_delta(key=key)
        for field_name, statelit_field in self.statelit_model.fields.items():
            if key in statelit_field.all_keys_generator:
                self.apply_field_delta(key, field_name)

    def apply_field_delta(self, key: str, field_name: str):
        data = {}
        for fn, field in self.statelit_model.fields.items():
            if fn != field_name:
                data[fn] = field.to_pydantic(self.session_state[field.base_state_key])
            else:
                data[fn] = field.to_pydantic(self.session_state[key])
        self.statelit_model.value = self.statelit_model.value.__class__(**data)

    def apply_obj_delta(self, key: str):
        raw_json: str = self.session_state[key]
        self.statelit_model.value = self.statelit_model.to_pydantic(raw_json)

    def widget(
            self,
            field_name: str,
            key_suffix: Optional[str] = None,
            run_to_pydantic_callback: bool = True,
            **kwargs
    ) -> Any:
        statelit_field = self.statelit_model.fields[field_name]

        if "key" in kwargs and key_suffix is not None:
            raise ValueError("key= and key_suffix= kwargs cannot both be set at the same time.")

        if "key" in kwargs:
            key = kwargs.pop("key")
        else:
            key = statelit_field.gen_key(key_suffix=key_suffix)

        statelit_field.commit_key(key=key, state_type="replicated")

        apply_delta = partial(self.apply_session_state_delta, key=key)

        if "on_change" in kwargs:
            apply_delta = chain_two_callables(apply_delta, kwargs.pop("on_change"))

        value = statelit_field.widget_callback(
            on_change=apply_delta,
            key=key,
            **kwargs,
        )

        if run_to_pydantic_callback:
            value = statelit_field.to_pydantic(value)

        return value

    def form(self, key_suffix: Optional[str] = None, exclude: List[str] = None) -> ModelInstanceType:
        if not exclude:
            exclude = []
        for field_name in self.statelit_model.fields:
            if field_name not in exclude:
                self.widget(field_name, key_suffix=key_suffix)
        return self.pydantic_obj

    def code(self) -> str:
        value = self.session_state[self.base_state_key]
        st.code(value, language="json")
        return value

    def text_area(self, key_suffix: str = None, **kwargs) -> str:
        if "key" in kwargs and key_suffix is not None:
            raise ValueError("key= and key_suffix= kwargs cannot both be set at the same time.")

        if "key" in kwargs:
            key = kwargs.pop("key")
        else:
            key = self.statelit_model.gen_key(key_suffix=key_suffix)

        self.statelit_model.commit_key(key=key, state_type="replicated")

        if "label" not in kwargs:
            kwargs["label"] = self.statelit_model.value.__class__.__name__

        apply_delta = partial(self.apply_session_state_delta, key=key)

        if "on_change" in kwargs:
            apply_delta = chain_two_callables(apply_delta, kwargs.pop("on_change"))

        return st.text_area(
            on_change=apply_delta,
            key=key,
            **kwargs
        )

    def lazy_text_area(self, key_suffix: str = None, **kwargs):
        if "key" in kwargs and key_suffix is not None:
            raise ValueError("key= and key_suffix= kwargs cannot both be set at the same time.")

        if "key" in kwargs:
            key = kwargs.pop("key")
        else:
            key = self.statelit_model.gen_key(key_suffix=key_suffix)

        self.statelit_model.commit_key(key=key, state_type="lazy")

        if "label" not in kwargs:
            kwargs["label"] = self.statelit_model.value.__class__.__name__

        def apply_delta():
            self.statelit_model.value = self.statelit_model.value.parse_raw(self.session_state[key])
            self.session_state[key] = self.session_state[self.base_state_key]

        if "on_click" in kwargs:
            apply_delta = chain_two_callables(apply_delta, kwargs.pop("on_click"))

        s = st.text_area(
            key=key,
            **kwargs
        )

        st.button("Apply", on_click=apply_delta, key=f"{key}._button")
        return s
