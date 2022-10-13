from setuptools import setup

setup(name='MandalaArt',
      version='0.1.0',
      description='This is a package for generating animated mandala art using python Turtle',
      url='https://github.com/meghc27/MandalaArt.git',
      author='Megha Chakraborty',
      author_email='megha.chkbrt@gmail.com',
      packages=['layers', 'designs'],
      install_requires=[
          'numpy', 'turtle', 'python-math', 'random2'
      ])