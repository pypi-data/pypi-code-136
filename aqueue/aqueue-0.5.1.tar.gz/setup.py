# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aqueue']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.1.0,<23.0.0',
 'rich>=12.6.0,<13.0.0',
 'sortedcontainers>=2.4.0,<3.0.0',
 'trio>=0.22.0,<0.23.0']

setup_kwargs = {
    'name': 'aqueue',
    'version': '0.5.1',
    'description': 'An async task queue with live progress display',
    'long_description': '.. teaser-begin\n\n==========\n``aqueue``\n==========\n\n``aqueue`` is an async task queue with live progress display.\n\nYou put items in, and they get processed, possibly creating more items which get processed, and so\non, until all items are completed. A typical use case would be to scrape a website.\n\n.. image:: https://raw.githubusercontent.com/t-mart/aqueue/master/docs/_static/demo.gif\n  :alt: Demonstration of aqueue\n\n.. note::\n\n  ``aqueue``, or any asynchronous framework, is only going to be helpful if you\'re performing\n  **I/O-bound** work.\n\n\nInstallation\n============\n\n``aqueue`` is a Python package `hosted on PyPI <https://pypi.org/project/aqueue/>`_. The recommended\ninstallation method is `pip <https://pip.pypa.io/en/stable/>`_-installing into a virtual\nenvironment:\n\n.. code-block:: shell\n\n   pip install aqueue\n\nGetting Started\n===============\n\nThere\'s two things you need to do to use aqueue:\n\n1. Implement your `Item <https://t-mart.github.io/aqueue/#items>`_ subclasses.\n2. `Start your queue <https://t-mart.github.io/aqueue/#starting-your-queue>`_ with one of those\n   items.\n\n.. teaser-end\n\nExample\n=======\n\nIf you had a hierarchy of items like this...\n\n.. image:: docs/_static/simple-diagram.png\n  :alt: Simple item hierarchy with one root item and many children items stemming from it.\n\nThen, you might process it with ``aqueue`` like this...\n\n.. code-block:: python\n\n   import aqueue\n\n\n   class RootItem(aqueue.Item):\n      async def process(\n         self, enqueue: aqueue.EnqueueFn, set_desc: aqueue.SetDescFn\n      ) -> None:\n         # display what we\'re doing in the worker status panel\n         set_desc("Processing RootItem")\n\n         # make an HTTP request, parse it, etc\n         ...\n\n         # when you discover more items you want to process, enqueue them:\n         for _ in range(5):\n               enqueue(ChildItem())\n\n      async def after_children_processed(self) -> None:\n         # run this method when this Item and all other Items it enqueued are done\n         print("All done!")\n\n\n   class ChildItem(aqueue.Item):\n\n      # track the enqueueing and completion of these items in the overall panel\n      track_overall: bool = True\n\n      async def process(\n         self, enqueue: aqueue.EnqueueFn, set_desc: aqueue.SetDescFn\n      ) -> None:\n         set_desc("Processing ChildItem")\n\n\n   if __name__ == "__main__":\n      aqueue.run_queue(\n         initial_items=[RootItem()],\n         num_workers=2,\n      )\n\n.. -project-information-\n\nProject Information\n===================\n\n- **License**: `MIT <https://choosealicense.com/licenses/mit/>`_\n- **PyPI**: https://pypi.org/project/aqueue/\n- **Source Code**: https://github.com/t-mart/aqueue\n- **Documentation**: https://t-mart.github.io/aqueue/\n- **Supported Python Versions**: 3.10 and later\n',
    'author': 'Tim Martin',
    'author_email': 'tim@timmart.in',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://t-mart.github.io/aqueue/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
