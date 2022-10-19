from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_desc = (this_directory / "README.md").read_text()

setup(
    name='socket_oneline',
    include_package_data=True,
    packages=find_packages(include='socket_oneline*', ),
    version='0.0.2',
    license='MIT',
    description='Client server base class over socket',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='JA',
    author_email='cppgent0@gmail.com',
    url='https://github.com/cppgent0/socket-oneline',
    download_url='https://github.com/cppgent0/socket-oneline/archive/refs/tags/v_0_0_2.tar.gz',
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
