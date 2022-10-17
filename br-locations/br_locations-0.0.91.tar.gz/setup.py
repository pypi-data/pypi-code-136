from setuptools import setup, find_packages


setup(
    name='br_locations',
    version='0.0.91',
    url='https://github.com/arthurfortes/br_locations',
    license='MIT License',
    author='Arthur Fortes',
    author_email='fortes.arthur@gmail.com',
    keywords='cities states brazil',
    description=u'Cities and States of Brazil (IBGE Info)',
    packages=find_packages(),
    package_data={'br_locations': ['states_and_cities_10_22.json']},
    include_package_data=True,
    install_requires=[],
)
