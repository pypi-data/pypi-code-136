# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['capylang',
 'capylang.core',
 'capylang.date',
 'capylang.decorators',
 'capylang.http',
 'capylang.terminal']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0', 'numpy>=1.22.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'capylang',
    'version': '1.1.0',
    'description': "Python's little programming language.",
    'long_description': '# Capylang\n### Capylang is a pretty simple language.\n### Regular Examples\n```python\nfrom capylang import capy\nmycapy = capy(id="MyCapy",printinst=True) # ID is for identification of Capylang Instances, and printinst prints the ID\nprint(mycapy.__doc__) # Returns help\na = 4\nb = 3\nprint(str(mycapy.add(a,b))) # Prints 7 (also uses the add function)\nprint(str(mycapy.minus(a,b))) # Prints 1 (also uses the subtract function)\nprint(str(mycapy.multi(a,b))) # Prints 12 (also uses the multiply function)\nprint(str(mycapy.div(a,b))) # Prints 2.3 (average, also uses the divide function)\nprint(str(mycapy.hyp(a,b))) # It returns the hypotenuse of opp, and adj\nprint(str(mycapy.opp(a,b))) # Try this yourself for more info, check mycapy.__doc__\nprint(str(mycapy.adj(a,b))) # Try this yourself for more info, check mycapy.__doc__\n```\n### Decorators (Make your own Capylang if you feel lazy or want to!)\n```python\nimport capylang\n@capylang.decorators.add # Equivalent to mycapy.add\ndef myadd(a,b,c):\n  return a,b,c # The decorator does it all for ya.\n\nprint(myadd(1,2,3))\n# Basicallly everything above. Add, minus, multi, div, hyp, opp, and adj. Fibonacci is here.\n```\n### DateTime alternative\n```python\nimport capylang\ndate = "1/16/1921" # MM/DD/YYYY (January 16th 1921)\nmydate = capylang.date.new(date)\nprint(mydate)\nprint(mydate.text())\n#\n```\n### Clearing on Terminals\n```python\nimport capylang\ncapylang.terminal.os_clear() # Clear with the os module\ncapylang.terminal.replit_clear() # Clear with the replit module\n```\n### Fibonacci Sequence\n```python\nfrom capylang import capy\n# The fibonacci sequence function returns numbers in the fibonacci sequence, it contains 2 args:\n# num_of_nums: the number of sequence numbers you\'d like to generate (required)\n# index: to return a specific number in the sequence (optional)\nfibo = capy(printinst=True,id="Fibonacci Sequence")\nprint(fibo.nacci(num_of_nums=10,index=6))\n```\n### Math string evaluation\n```python\n# Coming in decorators soon.\nfrom capylang import capy\neval = capy(printinst=True,id="Evaluation")\nprint(eval.calc("6/2*(1+2)")) # 9\n```\n### That\'s pretty much it for a basic tutorial of Capylang.',
    'author': 'Kia Kazemi',
    'author_email': 'kia@anistick.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0',
}


setup(**setup_kwargs)
