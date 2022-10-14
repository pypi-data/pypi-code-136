from setuptools import setup, find_packages

setup(
    name='gtja_vintex_qyt',
    version='0.0.5',
    keywords='gtja_vintex_qyt',
    description='Python Library for GTJA Vintex QYT',
    url='https://github.com/alfred42/gtja-qyt-python-lib',
    author='Liang Shi',
    author_email='shiliang022975@gtjas.com',
    packages=find_packages(include=["gtja_vintex_qyt"]),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests>=2.28.1'
    ]
)
