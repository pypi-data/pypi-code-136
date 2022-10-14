import logging, sys
from importlib import util
from makepie import makepie_load
from makepie.Config import config

from .Exceptions import MakepieException
from .Decorators import macro, get_macros
from .Utils import env
from .Makepie import main

log = logging.getLogger(__name__)

def import_from_path(name, path):
	spec = util.spec_from_file_location(name, path)
	module = util.module_from_spec(spec)
	sys.modules[name] = module
	spec.loader.exec_module(module)
	return module

def makepie():
	# Import make module containing targets
	module_path = env('MAKEPIE_MAKEFILE', './make.py')
	try:
		make = import_from_path("make", module_path)
	except ImportError as e:
		log.error(f"Cannot import module from '{module_path}': {e}")
		sys.exit(1)

	log.debug(f"Loaded user config")
	
	# Load with empty config if not already loaded by user script
	if not config("MAKEPIE_LOADED", False):
		makepie_load()

	# For each element in the make module
	for element in dir(make):
		func = getattr(make, element)
		# If the element is a function and was defined in the make module
		if type(func).__name__ == "function" \
			and func.__module__ == make.__name__:

			log.debug(f"Converting function '{func.__name__}' to macro")
			try:
				make.__dict__[element] = macro(func)
			except MakepieException as e:
				log.warning(f"Ignoring function '{func.__name__}': {e}")

	# Launch makepie
	(macros, default_macro) = get_macros()
	result = main(macros, default_macro, sys.argv)

	if isinstance(result, int):
		sys.exit(result)
	else:
		sys.exit(0)

if __name__ == '__main__':
	makepie()
