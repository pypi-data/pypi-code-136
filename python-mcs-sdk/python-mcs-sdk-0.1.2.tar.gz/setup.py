from setuptools import setup, find_packages

setup(name="python-mcs-sdk",
      version="0.1.2",
      description="A python software development kit for the Multi-Chain Storage",
      author="daniel8088",
      author_email="danilew8088@gmail.com",
      install_requires=["web3", "requests", "requests_toolbelt", "python_dotenv"],
      packages=["mcs", "mcs.api", "mcs.contract", "mcs.contract.abi", "mcs.common", "mcs.upload"],
      license="MIT",
      include_package_data=True
      )
