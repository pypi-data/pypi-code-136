from setuptools import setup, find_packages
 
 
 
setup(name='zp_config',
 
      version='0.0.1',
 
      url='https://github.com/',
 
      license='MIT',
 
      author='Ziuzin Pavel',
 
      author_email='zpavel.77@mail.ru',
 
      description='Manage configuration files',
 
      packages=find_packages(exclude=['tests']),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
 
      setup_requires=['argparse'],
 
      test_suite='nose.collector')