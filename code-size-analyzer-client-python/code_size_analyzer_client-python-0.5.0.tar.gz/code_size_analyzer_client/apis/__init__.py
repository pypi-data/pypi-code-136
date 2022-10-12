
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from code_size_analyzer_client.api.analyzer_api import AnalyzerApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from code_size_analyzer_client.api.analyzer_api import AnalyzerApi
from code_size_analyzer_client.api.default_api import DefaultApi
from code_size_analyzer_client.api.parser_api import ParserApi
from code_size_analyzer_client.api.results_api import ResultsApi
