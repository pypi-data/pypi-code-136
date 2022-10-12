import importlib
import logging

from .. import settings
from . import base


__all__ = ["base"]


logger = logging.getLogger(__name__)


backend_module = importlib.import_module(settings.BACKEND)

try:
    Dispatcher = getattr(backend_module, "Dispatcher")
except AttributeError as exception:  # pragma: no cover
    raise ImportError(
        f'Module "{settings.BACKEND}" does not define a "Dispatcher" class.'
    ) from exception
