from typing import TypeVar, Type, List, Dict, Callable, Any, Optional, Generic, ClassVar
from typing_extensions import Literal
from functools import lru_cache

from pydantic import BaseModel
from pydantic.fields import ModelField
from pydantic.utils import Representation
from statelit.state.field import StatelitField
from statelit.utils.mro import find_implementation


T = TypeVar("T")
FT = TypeVar("FT", bound=StatelitField)


def _identity(v: Any) -> Any:
    return v


class StatelitConverterAssociation(Representation):
    __slots__ = ("callback_name", "converter_type", "fields", "types")

    def __init__(
            self,
            callback_name: str,
            converter_type: Literal["widget", "to_streamlit", "to_pydantic"],
            fields: List[str] = None,
            types: List[type] = None
    ):
        self.callback_name = callback_name
        self.converter_type = converter_type
        if fields and types:
            raise ValueError("Pass only fields or types, not both.")
        self.fields = fields or []
        self.types = types or []


class FieldCallbacks(Representation):
    __slots__ = ("streamlit_callback", "to_statelit_callback", "to_pydantic_callback")

    def __init__(
            self,
            streamlit_callback: callable,
            *,
            to_statelit_callback: Optional[Callable[[Any], Any]] = None,
            to_pydantic_callback: Optional[Callable[[Any], Any]] = None
    ):
        self.streamlit_callback = streamlit_callback
        self.to_statelit_callback: Callable[[Any], Any] = to_statelit_callback or _identity
        self.to_pydantic_callback: Callable[[Any], Any] = to_pydantic_callback or _identity


class FieldFactoryBase(Generic[T]):
    field_class: ClassVar[Type[T]]

    def __init__(self, key_prefix: str, session_state: Dict[str, Any]):
        self.key_prefix = key_prefix
        self.session_state = session_state

    def __call__(self, value: Any, field: ModelField, model: Type[BaseModel]) -> T:
        raise NotImplementedError


class CallbackConverterTypeMeta(type):

    def __instancecheck__(self, instance):
        return bool(
            callable(instance)
            and hasattr(instance, "__statelit_callback_info__")
        )


class CallbackConverterType(metaclass=CallbackConverterTypeMeta):
    __statelit_callback_info__: List[StatelitConverterAssociation]
    __name__: str

    def __new__(cls, callback_converter: callable):
        callback_converter.__statelit_callback_info__ = []
        return callback_converter

    def __call__(self, value: Any, model: Type[BaseModel], field: ModelField) -> callable:
        raise NotImplementedError


def is_converter_for(
        callback_type: Literal["streamlit", "pre", "post"],
        *,
        fields: List[str] = None,
        types: List[type] = None
) -> Callable[[callable], CallbackConverterType]:
    def _wrap(func: callable) -> CallbackConverterType:
        if not isinstance(func, CallbackConverterType):
            func = CallbackConverterType(func)
        func.__statelit_callback_info__.append(StatelitConverterAssociation(
            callback_name=func.__name__,
            converter_type=callback_type,
            fields=fields,
            types=types
        ))
        return func

    return _wrap


def is_streamlit_callback_converter_for(
        fields: List[str] = None,
        types: List[type] = None
) -> Callable[[callable], CallbackConverterType]:
    return is_converter_for(
        "streamlit",
        fields=fields,
        types=types
    )


def is_post_callback_converter_for(
        fields: List[str] = None,
        types: List[type] = None
) -> Callable[[callable], CallbackConverterType]:
    return is_converter_for(
        "post",
        fields=fields,
        types=types
    )


def is_pre_callback_converter_for(
        fields: List[str] = None,
        types: List[type] = None
) -> Callable[[callable], CallbackConverterType]:
    return is_converter_for(
        "pre",
        fields=fields,
        types=types
    )


class DynamicFieldFactoryBase(FieldFactoryBase[FT]):
    field_class: ClassVar[Type[FT]] = StatelitField
    statelit_converter_associations: List[StatelitConverterAssociation]

    def __init__(self, key_prefix: str, session_state: Dict[str, Any]):
        super().__init__(key_prefix=key_prefix, session_state=session_state)
        self.statelit_converter_associations = []
        self._register_converter_callables()

    def _register_converter_callables(self):
        statelit_converter_associations: List[StatelitConverterAssociation] = []
        for attr_name in dir(self):
            obj = getattr(self, attr_name)
            if isinstance(obj, CallbackConverterType):
                for assoc in obj.__statelit_callback_info__:
                    statelit_converter_associations.append(assoc)
        self.statelit_converter_associations = statelit_converter_associations

    @lru_cache(maxsize=None)
    def callback_mapping(
            self,
            *,
            association_type: Literal["fields", "types"],
            callback_type: Literal["streamlit", "pre", "post"]
    ) -> Dict[Any, callable]:
        d: Dict[str, callable] = {}
        for assoc in self.statelit_converter_associations:
            if assoc.converter_type == callback_type:
                for i in getattr(assoc, association_type):
                    d[i] = getattr(self, assoc.callback_name)
        return d

    def get_callback_by_type(
            self,
            value: Any,
            field: ModelField,
            model: Type[BaseModel],
            callback_type: Literal["streamlit", "pre", "post"]
    ) -> Optional[callable]:
        if field.name in self.callback_mapping(callback_type=callback_type, association_type="fields"):
            converter = self.callback_mapping(callback_type=callback_type, association_type="fields")[field.name]
        else:
            converter = find_implementation(
                field.type_,
                self.callback_mapping(callback_type=callback_type, association_type="types")
            )
        if converter is not None:
            return converter(value=value, field=field, model=model)
        else:
            return None

    def get_widget_callback(self, value: Any, field: ModelField, model: Type[BaseModel]):
        callback = self.get_callback_by_type(
            value=value,
            field=field,
            model=model,
            callback_type="streamlit"
        )
        if callback is None:
            raise TypeError(
                f"Could not find a valid Streamlit callback for Field({field})."
                f" Check to make sure that {field.type_!r} is a supported type."
            )
        return callback

    def get_to_pydantic_callback(self, value: Any, field: ModelField, model: Type[BaseModel]):
        return self.get_callback_by_type(
            value=value,
            field=field,
            model=model,
            callback_type="post"
        )

    def get_to_streamlit_callback(self, value: Any, field: ModelField, model: Type[BaseModel]):
        return self.get_callback_by_type(
            value=value,
            field=field,
            model=model,
            callback_type="pre"
        )

    def get_field_callbacks(self, value: Any, field: ModelField, model: Type[BaseModel]) -> FieldCallbacks:
        return FieldCallbacks(
            streamlit_callback=self.get_widget_callback(value=value, field=field, model=model),
            to_statelit_callback=self.get_to_streamlit_callback(value=value, field=field, model=model),
            to_pydantic_callback=self.get_to_pydantic_callback(value=value, field=field, model=model)
        )

    def __call__(
            self,
            value: Any,
            field: ModelField,
            model: Type[BaseModel],
    ) -> FT:
        field_callbacks: FieldCallbacks = self.get_field_callbacks(value=value, model=model, field=field)
        base_state_key = f"{self.key_prefix}.{field.name}"
        statelit_field = self.field_class(
            value=value,
            base_state_key=base_state_key,
            widget_callback=field_callbacks.streamlit_callback,
            to_statelit=field_callbacks.to_statelit_callback,
            to_pydantic=field_callbacks.to_pydantic_callback,
            session_state=self.session_state,
        )
        return statelit_field
