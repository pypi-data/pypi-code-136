import setuptools
from distutils.core import setup
with open('requirements.txt') as f:
    setup(
        name='giosgapps_bindings',
        packages=setuptools.find_packages(),
        version='1.0.0',
        license='MIT',
        description='Module for Giosg Apps development',
        author='Giosg',
        author_email='developers@giosg.com',
        url='https://github.com/giosg/giosgapps_bindings',
        download_url='https://github.com/giosg/giosgapps_bindings/archive/v1.0.0.tar.gz',
        keywords=['AUTH', 'GIOSG'],
        install_requires=list(f.read().splitlines()),
        classifiers=[
            'Development Status :: 5 - Production/Stable',  # "3 - Alpha" or "4 - Beta" or "5 - Production/Stable"
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
    )
