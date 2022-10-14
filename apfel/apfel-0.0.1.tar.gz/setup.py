# SPDX-FileCopyrightText: (C) 2022 Avnet Embedded GmbH
# SPDX-License-Identifier: GPL-3.0-only
# noqa: D100

import setuptools
import os

_version = os.environ.get('APFEL_VERSION', '0.0.1')

data = open('README.rst', 'r').read()
print(len(data), data[:50])
setuptools.setup(
    author='Avnet Embedded GmbH',
    description='Apfel CLI tools',
    long_description=data,  # open('README.rst', 'r').read(),
    long_description_content_type='text/x-rst',
    license='GPL-3.0-only',
    license_files=('LICENSE',),
    entry_points={
        'console_scripts': [
            'bumper = bumper.bumper:main',
        ],
    },
    packages=['bumper'],
    install_requires=['GitPython >= 3.1, < 4.0'],
    name='apfel',
    scripts=['apfel', 'apfel-runqemu'],
    url='https://github.com/avnet-embedded/mscplus-tools',
    version=_version,
)
