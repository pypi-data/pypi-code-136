"""Installation script for BASEmesh.

This is used to set up the module after installation via PIP, as well
as to build local versions for testing and development.
"""

from setuptools import Extension, setup

from basemesh import __version__

# Load the project README
with open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

# Define the algorithm acceleration module
algorithms_c = Extension(name='basemesh._algorithms._algorithms_c',
                         sources=['basemesh/_algorithms/_algorithms_c.c'],
                         optional=True)

# Python packages to include
packages = [
    'basechange',
    'basemesh',
    'basemesh._algorithms',
    'basemesh._pslg_builder',
    'basemesh.triangle',
    'meshtool',
]

# Non-Python files to include
package_data = {
    'basemesh': ['py.typed'],
    'basemesh.triangle': ['bin/**'],
}

setup(name='BASEmesh',
      version=__version__,
      description='Pre-processing and mesh generation toolkit for BASEMENT.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='ETH Zürich',
      maintainer_email='seidelmann@vaw.ethz.ch',
      url='https://gitlab.ethz.ch/vaw/public/basemesh-v2/',
      license='GNU General Public License v3 (GPLv3)',
      packages=packages,
      package_data=package_data,
      ext_modules=[
          algorithms_c,
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.7',
          'Typing :: Typed',
      ],
      install_requires=[
        'numpy',
        'py2dm>=0.2.2',
      ])
