import importlib.metadata


try:
	__version__ = importlib.metadata.version('src')
except importlib.metadata.PackageNotFoundError:

	__version__ = None
