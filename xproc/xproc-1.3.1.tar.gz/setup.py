# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xproc']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['xproc = xproc.console:main']}

setup_kwargs = {
    'name': 'xproc',
    'version': '1.3.1',
    'description': 'Linux Proc File System Snooper',
    'long_description': '# [xproc](https://github.com/hungrybirder/xproc)\n\n## Install\n\n```bash\npip install -U xproc\n```\n\n## Support commands\n\n*   `xproc mem` or `xproc memory`\n\n```bash\nxproc mem\n        TIME       KERNEL         USER      MemFree     MemTotal\n    21:19:37    1345876kB   13143712kB   10079620kB   24624680kB\n    21:19:38    1345964kB   13143796kB   10079612kB   24624680kB\n    21:19:39    1345964kB   13143804kB   10079612kB   24624680kB\n    21:19:40    1345964kB   13143808kB   10079644kB   24624680kB\n    21:19:41    1345964kB   13143808kB   10079580kB   24624680kB\n```\n\n```bash\nxproc mem -e "Active,Inactive,Active(anon),Inactive(anon),Active(file),Inactive(file)"\n        TIME       Active     Inactive Active(anon) Inactive(anon) Active(file) Inactive(file)\n    21:21:19    4397264kB    8727816kB     173164kB          128kB    4224100kB      8727688kB\n    21:21:21    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n    21:21:23    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n    21:21:25    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n    21:21:27    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n```\n\n*   `xproc vmstat`\n\n```bash\nxproc vmstat 1 5\n        TIME allocstall_movable allocstall_normal compact_fail compact_free_scanned compact_isolated compact_migrate_scanned compact_stall compact_success\n    10:15:01              40908                55            0               108344            75443                   43462            56              56\n    10:15:02              40908                55            0               108344            75443                   43462            56              56\n    10:15:03              40908                55            0               108344            75443                   43462            56              56\n    10:15:04              40908                55            0               108344            75443                   43462            56              56\n    10:15:05              40908                55            0               108344            75443                   43462            56              56\n```\n\n*   `xproc load`\n\n```bash\nxproc load 1 3\n        TIME   LOAD_1_MIN   LOAD_5_MIN  LOAD_15_MIN   NR_RUNNING     NR_TOTAL     LAST_PID\n    14:28:34         0.07         0.18         0.15            1          316      2073102\n    14:28:35         0.07         0.18         0.15            1          316      2073102\n    14:28:36         0.07         0.18         0.15            1          316      2073102\n```\n',
    'author': 'liyong',
    'author_email': 'hungrybirder@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hungrybirder/xproc',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
