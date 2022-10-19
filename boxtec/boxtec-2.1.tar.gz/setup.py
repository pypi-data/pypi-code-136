from distutils.core import setup
import os
import glob

def increment_version():
      with open('version', 'r') as f:
            version = f.readlines()
            full, release = version[0].split('.')
            release = int(release) +1
      with open('version', 'w') as f:
            version = f'{full}.{release}'
            f.write(version)

      return version

for f in glob.glob('dist/*'):
      os.remove(f)

setup(name='boxtec',
      version=increment_version(),
      # py_modules=['utils'],
      packages=['boxtec'],
      data_files=['version'],
      install_requires=['pytz', 'mysql.connector'],
      )