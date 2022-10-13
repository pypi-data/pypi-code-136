from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
]

setup(
    name='Secret_helper',
    version='0.0.5',
    description='A helper function to get the secrets',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Pranav Chandran',
    author_email='pranav.chandran@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Secret_helper',
    packages=find_packages(),
    install_requires=['cryptocode']
)
