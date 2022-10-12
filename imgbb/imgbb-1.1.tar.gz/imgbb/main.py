import _io
import json
import requests


class ImgBB:
    API_URL = "https://api.imgbb.com/1/upload?key="

    def __init__(self, token: str):
        self.token = token
        self.API_URL += token

    def upload(self, name: str, image_bin: _io.BufferedReader = None, image_url: str = None,
               image_base64: str = None) -> dict:
        if not any([image_bin, image_url, image_base64]):
            raise AttributeError("You should use any one image transfer method")

        files = {}
        data = {"name": name}
        if image_bin:
            files['image'] = image_bin
        else:
            data['image'] = image_url or image_base64

        response = json.loads(requests.post(self.API_URL, data=data, files=files).text)

        return {
            "success": True,
            "id": response['data']['id'],
            "url": response['data']['url'],
            "url_viewer": response['data']['url_viewer'],
            "display_url": response['data']['display_url']
        } if response['status_code'] == 200 else {
            "success": False,
            "error": response['error']['message'],
            "status_code": response['status_code'],
            "error_code": response['error']['code']
        }
