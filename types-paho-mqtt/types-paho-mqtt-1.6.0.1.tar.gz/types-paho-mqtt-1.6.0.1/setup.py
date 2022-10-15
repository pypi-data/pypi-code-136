from setuptools import setup

name = "types-paho-mqtt"
description = "Typing stubs for paho-mqtt"
long_description = '''
## Typing stubs for paho-mqtt

This is a PEP 561 type stub package for the `paho-mqtt` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `paho-mqtt`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/paho-mqtt. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `51e18a860129b792123a088467a431cd044b2769`.
'''.lstrip()

setup(name=name,
      version="1.6.0.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/paho-mqtt.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['paho-stubs'],
      package_data={'paho-stubs': ['__init__.pyi', 'mqtt/__init__.pyi', 'mqtt/client.pyi', 'mqtt/matcher.pyi', 'mqtt/packettypes.pyi', 'mqtt/properties.pyi', 'mqtt/publish.pyi', 'mqtt/reasoncodes.pyi', 'mqtt/subscribe.pyi', 'mqtt/subscribeoptions.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
