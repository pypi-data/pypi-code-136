# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_bnhhsh']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0', 'nonebot2>=2.0.0b4']

setup_kwargs = {
    'name': 'nonebot-plugin-bnhhsh',
    'version': '0.1.0.post0',
    'description': 'Se-se!',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-bnhhsh\n\n_✨ 「不能好好说话！」 ✨_\n\n\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/lgc2333/nonebot-plugin-bnhhsh.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-bnhhsh">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-bnhhsh.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n<a href="https://pypi.python.org/pypi/nonebot-plugin-bnhhsh">\n    <img src="https://img.shields.io/pypi/dm/nonebot-plugin-bnhhsh" alt="pypi download">\n</a>\n\n</div>\n\n## 📖 介绍\n\n今晚看到莉沫酱的一个奇奇怪怪的项目[bnhhsh](https://github.com/RimoChan/bnhhsh)，所以心血来潮做了个插件玩！\n\n这个项目也有受到莉沫酱TG群里的黄巍Bot启发，如果想去玩的话 -> [点这里](https://t.me/+0mv0KLEw4TY5Mzdl)\n\n## 💿 安装\n\n<details>\n<summary>使用 nb-cli 安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n    nb plugin install nonebot-plugin-bnhhsh\n\n</details>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n    pip install nonebot-plugin-bnhhsh\n</details>\n<details>\n<summary>pdm</summary>\n\n    pdm add nonebot-plugin-bnhhsh\n</details>\n<details>\n<summary>poetry</summary>\n\n    poetry add nonebot-plugin-bnhhsh\n</details>\n<details>\n<summary>conda</summary>\n\n    conda install nonebot-plugin-bnhhsh\n</details>\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'nonebot_plugin_bnhhsh\')\n\n</details>\n\n<details>\n<summary>从 github 安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库\n\n    git clone https://github.com/lgc2333/nonebot-plugin-bnhhsh.git\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'src.plugins.nonebot_plugin_bnhhsh\')\n\n</details>\n\n## ⚙️ 配置\n\n暂无，以后可能会有\n\n<!--\n在 nonebot2 项目的`.env`文件中添加下表中的必填配置\n\n| 配置项 | 必填 | 默认值 | 说明 |\n|:-----:|:----:|:----:|:----:|\n| 配置项1 | 是 | 无 | 配置说明 |\n| 配置项2 | 否 | 无 | 配置说明 |\n-->\n\n## 🎉 使用\n\n插件使用正则匹配所有纯字母消息，并以空白符为分隔符分割每个单词，然后自动将转换结果发送出来～  \n具体安装插件自己体验一下就知道了哦～mua～\n\n<!--\n### 指令表\n| 指令 | 权限 | 需要@ | 范围 | 说明 |\n|:-----:|:----:|:----:|:----:|:----:|\n| 指令1 | 主人 | 否 | 私聊 |配置说明 |\n| 指令2 | 群员 | 是 | 群聊 |配置说明 |\n### 效果图\n如果有效果图的话\n-->\n\n## 📞 联系\n\nQQ：3076823485  \nTelegram：[@lgc2333](https://t.me/lgc2333)  \n吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  \n邮箱：<lgc2333@126.com>\n\n## 💡 鸣谢\n\n### [RimoChan](https://github.com/RimoChan/)\n\n- 依赖包的作者！经常做些有脑洞的有趣的东西～\n- p.s. ~~如果你喜欢TA的作品，请多多给TA发萝莉色图(~~\n- p.s.. ~~也给我发点awwa((~~\n\n## 💰 赞助\n\n感谢大家的赞助！你们的赞助将是我继续创作的动力！\n\n- [爱发电](https://afdian.net/@lgc2333)\n- <details>\n    <summary>赞助二维码（点击展开）</summary>\n\n  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)\n\n  </details>\n\n## 📝 更新日志\n\n暂无\n',
    'author': 'student_2333',
    'author_email': 'lgc2333@126.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
