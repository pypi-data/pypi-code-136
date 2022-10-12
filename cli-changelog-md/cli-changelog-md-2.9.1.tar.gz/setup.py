import os

import setuptools


setuptools.setup(
     name='cli-changelog-md',
     author="Y. Chudakov",
     author_email="kappasama.ks@gmail.com",
     version=os.getenv('RELEASE_VERSION'),
     description="A package for automatization work with changelog.md",
     packages=setuptools.find_packages(),
     package_dir={'cli-changelog-md': 'cli-changelog-md/'},
     install_requires=['click>=8.1.3', 'core-changelog-md>=1.5.5', "python-gitlab>=3.5.0"],
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
     scripts=['bin/changelog'],
     python_requires='>=3.8'
)
