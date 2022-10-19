from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='source_converter',
    version='0.1.3',
    packages=find_packages(where='src'),
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
