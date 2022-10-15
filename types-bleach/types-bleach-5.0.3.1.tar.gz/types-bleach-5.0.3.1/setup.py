from setuptools import setup

name = "types-bleach"
description = "Typing stubs for bleach"
long_description = '''
## Typing stubs for bleach

This is a PEP 561 type stub package for the `bleach` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `bleach`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/bleach. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `ce4668a1328cfbdccc0137cdf9b9bd5c64120a6c`.
'''.lstrip()

setup(name=name,
      version="5.0.3.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/bleach.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['bleach-stubs'],
      package_data={'bleach-stubs': ['__init__.pyi', 'callbacks.pyi', 'css_sanitizer.pyi', 'html5lib_shim.pyi', 'linkifier.pyi', 'sanitizer.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
