from setuptools import setup, find_namespace_packages

# read requirements/dependencies
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# read description/README.md
with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(name='c2s2',
      version='0.1.0',
      packages=find_namespace_packages(include=['c2s2.*']),
      install_requires=requirements,

      package_data={'': ['test_data/*']},
      long_description=long_description,
      long_description_content_type='text/markdown',

      author='Lex Dingemans, Daniel Danis',
      author_email='a.dingemans@radboudumc.nl',
      url='https://github.com/monarch-initiative/C2S2',
      description='Consensus clustering for a number of individuals with HPO terms or phenopackets.',
      license='BSD 3',
      keywords='clustering, HPO terms, phenopackets',
      zip_safe=False

      # entry_points={'console_scripts': [
          # 'c2s2 = c2s2.main:main'
      # ]}
      )
