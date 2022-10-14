import inspect
import json
import os
import traceback

import bson
from fastapi import status
from fastapi.responses import Response
from humps.main import camelize
from mongoengine import Document, QuerySet, DateTimeField, ObjectIdField, ReferenceField
from mongoengine.base import BaseField
from pydantic import BaseModel

from hautils.logger import logger
from hautils.slack import slack_notify


def to_camel_case(snake_str: dict):
    """
    The to_camel_case function takes a dictionary and converts all keys to camelCase.
    For example, if the input is:
        {'a_key': 'a value', 'another_key': ['list', 'of', 'values']}
    then the output will be:
        {'aKey': 'a value', anotherKey: ['list', of, values]}

    :param snake_str:dict: Pass the dictionary that is being converted to camel case
    :return: A dictionary with all keys converted to camel case
    :doc-author: Trelent
    """
    """
    The to_camel_case function takes a dictionary and converts all keys to camelCase.
    For example, if the input is:
        {'a_key': 'a value', 'another_key': ['list', 'of', 'values']}
    then the output will be:
        {'aKey': 'a value', anotherKey: ['list', of, values]}
    
    :param snake_str:dict: Pass the dictionary that is being converted to camel case
    :return: A dictionary with all keys converted to camel case
    :doc-author: Trelent
    """
    for k, v in list(snake_str.items()):
        if type(v) is dict:
            snake_str[camelize(k)] = to_camel_case(v)
        elif type(v) is list:
            snake_str[camelize(k)] = [to_camel_case(x) for x in v if type(x) is dict]
            snake_str[camelize(k)] = [x for x in v if type(x) is not dict]
        else:
            snake_str[camelize(k)] = v
        if camelize(k) != k:
            snake_str.pop(k)

    return snake_str


class UnsupportedContentType(Exception):
    """
    The UnsupportedContentType exception is raised when the content type is not supported.
    """

    def __init__(self, message, content=None):
        logger.warn(f"unsupported object type {type(content)} ")
        self.message = message
        self.content = content
        super().__init__(self.message)


class ErrorFilteringData(Exception):
    """
    The ErrorFilteringData exception is raised when there is an error filtering data.
    """

    def __init__(self, e: Exception, message, field: BaseField):
        logger.error(f"error handling sensitive field {field.name}")
        logger.debug(f"object dump of error field: {inspect.getmembers(field)}")
        self.message = message
        self.field = field
        self.exception = e
        super().__init__(self.message, self.exception, self.field)


def mongo_to_dict(content) -> dict:
    """
    The mongo_to_dict function takes a MongoDB object and returns a dictionary.
    It also removes the _id field from the returned dictionary, as it is not serializable.

    :param content: Determine the type of object to be transformed
    :return: The dictionary representation of the content
    :doc-author: Trelent
    """
    if not issubclass(type(content), Document) and not issubclass(type(content), dict) and not issubclass(type(content),
                                                                                                          BaseModel):
        raise UnsupportedContentType("unsupported object type", content)
    if issubclass(type(content), Document):
        content.reload()  # so that data will reflect the type in the db field
        response_object = json.loads(content.to_json())
        response_object["id"] = str(content.id)
        response_object.pop("_id")
        response_object = filter_and_transform(content, response_object)
    elif issubclass(type(content), BaseModel):
        response_object = content.dict()
    else:
        logger.debug(f"format type {type(content)}")
        response_object = content

    response_object = to_camel_case(response_object)

    return response_object


transformers = [
    (DateTimeField, int, "timestamp"),
    (ReferenceField, mongo_to_dict),
    (ObjectIdField, str),
    (bson.objectid.ObjectId, str),
]


