import requests
global tpypi, pypi
try:
  pypi = requests.get("https://pypi.org/pypi/capylang/json").json()['info']['version']
  tpypi = requests.get("https://test.pypi.org/pypi/capylang/json").json()['info']['version']
except:
  raise Exception("Could not check version")
def check(__version__):
  if pypi != __version__:
    if __version__ < pypi:
      print(f"Capylang has a PyPI update! Version: {pypi}, update via capy.update()")
  elif tpypi != __version__:
    if __version__ < tpypi:
      print(f"Capylang has a TestPyPI update! Version: {tpypi}, update via capy.update()")