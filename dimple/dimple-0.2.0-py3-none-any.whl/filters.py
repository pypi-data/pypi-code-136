import inspect
import logging
from   types   import ModuleType

_logger = logging.getLogger("dimple")

class filters:

	@staticmethod
	def _get_key(item):
		if isinstance(item, tuple):
			return item[0]
		return item

	@staticmethod
	def _get_value(item):
		if isinstance(item, tuple):
			return item[1]
		return item

	@staticmethod
	def ispublic(item):
		"""
		item is an attribute name or tuple
		"""
		item = filters._get_key(item)
		return not item.startswith("_")

	@staticmethod
	def isfrommodule(module):
		if isinstance(module, str):
			pass
		if hasattr(module, '__name__'):
			module = getattr(module, '__name__')
		else:
			raise ValueError('module')

		def isfrommodule_inner(item):
			item = filters._get_value(item)
			_logger.debug(f"filters.isfrommodule.isfrommodule_inner: begin module:'{module}' item:'{item}'")
			if isinstance(item, ModuleType):
				# A module we are loading has imported a module. We probably don't ever want to consider that internal.
				_logger.debug(f"filters.isfrommodule.isfrommodule_inner: end: returning False (imported module)")
				return True
			elif hasattr(item, '__module__'):
				# The item has a module attribute, so lets compare against that
				item_module = getattr(item, '__module__')
				r = module == item_module
				_logger.debug(f"filters.isfrommodule.isfrommodule_inner: end: returning {r} ('{module}' == '{item_module}')")
				return r
			else:
				# The item isn't a module and doesn't have a module attribute. (eg A module-level value type of some sort)
				# So not sure what's the correct thing to do here.
				return False
		return isfrommodule_inner

	@staticmethod
	def isclass(item):
		_logger.debug(f"filters.isclass.begin: item:'{item}'")
		item = filters._get_value(item)
		r = inspect.isclass(item)
		_logger.debug(f"filters.isclass.end: returning {r}")
		return r

	@staticmethod
	def isclassname(name):
		def isclassname_inner(item):
			_logger.debug(f"filters.isclassname.begin: name:'{name}' item:'{item}'")
			r = item[0] == name and inspect.isclass(item[1])
			_logger.debug(f"filters.isclassname.end: returning {r}")
			return r
		return isclassname_inner

	@staticmethod
	def issubclass(superclass):
		def issubclass_inner(item):
			_logger.debug(f"filters.issubclass.begin: superclass:'{superclass}' item:'{item}'")
			item = filters._get_value(item)
			r = inspect.isclass(item) and issubclass(item, superclass)
			_logger.debug(f"filters.isclassname.end: returning {r}")
			return r
		return issubclass_inner

