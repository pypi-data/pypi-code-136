from dataclasses import dataclass
from json import JSONDecodeError
from logging import getLogger
from typing import Tuple

from jsonschema import validate, ValidationError
import requests

class APIError(Exception):
    pass

api_logger = getLogger(__name__)

@dataclass(frozen=True)
class APIEndpoint:
    url: str
    method: str  # Valid HTTP method name
    request_schema: dict  # Schema to validate input data against
    response_schema: dict  # Schema to validate response against

    def execute(self, input_json: dict, **kwargs) -> Tuple[dict, requests.Response]:
        if __debug__:
            # Giving incorrect json as a request body is considered incorrect program.
            try:
                validate(input_json, schema=self.request_schema)
            except ValidationError as e:
                raise ValueError("Incorrect data for a given APIEndpoint") from e
        response = requests.request(
            url=self.url,
            method=self.method,
            json=input_json,
            **kwargs,
        )
        try:
            api_logger.info(f"Request on {self.url} with status: {response.status_code}")
            api_logger.debug("Response: %s", response.text)
            result = response.json()
        except JSONDecodeError as e:
            raise APIError("Response does not contain valid JSON") from e
        try:
            validate(result, schema=self.response_schema)
        except ValidationError as e:
            raise APIError("Response does not match the provided schema.") from e
        return result, response
