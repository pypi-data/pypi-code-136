import setuptools

with open("README.md", 'r') as f:
  long_description = f.read()

setuptools.setup(
  include_package_data = True,
  name = "fyers-api-builder",
  version = "0.0.4",
  description = "Fyers Api Builder",
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
