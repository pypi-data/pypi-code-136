from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'qtc/version.py'), 'r') as f:
    exec(f.read())


setup(
    name='qtc',
    version=__version__,
    url='',
    license='',
    author='Andrew Hu',
    author_email='AndrewWeiHu@gmail.com',
    description='Quant Trading Common',
    packages=find_packages(exclude=['backup']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'pandas>=1.3.4',
        'joblib',
        'sqlalchemy',
        'python-gssapi',
        'PyMySQL',
        'psycopg2',
        'pyarrow',
        'datatable',
        'pytest-html',
        'pyyaml',
        'requests-kerberos',
        'krb5',
        'nbparameterise'
    ],
    tests_require=[
        'pytest'
    ],
)
