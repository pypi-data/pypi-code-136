
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


"""
    use
      install_requires=[
          'markdown',
      ],
    for packages on pypi

    use
        dependency_links=[
            'http://github.com/user/repo/tarball/master#egg=package-1.0'
        ],
    for packages on github
"""

setup(
    name='dhpackagetest',
    version='0.1',
    description='The funniest joke in the world',
    url='http://github.com/danahynes/dhconfiguratorv1',
    author='Dana Hynes',
    author_email='danhynes@example.com',
    license='WTFPLv2',
    packages=find_packages(),
    long_description=readme(),
    classifiers=[],
    keywords='funniest joke comedy flying circus',
    include_package_data=True
)
