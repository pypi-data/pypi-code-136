# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['investiny']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'pydantic>=1.10.2,<2.0.0']

extras_require = \
{'docs': ['mkdocs>=1.4.0,<2.0.0',
          'mkdocs-material>=8.5.4,<9.0.0',
          'mkdocs-git-revision-date-localized-plugin>=1.1.0,<2.0.0',
          'mkdocstrings[python]>=0.19.0,<0.20.0']}

setup_kwargs = {
    'name': 'investiny',
    'version': '0.6.0',
    'description': '🤏🏻 `investpy` but made tiny.',
    'long_description': '# 🤏🏻 `investiny` is `investpy` but made tiny\n\n**`investiny` is faster, lighter, and easier to use** than `investpy`.\n\n`investiny` has been created due to the latest Investing.com changes in their API protection protocols, as \nnow their main APIs are Cloudflare V2 protected. Anyway, there are still some APIs working fine, so this package\nhas been created as a temporary replacement for `investpy` while we get to an agreement to continue the development\nof `investpy`. In the meantime, anyone can use `investiny` as I\'m actively working on it, and ideally, it should support\nmost of the functionality provided by `investpy`.\n\n\n---\n\n## 🤔 What are the differences with `investpy`?\n\n**`investiny` is faster, lighter and easier to use**, but with reduced functionality for the moment. `investiny` \nlets you retrieve historical data from Investing.com through `historical_data` and search any available asset\nthrough `search_assets`, while `investpy` offers more functions to also retrieve technical indicators, economic\ncalendars, dividends, etc. but those will come at some point to `investiny` too.\n\n`investiny` introduces intraday data, so the specified intervals when retrieving historical data for any asset\navailable at Investing.com goes from 1 minute to monthly data.\n\n`investpy` uses Investing.com\'s APIs at https://www.investing.com/instruments/HistoricalDataAjax and at\nhttps://api.investing.com/api/financialdata/historical, that are Cloudflare protected and not working any more,\nas you\'ll end up getting blocked with 403 Forbidden HTTP code; while `investiny` is using https://tvc4.investing.com/,\nwhich seems to be more reliable right now according to the ran tests, as well as providing intraday data.\n\n| | Intraday Data | Any Range Historical Data | Search Assets/Quotes | Dividends | Economic Calendar | Technical Indicators | Economic News |\n|:--:|--:|--:|--:|--:|--:|--:|--:|\n| **investiny** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |\n| **investpy**  | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |\n\n---\n\n## 🛠️ Installation\n\n`investiny` requires Python 3.8+ and can be installed with `pip` as it follows:\n\n`pip install investiny`\n\n---\n\n## 💻 Usage\n\nRetrieve historical data from Investing.com using the Investing.com ID of the asset\nthat you want to retrieve the data from.\n\n```python\nfrom investiny import historical_data\n\ndata = historical_data(investing_id=6408, from_date="09/01/2022", to_date="10/01/2022") # Returns AAPL historical data as JSON (without date)\n```\n\nThere\'s also a function to look for assets in Investing.com, that also lets you retrieve\nthe Investing.com ID that you can, later on, use in `historical_data` as an input parameter.\n\n```python\nfrom investiny import search_assets\n\nresults = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ") # Returns a list with all the results found in Investing.com\n```\n\nAs `search_assets` returns a list of results, you can check each of them, retrieve the `ticker` from the\nasset that you want to retrieve historical data from and pass it as a parameter to `historical_data`. So on, the\ncombination of both functions should look like the following:\n\n```python\nfrom investiny import historical_data, search_assets\n\nsearch_results = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ")\ninvesting_id = int(search_results[0]["ticker"]) # Assuming the first entry is the desired one (top result in Investing.com)\n\ndata = historical_data(investing_id=investing_id, from_date="09/01/2022", to_date="10/01/2022")\n```\n\n\n## ⚠️ Disclaimer\n\nInvesting.com is a registered trademark of Investing.com, and its services are offered by Fusion Media Limited.\n\nNeither `investpy` nor `investiny` is affiliated, endorsed, or vetted by Investing.com.\n\nBoth `investpy` and `investiny` are open-source packages that use Investing.com\'s available data, intended for research and educational purposes only.\n\nYou should refer to Investing.com\'s terms and conditions at https://www.investing.com/about-us/terms-and-conditions for details on your rights to use the actual data, as it is intended for personal use only.\n',
    'author': 'Alvaro Bartolome',
    'author_email': 'alvarobartt@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alvarobartt/investiny',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
