# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['serialite', 'serialite._implementations']

package_data = \
{'': ['*']}

install_requires = \
['typing_extensions>=4.3.0,<5.0.0']

extras_require = \
{'fastapi': ['fastapi>=0.78.0,<0.79.0', 'pydantic>=1.9.1,<2.0.0'],
 'numpy': ['numpy>=1.23.0,<2.0.0']}

setup_kwargs = {
    'name': 'serialite',
    'version': '0.3.1',
    'description': 'A serialization library for Python',
    'long_description': '# Serialite\n\nSerialite is a library serializing and deserializing arbitrarily complex objects in Python. You\napply the `@serializable` decorator to a dataclass to automatically create `to_data` and `from_data`\nmethods using the type annotations. Or for more control, inherit from the `SerializableMixin` and\nimplement the class attribute `__fields_serializer__`. For even more control, inherit from the \nabstract base class `Serializer` and implement the `to_data` and `from_data` methods directly. \n\n## Basics\n\nThe abstract base class is `Serializer`:\n\n```python\nclass Serializer(Generic[Output]):\n    def from_data(self, data: Json) -> DeserializationSuccess[Output]: ...\n    def to_data(self, value: Output) -> Json: ...\n```\n\nThe class is generic in the type of the object that it serializes. The two abstract methods\n`from_data` and `to_data` are the key to the whole design, which revolves around getting objects to\nand from JSON-serializable data, which are objects constructed entirely of `bool`s, `int`s, \n`float`s, `list`s, and `dict`s. Such structures can be consumed by `json.dumps` to produce a string\nand produced by `json.loads` after consuming a string. By basing the serialization around JSON\nserializable data, complex structures can be built up or torn down piece by piece while\nalternatively building up complex error messages during deserialization which pinpoint the location\nin the structure where the bad data exist.\n\nFor new classes, it is recommended that the `Serializer` be implemented on the class itself. There is\nan abstract base class `Serializable` that classes can inherit from to indicate this. There is a mixin\n`SerializableMixin` that provides an implementation of `from_data` and `to_data` for any class that\nimplements the `__fields_serializer` class attribute.\n\nFor `dataclass`es, it is even easier. There is a decorator `serializable` that inserts\n`SerializableMixin` into the list of base classes after the `dataclass` decorator has run and also\ngenerates `__fields_serializer__` from the data class attributes.\n\nFinding the correct serializer for each type can be a pain, so\n`serializer(cls: type) -> Serializer` is provided as a convenience function. This is a single\ndispatch function, which looks up the serializer registered for a particular type. For example,\n`serializer(list[float])` will return `ListSerializer(FloatSerializer)`.\n',
    'author': 'David Hagen',
    'author_email': 'david@drhagen.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/drhagen/serialite',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
