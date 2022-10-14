"""Setup for the tgm (temporal graph motifs) package."""

import setuptools

with open('README.md', encoding='utf-8') as f:
    README = f.read()

setuptools.setup(
    author="François Théberge",
    author_email="theberge@ieee.org",
    name='tgm',
    license="MIT",
    description='Python code to identify temporal K_{2,h} motifs in networks',
    version='v0.0.1',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/ftheberge/tgm',
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    py_modules=["tgm"],
    package_dir={'':'tgm'},
    install_requires=['numpy','pandas','igraph'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Science/Research',
    ],
)
