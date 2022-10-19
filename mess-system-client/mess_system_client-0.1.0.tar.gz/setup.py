from setuptools import setup, find_packages

setup(name="mess_system_client",
      version="0.1.0",
      description="Mess_System Client",
      author="Stasy_Kadr",
      author_email="holy_night@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      )
