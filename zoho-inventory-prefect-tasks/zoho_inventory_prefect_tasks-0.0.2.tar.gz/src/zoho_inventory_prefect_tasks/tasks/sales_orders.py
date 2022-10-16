from zoho_inventory_python_sdk.resources import SalesOrders

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
            sales_orders = SalesOrders()

            response = sales_orders.create(body=body, path_params=path_params, **task_kwargs)
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
            sales_orders = SalesOrders()

            response = sales_orders.list(**task_kwargs)
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
            sales_orders = SalesOrders()

            response = sales_orders.get(id_=id_, path_params=path_params, **task_kwargs)
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
            sales_orders = SalesOrders()

            response = sales_orders.update(id_=id_, body=body, path_params=path_params, **task_kwargs)
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
            raise ValueError("An object must be provided")

        try:
            sales_orders = SalesOrders()

            response = sales_orders.delete(id_=id_, path_params=path_params, **task_kwargs)
            return response
        except Exception as error:
            print(error)
            raise error


class MarkAsVoid(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, id_: str = None, path_params: dict = None, **task_kwargs: Any):

        if id_ is None:
            raise ValueError("An object must be provided")

        try:
            sales_orders = SalesOrders()

            response = sales_orders.mark_as_void(id_=id_)
            return response
        except Exception as error:
            print(error)
            raise error


class MarkAsConfirmed(Task):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @defaults_from_attrs()
    def run(self, id_: str = None, path_params: dict = None, **task_kwargs: Any):

        if id_ is None:
            raise ValueError("An object must be provided")

        try:
            sales_orders = SalesOrders()

            response = sales_orders.mark_as_confirmed(id_=id_)
            return response
        except Exception as error:
            print(error)
            raise error
