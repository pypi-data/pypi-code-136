from distutils.core import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'siricoin',         # How you named your package folder (MyLib)
  packages = ['siricoin'],   # Chose the same as "name"
  version = '0.9',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'F SiriCoin',   # Give a short description about your library
  author = 'SiriCoin F***kYOU',                   # Type in your name
  author_email = 'siricoinFYOU@pichisdns.com',      # Type in your E-Mail
  url = 'https://pypi.org/projects/siricoin',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['siricoin'],
  long_description=long_description,
  long_description_content_type='text/markdown'
)
