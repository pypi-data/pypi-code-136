import os

from distutils.core import setup

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

setup(
  name = 'aws_secrets_dict',
  packages = ['aws_secrets_dict'],
  version = '1.1.0',
  license='MIT',
  description = 'A class allowing you to interact with the AWS Secrets Manager with python dictionary syntax.',
  long_description=read_file('README.md'),
  long_description_content_type='text/markdown',
  author = 'David Carli-Arnold',
  author_email = 'davocarli@gmail.com',
  url = 'https://github.com/davocarli/aws_secrets_dictionary',
  keywords = ['AWS', 'AWS Secrets', 'aws-secrets', 'dictionary', 'class'],
  install_requires=[
          'boto3',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
