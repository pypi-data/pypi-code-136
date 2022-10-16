from setuptools import setup

long_description = None
with open("README.md", 'r') as fp:
    long_description = fp.read()

setup(
    name = 'pySomfyConnectedThermostat',
    packages = ['somfy_connected_thermostat'],
    install_requires=['aiohttp>=3.8.3'],
    version='0.0.2',
    description='A python3 library to communicate with Somfy connected thermostat',
    long_description=long_description,
    python_requires='>=3.5.3',
    author='Guillaume Nury',
    url='https://github.com/GuillaumeNury/pySomfyConnectedThermostat',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)