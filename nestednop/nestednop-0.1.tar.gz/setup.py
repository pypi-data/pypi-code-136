from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = "Editing deeply nested dicts/lists becomes the easiest thing in the world..."

# Setting up
setup(
    name="nestednop",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/nestednop',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['cprinter', 'flatten_any_dict_iterable_or_whatsoever', 'useful_functions_easier_life'],
    keywords=['list', 'dict', 'python', 'nested'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['cprinter', 'flatten_any_dict_iterable_or_whatsoever', 'useful_functions_easier_life'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*