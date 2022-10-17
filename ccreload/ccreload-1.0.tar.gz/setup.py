from setuptools import setup,find_packages
setup(name='ccreload',
      version='1.0',
      description='chen\'s autoreload script package',
      author='chen',
      author_email='690246265@qq.com',
      requires=[],
      packages=find_packages(),
      license="apache 3.0",
      package_data={"":['*.yaml']}
      )
