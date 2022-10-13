from typing import Callable, List, Union
import graphene
from django.core.validators import validate_email


Validator = Callable[[any], any]


def createValidScalar(
    scalar_name, validator: Validator
) -> Callable[[graphene.String], None]:
    def validate(value: str) -> None:
        return validator(value)

    return type(scalar_name, (graphene.String,), {"serialize": staticmethod(validate)})


class Email(graphene.String):
    @staticmethod
    def serialize(self, value):  #
        validate_email(value=value)
        return str(value)

    @staticmethod
    def parse_literal(node):
        return node.value

    @staticmethod
    def parse_value(value):
        return value
