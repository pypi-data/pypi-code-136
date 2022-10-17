from setuptools import setup, find_packages


setup(
    name='br_gender',
    version='0.1.0',
    url='https://github.com/arthurfortes/br_gender',
    license='MIT License',
    author='Arthur Fortes',
    author_email='fortes.arthur@gmail.com',
    keywords='gender names brazil',
    description=u'br_gender predicts gender from Brazilian first names using data from the Instituto Brasileiro de Geografia e Estatistica’s 2010 Census.',
    packages=find_packages(),
    package_data={'br_gender': ['gender_by_name.json']},
    include_package_data=True,
    install_requires=[],
)
