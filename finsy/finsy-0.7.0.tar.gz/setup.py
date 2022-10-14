# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finsy',
 'finsy.proto',
 'finsy.proto.gnmi1',
 'finsy.proto.google.rpc',
 'finsy.proto.google.rpc.context',
 'finsy.proto.p4',
 'finsy.proto.p4.config',
 'finsy.proto.p4.config.v1',
 'finsy.proto.p4.v1',
 'finsy.test']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.48.1,<2.0.0',
 'macaddress>=1.2.0,<2.0.0',
 'parsy>=2.0.0,<3.0.0',
 'protobuf>=4.21.5,<5.0.0',
 'pyee>=9.0.4,<10.0.0',
 'pylev>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'finsy',
    'version': '0.7.0',
    'description': 'P4Runtime Client Library',
    'long_description': '# 🐟 Finsy P4Runtime Library\n\n[![pypi](https://img.shields.io/pypi/v/finsy)](https://pypi.org/project/finsy/) [![ci](https://github.com/byllyfish/finsy/actions/workflows/ci.yml/badge.svg)](https://github.com/byllyfish/finsy/actions/workflows/ci.yml) [![codecov](https://codecov.io/gh/byllyfish/finsy/branch/main/graph/badge.svg?token=8RPYWRXNGS)](https://codecov.io/gh/byllyfish/finsy)\n\nFinsy is a [P4Runtime](https://p4.org/p4-spec/p4runtime/main/P4Runtime-Spec.html) controller library written in Python using asyncio. Finsy includes support for [gNMI](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md).\n\n```python\nimport asyncio\nimport finsy as fy\n\nasync def main():\n    async with fy.Switch("sw1", "127.0.0.1:50001") as sw1:\n        print(sw1.p4info)\n\nasyncio.run(main())\n```\n\n## Multiple Switches\n\nWith Finsy, you can write a P4Runtime controller that manages multiple switches.\n\nEach switch is managed by an async `ready_handler` function. Your `ready_handler` function can read or \nupdate various P4Runtime entities in the switch. It can also create tasks to listen for \npackets or digests.\n\nWhen you write P4Runtime updates to the switch, you use a unary operator (+, -, \\~) to specify the operation:\nINSERT (+), DELETE (-) or MODIFY (\\~).\n\n```python\nasync def ready_handler(sw: fy.Switch):\n    await sw.delete_all()\n    await sw.write(\n        [\n            # Insert multicast group with ports 1, 2, 3 and CONTROLLER.\n            +fy.P4MulticastGroupEntry(1, replicas=[1, 2, 3, 255]),\n            # Modify default table entry to flood all unmatched packets.\n            ~fy.P4TableEntry(\n                "ipv4",\n                action=fy.P4TableAction("flood"),\n                is_default_action=True,\n            ),\n        ]\n    )\n\n    async for packet in sw.read_packets():\n        print(f"{sw.name}: {packet}")\n```\n\nUse the `SwitchOptions` class to specify each switch\'s settings, including the p4info/p4blob and \n`ready_handler`. Use the `Controller` class to drive multiple switch connections. Each switch will call back\ninto your `ready_handler` function after the P4Runtime connection is established.\n\n```python\nfrom pathlib import Path\n\noptions = fy.SwitchOptions(\n    p4info=Path("hello.p4info.txt"),\n    p4blob=Path("hello.json"),\n    ready_handler=ready_handler,\n)\n\ncontroller = fy.Controller([\n    fy.Switch("sw1", "127.0.0.1:50001", options),\n    fy.Switch("sw2", "127.0.0.1:50002", options),\n    fy.Switch("sw3", "127.0.0.1:50003", options),\n])\n\nasyncio.run(controller.run())\n```\n\nIf the switch disconnects or its role changes to backup, the task running your `ready_handler` \n(and any tasks it spawned) will be cancelled and the `ready_handler` will begin again.\n\nFor more examples, see the [examples](https://github.com/byllyfish/finsy/tree/main/examples) directory.\n',
    'author': 'Bill Fisher',
    'author_email': 'william.w.fisher@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/byllyfish/finsy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
