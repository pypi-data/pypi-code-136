import sys
from faker import Faker
from json import dumps

fake = Faker()


def get_system_version():
    return sys.version


def get_faker_name():
    return fake.name()


def http_response(data, status_code=422):
    return {
        "statusCode": status_code,
        "body": dumps(data),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
        },
    }
