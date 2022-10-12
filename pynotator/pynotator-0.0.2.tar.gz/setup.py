from setuptools import find_packages, setup
setup(
    name='pynotator',
    packages=find_packages(include=['pynotator']),
    version='0.0.2',
    description='A python library for annotating data for NER and Question Answering tasks in Natural Language Processsing and Machine Learning',
    author='Innocent Charles',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.3'],
    test_suite='tests',
)

