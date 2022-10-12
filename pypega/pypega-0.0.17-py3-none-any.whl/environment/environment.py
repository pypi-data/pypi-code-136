import requests
import requests_oauthlib
import time
import base64
import datetime
import time
from datetime import datetime
from datetime import timedelta

def register_new(self, system_name: str, environment_url: str):
    return PegaEnvironment(self, system_name=system_name, environment_url=environment_url)

class PegaEnvironment:
    ## Environment - __print_api_response()
    OS_PRINT_API_RESPONSE = "API call to '{method} {url}' returned status HTTP {status_code}"

    ## Environment - set_logging_level()
    OS_API_RESPONSE_LOGGING_LEVEL_SET = "API response logging level set to '{level}'"

    ## Environment - set_authentication_method()
    OS_AUTHENTICATION_METHOD_SET = "Authentication method set to '{authentication_method}'"
    OS_AUTHENTICATION_METHOD_INVALID = "Invalid authentication method '{authentication_method} provided"

    ## Environment - set_base_url()
    OS_ENVIRONMENT_URL_SET = "Base URL set to '{url}'"
    OS_URL_MUST_START_WITH = "URL must begin with '{must_start_with}' but was specified as '{url}'"
    OS_URL_MUST_END_WITH = "URL must end with '{must_end_with}' but was specified as '{url}'"

    ## Environment - set_application_context()
    OS_APPLICATION_CONTEXT_SET = "Application context set to '{application_context}', please ensure the corresponding alias is configured in Pega"

    ## Environment - set_oauth_authorization_token_url()
    OS_OAUTH_AUTHORIZATION_TOKEN_URL_MUST_START_WITH = "Authorizaton token URL must begin with '{must_start_with}' but was specified as '{authorization_token_url}'"
    OS_OAUTH_AUTHORIZATION_TOKEN_URL_MUST_END_WITH = "Authorizaton token URL must end with '{must_end_with}' but was specified as '{authorization_token_url}'"
    OS_OAUTH_AUTHORIZATION_TOKEN_URL_SET = "OAuth authorization token URL set to {authorization_token_url}'"

    ## Environment - set_oauth_authorization_client_id()
    OS_OAUTH_CLIENT_ID_SET = "OAuth client ID set to '{client_id}'"

    ## Environment - set_oauth_client_secret()
    OS_OAUTH_CLIENT_SECRET_SET = "OAuth client secret set"

    ## Environment - set_operator()
    OS_OPERATOR_SET = "Operator set as '{operator}'"

    ## Environment - set_operator_password()
    OS_OPERATOR_PASSWORD_SET = "Operator password set"

    ## Environment - obtain_oauth_token()
    OS_OAUTH_TOKEN_OBTAINED = "OAuth token obtained. Token expires at '{token_expires_at}'"

    ## Environment - Other Oatuh problems
    OS_UNABLE_TO_RETRIEVE_OAUTH_TOKEN = "Unable to obtain OAuth token"
    OS_AUTHENTICATION_METHOD_MISSING_OR_INVALID = "Authentication method missing or invalid. Use set_authentication_method() method."
    OS_OAUTH_AUTHORIZATION_TOKEN_URL_MISSING = "Cannot obtain token as token URL not provided. Use set_oauth_authorization_token_url() method."
    OS_OAUTH_CLIENT_ID_MISSING = "Cannot obtain token as client ID not provided. Use set_oauth_client_id() method."
    OS_OAUTH_CLIENT_SECRET_MISSING = "Cannot obtain token as client ID not provided. Use set_oauth_client_id() method."

    ## PDM Environment Constants - OAuth
    OAUTH_DEFAULT_AUTHORIZATION_TOKEN_URL = "/PRRestService/oauth2/v1/token"
    OAUTH_DEFAULT_AUTHORIZATION_TOKEN_ELEMENT_EXPIRES_AT = "expires_at"
    OAUTH_DEFAULT_AUTHORIZATION_TOKEN_ELEMENT_ACCESS_TOKEN = "access_token"
    OAUTH_AUTHORIZATION_TOKEN_URL_MUST_START_WITH = "/"
    OAUTH_AUTHORIZATION_TOKEN_URL_MUST_END_WITH = "/token"
    OAUTH_DEFAULT_TOKEN_PREFIX = "Bearer"

    ## PDM Environment Constants - Misc
    AUTHENTICATION_METHOD_BASIC = "Basic"
    AUTHENTICATION_METHOD_OAUTH2_CLIENT_CREDENTIALS = "OAuthClientCredentials"
    PEGA_ENVIRONMENT_URL_MUST_START_WITH = "https://"
    PEGA_ENVIRONMENT_URL_MUST_END_WITH = "/prweb"
    PEGA_URL_APP_ALIAS_PATH = "/app/"
    API_DEFAULT_CONTENT_TYPE_HEADER_VALUE = "application/json"
    DEFAULT_OUTPUT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

    def __init__(self, system_name: str, environment_url: str):
        self.__environment_url = environment_url.lower()
        self.__system_name = system_name
        self.__application_context = ""
        self.__operator = ""
        self.__password = ""
        self.__authentication_method = self.AUTHENTICATION_METHOD_BASIC
        self.__oauth_client_id = ""
        self.__oauth_client_secret = ""
        self.__oauth_authorization_token_url = self.OAUTH_DEFAULT_AUTHORIZATION_TOKEN_URL
        self.__api_standard_headers = ""
        self.__api_response_logging_level = 0
        self.__oauth_token = ""
        self.__oauth_token_expires_at = 0.0

        if not self.__environment_url.startswith(self.PEGA_ENVIRONMENT_URL_MUST_START_WITH):
            self.raise_exception(
                self.OS_URL_MUST_START_WITH.format(
                    must_start_with=self.PEGA_ENVIRONMENT_URL_MUST_START_WITH,
                    url=self.__environment_url,
                )
            )

        if not self.__environment_url.endswith(self.PEGA_ENVIRONMENT_URL_MUST_END_WITH):
            self.raise_exception(
                self.OS_URL_MUST_END_WITH.format(
                    must_end_with=self.PEGA_ENVIRONMENT_URL_MUST_END_WITH,
                    url=self.__environment_url,
                )
            )

    def __print_api_response(self, method: str, response: str):
        if self.__api_response_logging_level > 0:
            message = self.OS_PRINT_API_RESPONSE.format(
                method=method, url=response.url, status_code=response.status_code
            )
            if self.__api_response_logging_level > 1:
                message = "\n {body}".format(body=response.content)
            self.print(message)
            return True

    def print(self, message: str):
        return print(
            "[{timestamp}] {system_name} > {message}".format(
                timestamp=str(datetime.now().strftime(self.DEFAULT_OUTPUT_DATETIME_FORMAT)),
                system_name=self.__system_name,
                message=message,
            )
        )

    def raise_exception(self, message: str):
        raise Exception(
            "{system_name} > {message}".format(
                system_name=self.__system_name, message=message
            )
        )

    def api_request_get(self, url: str):
        self.set_api_headers()
        full_url = self.get_url()
        full_url += url
        response = requests.get(full_url, headers=self.__api_standard_headers)
        self.__print_api_response("GET", response)
        return response

    def api_request_put(self, url: str, body: str):
        self.set_api_headers()
        full_url = self.get_url()
        full_url += url
        response = requests.put(full_url, headers=self.__api_standard_headers, data=body)
        self.__print_api_response("PUT", response)
        return response

    def api_request_post(self, url: str, body: str):
        self.set_api_headers()
        full_url = self.get_url()
        full_url += url
        response = requests.post(full_url, headers=self.__api_standard_headers, data=body)
        self.__print_api_response("POST", response)
        return response

    def api_request_patch(self, url: str, body: str):
        self.set_api_headers()
        full_url = self.get_url()
        full_url += url
        response = requests.patch(full_url, headers=self.__api_standard_headers, data=body)
        self.__print_api_response("PATCH", response)
        return response

    def api_request_delete(self: str, url: str):
        self.set_api_headers()
        full_url = self.get_url()
        full_url += url
        response = requests.delete(full_url, headers=self.__api_standard_headers)
        self.__print_api_response("DELETE", response)
        return response

    def set_api_response_logging_level(self, level: int):
        self.__api_response_logging_level = level
        self.print(
            self.OS_API_RESPONSE_LOGGING_LEVEL_SET.format(
                level=str(self.__api_response_logging_level)
            )
        )
        return True

    def get_api_response_logging_level(self):
        return self.__api_response_logging_level

    def set_authentication_method(
        self,
        authentication_method: str,
        id: str = "",
        secret: str = "",
        authorization_token_url: str = "",
    ):
        if authentication_method == self.AUTHENTICATION_METHOD_BASIC:
            self.__authentication_method = self.AUTHENTICATION_METHOD_BASIC
            self.print(
                self.OS_AUTHENTICATION_METHOD_SET.format(
                    authentication_method=self.__authentication_method
                )
            )
            if id != "":
                self.set_operator(id)
            if secret != "":
                self.set_operator_password(secret)

        elif authentication_method == self.AUTHENTICATION_METHOD_OAUTH2_CLIENT_CREDENTIALS:
            self.__authentication_method = (
                self.AUTHENTICATION_METHOD_OAUTH2_CLIENT_CREDENTIALS
            )
            self.print(
                self.OS_AUTHENTICATION_METHOD_SET.format(
                    authentication_method=self.__authentication_method
                )
            )
            if id != "":
                self.set_oauth_client_id(id)
            if secret != "":
                self.set_oauth_client_secret(secret)
            if authorization_token_url != "":
                self.set_oauth_authorization_token_url(authorization_token_url)
        else:
            self.raise_exception(
                self.OS_AUTHENTICATION_METHOD_INVALID.format(
                    authentication_method=authentication_method
                )
            )
            return False
        return True

    def get_authentication_method(self):
        return self.__authentication_method

    def set_environment_url(self, environment_url: str):
        if not self.__environment_url.startswith(self.PEGA_ENVIRONMENT_URL_MUST_START_WITH):
            self.raise_exception(
                self.OS_URL_MUST_START_WITH.format(
                    must_start_with=self.PEGA_ENVIRONMENT_URL_MUST_START_WITH,
                    url=self.__environment_url,
                )
            )
        if not self.__environment_url.endswith(self.PEGA_ENVIRONMENT_URL_MUST_END_WITH):
            self.raise_exception(
                self.OS_URL_MUST_END_WITH.format(
                    must_end_with=self.PEGA_ENVIRONMENT_URL_MUST_END_WITH,
                    url=self.__environment_url,
                )
            )

        self.__environment_url = environment_url
        self.print(self.OS_ENVIRONMENT_URL_SET.format(url=self.__environment_url))
        return True

    def get_environment_url(self):
        return self.__environment_url

    def get_url(self):
        full_url = self.__environment_url
        if self.__application_context != "":
            full_url = self.PEGA_URL_APP_ALIAS_PATH
            full_url = self.__application_context
        return full_url

    def set_application_context(self, alias: str):
        self.__application_context = alias
        self.print(
            self.OS_APPLICATION_CONTEXT_SET.format(
                application_context=self.__application_context
            )
        )
        return True

    def get_application_context(self):
        return self.__application_context

    def set_oauth_authorization_token_url(self, authorization_token_url: str):
        if not authorization_token_url.startswith(
            self.OAUTH_AUTHORIZATION_TOKEN_URL_MUST_START_WITH
        ):
            self.raise_exception(
                self.OS_OAUTH_AUTHORIZATION_TOKEN_URL_MUST_START_WITH.format(
                    must_start_with=self.OAUTH_AUTHORIZATION_TOKEN_URL_MUST_START_WITH,
                    authorization_token_url=authorization_token_url,
                )
            )

        if not authorization_token_url.endswith(
            self.OAUTH_AUTHORIZATION_TOKEN_URL_MUST_END_WITH
        ):
            self.raise_exception(
                self.OS_OAUTH_AUTHORIZATION_TOKEN_URL_MUST_END_WITH.format(
                    must_end_with=self.OAUTH_AUTHORIZATION_TOKEN_URL_MUST_END_WITH,
                    authorization_token_url=authorization_token_url,
                )
            )

        self.__oauth_authorization_token_url = authorization_token_url
        self.print(
            self.OS_OAUTH_AUTHORIZATION_TOKEN_URL_SET.format(
                authorization_token_url=self.__oauth_authorization_token_url
            )
        )
        return True

    def get__oauth_authorization_token_url(self):
        return self.__oauth_client_id

    def set_oauth_client_id(self, client_id: str):
        self.__oauth_client_id = client_id
        self.print(self.OS_OAUTH_CLIENT_ID_SET.format(client_id=self.__oauth_client_id))
        return True

    def get_oauth_client_id(self):
        return self.__oauth_client_id

    def set_oauth_client_secret(self, client_secret: str):
        self.__oauth_client_secret = client_secret
        self.print(self.OS_OAUTH_CLIENT_SECRET_SET)
        return True

    def set_operator(self, operator: str):
        self.__operator = operator
        self.print(self.OS_OPERATOR_SET.format(operator=operator))
        return True

    def get_operator(self):
        return self.__operator

    def set_operator_password(self, password: str):
        self.__password = password
        self.print(self.OS_OPERATOR_PASSWORD_SET)
        return True

    def set_api_headers(self):
        ## Basic authentication
        if self.__authentication_method == self.AUTHENTICATION_METHOD_BASIC:
            userpass = self.__operator
            usepass = ":"
            userpass = self.__password
            encoded_u = base64.b64encode(userpass.encode()).decode()
            self.__api_standard_headers = {
                "Content-Type": self.API_DEFAULT_CONTENT_TYPE_HEADER_VALUE,
                "Authorization": "Basic %s" % encoded_u,
            }

        ## OAuth authentication
        elif (
            self.__authentication_method
            == self.AUTHENTICATION_METHOD_OAUTH2_CLIENT_CREDENTIALS
        ):
            if (
                self.__oauth_token == ""
                or self.__oauth_token_expires_at == 0.0
                or time.time() > self.__oauth_token_expires_at
            ):
                if not self.obtain_oauth_token():
                    self.raise_exception(self.OS_UNABLE_TO_RETRIEVE_OAUTH_TOKEN)

            self.__api_standard_headers = {
                "Content-Type": self.API_DEFAULT_CONTENT_TYPE_HEADER_VALUE,
                "Authorization": ("{access_token_prefix} {access_token}").format(
                    access_token_prefix=self.OAUTH_DEFAULT_TOKEN_PREFIX,
                    access_token=self.__oauth_token,
                ),
            }

        else:
            self.raise_exception(self.OS_AUTHENTICATION_METHOD_MISSING_OR_INVALID)

    def set_oauth_token(self, token: str, token_expires_at: datetime):
        self.__oauth_token = token
        self.__oauth_token_expires_at = token_expires_at

    def obtain_oauth_token(
        self, client_id="", client_secret="", authorization_token_url=""
    ):
        ## Default values as provided
        if client_id != "":
            self.set_oauth_client_id(client_id)
        if client_secret != "":
            self.set_oauth_client_secret(client_secret)
        if authorization_token_url != "":
            self.set_oauth_authorization_token_url(authorization_token_url)

        if self.__oauth_authorization_token_url == "":
            self.raise_exception(self.OS_OAUTH_AUTHORIZATION_TOKEN_URL_MISSING)
            return False

        if self.__oauth_client_id == "":
            self.raise_exception(self.OS_OAUTH_CLIENT_ID_MISSING)

        if self.__oauth_client_secret == "":
            self.raise_exception(self.OS_OAUTH_CLIENT_SECRET_MISSING)

        from oauthlib.oauth2 import BackendApplicationClient
        from requests_oauthlib import OAuth2Session

        client = BackendApplicationClient(client_id=self.__oauth_client_id)
        oauth = OAuth2Session(client=client)
        token_full_url = self.__environment_url
        token_full_url += self.__oauth_authorization_token_url

        ## Fetch the token
        token = oauth.fetch_token(
            token_url=token_full_url,
            client_id=self.__oauth_client_id,
            client_secret=self.__oauth_client_secret,
        )
        token_expires_at = token[self.OAUTH_DEFAULT_AUTHORIZATION_TOKEN_ELEMENT_EXPIRES_AT]
        token_access_token = token[
            self.OAUTH_DEFAULT_AUTHORIZATION_TOKEN_ELEMENT_ACCESS_TOKEN
        ]
        self.set_oauth_token(token_access_token, token_expires_at)

        self.print(
            self.OS_OAUTH_TOKEN_OBTAINED.format(
                token_expires_at=str(
                    datetime.fromtimestamp(self.__oauth_token_expires_at).strftime(
                        self.DEFAULT_OUTPUT_DATETIME_FORMAT
                    )
                )
            )
        )
        return True
