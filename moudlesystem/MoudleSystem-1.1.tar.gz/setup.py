#-*- coding:utf-8 -*-

from setuptools import setup,find_packages            #这个包没有的可以pip一下

setup(
    name = "MoudleSystem",      #这里是pip项目发布的名称
    version = "1.1",  #版本号，数值大的会优先被pip
    keywords = ["pip", "MoudleSystem"],			# 关键字
    description = "handongliren's MoudleSystem",	# 描述
    long_description = "handongliren's MoudleSystem",
    license = "GUN Licence",		# 许可证

    url = "https://github.com/hhd2009/Python/tree/package/MoudleSystem",     #项目相关文件地址，一般是github项目地址即可
    author = "handongliren",			# 作者
    author_email = "1079489986@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['wheel']          #这个项目依赖的第三方库
)
