# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['datacls']
install_requires = \
['dtyper', 'xmod']

setup_kwargs = {
    'name': 'datacls',
    'version': '4.4.1',
    'description': 'Slightly improved, backward compatible dataclasses',
    'long_description': '========================================================\n``datacls``: a slightly improved dataclasses\n========================================================\n\nThe Python built-in module\n`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ is almost\nperfect.\n\n``datacls`` is a thin wrapper around\n``dataclasses``, completely backward-compatible,\nthat makes common use cases a little easier.\n\n---------------------------------\n\n``@datacls.mutable`` is exactly like\n`@dataclasses.dataclass()\n<https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass>`_\nexcept that the resulting dataclass has four new methods:\n\n* three new instance methods:\n\n  * ``self.asdict()``, like `dataclasses.asdict() <https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict>`_\n  * ``self.astuple()``, like `dataclasses.astuple() <https://docs.python.org/3/library/dataclasses.html#dataclasses.astuple>`_\n  * ``self.replace()``, like `dataclasses.replace() <https://docs.python.org/3/library/dataclasses.html#dataclasses.replace>`_\n\n* ...and one new class method:\n\n  * ``cls.fields()``, like `dataclasses.fields() <https://docs.python.org/3/library/dataclasses.html#dataclasses.fields>`_\n\nThe new methods are only added if they do not exist on the target dataclass,\nso it should be impossible for ``datacls`` to override or shadow user methods or\nmembers by mistake.\n\n-----------------------------------\n\n``@datacls.immutable``, or just ``@datacls``, is exactly like\n``datacls.mutable`` except ``frozen=True`` by default, so members can\'t\nbe changed after construction (without deliberately subverting the immutability).\n\n-----------------------------------\n\n``datacls.field()`` is just like\n`dataclasses.field() <https://docs.python.org/3/library/dataclasses.html#dataclasses.field>`_\nexcept the very common ``default_factory`` argument is now also the first and only\npositional parameter.\n\n``datacls.make_dataclass()`` is just like\n`dataclasses.make_dataclass() <https://docs.python.org/3/library/dataclasses.html#dataclasses.make_dataclass>`_\nexcept that the class created also has the four new methods listed above.\n\n\nUsage examples\n==================\n\n.. code-block:: python\n\n    import datacls\n    from typing import Dict\n\n    @datacls\n    class One:\n        one: str = \'one\'\n        two: int = 2\n        three: Dict = datacls.field(dict)\n\n    #\n    # Three new instance methods: asdict(), astuple(), replace()\n    #\n    o = One()\n    assert o.asdict() == {\'one\': \'one\', \'two\': 2, \'three\': {}}\n\n    # Same as:\n    #\n    # import dataclasses\n    #\n    # assert dataclasses.asdict(o) == {\'one\': \'one\', \'two\': 2, \'three\': {}}\n\n    assert o.astuple() == (\'one\', 2, {})\n\n    o2 = o.replace(one=\'seven\', three={\'nine\': 9})\n    assert o2 == One(\'seven\', 2, {\'nine\': 9})\n\n    #\n    # One new class method: fields()\n    #\n    assert [f.name for f in One.fields()] == [\'one\', \'two\', \'three\']\n\n    #\n    # @datacls is immutable: use @datacls.mutable for mutable classes\n    #\n    try:\n        o.one = \'three\'\n    except AttributeError:\n        pass\n    else:\n        raise AttributeError(\'Was mutable!\')\n\n    @datacls.mutable\n    class OneMutable:\n        one: str = \'one\'\n        two: int = 2\n        three: Dict = datacls.field(dict)\n\n    om = OneMutable()\n    om.one = \'three\'\n    assert str(om) == "OneMutable(one=\'three\', two=2, three={})"\n\n    #\n    # These four new methods won\'t break your old dataclass by mistake:\n    #\n    @datacls\n    class Overloads:\n        one: str = \'one\'\n        asdict: int = 1\n        astuple: int = 1\n        fields: int = 1\n        replace: int = 1\n\n    o = Overloads()\n\n    assert datacls.astuple(ov) == (\'one\', 1, 1, 1, 1)\n\n    assert ov.one == \'one\'\n    assert ov.asdict == 1\n    assert ov.astuple == 1\n    assert ov.fields == 1\n    assert ov.replace == 1\n\n    # You can still access the methods as functions on `datacls`:\n    assert (\n        datacls.asdict(ov) ==\n        {\'asdict\': 1, \'astuple\': 1, \'fields\': 1, \'one\': \'one\', \'replace\': 1}\n    )\n',
    'author': 'Tom Ritchford',
    'author_email': 'tom@swirly.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
