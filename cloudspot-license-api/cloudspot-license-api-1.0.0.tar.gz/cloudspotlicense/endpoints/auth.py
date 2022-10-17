from cloudspotlicense.constants.errors import NoValidToken
from .base import APIEndpoint

from cloudspotlicense.models.auth import AuthResponse, User

class AuthMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'auth')
        
    def authenticate(self, username, password):
        endpoint = '{0}/{1}'.format(self.endpoint, 'authenticate')
        data = { 'username' : username, 'password' : password }
        
        status, headers, resp_json = self.api.post(endpoint, data)
        
        if status != 200: return AuthResponse().parse_error(resp_json)
        authResp = AuthResponse().parse(resp_json)
        
        return authResp
    
    def get_user(self):
        if not self.api.token: raise NoValidToken('No token found. Authenticate the user first to retrieve a token or supply a token to the function.')
        
        endpoint = '{0}/{1}'.format(self.endpoint, 'users/profile')
        data = None
        
        status, headers, resp_json = self.api.get(endpoint, data)
        
        if status != 200: return User().parse_error(resp_json)
        user_resp = User().parse(resp_json)
        
        return user_resp