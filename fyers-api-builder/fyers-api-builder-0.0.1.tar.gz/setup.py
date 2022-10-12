import os

import setuptools

current_directory=os.path.dirname(os.path.realpath(__file__))

print(f'current_directory {current_directory}')

# long_description = (current_directory / "README.md").read_text()
long_description = "test"

setuptools.setup(
  include_package_data = True,
  name = "fyers-api-builder",
  version = "0.0.1",
  description = "Fyers Api V2",
  url = "https://github.com/krunaldodiya/fyers-api-builder",
  author = "Krunal Dodiya",
  author_email = "kunal.dodiya1@gmail.com",
  packages = setuptools.find_packages(),
  install_requires = [
    "requests",
    "fyers-apiv2"
  ],
  long_description = long_description,
  long_description_content_type = "text/markdown",
  classifiers =[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent"
  ]
)
