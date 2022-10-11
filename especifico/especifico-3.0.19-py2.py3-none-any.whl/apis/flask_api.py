"""
This module defines a Flask Especifico API which implements translations between Flask and
Especifico requests / responses.
"""

import logging
import pathlib
from typing import Any, Dict
import warnings

import flask
import werkzeug.exceptions
from werkzeug.local import LocalProxy

from especifico.apis import flask_utils
from especifico.apis.abstract import AbstractAPI
from especifico.handlers import AuthErrorHandler
from especifico.jsonifier import Jsonifier
from especifico.lifecycle import EspecificoRequest, EspecificoResponse
from especifico.security import FlaskSecurityHandlerFactory
from especifico.utils import is_json_mimetype, yamldumper

logger = logging.getLogger("especifico.apis.flask_api")


class FlaskApi(AbstractAPI):
    @staticmethod
    def make_security_handler_factory(pass_context_arg_name):
        """Create default SecurityHandlerFactory to create all security check handlers"""
        return FlaskSecurityHandlerFactory(pass_context_arg_name)

    def _set_base_path(self, base_path):
        super()._set_base_path(base_path)
        self._set_blueprint()

    def _set_blueprint(self):
        logger.debug("Creating API blueprint: %s", self.base_path)
        endpoint = flask_utils.flaskify_endpoint(self.base_path)
        self.blueprint = flask.Blueprint(
            endpoint,
            __name__,
            url_prefix=self.base_path,
            template_folder=str(self.options.openapi_console_ui_from_dir),
        )

    def add_openapi_json(self):
        """
        Adds spec json to {base_path}/swagger.json
        or {base_path}/openapi.json (for oas3)
        """
        logger.debug("Adding spec json: %s/%s", self.base_path, self.options.openapi_spec_path)
        endpoint_name = f"{self.blueprint.name}_openapi_json"

        self.blueprint.add_url_rule(
            self.options.openapi_spec_path, endpoint_name, self._handlers.get_json_spec,
        )

    def add_openapi_yaml(self):
        """
        Adds spec yaml to {base_path}/swagger.yaml
        or {base_path}/openapi.yaml (for oas3)
        """
        if not self.options.openapi_spec_path.endswith("json"):
            return

        openapi_spec_path_yaml = self.options.openapi_spec_path[: -len("json")] + "yaml"
        logger.debug("Adding spec yaml: %s/%s", self.base_path, openapi_spec_path_yaml)
        endpoint_name = f"{self.blueprint.name}_openapi_yaml"
        self.blueprint.add_url_rule(
            openapi_spec_path_yaml, endpoint_name, self._handlers.get_yaml_spec,
        )

    def add_swagger_ui(self):
        """
        Adds swagger ui to {base_path}/ui/
        """
        console_ui_path = self.options.openapi_console_ui_path.strip("/")
        logger.debug("Adding swagger-ui: %s/%s/", self.base_path, console_ui_path)

        if self.options.openapi_console_ui_config is not None:
            config_endpoint_name = f"{self.blueprint.name}_swagger_ui_config"
            config_file_url = f"/{console_ui_path}/swagger-ui-config.json"

            self.blueprint.add_url_rule(
                config_file_url,
                config_endpoint_name,
                lambda: flask.jsonify(self.options.openapi_console_ui_config),
            )

        static_endpoint_name = f"{self.blueprint.name}_swagger_ui_static"
        static_files_url = f"/{console_ui_path}/<path:filename>"

        self.blueprint.add_url_rule(
            static_files_url,
            static_endpoint_name,
            self._handlers.console_ui_static_files,
        )

        index_endpoint_name = f"{self.blueprint.name}_swagger_ui_index"
        console_ui_url = f"/{console_ui_path}/"

        self.blueprint.add_url_rule(
            console_ui_url, index_endpoint_name, self._handlers.console_ui_home,
        )

    def add_auth_on_not_found(self, security, security_definitions):
        """
        Adds a 404 error handler to authenticate and only expose the 404 status if the security
        validation pass.
        """
        logger.debug("Adding path not found authentication")
        not_found_error = AuthErrorHandler(
            self,
            werkzeug.exceptions.NotFound(),
            security=security,
            security_definitions=security_definitions,
        )
        endpoint_name = f"{self.blueprint.name}_not_found"
        self.blueprint.add_url_rule(
            "/<path:invalid_path>", endpoint_name, not_found_error.function,
        )

    def _add_operation_internal(self, method, path, operation):
        operation_id = operation.operation_id
        logger.debug("... Adding %s -> %s", method.upper(), operation_id, extra=vars(operation))

        flask_path = flask_utils.flaskify_path(path, operation.get_path_parameter_types())
        endpoint_name = flask_utils.flaskify_endpoint(
            operation.operation_id, operation.randomize_endpoint,
        )
        function = operation.function
        self.blueprint.add_url_rule(flask_path, endpoint_name, function, methods=[method])

    @property
    def _handlers(self):
        # type: () -> InternalHandlers
        if not hasattr(self, "_internal_handlers"):
            self._internal_handlers = InternalHandlers(
                self.base_path, self.options, self.specification,
            )
        return self._internal_handlers

    @classmethod
    def get_response(cls, response, mimetype=None, request=None):
        """Gets EspecificoResponse instance for the operation handler
        result. Status Code and Headers for response.  If only body
        data is returned by the endpoint function, then the status
        code will be set to 200 and no headers will be added.

        If the returned object is a flask.Response then it will just
        pass the information needed to recreate it.

        :type response: flask.Response | (flask.Response,) | (flask.Response, int) | (flask.Response, dict) | (flask.Response, int, dict)
        :rtype: EspecificoResponse
        """  # noqa
        return cls._get_response(
            response, mimetype=mimetype, extra_context={"url": flask.request.url},
        )

    @classmethod
    def _is_framework_response(cls, response):
        """Return True if provided response is a framework type"""
        return flask_utils.is_flask_response(response)

    @classmethod
    def _framework_to_especifico_response(cls, response, mimetype):
        """Cast framework response class to EspecificoResponse used for schema validation"""
        return EspecificoResponse(
            status_code=response.status_code,
            mimetype=response.mimetype,
            content_type=response.content_type,
            headers=response.headers,
            body=response.get_data() if not response.direct_passthrough else None,
            is_streamed=response.is_streamed,
        )

    @classmethod
    def _especifico_to_framework_response(cls, response, mimetype, extra_context=None):
        """Cast EspecificoResponse to framework response class"""
        flask_response = cls._build_response(
            mimetype=response.mimetype or mimetype,
            content_type=response.content_type,
            headers=response.headers,
            status_code=response.status_code,
            data=response.body,
            extra_context=extra_context,
        )

        return flask_response

    @classmethod
    def _build_response(
        cls,
        mimetype,
        content_type=None,
        headers=None,
        status_code=None,
        data=None,
        extra_context=None,
    ):
        if cls._is_framework_response(data):
            return flask.current_app.make_response((data, status_code, headers))

        data, status_code, serialized_mimetype = cls._prepare_body_and_status_code(
            data=data,
            mimetype=mimetype,
            status_code=status_code,
            extra_context=extra_context,
        )

        kwargs = {
            "mimetype": mimetype or serialized_mimetype,
            "content_type": content_type,
            "headers": headers,
            "response": data,
            "status": status_code,
        }
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return flask.current_app.response_class(**kwargs)

    @classmethod
    def _serialize_data(cls, data, mimetype):
        # TODO: harmonize flask and aiohttp serialization when mimetype=None or mimetype is not JSON  # noqa
        #       (cases where it might not make sense to jsonify the data)
        if isinstance(mimetype, str) and is_json_mimetype(mimetype):
            body = cls.jsonifier.dumps(data)
        elif not (isinstance(data, bytes) or isinstance(data, str)):
            warnings.warn(
                "Implicit (flask) JSON serialization will change in the next major version. "
                "This is triggered because a response body is being serialized as JSON "
                "even though the mimetype is not a JSON type. "
                "This will be replaced by something that is mimetype-specific and may "
                "raise an error instead of silently converting everything to JSON. "
                "Please make sure to specify media/mime types in your specs.",
                FutureWarning,  # a Deprecation targeted at application users.
            )
            body = cls.jsonifier.dumps(data)
        else:
            body = data

        return body, mimetype

    @classmethod
    def get_request(cls, *args: Any, **params: Any) -> EspecificoRequest:
        """Gets EspecificoRequest instance for the operation handler
        result. Status Code and Headers for response.  If only body
        data is returned by the endpoint function, then the status
        code will be set to 200 and no headers will be added.

        If the returned object is a flask.Response then it will just
        pass the information needed to recreate it.

        :rtype: EspecificoRequest
        """
        context_dict = {}  # type: Dict[str, Any]
        flask._request_ctx_stack.top.especifico_context = context_dict
        flask_request = flask.request
        request = EspecificoRequest(
            flask_request.url,
            flask_request.method,
            headers=flask_request.headers,
            form=flask_request.form,
            query=flask_request.args,
            body=flask_request.get_data(),
            json_getter=lambda: flask_request.get_json(silent=True),
            files=flask_request.files,
            path_params=params,
            context=context_dict,
            cookies=flask_request.cookies,
        )
        logger.debug(
            "Getting data and status code",
            extra={
                "data": request.body,
                "data_type": type(request.body),
                "url": request.url,
            },
        )
        return request

    @classmethod
    def _set_jsonifier(cls):
        """
        Use Flask specific JSON loader
        """
        cls.jsonifier = Jsonifier(flask.json, indent=2)


