from lord_of_the_rings.constants import HOST, BASEPATH
from lord_of_the_rings.session import TheOneAPISession


class TheOneAPIBase:
    """
    TheOneAPI Base Class
    """
    def __init__(self, access_token: str = None, verify: bool = True):
        """
        Initialize the LordOfTheRingsAPI class object.
        :param access_token: token used for initial Bearer Auth
        :param verify: Certificate verification flag. Defaults to True
        """
        self.base_url = f'https://{HOST}{BASEPATH}'

        self.session = TheOneAPISession()
        self.session.set_bearer_auth(access_token) if access_token else None
        self.session.set_verify(verify)

    def _build_url(self, resource: str) -> str:
        """
        Generate the full URL based on the self.base_url plus provided resource (API endpoint)
        :param resource: API Endpoint suffix
        :return: Full URL for API call
        """
        return self.base_url + resource

    def _make_request(self, method: str, url: str, json: dict = None, params: dict = None):
        """
        Execute the request method of the Session object
        :param method: HTTP Method passed to the session object (e.g. GET, POST, PUT..)
        :param url: Full URL of the API endpoint
        :param json: Body if required
        :param params: params if required
        :return: json response
        """
        response = self.session.request(method, url, json=json, params=params)

        if response.ok:
            return response.json()

        response.raise_for_status()
