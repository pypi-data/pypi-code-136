# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

modules = \
['ayaka']
install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0', 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka',
    'version': '0.3.0',
    'description': 'a useful plugin providing convinient tools for the development of textual game on QQ',
    'long_description': '# Ayaka 0.3.0\n针对Nonebot2框架 Onebot_v11协议的文字游戏开发辅助插件\n\n<img src="https://img.shields.io/badge/python-3.8%2B-blue">\n\n<b>注意：由于更新pypi的readme.md需要占用版本号，因此其readme.md可能不是最新的，强烈建议读者前往[github仓库](https://github.com/bridgeL/nonebot-plugin-ayaka)以获取最新版本的帮助</b>\n\n\n# 更新记录\n\n<details>\n<summary>更新记录</summary>\n\n版本|备注\n-|-\n0.3.0 | 借助contextvar内置模块，全部重写了之间的代码，现在它们被合并为一个单文件，并能实现ayaka插件先前提供的所有功能，但不幸的是，其无法兼容0.2.x的ayaka插件，需要代码迁移\n\n\n</details>\n\n# 安装\n`pip install nonebot-plugin-ayaka` \n\n在 `bot.py` 中 写入 `nonebot.load_plugin("ayaka")`\n\n# 快速了解\n\n通过ayaka插件，二次封装nonebot2提供的api，提供专用api，便于其他文字游戏插件的编写\n\n## 特性\n\n群聊\n\n## 插件编写范例\n\n```python\n\'\'\'\n    具有状态机的复读模块\n\'\'\'\nfrom ayaka import *\n\napp = AyakaApp("echo")\n\n# ayaka内置帮助插件，用户可通过#help命令展示app.help\napp.help = "复读只因"\n\n# 另一种写法\n# 当app处于run状态时，用户发送help指令将返回对应的提示 \napp.help = {\n    "":"复读只因",\n    "run":"echo正在运行~\\n使用[#exit] 退出"\n}\n\n\n@app.on_command("echo")\nasync def app_entrance():\n    # 运行该应用\n    await app.start()\n\n    # 用户可以为该复读提供一个前缀，例如 "无穷小亮说："\n    if app.args:\n        app.cache.prefix = str(app.args[0])\n\n    await app.send(info)\n\n\n# 当app为run状态时响应\n@app.on_state_command(["exit", "退出"])\nasync def app_exit():\n    # 关闭该应用\n    f, info = app.close()\n    await app.send(info)\n\n\n# 当app为run状态时响应\n@app.on_state_text()\nasync def repeat():\n    prefix = app.cache.prefix\n    if prefix is None:\n        prefix = ""\n    await app.send(prefix + str(app.message))\n\n\n# 桌面模式下执行\n@app.on_text()\nasync def hi():\n    if str(app.message).startswith("hello"):\n        await app.send(app.message)\n```\n\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
