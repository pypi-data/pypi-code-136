from distutils.core import setup

with open('version', 'r') as f:
      version = f.readlines()[0]

setup(name='boxtec',
      version = version,
      # py_modules=['utils'],
      packages=['boxtec'],
      data_files=['version'],
      install_requires=['pytz', 'mysql.connector'],
      )