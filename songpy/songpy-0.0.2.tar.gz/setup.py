from setuptools import setup, find_packages


# with open('README.rst') as f:
#     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='songpy',
    version='0.0.2',
    description='Package with objects representing objects of musical notation',
#    long_description=readme,
    author='Karol Ważny',
    author_email='me@kennethreitz.com',
#    url='https://github.com/kennethreitz/samplemod',
#    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)