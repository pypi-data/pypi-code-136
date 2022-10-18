from distutils.core import setup
import os

OS_SEPARATOR = os.path.sep

version = '0.3.56'
name = 'python_helper'
packageName = name
repositoryName = name.replace("_", "-")
url = f'https://github.com/SamuelJansen/{repositoryName}/'


setup(
    name = name,
    packages = [
        packageName,
        f'{packageName}{OS_SEPARATOR}api',
        f'{packageName}{OS_SEPARATOR}api{OS_SEPARATOR}src',
        f'{packageName}{OS_SEPARATOR}api{OS_SEPARATOR}src{OS_SEPARATOR}service',
        f'{packageName}{OS_SEPARATOR}api{OS_SEPARATOR}src{OS_SEPARATOR}domain',
        f'{packageName}{OS_SEPARATOR}api{OS_SEPARATOR}src{OS_SEPARATOR}helper',
        f'{packageName}{OS_SEPARATOR}api{OS_SEPARATOR}src{OS_SEPARATOR}annotation'
    ],
    version = version,
    license = 'MIT',
    description = 'python helper package',
    author = 'Samuel Jansen',
    author_email = 'samuel.jansenn@gmail.com',
    url = url,
    download_url = f'{url}archive/v{version}.tar.gz',
    keywords = ['helper', 'python helper package', 'python helper', 'helper package'],
    install_requires = [
        'colorama==0.4.4'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires='>=3.7'
)
