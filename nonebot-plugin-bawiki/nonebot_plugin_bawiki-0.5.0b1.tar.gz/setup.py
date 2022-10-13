# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_bawiki']

package_data = \
{'': ['*'], 'nonebot_plugin_bawiki': ['res/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'aiohttp>=3.8.1,<4.0.0',
 'nonebot-adapter-onebot>=2.1.1,<3.0.0',
 'nonebot-plugin-htmlrender>=0.1.1,<0.2.0',
 'nonebot-plugin-imageutils>=0.1.8,<0.2.0',
 'nonebot2>=2.0.0-beta.5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-bawiki',
    'version': '0.5.0b1',
    'description': 'A nonebot2 plugin for Blue Archive.',
    'long_description': '<!-- markdownlint-disable MD033 MD036 MD041 -->\n\n<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://raw.githubusercontent.com/lgc2333/nonebot-plugin-bawiki/master/readme/nonebot-plugin-bawiki.png" width="200" height="200" alt="BAWiki"></a>\n</div>\n\n<div align="center">\n\n# NoneBot-Plugin-BAWiki\n\n_✨ 基于 NoneBot2 的碧蓝档案 Wiki 插件 ✨_\n\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/lgc2333/nonebot-plugin-bawiki.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-bawiki">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-bawiki.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n<a href="https://pypi.python.org/pypi/nonebot-plugin-bawiki">\n    <img src="https://img.shields.io/pypi/dm/nonebot-plugin-bawiki" alt="pypi download">\n</a>\n<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/371bbbba-9dba-4e40-883c-72b688876575">\n    <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/371bbbba-9dba-4e40-883c-72b688876575.svg" alt="wakatime">\n</a>\n\n</div>\n\n## 💬 前言\n\n诚邀各位帮忙扩充别名词库以及更新插件内置数据源！\n\n本人在学校没有太多时间能够写代码，所以维护插件变成了一件比较困难的事  \n感谢各位的帮助！\n\n[点击跳转学生别名字典](https://github.com/lgc2333/nonebot-plugin-bawiki/blob/master/nonebot_plugin_bawiki/const.py#L1)  \n[点击跳转学生 L2D 预览图列表](https://github.com/lgc2333/nonebot-plugin-bawiki/blob/master/nonebot_plugin_bawiki/const.py#L125)\n\n修改后直接往本仓库提交 Pull Request 即可！\n\n## 📖 介绍\n\n一个碧蓝档案的 Wiki 插件，数据来源为 [GameKee](https://ba.gamekee.com/) 与 [SchaleDB](https://lonqie.github.io/SchaleDB/)  \n插件灵感来源：[ba_calender](https://f.xiaolz.cn/forum.php?mod=viewthread&tid=145)\n\n## 💿 安装\n\n<details open>\n<summary>【推荐】使用 nb-cli 安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n    nb plugin install nonebot-plugin-bawiki\n\n</details>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n    pip install nonebot-plugin-bawiki\n\n</details>\n<details>\n<summary>pdm</summary>\n\n    pdm add nonebot-plugin-bawiki\n\n</details>\n<details>\n<summary>poetry</summary>\n\n    poetry add nonebot-plugin-bawiki\n\n</details>\n<details>\n<summary>conda</summary>\n\n    conda install nonebot-plugin-bawiki\n\n</details>\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'nonebot_plugin_bawiki\')\n\n</details>\n\n<details>\n<summary>从 github 安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库\n\n    git clone https://github.com/lgc2333/nonebot-plugin-bawiki.git\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'src.plugins.nonebot_plugin_bawiki\')\n\n</details>\n\n## ⚙️ 配置\n\n暂无\n\n<!--\n在 nonebot2 项目的`.env`文件中添加下表中的配置\n\n| 配置项  | 必填 | 默认值 |            说明            |\n| :-----: | :--: | :----: | :------------------------: |\n| `proxy` |  否  | `None` | 访问`SchaleDB`时使用的代理 |\n-->\n## 🎉 使用\n\n### 指令表\n\n兼容 [nonebot-plugin-PicMenu](https://github.com/hamo-reid/nonebot_plugin_PicMenu)\n\n![menu](https://raw.githubusercontent.com/lgc2333/nonebot-plugin-bawiki/master/readme/menu.png)\n\n待更新\n\n### 效果图\n\n<details>\n<summary>长图，点击展开</summary>\n\n![example](https://raw.githubusercontent.com/lgc2333/nonebot-plugin-bawiki/master/readme/example.png)  \n![example2](https://raw.githubusercontent.com/lgc2333/nonebot-plugin-bawiki/master/readme/example2.png)\n\n</details>\n\n## 📞 联系\n\nQQ：3076823485  \nTelegram：[@lgc2333](https://t.me/lgc2333)  \n吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  \n邮箱：<lgc2333@126.com>\n\n## 💡 鸣谢\n\n### [RainNight0](https://github.com/RainNight0)\n\n- 日程表 html 模板提供\n\n### [黑枪灬王子](mailto:1109024495@qq.com)\n\n- 学生别名提供\n\n## 💰 赞助\n\n感谢大家的赞助！你们的赞助将是我继续创作的动力！\n\n- [爱发电](https://afdian.net/@lgc2333)\n- <details>\n    <summary>赞助二维码（点击展开）</summary>\n\n  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)\n\n  </details>\n\n## 📝 更新日志\n\n### 0.4.2\n\n- `ba羁绊` `baL2D` 的 L2D 预览图改为实时从 GameKee 抓取\n\n### 0.4.1\n\n- 优化带括号学生名称的别名匹配\n\n### 0.4.0\n\n- `ba日程表`的`SchaleDB`数据源\n- `ba学生图鉴` `ba羁绊` 数据源更换为`SchaleDB`\n- 原`ba学生图鉴`修改为`ba学生wiki`\n\n### 0.3.0\n\n- 新指令 `baL2D`\n- 新指令 `ba羁绊`\n\n### 0.2.2\n\n- 添加学生别名判断\n- 修改日程表图片宽度\n\n### 0.2.1\n\n- 修改页面加载等待的事件，可能修复截图失败的问题\n\n### 0.2.0\n\n- 新指令 `ba新学生` （详情使用 [nonebot-plugin-PicMenu](https://github.com/hamo-reid/nonebot_plugin_PicMenu) 查看）\n\n### 0.1.1\n\n- 日程表改为以图片形式发送\n- 日程表不会显示未开始的活动了\n- 小 bug 修复\n- ~~移除了 herobrine~~\n',
    'author': 'student_2333',
    'author_email': 'lgc2333@126.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lgc2333/nonebot-plugin-bawiki/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
