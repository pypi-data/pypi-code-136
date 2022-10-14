import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='youless_api',
      version='1.0',
      description='A bridge for python to the YouLess sensor',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://bitbucket.org/jongsoftdev/youless-python-bridge/src/master/',
      author='G. Jongerius',
      license='MIT',
      packages=setuptools.find_packages(exclude=("test",)),
      zip_safe=False)
