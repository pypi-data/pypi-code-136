from setuptools import setup

setup(
  name='colorbytes',
  version='1.0.1',
  description='A simple module to make your Python code come alive with color.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='',  
  author='',
  author_email='',
  license='MIT', 
  keywords='colorbytes', 
  packages=['colorbytes',],
  install_requires=[
    'pynput',
    'colr',
    'pyperclip',
    'psutil',
    'colorama'] 
)