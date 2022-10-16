import requests

class S2hapi():
    """
        Simple api for stand2hacks
    """
    def __init__(self, token):
        self.token = token
    def account(self):
        """
            Information about selected account, returns json
        """
        return requests.get(f"https://stend2hacks.com/api/v1/{self.token}/account").json()
    def getKeys(self):
        """
            Get all keys, returns json
        """
        return requests.get(f"https://stend2hacks.com/api/v1/{self.token}/keys/all").json()
    def keyInfo(self, key):
        """
            Information about specified key, returns json
        """
        return requests.get(f"https://stend2hacks.com/api/v1/{self.token}/keys/get?&key={key}").json()
    def unlinkKey(self, key):
        """
            Unlinks key from all devices, limitation 1 key per 40 minutes.
            Returns nothing
        """
        return requests.get(f"https://stend2hacks.com/api/v1/{self.token}/keys/disconnect?&key={key}")
