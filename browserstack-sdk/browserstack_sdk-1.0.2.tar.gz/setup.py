from os.path import abspath, join, dirname
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(join(dirname(abspath(__file__)), 'LICENSE.txt')) as f:
    LICENSE = f.read()

setup(
    name='browserstack_sdk',
    packages=['browserstack_sdk'],
    version='1.0.2',
    description='Python SDK for browserstack selenium-webdriver tests',
    long_description='Python SDK for browserstack selenium-webdriver tests',
    author='BrowserStack',
    author_email='support@browserstack.com',
    keywords=['browserstack', 'selenium', 'python'],
    classifiers=[],
    install_requires=[
        'psutil',
        'pyyaml',
        'browserstack-local',
        'packaging',
        'requests'
    ],
    scripts=['bin/browserstack-sdk'],
    license=LICENSE,
)
