from setuptools import setup, find_packages

setup(
    install_requires=[
        'inquirer',
        'fastapi',
        'uvicorn',
        'configobj',
        'SQLAlchemy',
        'pydantic',
        'psutil',
        'requests',
        'fastapi-utils'
    ],
    packages=find_packages(
        exclude=["docs", ]),
)
