# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

modules = \
['ayaka_prevent_bad_words']
install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot-plugin-ayaka>=0.3.5,<0.4.0',
 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka-prevent-bad-words',
    'version': '0.0.3',
    'description': '坏词撤回',
    'long_description': '# 坏词撤回\n\n基于ayaka开发的 坏词撤回 插件\n\n任何问题请发issue\n\n注意：只适用于群聊！管理员无法撤回或禁言其他管理员和群主！\n\n<b>注意：由于更新pypi的readme.md需要占用版本号，因此其readme.md可能不是最新的，强烈建议读者前往[github仓库](https://github.com/bridgeL/nonebot-plugin-ayaka-prevent-bad-words)以获取最新版本的帮助</b>\n\n自动撤回包含屏蔽词的消息\n\n# How to start\n\n## 安装 ayaka\n\n安装 [前置插件](https://github.com/bridgeL/nonebot-plugin-ayaka) \n\n`poetry add nonebot-plugin-ayaka`\n\n\n## 安装 本插件\n\n安装 本插件\n\n`poetry add nonebot-plugin-ayaka-prevent-bad-words`\n\n修改nonebot2  `bot.py` \n\n```python\nnonebot.load_plugin("ayaka_prevent_bad_words")\n```\n\n## 配置\n\n推荐配置（非强制要求）\n```\nCOMMAND_START=["#"]\nCOMMAND_SEP=[" "]\n```\n\n\n## 修改屏蔽词列表\n打开nonebot下的`data/plugins/坏词撤回/words.txt`（该文件在第一次启动时会自动生成），一行一个敏感词\n\n例如\n```\n芝士雪豹\n雪豹闭嘴\n```\n\n之后群友发言包含这些词时会被撤回\n\n\n## 其他配置\n`data/plugins/坏词撤回/config.json`\n\n`delay` 延迟n秒后撤回，默认为0\n\n`powerful` 检测力度，默认为0\n\n| powerful | 效果                               |\n| -------- | ---------------------------------- |\n| -1       | 仅仅是提示，不撤回                 |\n| 0        | 只有坏词完全匹配时，才会撤回       |\n| 1        | 即使坏词中夹杂了标点符号，也会撤回 |\n\n`tip` 提示语，默认为 请谨言慎行\n\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka-prevent-bad-words',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