def transform(field, content, response_object):
    """
    The transform function takes a field and a content object and transforms the field based on the transformers list.


    :param field: Determine the field that is being transformed
    :param content: Get the content object from the response
    :param response_object: Store the transformed field
    :return: The transformed response object
    :doc-author: Trelent
    """
    """
    The transform function takes a field and a content object and transforms the field based on the transformers list.
    :param field:
    :param content:
    :param response_object:
    """
    if hasattr(field, 'sensitive') and field.sensitive and field.name in response_object:
        response_object.pop(field.name)
        return response_object
    for transformer in transformers:
        logger.debug(f"matching {type(field)} to {transformer[0]}")
        if not isinstance(field, transformer[0]) or content[field.name] is None:
            continue
        if len(transformer) == 3:
            callable(pipe := content[field.name].__getattribute__(transformer[2]))
        else:
            pipe = None
        if type(transformer[1]) == type:
            response_object[field.name] = transformer[1](content[field.name]) if pipe is None else transformer[1](
                pipe())

        if inspect.isfunction(transformer[1]):
            if pipe is None:
                response_object[field.name] = transformer[1](content[field.name])
            else:
                response_object[field.name] = transformer[1](pipe(content[field.name]))
    return response_object


def filter_and_transform(content, response_object):
    """
    The filter_and_transform function takes a Mongoengine Document object and returns a dictionary.
    The function will iterate through the fields of the document, filtering out any that are not defined in
    the schema. It will also transform any datetime objects into Unix timestamps.

    :param content: Get the data from the database
    :param response_object: Store the transformed data
    :return: The response_object that is passed in
    :doc-author: Trelent
    """
    """

    :param content: 
    :param response_object: 
    :return: 
    """
    for field in content._fields.values():
        try:
            response_object = transform(field, content, response_object)
        except Exception as e:
            raise ErrorFilteringData(e, "error filtering data", field)
    return response_object


# DeprecationWarning("pop fields in this function will not be supported in the future")
def json_response(content=None, dict_content: dict = None, http_status=200, pop_fields=None):
    """
    The json_response function is a helper function that takes in an object and returns a Response
    object with the appropriate content-type header.  It also populates the response body with json encoded
    data, which can be either a list or dictionary.  The function will also accept QuerySets as input, but it will
    convert them to lists before encoding.

    :param content:
    :param dict_content:dict=None: Pass in a dictionary that will be encoded into json
    :return: A json encoded response
    :doc-author: Trelent
    """
    if pop_fields is None:
        pop_fields = {}
    try:
        if issubclass(type(content), QuerySet) or issubclass(type(content), list):
            response = [doc_cleanup(doc, pop_fields) for doc in content]
        else:
            response = doc_cleanup(content if content is not None else dict_content, pop_fields)
        logger.debug(f"json dumping type {type(response)}")
        response = json.dumps(response)
        logger.info(f"json encode {response}")
        return Response(content=response, status_code=http_status, media_type="application/json")
    except Exception as e:
        exception_log(e)


def deprecated(args):
    """

    :param args:
    """
    print("this function is deprecated, use the sensitive attribute")


def doc_cleanup(doc, pop_fields):
    """

    :param doc:
    :param pop_fields:
    :return:
    """
    response = mongo_to_dict(doc)
    for field in pop_fields:
        try:
            response.pop(field)
        except Exception as e:
            logger.error(f"field {field} not in dictionary")
    return response


def mongo_to_log(content):
    try:
        return json.dumps(mongo_to_dict(content))
    except Exception as e:
        return ""


def exception_log(e):
    logger.error(e)
    traceback_log = traceback.format_exception(type(e), e, e.__traceback__)
    logger.debug(traceback_log)
    formatted_message = """# Exception 
```
{}
```
""".format(traceback_log, os.getenv("APP_PREFIX"))
    slack_notify(message=formatted_message)
    raise ProcessException(http_status=status.HTTP_500_INTERNAL_SERVER_ERROR, errors={"error": str(type(e))})


class ProcessException(Exception):
    def __init__(self, errors=None, data=None, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR):
        if data is None:
            data = {}
        self.errors = errors
        self.data = data
        self.status = http_status
