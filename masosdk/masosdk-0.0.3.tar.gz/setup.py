from setuptools import setup

setup(name='masosdk',
      version='0.0.3',
      description='Software Development Kit for Maso',
      author='Tomas Psorn',
      author_email='tomaspsorn@isibrno.cz',
      url='https://www.isibrno.cz',
      packages=['masosdk',],
      install_requires=['numpy', 'requests'],
      include_package_data=True,
      license='GPL',
      zip_safe=False
     )

