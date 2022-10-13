import importlib
import importlib.util
import logging
import sys
import types
from   pathlib   import Path

from   .internal import _internal
from   .filters  import filters


def load(path, *paths, attr=None, call=False, external=False, private=False):
	"""
	Load a module, and return the module, or an attribute from that module.

	Can be called directly, but consider some of wrapper functions: dimple.classes, dimple.instances, 

	The value of attr determines load's return value. When -
		- attr is None, return the loaded module.
		- attr is a str, return the attribute of that name in the loaded module
		- attr is a regex, return the first attribute whose name matches
		- attr is callable, return its return value when called with the loaded module
	"""

	logger = logging.getLogger("dimple")
	logger.debug(f"load: begin: {locals()}")

	if not len(path):
		raise ValueError('path')

	name = _internal.get_module_basename_without_ext(path)
	path = _internal.get_path(path, *paths)

	r, _ = _internal.load(name, path, attr=attr, call=call, external=external, private=private)

	return r

