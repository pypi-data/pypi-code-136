#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    'linter': [
        "flake8==3.7.9"
    ],
    'dev': [
        "twine==3.1.1",
        "pytest==6.2.5"
    ],
}

extras_require['dev'] = (
    extras_require['linter'] + extras_require['dev']
)

setup(
    name='config-controller-predeployed',
    version='1.0.1dev1',
    description='A tool for generating predeployed config controller smart contract',
    long_description_content_type="text/markdown",
    author='SKALE Labs',
    author_email='support@skalelabs.com',
    url='https://github.com/skalenetwork/config-controller',
    install_requires=[
        "predeployed-generator >= 1.1.0a0"
    ],
    python_requires='>=3.7,<4',
    extras_require=extras_require,
    keywords=['skale', 'predeployed'],
    packages=find_packages(exclude=['tests']),
    package_data={
        'config_controller_predeployed': [
            'artifacts/ConfigController.json',
            'artifacts/ConfigController.meta.json'
        ]
    },
    setup_requires=["setuptools-markdown"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ]
)
