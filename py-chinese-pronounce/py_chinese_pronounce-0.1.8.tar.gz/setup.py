# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_chinese_pronounce']

package_data = \
{'': ['*']}

install_requires = \
['Levenshtein>=0.20.5,<0.21.0']

setup_kwargs = {
    'name': 'py-chinese-pronounce',
    'version': '0.1.8',
    'description': '文字/漢語發音/注音互轉。相似發聲字/單詞。',
    'long_description': '# Python Chinese Pronounce\n- 文字轉注音、漢語發音\n- 注音、漢語發音轉文字\n- 尋找相似、相同發聲字/單詞\n\n> 資料來源：[政府開放資料](https://data.gov.tw/dataset/5961), [超齊百萬字典檔](https://github.com/samejack/sc-dictionary)\n\n## Install\n### From PyPI\n```sh\npip install py-chinese-pronounce\n```\n### From Repo\n```sh\npip install -U git+https://github.com/p208p2002/py-chinese-pronounce.git\n```\n## Usage\n```python\nfrom py_chinese_pronounce import Word2Pronounce,Pronounce2Word\n\nw2p = Word2Pronounce()\np2w = Pronounce2Word()\n```\n### Word2Pronounce\n僅支援*單一字元*轉換\n#### 文字轉注音\n```python\nw2p.to_chewin("我") # ㄨㄛˇ\n```\n#### 文字轉漢語發音\n```python\nw2p.to_han("我") # wo3\n```\n\n#### 發音相似度比較\n```python\nw2p.char_pronounce_similar(a,b)\nw2p.sent_pronounce_similar(sent_a, sent_b)\n# 數值區間落在[0-1]\n```\n\n#### 其他轉換\n- Word2Pronounce._word2unicode(self, x)\n- Word2Pronounce._uni2word(self,uni)\n- Word2Pronounce._cns2word(self,cns)\n- Word2Pronounce._uni2cns(self, uni)\n> CNS: [中文標準交換碼](https://www.cns11643.gov.tw/index.jsp)\n\n### Pronounce2Word\n詞彙尋功能支援多字元，其餘僅支援*單一字元*查詢\n\n#### 注音找文字 \n```python\np2w.chewin2word("ㄨㄛˇ") \n# [\'䰀\', \'婑\', \'捰\', \'㦱\', \'我\', \'䂺\']\n```\n\n#### 漢語發音找文字\n```python\np2w.han2word("wo3")\n# [\'䰀\', \'婑\', \'捰\', \'㦱\', \'我\', \'䂺\']\n```\n\n#### 文字找同發音\n```python\np2w.find_same("我")\n# [\'䰀\', \'婑\', \'捰\', \'㦱\', \'䂺\']\n```\n\n#### 文字找近似發音\n```python\np2w.find_similar("我")\n# [\'蠖\', \'臥\', \'䇶\', \'䂺\', \'䪝\', \'捾\', \'偓\', \'握\', \'捰\', \'卧\', \'雘\', \'㦱\', \'濣\', \'䠎\', \'楃\', \'沃\', \'渥\', \'䁊\', \'涴\', \'幄\', \'龌\', \'㓇\', \'矱\', \'斡\', \'㠛\', \'肟\', \'齷\', \'仴\', \'䰀\', \'婑\', \'喔\', \'腛\', \'䀑\']\n```\n\n#### 相似發聲單詞\n```python\np2w.find_similar_vocab("汽車") # 去除聲調找相似\n# [\'七尺\', \'棋車\', \'棋车\', \'气车\', \'氣車\', \'汽车\', \'騎車\', \'骑车\']\n```\n```python\np2w.find_similar_vocab_level("清晨",level=1) # 發音編輯距離找相似\n# [\'傾城\', \'清城\', \'清澄\', \'青城\', \'清淳\', \'清純\', \'清纯\', \'清醇\', \'清神\', \'青神\', \'星塵\', ...\n```\n\n#### 相同發聲單詞\n```python\np2w.find_same_vocab("汽車")\n# [\'气车\', \'氣車\', \'汽车\']\n```\n\n#### 其他轉換\n- Pronounce2Word._find_similar_han_pronounces(self,han,level=1)\n\n    尋找相似發音\n    - han: 漢語發音\n    - level: 編輯距離（越大越寬鬆）',
    'author': 'Philip Huang',
    'author_email': 'p208p2002@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/p208p2002/py-chinese-pronounce',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)
