from setuptools import find_packages, setup


setup(
    name='cgwpy',
    packages=find_packages(include=['cgwpy']),
    version='0.2.1',
    description='Continuous Gravitational Waves library toolkit',
    author='Jules Perret',
    license='MIT',
    install_requires=['numba','numpy','astropy','gwpy','gwosc'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
