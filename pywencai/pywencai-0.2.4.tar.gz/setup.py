# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pywencai']

package_data = \
{'': ['*']}

install_requires = \
['PyExecJS>=1.5.1,<2.0.0', 'pandas>=1.5.0,<2.0.0', 'requests']

setup_kwargs = {
    'name': 'pywencai',
    'version': '0.2.4',
    'description': '',
    'long_description': "# pywencai\n\n获取同花顺问财数据\n\n## 安装\n\n```\npip install pywencai\n```\n\n# Demo\n\n```python\nimport pywencai\n\nres = pywencai.get(question='退市股票', sort_key='退市@退市日期', sort_order='asc')\nprint(res)\n```\n\n[demo.ipynb](./demo.ipynb)\n\n# API\n\n## get(**kwargs)\n\n根据问财语句查询结果\n\n### 参数\n\n#### question\n\n必填，查询问句\n\n#### sort_key\n\n非必填，指定用于排序的字段，值为返回结果的列名\n\n#### sort_order\n\n非必填，排序规则，至为`asc`（升序）或`desc`（降序）\n\n#### page\n\n非必填，查询的页号，默认为1\n\n#### perpage\n\n非必填，每页数据条数，默认值100，由于问财做了数据限制，最大值为100，指定大于100的数值无效。\n\n#### loop\n\n非必填，是否循环分页，返回多页合并数据。默认值为`False`，可以设置为`True`或具体数值。\n\n当设置为`True`时，程序会一直循环到最后一页，返回全部数据。\n\n当设置具体数值`n`时，循环请求n页，返回n页合并数据。\n\n### 返回值\n\n该方法返回一个`pandas`的`Dataframe`",
    'author': 'pluto',
    'author_email': 'mayuanchi1029@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
