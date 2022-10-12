# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kea_exporter']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7', 'prometheus-client>=0.1.1']

entry_points = \
{'console_scripts': ['kea-exporter = kea_exporter.__main__:cli']}

setup_kwargs = {
    'name': 'kea-exporter',
    'version': '0.4.4',
    'description': 'Export Kea Metrics in the Prometheus Exposition Format',
    'long_description': "|license| |version|\n\n.. |license| image:: https://img.shields.io/github/license/mweinelt/kea-exporter\n   :alt: GitHub license\n   :target: https://github.com/mweinelt/kea-exporter/blob/develop/LICENSE\n\n.. |version| image:: https://img.shields.io/github/v/tag/mweinelt/kea-exporter\n   :alt: GitHub tag (latest SemVer)\n\nkea-exporter\n============\n\nPrometheus Exporter for the ISC Kea DHCP Server.\n\nFrom v0.4.0 on Kea >=1.3.0 is required, as the configuration, specifically\nsubnet information, will be read from the control socket.\n\nInstallation\n------------\n\n.. image:: https://repology.org/badge/vertical-allrepos/kea-exporter.svg\n   :alt: Package versions via repology.org\n\nThe latest stable version can always be installed from PyPi:\n\n::\n\n    $ pip install kea-exporter\n\n\nand upgraded with:\n\n::\n\n    $ pip install --upgrade kea-exporter\n\nFeatures\n--------\n\n- DHCP4 & DHCP6 Metrics (tested against Kea 1.6.0)\n- Configuration and statistics via control socket\n\nCurrently not working:\n\n- Automatic config reload (through inotify)\n\n\nKnown Limitations\n-----------------\n\nThe following features are not supported yet, help is welcome.\n\n- HTTP REST API (as a means to query a Kea instance)\n- Shared Networks\n- Custom Subnet Identifiers\n\nUsage\n-----\n\n::\n\n    Usage: kea-exporter [OPTIONS] SOCKETS...\n\n    Options:\n      --address TEXT      Specify the address to bind against.\n      --port INTEGER      Specify the port on which to listen.\n      --interval INTEGER  Specify the metrics update interval in seconds.\n      --version           Show the version and exit.\n      --help              Show this message and exit.\n\n\n\nConfigure Control Socket\n////////////////////////\n\nThe exporter uses Kea's control socket to request both configuration and \nstatistics. Consult the documentation on how to set up the control socket:\n\n- https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html#management-api-for-the-dhcpv4-server\n- https://kea.readthedocs.io/en/latest/arm/dhcp6-srv.html#management-api-for-the-dhcpv6-server\n\nPermissions\n///////////\n\nKea Exporter needs to be able to read and write on the socket, hence it's\npermissions might need to be modified accordingly.\n\nGrafana-Dashboard\n/////////////////\n\nA dashboard for this exporter is available at https://grafana.com/grafana/dashboards/12688.\n",
    'author': 'Martin Weinelt',
    'author_email': 'hexa@darmstadt.ccc.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mweinelt/kea-exporter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
