# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_randomtkk']

package_data = \
{'': ['*'], 'nonebot_plugin_randomtkk': ['resource/*']}

install_requires = \
['aiofiles>=0.8.0,<0.9.0',
 'httpx>=0.23.0,<0.24.0',
 'nonebot-adapter-onebot>=2.1.1,<3.0.0',
 'nonebot2>=2.0.0b3,<3.0.0',
 'pillow>=9.0.1,<10.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-randomtkk',
    'version': '0.1.4',
    'description': 'Find Tan Kuku!',
    'long_description': '<div align="center">\n    <img width="200" src="tkk_logo.png" alt="logo"></br>\n\n# Random Tan Kuku\n\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable-next-line MD036 -->\n_🎶 随机唐可可 🎶_\n<!-- prettier-ignore-end -->\n\n</div>\n<p align="center">\n  \n  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_randomtkk/blob/main/LICENSE">\n    <img src="https://img.shields.io/github/license/MinatoAquaCrews/nonebot_plugin_randomtkk?color=blue">\n  </a>\n\n  <a href="https://github.com/nonebot/nonebot2">\n    <img src="https://img.shields.io/badge/nonebot2-2.0.0beta.3+-green">\n  </a>\n\n  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_randomtkk/releases/tag/v0.1.4">\n    <img src="https://img.shields.io/github/v/release/MinatoAquaCrews/nonebot_plugin_randomtkk?color=orange">\n  </a>\n\n  <a href="https://www.codefactor.io/repository/github/MinatoAquaCrews/nonebot_plugin_randomtkk">\n    <img src="https://img.shields.io/codefactor/grade/github/MinatoAquaCrews/nonebot_plugin_randomtkk/main?color=red">\n  </a>\n  \n</p>\n\n## 版本\n\nv0.1.4\n\n⚠ 适配nonebot2-2.0.0b3+\n\n[更新日志](https://github.com/MinatoAquaCrews/nonebot_plugin_randomtkk/releases/tag/v0.1.4)\n\n## 安装\n\n1. 通过`pip`或`nb`安装；\n\n2. 随机唐可可图片等资源位于`./resource`下，可在`env`下设置`TKK_PATH`更改；\n\n    ```python\n    TKK_PATH="your_path_to_resource"\n    ```\n\n3. 可更改默认配置：\n\n    ```python\n    TKK_PATH="./data/resource"  # 资源路径，可自行修改\n    EASY_SIZE=10                # 简单\n    NORMAL_SIZE=20              # 普通\n    HARD_SIZE=40                # 困难\n    EXTREME_SIZE=60             # 地狱\n    MAX_SIZE=80                 # 自定义的最大尺寸，建议不要大于99\n    ```\n\n    注意图片最小尺寸为10，最大尺寸可通过`MAX_SIZE`修改（默认80，不要超过99，否则无法指定），但生成时间会变长；\n    \n4. 缺失资源时会尝试从repo中下载至指定路径。\n\n    ⚠ 使用`raw.fastgit.org`进行加速，不确保下载成功\n\n5. 呜↗太⬆好⬇听↙了↖吧↗你唱歌真的好好听啊，简直就是天籁！我刚才，听到你唱歌了。我们以后一起唱好不好？一起唱！一起做学园偶像！\n\n## 功能\n\n寻找LoveLive角色！（主要是唐可可）\n\n## 命令\n\n1. 开始游戏：[随机唐可可][空格][简单/普通/困难/地狱/自定义数量]，开始游戏后会限时挑战，可替换为其他角色名；\n\n    ⚠ 可以[随机唐可可]不指定难度（默认普通）的方式开启游戏，可替换为其他角色名\n\n    ⚠ 角色名包括组合「[LoveLive!-μ\'s](https://zh.moegirl.org.cn/LoveLive!)」、「[LoveLive!Sunshine!!-Aqours](https://zh.moegirl.org.cn/LoveLive!Sunshine!!)」、「[LoveLive!Superstar!!-Liella](https://zh.moegirl.org.cn/LoveLive!Superstar!!)」成员名称及常见昵称\n\n2. 显示帮助：[随机唐可可][空格][帮助]，可替换为其他角色名，效果一样；\n\n3. 输入答案：[答案是][行][空格][列]，行列为具体数字，例如：答案是114 514；\n\n4. 答案正确则结束此次游戏；若不正确，则直至倒计时结束，Bot公布答案并结束游戏；\n\n5. 提前结束游戏：[找不到唐可可]（或其他角色名，需要与开启时输入的角色名相同），仅**游戏发起者**可提前结束游戏；\n\n6. 各群聊互不影响，每个群聊仅能同时开启一局游戏。\n\n## 功能展示\n\n![tkk_display](./tkk_display.jpg)\n\n## 本插件改自\n\n[Hoshino-randomtkk](https://github.com/kosakarin/hoshino_big_cockroach)',
    'author': 'KafCoppelia',
    'author_email': 'k740677208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
