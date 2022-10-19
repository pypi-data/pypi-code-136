from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()


setup(name='pymetrick',
      version='0.76.0',
      description='Lightweight web framework',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
              'Development Status :: 5 - Production/Stable',
              'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              'Environment :: Web Environment',
              'Topic :: Internet :: WWW/HTTP :: WSGI',
            ],
      url='https://pythonhosted.org/pymetrick/',
      author='Fco. Javier Tamarit V',
      author_email='javtamvi@gmail.com',
      maintainer='Fco. Javier Tamarit V',
      maintainer_email='pymetrick@pymetrick.org',
      license='GNU/GPLv3',
      packages=['pymetrick'],
      install_requires=['openpyxl>=3.0.0','pillow>=4.0.0','mysql-connector-python==8.0.28','qrcode','pyaes','six>=1.15.0','boto3==1.23.9','botocore==1.26.9','zeep'],
      include_package_data=False,
      zip_safe=False)

