# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/13
@Auth ： zhangping
"""
import requests


class ApiClient():
    def __init__(self, token: str, host=None):
        self.host = host or 'http://service.diigii.com'
        self._token = token

    @property
    def token(self): return self._token

    @property
    def host(self): return self.host

    def create_idx_list(self, name, parent_id=None, code=None, description=None):
        '''
        创建指标目录
        :param name:
        :param parent_id:
        :param code:
        :param description:
        :return:
        '''
        url = self.host + '/api/ds/list/save'
        headers = {'token': self.token}
        body = {
            'type': 'idx',
            'name': name,
            'code': code,
            'parent_id': parent_id,
            'description': description,
        }
        r = requests.post(url, None, body, headers=headers)
        print(r)
        print(r.json())


if __name__ == "__main__":
    api = ApiClient(
        'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5MTczY2E5MmYyYjk0MWUwYWQyY2Q2MWM5MzE5NGQ1MyIsInN1YiI6IjAiLCJpc3MiOiJ6aGFuZ3AiLCJpYXQiOjE2NjU1MDM1Nzh9.Zk31rY_yei88Hy2VRyzmqrbOUBoI_ChIrWXgdR7tlwM')
    # api.create_idx_list('国家统计局') #55362
    # api.create_idx_list('月度指标', 55362, 'A01')  # 55363
    # api.create_idx_list('季度指标', 55362, 'B01')  # 55364
    # api.create_idx_list('年度指标', 55362, 'C01')  # 55365
