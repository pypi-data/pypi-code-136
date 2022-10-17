from setuptools import setup

setup(
    name='stack_bot',
    version='0.1.0',    
    description='A Python package to create stack based Telegram bots hosting on Yandex.Cloud',
    url='https://github.com/Brat-vseznamus/stack_bot',
    author='Brat-vseznamus',
    packages=[
        'stack_bot', 
        'stack_bot.src.elements',
        'stack_bot.src.database_base',
        'stack_bot.src.init',
        'stack_bot.src.state_base',
        'stack_bot.src.utils'
    ],
    author_email='fvixnin@gmail.com',
    license='MIT',
    install_requires=[
        'numpy',                     
        'dataclasses_json>=0.5.7',
        'requests>=2.25.1',
        'ydb>=2.10.0'
    ]
)