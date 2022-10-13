import importlib
import logging
import os.path
from   collections.abc import Mapping
from   functools       import partial
from   time            import time, asctime, gmtime

from  .constants       import *
from  .internal        import _internal
from  .load            import load
from  .filters         import filters
from  .globber         import Globber


class Catalog(dict):
	"""
	A catalog of modules, or module members, that match certain criteria.
	"""

	class __ItemMetaData:
		__slots__ = 'file', 'module', 'import_time', 'load'

	def __init__(self, *, attr=None, path=None, pattern=None, files=None, package=None, recursive=False, call=False, private=False, external=False, key=None, each=None, error=RAISE, reload=False):
		"""
		Do stuff
		:param attr:    The name of the attribute to find in each module
		:param files:   Iterable of file paths to import. If this is not None
		:param path:    The directory to scan
		:param pattern: The globbing pattern to use. (See glob() from the builtin glob module for further information)
		:
		:param key:     How to add a found module to the catalog. If None, use a key derived from the filename. If a str, use an attr of that name ...

		:param error:   Simple usage:
							error=dimple.RAISE
								Reraise any exception.
							error=dimple.IGNORE
								Silently ignore all exceptions. Modules imports that raise an exception will not be added to the catalog.

						Tuple:
							More granular behaviour can be had by passing a tuple. The first element is one of dimple.RAISE/dimple.IGNORE, and the remaining elements are Exception subclasses

							error=(dimple.RAISE, Exception1, Exception2, ...)
								Raise any exceptions that are instances of any of the given Exception types (isinstance returns True). Other exceptions are silenty ignored.

							error=(dimple.IGNORE, Exception1, Exception2, ...)
								Ignore exceptions that are instances of any of the given Exception types (isinstance returns True). Any other exceptions are raised

						Mapping:
							Takes no action in response to an error, except to add an entry to the Mapping with key ''

						Callable:
							Similar to each

		:param each:    Optional provide a callable of the form func(obj, 


		"""

		logger = logging.getLogger("dimple")
		logger.debug(f"Catalog.__init__: begin: {locals()}")

		self.__each   = each
		self.__reload = reload
		if reload:
			self.__item_meta_data = {}

		if files is None:

			if path is None:
				path = ""
			path = _internal.get_path(path)

			if pattern is None:
				pattern="[!_]*.py"

			if recursive:
				pattern="**/" + pattern

			files = Globber().iglob(path=path, pattern=pattern, recursive=recursive)

		elif path is not None:

			path = _internal.get_path(path)

			if not os.path.isdir(path):
				raise ValueError("'path' must be a valid directory if passed with 'files'")

			files = map(lambda x : os.path.join(path, x), files)


		if isinstance(error, tuple):
			logger.debug(f"Catalog.__init__: error tuple: {error}")
			error, *exceptions = error
			logger.debug(f"Catalog.__init__: unpacked to: {error}, {exceptions}")
			if not (error is RAISE or error is IGNORE):
				raise ValueError(f"error:'{error}'")
			exceptions = tuple(exceptions)
		else:
			exceptions = None


		for file in files:

			kwargs = None

			try:
				logger.debug(f"Catalog.__init__: loop begin: '{file}'")
				basename_without_ext = _internal.get_module_basename_without_ext(file)

				if callable(self.__each) or callable(error) or callable(key):
					kwargs = {
						'basename':             os.path.basename(file),
						'basename_without_ext': basename_without_ext,
						'dirname':              os.path.abspath(os.path.dirname(file)),
						'file':                 os.path.abspath(file),
					}

				# get value
				v, module = self.__load(file, each_kwargs=kwargs, attr=attr, call=call, private=private)

				if v is None:
					# TODO option to abort?
					continue

				# get key
				if key is None:
					# What was this?
					#if filters.isclass(attr):
					#	logger.debug(f"_get_key: using __name__ {attr.__name__}")
					#	k = attr.__name__

					# What was this?
					#if hasattr(attr, '__module__'):
					#	logger.debug(f"Catalog.__init__:   key: using __module__")
					#	k = getattr(attr, '__module__')
					#else:

					logger.debug(f"Catalog.__init__:   key: using basename_without_ext '{basename_without_ext}'")
					k = basename_without_ext
				elif callable(key):
					if hasattr(key, '__objclass__') and key.__objclass__ is str:
						logger.debug(f"Catalog.__init__:   key: builtin str method: calling {key} with only basename_without_ext ...")
						k = key(basename_without_ext)
					else:
						logger.debug(f"Catalog.__init__:   key: calling {key} ...")
						k = key(**kwargs)
				elif isinstance(key, str):
					logger.debug(f"Catalog.__init__:   key: using getattr('{key}') ...")
					k = getattr(v, key)
					if callable(k):
						k = k()
				else:
					raise ValueError('key')

				if self.__reload:
					item_meta_data             = Catalog.__ItemMetaData()
					item_meta_data.file        = file
					item_meta_data.module      = module
					item_meta_data.import_time = time()
					item_meta_data.load        = partial(Catalog.__load, self, file, each_kwargs=kwargs, attr=attr, call=call, private=private)
					logger.debug(f"Catalog.__init__: reload True, storing meta data for later: key:{k} v:{item_meta_data} ...")
					self.__item_meta_data[k]   = item_meta_data

				logger.debug(f"Catalog.__init__:   adding with key:{k} value:{v} ...")
				self[k] = v

			except Exception as ex:
				logger.debug(f"Catalog.__init__:   exception: {type(ex)} {ex}")

				if error is RAISE:
					if exceptions is None:
						logger.debug(f"Catalog.__init__:   exception: RAISE all")
						raise ex
					if type(ex) in exceptions:
						logger.debug(f"Catalog.__init__:   exception: RAISE and ex in exceptions:{exceptions}")
						raise ex
					logger.debug(f"Catalog.__init__:   exception: RAISE but ex not in exceptions:{exceptions}")

				elif error is IGNORE:
					if exceptions is None:
						logger.debug(f"Catalog.__init__:   exception: IGNORE all")
					elif type(ex) not in exceptions:
						logger.debug(f"Catalog.__init__:   exception: IGNORE and ex not in exceptions:{exceptions}")
						raise ex
					logger.debug(f"Catalog.__init__:   exception: IGNORE but ex in exceptions:{exceptions}")

				elif isinstance(error, Mapping):
					error[file] = ex

				elif callable(error):
					error(ex, **kwargs)

			logger.debug(f"Catalog.__init__: loop end")

		logger.debug(f"Catalog.__init__: end")

	def __getitem__(self, key):
		logger = logging.getLogger("dimple")
		logger.debug(f"Catalog.__getitem__: begin: key:{key}")
		if self.__reload:
			item_meta_data = self.__item_meta_data[key]
			mtime = os.path.getmtime(item_meta_data.file)
			delta = item_meta_data.import_time - mtime
			logger.debug(f"Catalog.__getitem__: reload=True")
			logger.debug(f"Catalog.__getitem__: import time:       {item_meta_data.import_time:2.3f} - {asctime(gmtime(item_meta_data.import_time))}")
			logger.debug(f"Catalog.__getitem__: modification time: {mtime:2.3f} - {asctime(gmtime(mtime))}")
			logger.debug(f"Catalog.__getitem__: delta:             {delta}")
			if delta < 0:
				logger.debug(f"Catalog.__getitem__: reloading module {item_meta_data.file} ...")
				v = super().__getitem__(key)
				v, module = item_meta_data.load()
				item_meta_data.module = module
				self[key] = v
				item_meta_data.import_time = time()
				logger.debug(f"Catalog.__getitem__: import time updated: {item_meta_data.import_time:2.3f} - {asctime(gmtime(item_meta_data.import_time))}")
				return v
		r = super().__getitem__(key)
		logger.debug(f"Catalog.__getitem__: end")
		return r

	def __load(self, path, each_kwargs, **kwargs):
		logger = logging.getLogger("dimple")
		logger.debug(f"Catalog.__load: calling _internal.load() ...")
		name = _internal.get_module_basename_without_ext(path)
		v, m = _internal.load(name, path, **kwargs)
		if v is not None:
			if self.__each is not None:
				logger.debug(f"Catalog.__load: calling each func {self.__each} with kwargs {each_kwargs}...")
				self.__each(v, **each_kwargs)
		return v, m

	def filter(self, *, attr=None, call=False, external=False, private=False):
		r = {}
		for item in self.items():
			v = _internal.get_module_attr(module=item[1], attr=attr, external=external, private=private, call=call)
			if v is not None:
				r[item[0]] = v
		return r

	def classes(self, *, attr=None, super=None, **kwargs):
		"""
		Return a dictionary of classes found within the modules of this catalog
		"""
		attr = _internal.get_cls_filter(attr, super)
		call = False
		return self.filter(attr=attr, call=call, **kwargs)

	def instances(self, *, attr=None, super=None, **kwargs):
		"""
		Return a dictionary of instances of classes found within the modules of this catalog
		"""
		attr = _internal.get_cls_filter(attr, super)
		call = True
		return self.filter(attr=attr, call=call, **kwargs)
