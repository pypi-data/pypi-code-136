import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")
setup(name='commugen_api',
      version='0.4',
      description='Python wrapper for commugen api',
      url='https://bitbucket.org/kobi_commugen/commugen_api/',
      author='kobi kolodner',
      author_email='kobi@commugen.com',
      license='MIT',
      packages=['commugen_api'],
      install_requires=[
            'requests',
            'tablib'
      ],
      classifiers=[
            'Development Status :: 2 - Pre-Alpha'
      ],
      long_description=long_description,  # Optional
      long_description_content_type="text/markdown",  # Optional (see note above)

)