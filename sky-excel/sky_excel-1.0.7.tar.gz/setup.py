# encoding: utf-8
"""
@project: djangoModel->setup
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 模块打包文件
@created_time: 2022/6/18 15:14
"""
import platform

from setuptools import setup, find_packages

# 版本兼容
if platform.python_version()[0] == "2":
    import io

    with io.open('README.md', "r", encoding="utf-8") as fp:
        log_desc = fp.read()


else:
    with open('README.md', 'r', encoding='utf8') as fp:
        log_desc = fp.read()

setup(
    name='sky_excel',  # 模块名称
    version='1.0.7',  # 模块版本
    description='excel模板配置化导出模块',  # 项目 摘要描述
    long_description=log_desc,  # 项目描述
    author='孙楷炎',  # 作者
    author_email='sky483@163.com',  # 作者邮箱
    maintainer="孙楷炎",  # 维护者
    maintainer_email="sky4834@163.com",  # 维护者的邮箱地址
    long_description_content_type="text/markdown",  # md文件，markdown格式
    packages=find_packages(),  # 系统自动从当前目录开始找包
    license="apache 3.0",
    install_requires=[
        'openpyxl',
        'xlutils',
    ]
)
