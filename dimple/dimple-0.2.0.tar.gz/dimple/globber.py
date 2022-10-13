import glob
import logging
import os

_logger = logging.getLogger("dimple")

class Globber:

	def iglob(self, *, path, pattern, recursive):
		_logger.debug(f"Globber.glob: path:'{path}' pattern:'{pattern}' recursive:{recursive} cwd:{os.getcwd()}")

		if path is not None and len(path):
			path     = os.path.normpath(path)
			pathname = os.path.join(path, pattern)
		else:
			pathname = pattern

		_logger.debug(f"Globber.glob: calling iglob with pathname:{pathname} recursive:{recursive} ...")
		return glob.iglob(pathname, recursive=recursive)

