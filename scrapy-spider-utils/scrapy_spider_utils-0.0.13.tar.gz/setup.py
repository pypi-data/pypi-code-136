# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrapy_spider_utils', 'scrapy_spider_utils.login']

package_data = \
{'': ['*']}

install_requires = \
['Scrapy>=2.5.1',
 'elasticsearch==7.15.0',
 'fake-useragent>=0.1.11',
 'itemadapter>=0.4.0',
 'qrcode>=7.3.1',
 'requests>=2.28.1']

setup_kwargs = {
    'name': 'scrapy-spider-utils',
    'version': '0.0.13',
    'description': 'scrapy爬虫的一些工具类',
    'long_description': "## 打包\n\n- 确保我们已安装最新setuptools 和 wheel和twine ，下面是安装/更新命令\n\n```sh\npython3 -m pip install --user --upgrade setuptools wheel twine\n```\n\n- 打包的我们的库/项目\n\n```sh\npython3 -m\n```\n\n此时在当前目录我们会看到以下：\n\n```text\ndist/\n  example_pkg_your_username-0.0.1-py3-none-any.whl\n  example_pkg_your_username-0.0.1.tar.gz\n```\n\n- 使用 twine 将打包好的库/项目上传到PYPI\n\n（需用到PYPI帐号密码）（此时只是上传到PYPI测试服，还不能 pip install 这个库/项目）\n\n```sh\npython3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*\n```\n\n我们会看到如下界面：\n\n```sh\nUploading distributions to https://test.pypi.org/legacy/\nEnter your username: [your username]\nEnter your password:\nUploading example_pkg_your_username-0.0.1-py3-none-any.whl\n100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]\nUploading example_pkg_your_username-0.0.1.tar.gz\n100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]\n```\n\n上传成功之后，我们可以去PYPI的测试服查看是否上传成功，能上传成功的话就说明肯定也能成功上传到PYPI正式服（附：PYPI测试服地址）\n\nPYPI测试服的管理员会不定期删除上边的库，正式投入使用还是得上传到正式服。\n\n由于我先前有上传库到测试服，我们可以尝试搜索看看\n\n若是想测试下上传到测试服的库能否使用，可以使用如下命令\n\n```sh\npython3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username\n```\n\n大致会出现以下：\n\n```sh\nCollecting example-pkg-your-username\n  Downloading https://test-files.pythonhosted.org/packages/.../example-pkg-your-username-0.0.1-py3-none-any.whl\nInstalling collected packages: example-pkg-your-username\nSuccessfully installed example-pkg-your-username-0.0.1\n```\n\n若是从测试服安装的我们的库能正常使用，那么我们就可以开始行动把它上传到PYPI正式服供大家使用了。（之所以特地提出这一步，是因为第一次上传库时，我们总会因为目录结构不会、未打包成库可正常使用打包了却不能用等等原因导致上传的是个“失败的库”，这样能避免别人会安装到我们的失败库）\n\n简单测试是否能正常使用直接如下即可，但具体里边的功能能否正常用我们还需调用一下，此处不做介绍\n\n```python3\n>>> import example_pkg\n>>> example_pkg.name\n'example_pkg'\n```\n\n- 【重头戏】将库上传到 PYPI正式服\n\n```sh\ntwine upload dist/*\n```\n\n上传成功后该库即可直接pip安装\n\n如果对目录结构或者其他有什么不清楚的可以参考我这个库（结构较简单适合初学者），或者我们平时使用的库（譬如本人平时经常使用 scrapy 也可以去 scrapy 主页参考大佬的写法）\n",
    'author': 'gwq5210',
    'author_email': 'gwq5210@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0.0',
}


setup(**setup_kwargs)
