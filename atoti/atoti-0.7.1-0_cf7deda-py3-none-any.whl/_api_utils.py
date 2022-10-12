import inspect
from types import ModuleType
from typing import Any, Callable, Optional, Set, TypeVar, Union

from atoti_core import get_top_level_package_name

ContainerType = Union[type, ModuleType]

ATOTI_NON_PLUGIN_PACKAGE_SUFFIXES = ["core", "query"]


def _is_dunder_method(method_name: str) -> bool:
    return method_name.startswith("__") and method_name.endswith("__")


def _is_plugin(method_module: str) -> bool:
    return method_module.startswith("atoti_") and not any(
        method_module.startswith(f"atoti_{package_suffix}")
        for package_suffix in ATOTI_NON_PLUGIN_PACKAGE_SUFFIXES
    )


def _is_exported_element(
    element: Any,
    *,
    elem_container_module: Optional[ModuleType],
    elem_module: Optional[ModuleType],
) -> bool:
    try:
        if not elem_module:
            return False

        is_part_of_some_public_atoti_package = (
            elem_module.__name__.startswith("atoti")
            and not get_top_level_package_name(elem_module.__name__) == "atoti_core"
        )

        if not is_part_of_some_public_atoti_package:
            return False

        full_name = f"{elem_module.__name__}.{element.__name__}"

        is_monkey_patched_method_by_plugin = (
            elem_container_module is not None
            and _is_plugin(full_name)
            and not _is_plugin(elem_container_module.__name__)
        )

        if is_monkey_patched_method_by_plugin:
            return True

        is_in_private_module = "._" in full_name

        if is_in_private_module:
            return _is_dunder_method(element.__name__)

        return True

    except AttributeError:
        return False


def _walk_api(
    container: ContainerType,
    *,
    callback: Callable[[ContainerType, str], None],
    include_attribute: Optional[Callable[[ContainerType, str], bool]] = None,
    visited_elements: Set[str],
) -> None:
    # Recursively iterate through all the attributes of the container to find public functions.
    for attribute_name in dir(container):
        element = getattr(container, attribute_name)

        # Make sure the element has not been visited already.
        full_name = f"{container.__name__}.{attribute_name}"
        if full_name in visited_elements:
            continue
        visited_elements.add(full_name)
        # Make sure the element should be considered.
        if include_attribute:
            if not include_attribute(container, attribute_name):
                continue
        elif not _is_exported_element(
            element,
            elem_container_module=inspect.getmodule(container),
            elem_module=inspect.getmodule(element),
        ):
            continue

        # Follow "container" types.
        if inspect.ismodule(element) or inspect.isclass(element):
            _walk_api(
                element,
                callback=callback,
                visited_elements=visited_elements,
            )
            continue

        # Invoke the callback on functions.
        if inspect.isfunction(element) or inspect.ismethod(element):
            callback(container, attribute_name)
            continue

        if isinstance(element, TypeVar):
            continue

        # What is this?
        raise RuntimeError(f"Unexpected element {element}")


def walk_api(
    container: ContainerType,
    *,
    callback: Callable[[ContainerType, str], None],
    include_attribute: Optional[Callable[[ContainerType, str], bool]] = None,
) -> None:
    """Recursively explore the public API of the input container.

    Args:
        container: The container to explore.
        callback: The callback to invoke on all public functions.
            It takes the parent container of the exposed function and the function name as arguments.
        include_attribute: A function that returns whether the callback function should be invoked on the given attribute of the container.
            It takes the container and its attribute as inputs.
            If ``None``, this defaults to calling :func:`_is_exported_element` on the attribute.
    """
    visited_elements: Set[str] = set()
    _walk_api(
        container,
        callback=callback,
        include_attribute=include_attribute,
        visited_elements=visited_elements,
    )
