# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

modules = \
['ayaka_timezone']
install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot-plugin-ayaka>=0.3.5,<0.4.0',
 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka-timezone',
    'version': '0.0.1',
    'description': '时区助手',
    'long_description': '# 时区助手\n\n基于ayaka开发的 时区助手 插件\n\n任何问题请发issue\n\n注意：只适用于群聊！\n\n<b>注意：由于更新pypi的readme.md需要占用版本号，因此其readme.md可能不是最新的，强烈建议读者前往[github仓库](https://github.com/bridgeL/nonebot-plugin-ayaka-timezone)以获取最新版本的帮助</b>\n\n\n# How to start\n\n## 安装 ayaka\n\n安装 [前置插件](https://github.com/bridgeL/nonebot-plugin-ayaka) \n\n`poetry add nonebot-plugin-ayaka`\n\n\n## 安装 本插件\n\n安装 本插件\n\n`poetry add nonebot-plugin-ayaka-timezone`\n\n修改nonebot2  `bot.py` \n\n```python\nnonebot.load_plugin("ayaka_timezone")\n```\n\n## 配置\n\n推荐配置（非强制要求）\n```\nCOMMAND_START=["#"]\nCOMMAND_SEP=[" "]\n```\n\n# 指令\n指令|参数|功能\n-|-|-\ntz_add|name, timezone|添加一条时区转换，例如，#tz_add 北京 8，#tz_add 伦敦 0，#tz_add 洛杉矶 -8\ntz|name|返回name对应时区的时间，例如 #tz 北京\ntz|number|返回对应时区的时间，例如 #tz 8\ntz_list|无|查看所有的时区转换\n\n\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka-timezone',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
