from distutils.core import setup
setup(
    name = 'pymellon',
    packages = ['pymellon'],
    version = '0.2.13',
    description = 'A python binding to work with the Mellanox API',
    author = 'Rick Kauffman',
    author_email = 'rick@rickkauffman.com',
    url = 'https://github.com/xod442/pymellon',
    download_url = 'https://github.com/xod442/pymellon/archive/refs/tags/v.0.2.13.tar.gz',
    keywords = ['mellanox', 'api', 'python'],
    install_requires=[
          'requests',
          'urllib3',
      ],
    classifiers = [],
)
