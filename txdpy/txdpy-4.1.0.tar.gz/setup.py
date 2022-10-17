from distutils.core import setup

packages = ['txdpy']

setup(name='txdpy',
    version='4.1.0',
    author='唐旭东',
    install_requires=['mmh3','pymysql','loguru','redis','lxml','colorama','requests','colorama','fake_useragent'],
    packages=packages,
    package_dir={'requests': 'requests'})