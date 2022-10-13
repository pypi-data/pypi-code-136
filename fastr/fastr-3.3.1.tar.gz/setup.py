# Copyright 2011-2014 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import imp
import os
import sys

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')

from typing import List, Optional

from setuptools import setup

with open('requirements.txt', 'r') as fh:
    _requires = fh.read().splitlines()

with open('test_requirements.txt', 'r') as fh:
    _tests_require = fh.read().splitlines()

with open('README', 'r') as fh:
    _description = fh.read()


def scan_dir(path: str, prefix: Optional[str]=None) -> List[str]:
    """
    Scan directory for resources to use

    :param path: Path to scan
    :param prefix: Prefix of files to remove to obtain relative paths
                   (defaults to path argument)
    :return: List of relative paths of the files found
    """
    if prefix is None:
        prefix = path

    # Scan resources package for files to include
    file_list = []
    for root, dirs, files in os.walk(path):
        # Strip this part as setup wants relative directories
        root = root.replace(prefix, '')
        root = root.lstrip('/\\')

        for filename in files:
            if filename[0:8] == '__init__':
                continue
            file_list.append(os.path.join(root, filename))

    return file_list


# Create version file
version = imp.load_source('version', os.path.join(os.path.dirname(__file__), 'fastr', 'version.py'))
__version__ = version.version
version.save_version(__version__, version.git_head, version.git_branch)

# Determine the extra resources and scripts to pack
resources_list = scan_dir('./fastr/resources')
examples_list = scan_dir('./fastr/examples/data', './fastr/examples')

print('[setup.py] called with: {}'.format(' '.join(sys.argv)))
if hasattr(sys, 'real_prefix'):
    print('[setup.py] Installing in virtual env {} (real prefix: {})'.format(sys.prefix, sys.real_prefix))
else:
    print('[setup.py] Not inside a virtual env!')

# Set the entry point
entry_points = {
    "console_scripts": [
        "fastr = fastr.utils.cmd.__init__:main",
    ]
}

# When building something else than a release (tag) append the job id to the version.
if os.environ.get('CI_COMMIT_TAG'):
    pass
elif os.environ.get('CI_JOB_ID'):
    __version__ += f".{os.environ['CI_JOB_ID']}"

setup(
    name='fastr',
    version=__version__,
    author='H.C. Achterberg, M. Koek',
    author_email='hakim.achterberg@gmail.com',
    packages=['fastr',
              'fastr.abc',
              'fastr.api',
              'fastr.core',
              'fastr.core.test',
              'fastr.data',
              'fastr.datatypes',
              'fastr.examples',
              'fastr.examples.test',
              'fastr.execution',
              'fastr.helpers',
              'fastr.planning',
              'fastr.plugins',
              'fastr.plugins.managers',
              'fastr.resources',
              'fastr.test',
              'fastr.utils',
              'fastr.utils.cmd'],
    package_data={'fastr.resources': resources_list,
                  'fastr.examples': examples_list,
                  'fastr': ['versioninfo']
                  },
    scripts=[],
    url='https://gitlab.com/radiology/infrastructure/fastr',
    license='Apache License 2.0',
    description='Workflow creation and batch execution environment.',
    long_description=_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Logging',
        'Topic :: Utilities',
    ],
    python_requires=">=3.6",
    setup_requires=["pytest-runner"],
    install_requires=_requires,
    tests_require=_tests_require,
    entry_points=entry_points,
)
