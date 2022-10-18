from setuptools import setup, find_packages

setup(
    name='iliadconn',
    version='0.0.2',
    packages=find_packages(),
    url='',
    license='GPL',
    author='massimo',
    author_email='massimo.cavalleri@gmail.com',
    description='get monthly outgoing traffic per iliad SIM',
    install_requires=[
        'beautifulsoup4',
        'lxml',
        'requests',
        'python-dateutil',
        'appdirs'
    ],
    entry_points={
        'console_scripts': [
            'iliadconn=iliad.iliadconn:main',
        ],
    }
)
