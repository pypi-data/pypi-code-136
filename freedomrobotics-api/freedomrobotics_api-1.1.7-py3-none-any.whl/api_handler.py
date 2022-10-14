import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import ConnectTimeout, ReadTimeout

from freedomrobotics_api.credentials import credentials_exist, get_credentials, URLS, DEFAULT_URL

default_api = None


def set_default_api(api):
    global default_api
    default_api = api


def api_auth(token, secret, url=DEFAULT_URL):
    global default_api
    default_api = APIHandler.get_instance(token=token, secret=secret, url=url)


def api_call(*args, **kwargs):
    global default_api
    return default_api.call(*args, **kwargs)


def get_url(url=None, env=None, credentials=None):
    """Selects the correct url looking at the available ones.
    The priority order is:
    1. explicit url
    2. env url
    3. credentials url
    4. default url
    """
    if url is not None:
        return url
    if env is not None and env in URLS:
        return URLS[env]
    if credentials is not None and credentials.url is not None:
        return credentials.url
    return DEFAULT_URL


def login(username, password, url=None, env=None):
    url = get_url(url=url, env=env)
    response = APIHandler.simple_call(
        url,
        "PUT",
        "/users/{}/login".format(username),
        data={
            "password": password
        }
    )
    token = response.get("token")
    secret = response.get("secret")
    return url, token, secret


