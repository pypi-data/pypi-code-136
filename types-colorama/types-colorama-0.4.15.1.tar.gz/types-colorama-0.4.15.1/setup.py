from setuptools import setup

name = "types-colorama"
description = "Typing stubs for colorama"
long_description = '''
## Typing stubs for colorama

This is a PEP 561 type stub package for the `colorama` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `colorama`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/colorama. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `51e18a860129b792123a088467a431cd044b2769`.
'''.lstrip()

setup(name=name,
      version="0.4.15.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/colorama.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['colorama-stubs'],
      package_data={'colorama-stubs': ['__init__.pyi', 'ansi.pyi', 'ansitowin32.pyi', 'initialise.pyi', 'win32.pyi', 'winterm.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