def _get_context():
    return flask._request_ctx_stack.top.especifico_context


context = LocalProxy(_get_context)


class InternalHandlers:
    """
    Flask handlers for internally registered endpoints.
    """

    def __init__(self, base_path, options, specification):
        self.base_path = base_path
        self.options = options
        self.specification = specification

    def console_ui_home(self):
        """
        Home page of the OpenAPI Console UI.

        :return:
        """
        escaped = flask_utils.flaskify_endpoint(self.base_path)
        openapi_json_route_name = f"{escaped}.{escaped}_openapi_json"
        template_variables = {
            "openapi_spec_url": flask.url_for(openapi_json_route_name),
            **self.options.openapi_console_ui_index_template_variables,
        }
        if self.options.openapi_console_ui_config is not None:
            template_variables["configUrl"] = "swagger-ui-config.json"

        # Use `render_template_string` instead of `render_template` to circumvent the flask
        # template lookup mechanism and explicitly render the template of the current blueprint.
        # https://github.com/zalando/especifico/issues/1289#issuecomment-884105076
        template_dir = pathlib.Path(self.options.openapi_console_ui_from_dir)
        index_path = template_dir / "index.j2"
        return flask.render_template_string(index_path.read_text(), **template_variables)

    def console_ui_static_files(self, filename):
        """
        Servers the static files for the OpenAPI Console UI.

        :param filename: Requested file contents.
        :return:
        """
        # convert PosixPath to str
        static_dir = str(self.options.openapi_console_ui_from_dir)
        return flask.send_from_directory(static_dir, filename)

    def get_json_spec(self):
        return flask.jsonify(self._spec_for_prefix())

    def get_yaml_spec(self):
        return yamldumper(self._spec_for_prefix()), 200, {"Content-Type": "text/yaml"}

    def _spec_for_prefix(self):
        """
        Modify base_path in the spec based on incoming url
        This fixes problems with reverse proxies changing the path.
        """
        base_path = flask.url_for(flask.request.endpoint).rsplit("/", 1)[0]
        return self.specification.with_base_path(base_path).raw
