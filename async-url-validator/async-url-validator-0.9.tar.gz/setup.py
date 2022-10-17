from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="async-url-validator",
      version="0.9",
      description="Async python package and CLI command for URL validation.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Aleksandr Gavrilov",
      author_email='sanya-991@mail.ru',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="MIT",
      url="http://github.com/cfytrok/async-url-validator",
      packages=find_packages(),
      install_requires=['aiohttp', 'asyncio-throttle', 'yarl'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.5',
      entry_points={
          'console_scripts':
              ['async_url_validator = async_url_validator.url_validator:main']
      },
      test_suite='tests'
      )
