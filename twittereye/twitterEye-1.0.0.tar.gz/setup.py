from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='twitterEye',
  version='1.0.0',
  description='Analyze and visualize how public is reacting to a certain topic on Twitter',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),  
  url='',  
  author='Hinan Bilal',
  author_email='hinanbilalshah@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='twitter sentimentanalysis visualization', 
  packages=find_packages(),
  install_requires=['tweepy', 'textblob', 'matplotlib'] 
)
