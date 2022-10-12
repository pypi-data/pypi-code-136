from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
]

setup(
    name='testsecrets',
    version='0.0.1',
    description='A helper function to get the secrets',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Pranav Chandran',
    author_email='pranav.chandran@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='secrets',
    packages=find_packages(),
    install_requires=['']
)
