import requests

class Base:
    def __init__(self, baseurl='http://seriesapi-prod:8000'):
        self.baseurl = baseurl

    def _get_url(self, path:str):
        return "{}{}".format(self.baseurl, path)

    def _do_post(self, path, json):
        # print(self._get_url(path))
        response = requests.post(self._get_url(path), json=json)
        if response.status_code==200:
            # print(response.content)
            try:
                info = response.json()
            except Exception as e:
                raise Exception("返回值不是合法的JSON {}".format(response.content))

            if info['code']==0:
                return info['data']
            else:
                raise Exception("调用失败 {}".format(response.content))
        else:
            raise Exception("Error Response({})".format(response.status_code)) 