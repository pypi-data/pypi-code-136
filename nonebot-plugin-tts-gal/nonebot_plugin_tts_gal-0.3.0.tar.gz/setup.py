# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_tts_gal',
 'nonebot_plugin_tts_gal.monotonic_align',
 'nonebot_plugin_tts_gal.text']

package_data = \
{'': ['*']}

install_requires = \
['ffmpy>=0.3.0,<0.4.0',
 'jamo>=0.4.1,<0.5.0',
 'jieba>=0.42.1,<0.43.0',
 'nonebot-adapter-onebot>=2.1.1,<3.0.0',
 'nonebot2>=2.0.0b4,<3.0.0',
 'numba>=0.56.2,<0.57.0',
 'numpy>=1.20.0,<2.0.0',
 'pyopenjtalk>=0.3.0,<0.4.0',
 'pypinyin>=0.47.0,<0.48.0',
 'scipy>=1.5.2,<2.0.0',
 'torch>=1.6.0,<2.0.0',
 'unidecode>=1.1.1,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-tts-gal',
    'version': '0.3.0',
    'description': '',
    'long_description': '\n<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# nonebot_plugin_tts_gal\n\n基于nonebot和vits的部分gal角色的语音合成插件\n\n</div>\n\n# 旧版本用户注意\n\n在0.3.0版本再次对代码进行了更改，支持添加部分中文VITS模型，也许可能会报错下面的关键错误，具体解决方案可以看可以查看[Usage.md](https://github.com/dpm12345/nonebot_plugin_tts_gal/blob/master/Usage.md)\n\n# 安装\n\npip安装\n\n```\npip install nonebot_plugin_tts_gal\n```\n\nnb-cli安装\n\n```\nnb plugin install nonebot-plugin-tts-gal\n```\n\n## 相关依赖\n\n<details>\n<summary>ffmpeg的安装</summary> \n**Windows**\n\n在ffmpeg官网[下载](https://github.com/BtbN/FFmpeg-Builds/releases),选择对应的版本，下载后解压，并将位于`bin`目录添加到环境变量中\n\n其他具体细节可自行搜索\n\n**Linux**\n\nUbuntu下\n\n```\napt-get install ffmpeg\n```\n\n或者下载源码安装(具体可搜索相关教程)\n\n</details>\n\n# 配置项\n\n<details>\n<summary>auto_delete_voice</summary> \n\n请在使用的配置文件(.env.*)加入\n\n```\nauto_delete_voice = true\n```\n\n用于是否自动删除生成的语音文件，如不想删除，可改为\n\n```\nauto_delete_voice = false\n```\n\n</details>\n\n<details>\n<summary>tts_gal</summary> \n\n该配置项采用python的字典，其中键为元组，值为列表，具体代表含义及设置可以查看[Usage.md](https://github.com/dpm12345/nonebot_plugin_tts_gal/blob/master/Usage.md)\n\n</details>\n\n# 使用\n\n群聊和私聊仅有细微差别，其中下面语句中，`name`为合成语音的角色，`text`为转语音的文本内容(根据配置文件中的`lang`会自动翻译为对应语言)\n\n## 群聊\n\n`@机器人 [name]说[text]`\n\n## 私聊\n\n`[name]说[text]`\n\n例如：宁宁说おはようございます.\n\n**关于此方面自定义问题的可以查看**[Usage.md](https://github.com/dpm12345/nonebot_plugin_tts_gal/blob/master/Usage.md)\n\n\n\n# 感谢\n\n+ 部分代码参考自[nonebot-plugin-petpet](https://github.com/noneplugin/nonebot-plugin-petpet)\n+ **[CjangCjengh](https://github.com/CjangCjengh/)**：g2p转换，适用于日语调形标注的符号文件及分享的[柚子社多人模型](https://github.com/CjangCjengh/TTSModels)\n+ **[luoyily](https://github.com/luoyily)**：分享的[ATRI模型](https://pan.baidu.com/s/1_vhOx50OE5R4bE02ZMe9GA?pwd=9jo4)\n\n\n\n**其他完整内容请前往github查看**\n\n# 更新日志\n\n**2022.10.20 version 0.3.0：**\n\n支持添加中文模型，优化相关代码，增添更多提示\n\n**2022.10.7 version 0.2.3:**\n\n适配nonebot2-rc1版本，并添加部分报错信息提醒\n\n**2022.9.28 version 0.2.2:**\n\n添加中文逗号替换成英文逗号\n\n**version 0.2.1:**\n\n将pyopenjtalk依赖更新为0.3.0，使python3.10也能使用\n\n**2022.9.25 version 0.2.0:**\n\n优化修改代码逻辑，支持自行添加vits模型，简单修复了一下有道翻译的翻译问题，启动时自动检测所需文件是否缺失\n\n**2022.9.21 version 0.1.1:**\n\n修改依赖\n\n',
    'author': 'dpm12345',
    'author_email': '1006975692@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dpm12345/nonebot_plugin_tts_gal',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
