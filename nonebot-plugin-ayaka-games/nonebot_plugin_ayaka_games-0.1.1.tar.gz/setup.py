# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayaka_games']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot-plugin-ayaka>=0.3.2,<0.4.0',
 'nonebot2>=2.0.0b5,<3.0.0',
 'pypinyin>=0.47.1,<0.48.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka-games',
    'version': '0.1.1',
    'description': 'a pack of textual game on QQ via nonebot-plugin-ayaka',
    'long_description': '# ayaka文字小游戏合集 v0.1.1\n\n基于ayaka开发的文字小游戏合集（共计10个）\n\n任何问题请发issue\n\n<b>注意：由于更新pypi的readme.md需要占用版本号，因此其readme.md可能不是最新的，强烈建议读者前往[github仓库](https://github.com/bridgeL/nonebot-plugin-ayaka-games)以获取最新版本的帮助</b>\n\n\n1. ayaka_master\n2. 背包\n3. 签到\n4. 印加宝藏 [@灯夜](https://github.com/lunexnocty/Meiri)\n5. 原神接龙\n6. 成语接龙\n7. b站视频链接分析\n8. bingo\n9. 生成糊文字截图\n10. 缩写翻译\n\n# 更新记录\n\n<details>\n\n<summary>更新记录</summary>\n\n## 0.1.0 \n适配0.3.x版本的ayaka插件\n\n## 0.1.1\n修复了checkin失效的问题\n\n</details>\n\n# How to start\n\n## 安装 ayaka\n\n安装 [前置插件](https://github.com/bridgeL/nonebot-plugin-ayaka) \n\n`poetry add nonebot-plugin-ayaka`\n\n\n## 安装 本插件\n\n安装 本插件\n\n`poetry add nonebot-plugin-ayaka-games`\n\n修改nonebot2  `bot.py` \n\n```python\n# 导入ayaka_games插件\nnonebot.load_plugin("ayaka_games")\n```\n\n## 导入数据\n\n将[本仓库](https://github.com/bridgeL/nonebot-plugin-ayaka-games)的data文件夹，放到nonebot的工作目录下\n\n之后运行nonebot即可\n\n# 特别感谢\n\n[@灯夜](https://github.com/lunexnocty/Meiri) 大佬的插件蛮好玩的~\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka-games',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
