import urllib.request
import urllib.parse
import json
from fake_useragent import UserAgent  # 反爬策略


def translate_cn_to_en_(keyword):
    return json.loads(urllib.request.urlopen(
        urllib.request.Request('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule',
                               data=bytes(urllib.parse.urlencode({
                                   'i': keyword,
                                   'from': 'AUTO',
                                   'to': 'AUTO',
                                   'smartresult': 'dict',
                                   'client': 'fanyideskweb',
                                   'salt': '16655670214740',
                                   'sign': 'e34942cbba04c429eabed2f422cb4356',
                                   'ts': '1665567021474',
                                   'bv': '11b95c1bfe257341e4f01ee957a18428',
                                   'doctype': 'json',
                                   'version': '2.1',
                                   'keyfrom': 'fanyi.web',
                                   'action': 'FY_BY_CLICKBUTTION'

                               }), 'utf-8'), headers={'User-Agent': UserAgent().chrome})).read().decode())[
        'translateResult'][0][0]['tgt']
