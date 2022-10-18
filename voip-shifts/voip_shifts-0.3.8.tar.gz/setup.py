from setuptools import setup

setup(
    name='voip_shifts',
    version='0.3.8',
    description='Shared modules for voip project',
    install_requires=["redis", "rq", "sqlalchemy", "psycopg2", "requests"]
) 
