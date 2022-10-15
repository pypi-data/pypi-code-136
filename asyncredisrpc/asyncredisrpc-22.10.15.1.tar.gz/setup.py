from setuptools import setup

setup(
    name='asyncredisrpc',
    version='22.10.15.1',
    packages=['asyncredisrpc'],
    url='https://github.com/LiangZuoting/aioredisrpc.git',
    license='',
    author='LiangZuoting',
    author_email='liangzuoting2016@icloud.com',
    description='A naive async rpc framework based on redis.',
    install_requires=['redis']
)
