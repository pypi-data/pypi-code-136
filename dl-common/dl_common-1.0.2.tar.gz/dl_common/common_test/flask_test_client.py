import typing as t
from flask.testing import FlaskClient


class DL_TestClientWithWorkpsaceHeaders(FlaskClient):
    def open(self, *args: t.Any, **kwargs: t.Any):
        self.add_workspace_name_as_request_headers_in_kwargs(kwargs=kwargs)
        return super().open(*args,  **kwargs)

    def add_workspace_name_as_request_headers_in_kwargs(self, kwargs: dict):
        request_headers = kwargs.get("headers", {})
        request_headers.update({"x-workspace-name": "some workspace"})
        kwargs['headers'] = request_headers
        return kwargs
