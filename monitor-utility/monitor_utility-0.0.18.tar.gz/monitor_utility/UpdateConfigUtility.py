import requests
import base64
import json

class UploadConfigToGitHub:
    def __init__(self,access_token):
        self.ac_token = access_token
    def uploadFile(self,comments,git_url,update_data):
        data_b64 = base64.b64encode(bytes(update_data, 'utf-8')).decode('utf-8')
        content = data_b64
        sha = requests.get(url=git_url).json()
        data = json.dumps({"message": comments, "content": content, "sha": sha['sha']})
        headers = {"Authorization": "token " + self.ac_token, "Accept": "application/vnd.github.v3+json"}
        requests.put(url=git_url, data=data, headers=headers)

if __name__ == '__main__':
    pass