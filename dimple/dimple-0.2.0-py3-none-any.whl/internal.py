import importlib
import importlib.util
import inspect
import logging
import os
import re
import sys
import types
from   pathlib import Path

from  .filters import filters


class _internal:

	@staticmethod
	def get_path(path, *paths):
		"""
		Assembles path compontents, and handles special values
		"""

		logger = logging.getLogger("dimple")
		logger.debug(f"_get_path: begin")

		path = os.path.join(path, *paths)

		prefix = "__dir__"
		prefix_with_slash = f"{prefix}/"

		if path == prefix:
			path_remaining = ""
		elif path.startswith(prefix_with_slash):
			path_remaining = path[len(prefix_with_slash):]
		else:
			logger.debug(f"_get_path: end: returning '{path}' (nothing else to do)")
			return path

		# Find caller dir
		for i, frame in enumerate(inspect.stack()):
			logger.debug(f"_get_path: stack {i:2} {frame.filename}")
			if re.search("^.+/dimple/[\w.]+.py", frame.filename) is None:
				logger.debug(f"_get_path: found caller")
				caller_dir = os.path.split(frame.filename)[0]
				logger.debug(f"_get_path: directory of caller module: {caller_dir}")
				logger.debug(f"_get_path: remaining path argument: {path_remaining}")
				path = os.path.join(caller_dir, path_remaining)
				logger.debug(f"_get_path: end: returning '{path}'")
				return path

	@staticmethod
	def get_cls_filter(attr, super):
		"""
		Returns the appropriate filter function for the given parameters
		"""
		if attr is not None:
			if super is not None:
				raise ValueError('attr and super')
			attr = filters.isclassname(attr)
		else:
			if super is not None:
				attr = filters.issubclass(super)
			else:
				attr = filters.isclass
		return attr


	@staticmethod
	def get_module_basename_without_ext(path):
		# TODO: improve this, just assumes .py and no other '.'s in basename
		logger = logging.getLogger("dimple")
		logger.debug(f"_get_module_basename: path: {path}")
		basename = os.path.basename(path)
		logger.debug(f"_get_module_basename: {basename}")
		r = basename.rsplit('.', maxsplit=1)[0]
		return r


	@staticmethod
	def get_module_attr(*, module, attr, call, external, private):
		"""
		If attr is None, return module
		If attr is a str, return the attribute of that name from module
		If attr is a regex, return the first attribute whose name matches that regex
		If attr is callable, return its return value when called like so: attr(module)

		external:
		private:

		call: If True, call the return value and return the result of the call

		"""

		logger = logging.getLogger("dimple")
		logger.debug(f"_internal.get_module_attr: begin: {locals()}")

		if attr is None:
			logger.debug(f"_internal.get_module_attr: end: attr None, returning module")
			return module

		if isinstance(attr, int):
			# TODO return nth attrribute?
			pass

		if isinstance(attr, str):
			if any(map(lambda c : c in '^$*+?.', attr)):
				# Regex
				logger.debug(f"_internal.get_module_attr: looking for attr that matches pattern {pattern} ...")
				attr = re.compile(attr)
			else:
				# Get attr by name
				logger.debug(f"_internal.get_module_attr: looking for attr called '{attr}'")
				s = attr
				def equals(item):
					return item[0] == s
				attr = equals

		if hasattr(attr, 'search') and callable(attr.search):
			pattern = attr
			def search(item):
				return pattern.search(item[0]) is not None
			attr = search

		if not callable(attr):
			raise ValueError('attr')

		# Find first "unfiltered" attribute
		r = None
		for item in module.__dict__.items():
			item_value_str = str(item[1]).replace('\n','')[:32]
			logger.debug(f"_internal.get_module_attr: module attribute: {item[0]} => '{item_value_str} ...'")
			if not private and not filters.ispublic(item):
				logger.debug(f"_internal.get_module_attr:   skipped (private)")
				continue
			if not external and not filters.isfrommodule(module)(item):
				logger.debug(f"_internal.get_module_attr:   skipped (external)")
				continue
			if not attr(item):
				logger.debug(f"_internal.get_module_attr:   skipped (callable attr returned False)")
				continue
			r = item[1]
			break

		if r is not None and call:
			logger.debug(f"_internal.get_module_attr: return value before call: {r}")
			r = r()
			logger.debug(f"_internal.get_module_attr: return value after call:  {r}")

		logger.debug(f"_internal.get_module_attr: end: returning: {r}")
		return r


	@staticmethod
	def load(name, path, attr=None, call=False, external=False, private=False):
		"""
		Imports a module and optional select an attribute from that module.
		"""

		logger = logging.getLogger("dimple")
		logger.debug(f"_internal.load: begin: {locals()}")

		# Load module
		logger.debug(f"_internal.load: calling spec_from_file_location with name:'{name}' path:'{path}'")
		spec = importlib.util.spec_from_file_location(name, path)

		logger.debug(f"_internal.load: calling module_from_spec: {spec} ...")
		module = importlib.util.module_from_spec(spec)

		logger.debug(f"_internal.load: calling exec_module: {module} ...")
		spec.loader.exec_module(module)

		logger.debug(f"_internal.load: module: {module} name:{module.__name__}")

		# Get return value
		r = _internal.get_module_attr(module=module, attr=attr, call=call, external=external, private=private)

		logger.debug(f"_internal.load: returning: {r}, {module}")
		return r, module
