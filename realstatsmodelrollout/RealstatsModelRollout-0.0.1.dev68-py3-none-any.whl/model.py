from .settings import Settings
from six import string_types
import requests

class Model:
    def __init__(self, id="Development"):
        self._id = id
        self._model_port = "8000"
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

    def Info_request(self):
        response = ""
        try:
            response = requests.get(url=self._modelURL + ':' + self._model_port + "/info")
        except:
            return Exception("Not able to get data from URL please check if model is running or online")
        return response

    def Predict_request(self, json_data=''):
        response = ""
        try:
            response = requests.post(url=self._modelURL + ':' + self._model_port + "/predict", json=json_data)
        except:
            return Exception("Not able to get data from URL please check if model is running or online")
        return response

    def Custom_request(self, request_type="", pathing="", json_data='Development'):
        request_type = request_type.lower()
        response = ""
        match request_type:
            case "post":
                response = requests.post(url=self._modelURL + ':' + self._model_port + "/" + pathing, json=json_data)
                return response
            case "put":
                response = requests.put(url=self._modelURL + ':' + self._model_port + "/" + pathing, json=json_data)
                return response
            case "get":
                response = requests.get(url=self._modelURL + ':' + self._model_port + "/" + pathing)
                return response
            case "_":
                return Exception("Request type not found please the following: get, put, post")