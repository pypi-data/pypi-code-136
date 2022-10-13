from requests import Session
from urllib.parse import urljoin

class Authenticate:
    def __init__(self, asset, asset_schema, http_proxy):
        self.asset = asset
        self.asset_meta = asset_schema.get('meta', {})
        self.params = {}
        self.auth_error = False
        self.auth_error_response = None

        self.session = WrappedSession()
        self.session.proxies = {
            'http_proxy': http_proxy,
            'https_proxy': http_proxy
        }
        self.session.verify = self.asset.get('verify_ssl', True)
        self.session.headers.update(self._get_asset_headers())
        self.url = asset.get('url', self.asset_meta.get('url'))
        if not self.url:
            raise ValueError("No URL was provided. A URL must be provided in the asset parameters or under the meta"
                             "key in the asset schema.")

        self.authenticate(asset_schema.get('name', None))

    def _get_asset_headers(self):
        return self.asset_meta.get('headers', {})

    def authenticate(self, auth_type):
        # The asset name is the name of the function which was set by the get_asset_name function.
        if auth_type is not None:
            auth = getattr(self, auth_type)
            auth()

    def http_basic(self):
        self.session.auth = (self.asset['username'], self.asset['password'])

    def http_bearer(self):
        self.session.headers.update({
            'Authorization': f'Bearer {self.asset["token"]}'
        })

    def apikey(self):
        def handle_item(item: dict):
            if item['name'] not in self.asset:
                return
            if item['in'] == 'header':
                self.session.headers.update({
                    item['name']: self.asset[item['name']]
                })
            elif item['in'] == 'cookie':
                self.session.cookies.update({
                    item['name']: self.asset[item['name']]
                })
            elif item['in'] == 'query':
                self.params.update({
                    item['name']: self.asset[item['name']]
                })
        if isinstance(self.asset_meta['security'], list):
            for item in self.asset_meta['security']:
                handle_item(item)
        else:
            handle_item(self.asset_meta['security'])

    def oauth2(self, grant_type):
        scopes = self.asset.get('scopes')
        if scopes:
            scopes = scopes.join(' ')
        data = {
            'scope': scopes,
            'grant_type': grant_type
        }
        for key in ['client_id', 'client_secret', 'username', 'password']:
            if key in self.asset:
                data[key] = self.asset[key]
        token_url = self.asset.get("token_url") or urljoin(self.url, self.asset_meta['security']['token_endpoint'])
        response = self.session.request("POST",
                                        token_url,
                                        data=data)
        if response.status_code >= 300:
            self.auth_error = True
            self.auth_error_response = response
        else:
            access_token = response.json()['access_token']
            self.session.headers.update({"Authorization": "Bearer {}".format(access_token)})

    def oauth2_client_credentials(self):
        self.oauth2('client_credentials')

    def oauth2_password(self):
        self.oauth2('password')

class WrappedSession(Session):
    """A wrapper for requests.Session to override 'verify' property, ignoring REQUESTS_CA_BUNDLE environment variable.
    This is a workaround for https://github.com/kennethreitz/requests/issues/3829 (will be fixed in requests 3.0.0)
    Code sourced from user intgr https://github.com/kennethreitz/requests/issues/3829
    """

    def merge_environment_settings(self, url, proxies, stream, verify, *args, **kwargs):
        if self.verify is False:
            verify = False

        return super(WrappedSession, self).merge_environment_settings(url, proxies, stream, verify, *args, **kwargs)
