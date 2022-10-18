from .settings import Settings
from six import string_types
import requests

class Validate:
    def __init__(self, id="Development"):
       self._id = id
       self. = "8000"
       self._modelURL = "127.0.0.1"

    ### Port that is being used by the virtual env ###
    @property
    def Model_port(self):
        """
        :type: string
        """
        return self._model_port

    @Model_port.setter
    def Model_port(self, value):
        """
        :type: string
        """
        if isinstance(value, string_types):
            self._model_port = value
        else:
            raise Exception("Value must be string")

    ### URL to model ###
    @property
    def Model_URL(self):
        """
        :type: string
        """
        return self._modelURL

    @Model_URL.setter
    def Model_URL(self, value):
        """
        :type: string
        """
        if isinstance(value, string_types):
            self._modelURL = value
        else:
            raise Exception("Value must be string")

