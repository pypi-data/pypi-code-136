# -*- coding: utf-8 -*-
from abc import abstractproperty

from fastapi import HTTPException  # noqa


class ClassABC(type):
    def __init__(cls, name, bases, attrs):
        abstracts = set()

        for base in bases:
            abstracts.update(getattr(base, "__abstractclassmethods__", set()))

        for abstract in abstracts:
            annotation_type = bases[0].__annotations__.get(abstract)

            if not isinstance(getattr(cls, abstract), annotation_type):
                raise TypeError("Wrong type of {}".format(abstract))

            if getattr(getattr(cls, abstract), "__isabstractmethod__", False):
                raise TypeError("Your class doesn't define {}".format(abstract))

        for attr in attrs:
            if getattr(attrs[attr], "__isabstractmethod__", False):
                abstracts.add(attr)

        cls.__abstractclassmethods__ = abstracts

        super().__init__(name, bases, attrs)


class BaseHTTPException(HTTPException, metaclass=ClassABC):
    status_code: int = 400

    def __init__(
        self,
    ) -> None:
        super().__init__(status_code=self.status_code)


class DefaultHTTPException(BaseHTTPException):
    code: str = abstractproperty()
    type: str = abstractproperty()
    message: str = abstractproperty()
