# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zh_mistake_text_gen']

package_data = \
{'': ['*']}

install_requires = \
['OpenCC>=1.1.4,<2.0.0',
 'jieba>=0.42.1,<0.43.0',
 'loguru>=0.6.0,<0.7.0',
 'py-chinese-pronounce>=0.1.7,<0.2.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'zh-mistake-text-gen',
    'version': '0.3.3',
    'description': '中文錯誤類型文字增量',
    'long_description': '# 錯誤類型中文語料生成\n## 安裝\n```bash\npip install zh-mistake-text-gen\n```\n## 使用 (Pipeline)\n```python\nfrom zh_mistake_text_gen import Pipeline\npipeline = Pipeline()\nincorrect_sent = pipeline("中文語料生成")\nprint(incorrect_sent)\n# type=\'PronounceSimilarVocabMaker\' correct=\'中文語料生成\' incorrect=\'鍾文語料生成\' incorrect_start_at=0 incorrect_end_at=2 span=\'鍾文\'\n```\n## 文檔\n### `Pipeline`\n- `__init__`\n    - `makers` = None : maker實例，可選\n    - `maker_weight` = None : maker被抽中的機率，可選\n\n- `__call__`\n    - `x` : 輸入句(str)，必需\n    - `error_per_sent`: 每句要多少錯誤。預設:`1`\n    - `no_change_on_gen_fail`: 生成方法失敗的時候允許不變動。啟用時不拋出錯誤，反之。預設:`False`\n    - `verbose`=True : debug 訊息，可選\n\n## 可用方法\n```python\nfrom zh_mistake_text_gen.data_maker import *\n```\n|Data Maker|Description|\n|---|---|\n|NoChangeMaker|沒有任何變換|\n|MissingWordMaker|隨機缺字|\n|MissingVocabMaker|隨機缺詞|\n|PronounceSimilarWordMaker|隨機相似字替換|\n|PronounceSimilarWordPlusMaker|編輯距離找發音相似並且用高頻字替換|\n|PronounceSimilarVocabMaker|發音相似詞替換|\n|PronounceSimilarVocabPlusMaker|編輯距離找發音相似發音相似詞替換|\n|PronounceSameWordMaker|發音相同字替換|\n|PronounceSameVocabMaker|發音相同詞替換|\n|RedundantWordMaker|隨機複製旁邊一個字作為沆於字|\n|RandomInsertVacabMaker|隨機插入詞彙|\n|MistakWordMaker|隨機替換字|\n|MistakeWordHighFreqMaker|隨機替換高頻字|\n|MissingWordHighFreqMaker|隨機刪除高頻字|',
    'author': 'Philip Huang',
    'author_email': 'p208p2002@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/p208p2002/zh-mistake-text-gen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
