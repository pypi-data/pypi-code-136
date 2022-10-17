from setuptools import setup, find_packages

setup(name='opta_api',
      version='0.0.3',
      description='API wrapper for OPTA/StatsPerform',
      packages=find_packages(where="src"),
      package_dir={'': 'src'},
      extras_require={
            "test": ["pytest>=3.7", "pandas>=1.0.0"]
      }
      )
