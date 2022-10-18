import requests

class Model:
    id = ""
    def __init__(self, name):
        self.id = name
        
    def Get_info(self, base_url, base_port):
        respone = requests.get(url=base_url + ':' + base_port)
        return respone