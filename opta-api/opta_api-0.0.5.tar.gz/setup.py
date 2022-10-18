from setuptools import setup, find_packages

setup(name='opta_api',
      version='0.0.5',
      description='API wrapper for OPTA/StatsPerform',
      packages=find_packages(),
      extras_require={
            "test": ["pytest>=3.7", "pandas>=1.0.0"]
      }
     )
