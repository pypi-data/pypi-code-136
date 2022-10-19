from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


packages = find_packages(exclude=['tests', 'tests.*'])
packages = ['source_converter.py', 'github_downloader.py']
print(f'packages: {packages}')

setup(
    name='source_converter',
    version='0.1.5',
    packages=find_packages(where='src'),
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
