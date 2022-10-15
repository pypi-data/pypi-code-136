from setuptools import setup

name = "types-flake8-builtins"
description = "Typing stubs for flake8-builtins"
long_description = '''
## Typing stubs for flake8-builtins

This is a PEP 561 type stub package for the `flake8-builtins` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `flake8-builtins`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/flake8-builtins. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `ce4668a1328cfbdccc0137cdf9b9bd5c64120a6c`.
'''.lstrip()

setup(name=name,
      version="2.0.0.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/flake8-builtins.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['flake8_builtins-stubs'],
      package_data={'flake8_builtins-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
