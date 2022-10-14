from distutils.core import setup
import setuptools
packages = ['io2p']
setup(name='io2p',
	version='1.0',
	author='hzy',
    packages=packages,
    package_dir={'requests': 'requests'},
)