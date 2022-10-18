from .settings import Settings
from six import string_types
import requests

class Validate:
    def __init__(self, id="Development"):
       self._id = id
