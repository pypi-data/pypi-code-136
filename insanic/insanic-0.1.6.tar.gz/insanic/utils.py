"""Common classes and methods used in framework."""
import asyncio
import importlib
from collections.abc import AsyncGenerator, Coroutine, Generator
from contextlib import asynccontextmanager
from inspect import isawaitable
from pathlib import Path
from typing import Any, Awaitable, Callable, cast

from insanic.app import Application

class ContainerField:
    source: str | None

    """Common class for Form and Serializer."""
    def __init__(self, source: str | None = None):
        self.source = source

class Container:
    FIELD_BASE_CLASS = ContainerField
    RESERVED_ATTRS: list[str] = []

    _field_names: list[str] = []

    def __init__(self, *args: Any, **kwargs: Any) -> None: # pylint: disable=unused-argument
        # List of declared fields
        self._field_names = [
            attribute
            for attribute in dir(self)
            if attribute not in self.RESERVED_ATTRS and isinstance(getattr(self, attribute), self.FIELD_BASE_CLASS)
        ]

    def _field_values(self, data: Any) -> Generator:
        for field_name in self._field_names:
            field: ContainerField = getattr(self, field_name)
            field_source = getattr(field, 'source', None)  # Using field's `source` attribute as value path
            property_value_path = field_source or field_name
            field_value = get_property_value(data, property_value_path)
            yield field_name, field_value, field

def get_property_value(entity: dict | object, key: str) -> Any:
    """Get value by key from dict or any object.

    Returns None if key missing in entity
    """
    if isinstance(entity, dict):
        return entity.get(key, None)

    return getattr(entity, key, None)

def read_file_content(file_path: str | Path) -> str:
    with open(file_path, 'rt', encoding="utf-8") as file:
        return file.read()

def run_async(coroutine: Coroutine) -> Any:
    return asyncio.run(coroutine)

async def ensure_run(result: Awaitable | Callable) -> Any:
    if isawaitable(result):
        return await cast(Awaitable, result)

    return result

def load_application() -> Application:
    app_module = importlib.import_module('app', package='src')  # importing src/app.py
    application: Application = getattr(app_module, 'application')

    return application

@asynccontextmanager
async def application_context() -> AsyncGenerator:
    application = load_application()
    loop = asyncio.get_running_loop()

    await application.boot(application, loop)
    try:
        yield application
    except Exception as error:
        raise error
    finally:
        await application.shutdown(application, loop)
