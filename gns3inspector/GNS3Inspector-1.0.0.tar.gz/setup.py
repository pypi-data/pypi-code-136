# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gns3inspector']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'black>=22.10.0,<23.0.0',
 'click>=8.1.3,<9.0.0',
 'fagus>=1.0.1,<2.0.0',
 'readline>=6.2.4.1,<7.0.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['gns3inspector = gns3inspector.main:main']}

setup_kwargs = {
    'name': 'gns3inspector',
    'version': '1.0.0',
    'description': "Tool to easier view and edit the router's configuration files in GNS3",
    'long_description': '# GNS3Inspector\n\n## Overview\nA simple python-package to help get an overview of what is configured in a network-project that was created using GNS3. It also allows to configure several routers at the same time.\n\n**NOTE**: This tool doesn\'t verify any of the inputs you give to it. You should know what you\'re doing. Preferably you should run the commands on one router to see if they work. If they work as intended, you can use `gns3inspector` for an easier way to deploy the same configuration to other routers.\n\n*This tool was written to make your life a little easier using GNS3. It doesn\'t aim to be perfect or solve all the problems GNS3 has. I just wrote it quickly to help my group solve a university assignment easier. Feedback is still welcome, just hmu here on GitHub.*\n\n## Installation\nSimply run `pip install gns3inspector` to install the package. By adding `.local/bin` to your `PATH` variable, you can use the command `gns3inspector` from any directory.\n\n`gns3inspector` uses the readline-library, to make it work make sure `ncurses-dev` is installed via `apt`.\n\n## Usage\nNavigate to your GNS3 project directory (where the `*.gns3`-file is located), and open a terminal there. Then run `gns3inspector` to start the tool. If you opened a valid GNS3-project-directory, you will now see a terminal input `>>> ` indicating that you can now run `gns3inspector` commands to see your project.\n\n## gns3inspector commands\nThe letter in parantesis can be used as a shortcut to run the commands, e.g. `help` will open the help-text, but `h` will also do that.\n- **(h)elp**: Shows a list of the available commands\n- **(l)ist**: Shows all the routers in the current project. It generates abbreviations and id\'s for each router, which can be used to not have to write out the full router name each time.\n- **(s)elect**: select the following device(s) as shown in (l)ist. E.g. TeleStar_R1 or TS_R1 or 3. The id\'s can also be selected as ranges, e.g. 3-5 or 4-9. \nTo select all devices leave the parameter empty, defaults to all devices.\n- **(c)config**: shows all commands in the configuration starting with the provided prefix, e.g. "interface f/." If no parameter is provided, all the startup configuration is shown. \n- **(e)dit**: Like c, but now the selected configuration can be edited in a file called tmp_gns3.txt in the current working directory. **Make sure that all the devices whose configuration you would like to edit are turned off in GNS3 before using this command!**\n- **(r)eload**: reloads all the router\'s startup config files from disk\n- **exit**: or quit, ends the shell \n\n',
    'author': 'Lukas Neuenschwander',
    'author_email': 'fjellvannet@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fjellvannet/GNS3Inspector.git',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
