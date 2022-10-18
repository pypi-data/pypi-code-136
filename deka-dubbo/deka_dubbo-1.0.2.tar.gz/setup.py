# coding=utf-8

from setuptools import setup, find_packages
setup(
    name='deka_dubbo',  #
    version='1.0.2',
    description=(
        'rabbitmq为中间件的分布式任务框架'
    ),
    long_description_content_type="text/markdown",
    long_description=open('README.md', 'r', encoding='utf8').read(),
    author='zy',
    author_email='517826265@qq.com',
    packages=find_packages(),
    include_package_data=True,
    platforms=["all"],
    install_requires=[
        'AMQPStorm==2.7.1',
        'redis2',
        'redis3',
        'redis',
        'deka_plog',
        'pytz'
    ]
)
