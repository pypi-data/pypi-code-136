# https://github.com/pixegami/python-cli-template/blob/main/publish/setup.py

import os
import setuptools

# Long Description / Markdown
with open('README.md', 'r') as f:
    long_description = f.read()

reqtxt = 'requirements.txt'

if os.path.exists(reqtxt):
    with open(reqtxt, 'r') as f:
        requirement_packages = [line.strip("\n") for line in f.readlines() if not line.startswith('#')]
    print(f'Set requirements: {requirement_packages}')

else:
    print(f'WARN Requirements file {reqtxt} not found!')
    print('No packages will be required on install.')
    requirement_packages = []

setuptools.setup(
    name='bkpk',
    version='0.1',
    summary='A simple Python CLI boilerplate project',
    license='MIT',
    author="NSDE",
    author_email='mail@onlix.me',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Natural Language :: English",

        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",

        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",

        "Topic :: Software Development :: Libraries",
        "Topic :: Desktop Environment :: File Managers",
        "Topic :: Multimedia",
    ],
    keywords=['backpack', 'bkpk', 'zip', 'unzip', 'package', 'backpkg', 'bkpack', 'backpk', 'bkpkg', 'compress', 'file'],

    url='https://github.com/nsde/bkpk',
    home_page='https://github.com/nsde/bkpk',


    long_description=long_description,
    description_file='README.md',
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages('bkpk'),
    package_dir={'': 'bkpk'},
    install_requires=requirement_packages,

    entry_points={'console_scripts': [
        'bkpk = __main__:main',
    ]},
)
