import logging
import os

from  .constants import *
from  .catalog   import Catalog
from  .filters   import filters
from  .internal  import _internal
from  .load      import load


_logger = logging.getLogger("dimple")

# Load wrappers

def module(path, *paths, **kwargs):
	_logger.debug(f"module: begin")

	for k in ('attr', 'call', 'super'):
		if k in kwargs:
			raise ValueError(k)

	kwargs['attr'] = None
	kwargs['call'] = False

	r = load(path, *paths, **kwargs)

	_logger.debug(f"module: end: returning {r}")
	return r


def cls(path, *paths, attr=None, private=False, super=None):
	_logger.debug(f"cls: begin")
	attr = _internal.get_cls_filter(attr, super)
	r = load(path, *paths, attr=attr, call=False, private=private)
	_logger.debug(f"cls: end: returning {r}")
	return r


def instance(path, *paths, attr=None, private=False, super=None):
	_logger.debug(f"instance: begin")
	attr = _internal.get_cls_filter(attr, super)
	r = load(path, *paths, attr=attr, call=True, private=private)
	_logger.debug(f"instance: end: returning {r}")
	return r


# Catalog wrappers

def catalog(**kwargs):
	return Catalog(**kwargs)


def modules(**kwargs):
	for k in ('attr', 'call', 'super'):
		if k in kwargs:
			raise ValueError(k)
	attr = None
	call = False
	return catalog(attr=attr, call=call, **kwargs)


def classes(*, attr=None, super=None, **kwargs):
	"""
	Return a dictionary of classes found in the specified files
	"""
	_logger.debug(f"classes: begin: {locals()}")
	attr = _internal.get_cls_filter(attr, super)
	call = False
	r = catalog(attr=attr, call=call, **kwargs)
	_logger.debug(f"classes: end")
	return r


def instances(*, attr=None, super=None, **kwargs):
	"""
	Return a dictionary of instances of classes found in the specified files
	"""
	_logger.debug(f"instances: begin: {locals()}")
	attr = _internal.get_cls_filter(attr, super)
	call = True
	r = catalog(attr=attr, call=call, **kwargs)
	_logger.debug(f"instances: end")
	return r


def public(object):
	return list(filter(filters.ispublic, dir(object)))
