import os
import sys
from functools import lru_cache
from importlib.metadata import version
from typing import Dict, Union

from .get_package_version import get_package_version
from .missing_plugin_error import MissingPluginError
from .plugin import Plugin

# https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata
# The “selectable” entry points were introduced in importlib_metadata 3.6 and Python 3.10.
# Prior to those changes, entry_points accepted no parameters and always returned a dictionary of entry points.
if sys.version_info < (3, 10):
    from importlib_metadata import (  # pylint: disable=nested-import
        EntryPoint,
        entry_points,
    )
else:
    from importlib.metadata import (  # pylint: disable=nested-import
        EntryPoint,
        entry_points,
    )


def create_plugin(entry_point: EntryPoint, /) -> Plugin:
    plugin_class = entry_point.load()  # type: ignore[no-untyped-call]
    plugin = plugin_class()

    if not isinstance(plugin, Plugin):
        raise TypeError(f"Unexpected plugin type: {type(plugin)}.")

    return plugin


@lru_cache
def get_installed_plugins_entry_points() -> Dict[str, EntryPoint]:
    main_package_version = get_package_version(__name__)
    plugin_entry_points: Dict[str, EntryPoint] = {}

    for entry_point in entry_points(group="atoti.plugins"):
        entry_point_name: str = entry_point.name
        plugin_package_name = f"atoti-{entry_point_name}"
        plugin_version = version(plugin_package_name)

        if plugin_version != main_package_version:
            raise RuntimeError(
                f"Plugin {plugin_package_name} v{plugin_version} does not have the same version as the main package (v{main_package_version})."
            )

        plugin_entry_points[entry_point_name] = entry_point

    return plugin_entry_points


class _ActivePlugins:
    _FILTER_ENV_VAR = "_ATOTI_PLUGIN_FILTER"
    _NO_PLUGINS_FILTER = "no-plugins"

    def __init__(self) -> None:
        self._selected: bool = False

    def selected(self) -> None:
        self._selected = True

    @property
    def filter(self) -> Union[bool, str]:
        value = os.environ.get(_ActivePlugins._FILTER_ENV_VAR)
        if not value:
            return True
        if value == _ActivePlugins._NO_PLUGINS_FILTER:
            return False
        return value

    @filter.setter
    def filter(self, value: Union[bool, str], /) -> None:
        if self._selected:
            raise RuntimeError(
                "Too late to change the plugin filter, the active plugins have already been selected."
            )

        if isinstance(value, bool):
            if value:
                if _ActivePlugins._FILTER_ENV_VAR in os.environ:
                    del os.environ[_ActivePlugins._FILTER_ENV_VAR]
            else:
                os.environ[
                    _ActivePlugins._FILTER_ENV_VAR
                ] = _ActivePlugins._NO_PLUGINS_FILTER
        else:
            plugin_key = next(
                plugin_key
                for plugin_key in get_installed_plugins_entry_points()
                if plugin_key == value
            )
            os.environ[_ActivePlugins._FILTER_ENV_VAR] = plugin_key


_ACTIVE_PLUGINS = _ActivePlugins()


def set_plugin_filter(value: Union[bool, str], /) -> None:
    """Indicate which plugins to activate:

    * ``True`` (default): all installed plugins
    * ``False``: no plugins
    * The plugin key of the only plugin to activate (e.g. ``"aws"``).
    """
    _ACTIVE_PLUGINS.filter = value


@lru_cache
def get_active_plugins() -> Dict[str, Plugin]:
    _ACTIVE_PLUGINS.selected()
    return {
        plugin_key: create_plugin(entry_point)
        for plugin_key, entry_point in get_installed_plugins_entry_points().items()
        if _ACTIVE_PLUGINS.filter is True or _ACTIVE_PLUGINS.filter == plugin_key
    }


def activate_plugins() -> None:
    for plugin in get_active_plugins().values():
        plugin.activate()


def is_plugin_active(plugin_key: str) -> bool:
    return plugin_key in get_active_plugins()


def ensure_plugin_active(plugin_key: str) -> None:
    if not is_plugin_active(plugin_key):
        raise MissingPluginError(plugin_key)
