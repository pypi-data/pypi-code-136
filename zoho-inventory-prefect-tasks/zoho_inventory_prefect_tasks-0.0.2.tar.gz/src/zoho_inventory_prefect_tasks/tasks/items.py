from zoho_inventory_python_sdk.resources import Items

from prefect import Task
from prefect.utilities.tasks import defaults_from_attrs
from typing import Any


class Create(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, body: dict = None, path_params: dict = None, **task_kwargs: Any):

        if body is None:
            raise ValueError("An object must be provided")

        try:
            items = Items()

            response = items.create(body=body, path_params=path_params, **task_kwargs)
            return response
        except Exception as error:
            print(error)
            raise error


class List(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, **task_kwargs: Any):

        try:
            items = Items()

            response = items.list(**task_kwargs)
            return response
        except Exception as error:
            print(error)
            raise error


class Fetch(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, id_: str = None, path_params: dict = None, **task_kwargs: Any):

        if id_ is None:
            raise ValueError("An id must be provided")

        try:
            items = Items()

            response = items.get(id_=id_, path_params=path_params, **task_kwargs)
            return response
        except Exception as error:
            print(error)
            raise error


class Update(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, id_: str = None, body: dict = None, path_params: dict = None, **task_kwargs: Any):

        if id_ is None:
            raise ValueError("An id must be provided")

        if body is None:
            raise ValueError("An object must be provided")

        try:
            items = Items()

            response = items.update(id_=id_, body=body, path_params=path_params, **task_kwargs)
            return response
        except Exception as error:
            print(error)
            raise error


class Delete(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, id_: str = None, path_params: dict = None, **task_kwargs: Any):

        if id_ is None:
            raise ValueError("An id must be provided")

        try:
            items = Items()

            response = items.delete(id_=id_, path_params=path_params, **task_kwargs)
            return response
        except Exception as error:
            print(error)
            raise error


class MarkAsActive(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, id_: str = None):

        if id_ is None:
            raise ValueError("An id must be provided")

        try:
            items = Items()

            response = items.mark_as_active(id_=id_)
            return response
        except Exception as error:
            print(error)
            raise error


class MarkAsInactive(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, id_: str = None):

        if id_ is None:
            raise ValueError("An id must be provided")

        try:
            items = Items()

            response = items.mark_as_inactive(id_=id_)
            return response
        except Exception as error:
            print(error)
            raise error
