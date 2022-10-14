# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import setuptools


setuptools.setup(
    name='python-oauth-token-manager',
    version='0.2.0',
    description='API for managing stored OAuth credentials.',
    long_description="""
Multi-style OAuth credentials store
===================================
""",
    long_description_content_type='text/markdown',
    url='',
    author='David Harcombe',
    author_email='davidharcombe@google.com',
    license='Apache 2.0',
    zip_safe=False,
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
                     'Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'Topic :: Software Development',
                     'License :: OSI Approved :: Apache Software License',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.10',
    ]
)
