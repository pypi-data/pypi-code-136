import inspect
from dataclasses import dataclass, field
from importlib import import_module
from typing import Union, Callable, Any, Optional, Dict

from .base import ModelProtocol


@dataclass
class Relationship:
    key: Union[str, Callable[[ModelProtocol], Any]]
    model: Union[type, str]
    join_model: Optional[Union[type, str]] = None
    single: bool = True
    on_clause: Optional[Any] = None
    _globals: Dict[str, Any] = field(default_factory=lambda: inspect.stack()[2][0].f_globals, repr=False, compare=False)

    def get_key(self, instance: ModelProtocol):
        if callable(self.key):
            return self.key(instance)
        return getattr(instance, self.key)

    def _get_model(self, model_field) -> ModelProtocol:
        if isinstance(model_field, str):
            if '.' in model_field:
                class_path, class_name = model_field.rsplit('.', maxsplit=1)
                try:
                    module = import_module(class_path)
                    return getattr(module, class_name)
                except ImportError:
                    pass

            if model_field in self._globals:
                return self._globals[model_field]
            else:
                return eval(model_field, self._globals)

        return model_field

    def get_model(self) -> ModelProtocol:
        return self._get_model(self.model)

    def get_join_model(self) -> ModelProtocol:
        return self._get_model(self.join_model or self.model)

    def get_on_clause(self, model):
        if callable(self.on_clause):
            return self.on_clause(model)
        elif isinstance(self.on_clause, str):
            return eval(self.on_clause, self._globals)
        return self.on_clause
