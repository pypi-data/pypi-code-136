import requests


class TheOneAPISession(requests.Session):
    """
    Lord Of The Rings Session Object
    :param requests.Session: Sub-classes requests Session
    """
    def __init__(self):
        """
        Initialize TheOneAPISession
        """
        super(TheOneAPISession, self).__init__()

        self.headers.update({
            'Content-Type': 'application/json'
        })
    
    def set_bearer_auth(self, access_token: str) -> None:
        """
        Sets the access token for Bearer Auth in the headers
        :param access_token: Token gotten by registering / creating an account
        :return: None
        """
        self.headers.update({
            'Authorization': f'Bearer {access_token}'
        })

    def set_verify(self, verify: bool) -> None:
        """
        Sets the 'verify' boolean of a request.Session object
        :param verify: Boolean for validating certificates
        :return: None
        """
        self.verify = verify