class APIHandler(object):

    def __init__(self,
                 token=None,
                 secret=None,
                 url=DEFAULT_URL,
                 retry_config=None,
                 profiler=False,
                 profiler_min_duration=1,
                 global_timeout=30,
                 ):
        """Class that perform all the requests to the API

        Args:
            token (str): API token. Can be a session or user token.
            secret (str): API secret.
            url (str): Optional url to point to a specific API.
            retry_config (dict): Configuration for requests retry.
                By default it will use the usual requests configuration
            profiler (bool): If enabled, will enable the profiler on all API requests.
            profiler_min_duration (float/int): If profiler is enabled, will add the min duration
                for a profile results to be dumped on the API side.
            global_timeout (float/int): Default timeout for all API requests. By default is 30, which
                is the lambda timeout for the API.
        """
        self.token = token
        self.secret = secret
        self.url = url
        if retry_config is None:
            retry_config = {}
        self.retry_config = retry_config
        self.profiler = profiler
        self.profiler_min_duration = profiler_min_duration
        self.global_timeout = global_timeout

    def get_session(self, retry_total=None, retry_backoff_factor=None):
        session = requests.Session()
        if retry_total is None:
            retry_total = self.retry_config.get('total')
        if retry_backoff_factor is None:
            retry_backoff_factor = self.retry_config.get('backoff_factor')
        if retry_total is not None or retry_backoff_factor is not None:
            retry = Retry(
                total=retry_total or 1,
                backoff_factor=retry_backoff_factor or 1,
                status_forcelist=self.retry_config.get('status_forcelist', (500, 502, 504))
            )
            adapter = HTTPAdapter(
                max_retries=retry,
                pool_connections=self.retry_config.get('pool_connections', 10),
                pool_maxsize=self.retry_config.get('pool_maxsize', 10)
            )
            session.mount('http://', adapter)
            session.mount('https://', adapter)
        return session

    @classmethod
    def get_instance(cls, url=None, token=None, secret=None, username=None, password=None, env=None, **kwargs):
        if token is not None and secret is not None:
            token = token
            secret = secret
            url = get_url(url, env)
        # if class is initialized with a username and password, use it
        elif username is not None and password is not None:
            url, token, secret = login(username, password, url=url, env=env)

        # if there is a saved freedom credentials file, use it
        elif credentials_exist():
            credentials = get_credentials()
            url = get_url(url, env, credentials=credentials)
            token = credentials.token
            secret = credentials.secret
        else:
            raise MissingArgumentsError(
                "Required: either token/secret, username/password, or saved ~/.freedom_credentials file"
            )

        api = cls(token, secret, url=url, **kwargs)
        if default_api is None:
            set_default_api(api)
        return api

    @classmethod
    def simple_call(cls, url, *args, **kwargs):
        instance = cls(url=url)
        return instance.call(no_auth=True, *args, **kwargs)

    def call(
            self,
            method,
            path,
            data=None,
            params=None,
            no_auth=False,
            raw=False,
            timeout=None,
            retry_total=None,
            retry_backoff_factor=None,
            ):
        """Performs the API request handling authorization and the status codes errors.
        Returns the response content as a dictionary or text if argument raw=True.

        Args:
            method (str): Http methods allowed are GET, PUT, POST, DELETE or OPTIONS.
            path (str): URL path. Could start either with / or without it. Eg: '/accounts/A1234'
            data (dict/list): Object to be passed in the body when the method is one of PUT or POST.
            params (dict): Query params of the request.
            no_auth (bool): False by default. If True, authorization headers with mc_token and mc_secret won't be sent.
            raw (bool): False by default. If True, will return the raw text of the response instead of trying to parse
                it from JSON. This is needed when working with CSV endpoints.
            timeout (float/tuple): requests module timeout parameter. Timeouts can be for connecting or for reading. If
                a tuple is sent, the first value will be the timeout for connections and the second for reads, otherwise
                will use the same value for both.
            retry_total (int): Number of times it will retry the request if it timeouts or if an 5xx error is raised.
                If not present, will use the values from the retry_config argument passed when creating the APIHandler
                instance.
            retry_backoff_factor (float): Backoff factor for waiting before retrying the request.
                If not present, will use the values from the retry_config argument passed when creating the APIHandler
                instance.
        """
        if method.upper() not in ['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS']:
            raise Exception("Invalid method ")

        if no_auth:
            auth_headers = {}
        else:
            auth_headers = {
                "mc_token": self.token,
                "mc_secret": self.secret,
            }
        if self.profiler:
            if params is None:
                params = {}
            params['profiler'] = 'enable'
            params['profiler_min_duration'] = self.profiler_min_duration

        request_kwargs = dict(
            headers=auth_headers,
            params=params,
        )
        timeout = timeout if timeout is not None else self.global_timeout
        if timeout is not None:
            request_kwargs['timeout'] = timeout

        if method.upper() in ['PUT', 'POST']:
            request_kwargs['json'] = data

        url = self.url.strip("/") + "/" + path.strip("/")

        with self.get_session(retry_total=retry_total, retry_backoff_factor=retry_backoff_factor) as session:
            func = getattr(session, method.lower())
            try:
                response = func(url, **request_kwargs)
            except (ConnectTimeout, ReadTimeout) as e:
                raise RequestTimeoutError(e)

        if response.status_code >= 400:
            raise APIError.from_response(response)

        try:
            if raw:
                return response.text
            else:
                return response.json()
        except ValueError:
            raise ServerError(
                "Error parsing API response to JSON: [{}] {}".format(response.status_code, response.text)
            )


class APIError(Exception):
    ERROR = "API Error"

    def __init__(self, response):
        self.response = response
        super().__init__(self.make_message())

    def make_message(self):
        try:
            body = self.response.json()
            body = body.get("Message", self.response.text)
        except ValueError:
            body = self.response.text
        return "{} [{}]: {}".format(self.ERROR, self.response.status_code, body)

    @classmethod
    def from_response(cls, response):
        if response.status_code in (401, 403):
            return UnauthorizedError(response)
        elif response.status_code == 404:
            return NotFoundError(response)
        elif response.status_code >= 500:
            return ServerError(response)
        else:
            return cls(response)


class UnauthorizedError(APIError):
    ERROR = "Unauthorized"


class NotFoundError(APIError):
    ERROR = "Not Found"


class ServerError(APIError):
    ERROR = "Server Error"


class RequestTimeoutError(APIError):

    def __init__(self, request_exception):
        if isinstance(request_exception, ConnectTimeout):
            msg = "Timeout when connecting to the API: {}".format(request_exception)
        elif isinstance(request_exception, ReadTimeout):
            msg = "Timeout when reading response from the API: {}".format(request_exception)
        Exception.__init__(self, msg)


class MissingArgumentsError(Exception):
    pass
