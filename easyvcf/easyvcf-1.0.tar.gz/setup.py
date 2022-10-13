from setuptools import setup

setup(name='easyvcf',
      version='1.0',
      description='Easily convert data in csv to vcf contacts!',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      keywords='python utaa thkü ieee easyvcf vcf csv convert dogukan meral',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
       	  'Operating System :: MacOS',
          'Programming Language :: Python :: 3.8',
	  'Topic :: Communications',
	  'Topic :: Database',
	  'Topic :: Office/Business :: Groupware',
          'Topic :: Utilities',
          ],
      url='http://github.com/dogumer/easyvcf',
      author='Dogukan Meral',
      author_email='dogukan.meral@yahoo.com',
      license='MIT',
      include_package_data=True,
      packages=['easyvcf'],
      entry_points = {
          'console_scripts': ['easyvcf=easyvcf.command_line:main'],
          },
      install_requires=[
          ],
      zip_safe=False)