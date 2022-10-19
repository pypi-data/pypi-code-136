from pathlib import Path

from setuptools import find_packages, setup

version = '0.0.6'

this_directory = Path(__file__).parent
long_desc = (this_directory / "README.md").read_text()
long_version = version.replace('.', '_')
setup(
    name='socket_oneline',
    include_package_data=True,
    packages=find_packages(include='socket_oneline*', ),
    version=version,
    license='MIT',
    description='Client server base class over socket',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='JA',
    author_email='cppgent0@gmail.com',
    url='https://github.com/cppgent0/socket-oneline',
    download_url=f'https://github.com/cppgent0/socket-oneline/archive/refs/tags/v_{long_version}.tar.gz',
    keywords=['socket', 'client server', 'simple'],
    install_requires=[
        'pytest',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
