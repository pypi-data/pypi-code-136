from setuptools import setup, find_packages

setup(name="maya_mess_server",
      version="0.4.3",
      description="Maya Mess Server",
      author="Maya",
      author_email="maya@dihalt.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      # scripts=['server/server_run']
      )
