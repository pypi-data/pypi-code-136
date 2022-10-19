# coding=utf-8

from setuptools import setup, find_packages
setup(
    name='funboost-install',  #
    version='17.4',
    description=(
        'pip install funboost，python全功能分布式函数调度框架,。支持python所有类型的并发模式和一切知名消息队列中间件，python函数加速器，框架包罗万象，一统编程思维，兼容50% python业务场景，适用范围广。只需要一行代码即可分布式执行python一切函数。旧名字是function_scheduling_distributed_framework'
    ),
    # long_description=open('README.md', 'r',encoding='utf8').read(),
    keywords=["funboost", "distributed-framework", "function-scheduling", "rabbitmq", "rocketmq", "kafka", "nsq", "redis", "disk",
              "sqlachemy", "consume-confirm", "timing", "task-scheduling", "apscheduler", "pulsar", "mqtt", "kombu","的","celery","框架",'分布式调度'],
    long_description_content_type="text/markdown",
    long_description=open('README.md', 'r', encoding='utf8').read(),
    author='bfzs',
    author_email='ydf0509@sohu.com',
    maintainer='dragons96',
    maintainer_email='521274311@qq.com',
    license='BSD License',
    # packages=['douban'], #
    packages=find_packages() + ['funboost.beggar_version_implementation','funboost.assist'],   # 也可以写在 MANiFEST.in
    # packages=['function_scheduling_distributed_framework'], # 这样内层级文件夹的没有打包进去。
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/ydf0509/funboost',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        # 'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'nb_log>=7.6',
        'pytz>=2022.5',
        'apscheduler>=3.9.1',
        'deprecated>=1.2.13',
    ],
    extras_require={
        'KOMBU': [
            'kombu==4.6.11',
            'redis',
        ],
        'DEBUGGER': {
            'pysnooper',
        },
        'SSH_ALL': [
            'fabric2==2.6.0',
            'paramiko',
        ],
        'DECORATOR': [
            'decorator==4.4.0'
        ],
        'ROCKETMQ': [
            'rocketmq',
        ],
        'CONCURRENT_ALL': [
            'eventlet==0.31.0',
            'gevent==21.12.0',
            'aiohttp==3.8.0',
        ],
        'FLASK_ALL': [
            'Flask',
            'flask_bootstrap',
            'flask_wtf',
            'flask_login',
            'wtforms'
        ],
        'NATS': [
            'nats-python',
        ],
        'RABBITMQ_PIKA': [
            'pikav0',
            'pikav1',
        ],
        'RABBITMQ_RABBITPY': [
            'rabbitpy==2.0.1',
        ],
        'PERSISTQUEUE': [
            'persist-queue==0.8.0',
        ],
        'SQLITE_QUEUE': [
            'persist-queue==0.8.0',
        ],
        'TXT_FILE': [
            'persist-queue==0.8.0',
        ],
        'NSQ': [
            'gnsq==1.0.1',
        ],
        'ZEROMQ': [
            'zmq'
        ],
        'PEEWEE': [
            'peewee',
            'pymysql'
        ],
        'PLAYHOUSE': [
            'playhouse',
        ],
        'EVENTLET': [
            'eventlet',
        ],
        'MQTT': [
            'paho-mqtt'
        ],
        'REDIS': [
            'redis2',
            'redis3',
        ],
        'RABBITMQ_AMQPSTORM': [
            'amqpstorm==2.7.1'
        ],
        'MONGOMQ': [
            'pymongo==4.0.2',
        ],
        'KAFKA': [
            'kafka-python==2.0.2',
        ],
        'CONFLUENT_KAFKA': [
            'confluent-kafka==1.7.0',
        ],
        'KAFKA_CONFLUENT': [
            'confluent-kafka==1.7.0',
        ],
        'REDIS_ACK_ABLE': [
            'redis2',
            'redis3',
        ],
        'SQLACHEMY': [
            'sqlalchemy==1.3.10',
        ],
        'REDIS_STREAM': [
            'redis2',
            'redis3',
        ],
        'HTTP': [
            'aiohttp==3.8.0',
        ],
        'RedisBrpopLpush': [
            'redis2',
            'redis3',
        ],
        'REDIS_PUBSUB': [
            'redis2',
            'redis3'
        ]
    }
)
"""
官方 https://pypi.org/simple
清华 https://pypi.tuna.tsinghua.edu.cn/simple
豆瓣 https://pypi.douban.com/simple/ 
阿里云 https://mirrors.aliyun.com/pypi/simple/
腾讯云  http://mirrors.tencentyun.com/pypi/simple/

打包上传
python setup.py sdist upload -r pypi

# python setup.py bdist_wheel
python setup.py bdist_wheel ; python -m twine upload dist/funboost-15.0-py3-none-any.whl
python setup.py bdist_wheel && python -m twine upload dist/funboost-17.4-py3-none-any.whl
python setup.py sdist & twine upload dist/funboost-10.9.tar.gz

最快的下载方式，上传立即可安装。阿里云源同步官网pypi间隔要等很久。
./pip install funboost==3.5 -i https://pypi.org/simple   
最新版下载
./pip install funboost --upgrade -i https://pypi.org/simple       
"""
