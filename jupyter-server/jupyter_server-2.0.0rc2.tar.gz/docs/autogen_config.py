#!/usr/bin/env python
import os

from jupyter_server.serverapp import ServerApp

header = """\
.. _other-full-config:


Config file and command line options
====================================

The Jupyter Server can be run with a variety of command line arguments.
A list of available options can be found below in the :ref:`options section
<options>`.

Defaults for these options can also be set by creating a file named
``jupyter_server_config.py`` in your Jupyter folder. The Jupyter
folder is in your home directory, ``~/.jupyter``.

To create a ``jupyter_server_config.py`` file, with all the defaults
commented out, you can use the following command line::

  $ jupyter server --generate-config


.. _options:

Options
-------

This list of options can be generated by running the following and hitting
enter::

  $ jupyter server --help-all

"""
try:
    destination = os.path.join(os.path.dirname(__file__), "source/other/full-config.rst")
except BaseException:
    destination = os.path.join(os.getcwd(), "other/full-config.rst")

with open(destination, "w") as f:
    f.write(header)
    f.write(ServerApp().document_config_options())
