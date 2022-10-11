from setuptools import setup, find_packages


setup(
    name="ice-commercial-power",
    version="0.1",
    description="ICE Commercial Power",
    url="https://github.com/IceCommercialPower/azure-function-spike-detector",
    author="ICE Commercial Power",
    maintainer="ICE Commercial Power",
    install_requires=[
        "pydantic>=1.8.2",
        "azure-cosmos>=4.2.0",
        "azure-appconfiguration>=1.3.0",
        "azure-servicebus>=7.4.0",
        "opencensus-extension-azure-functions>=1.0.0",
        "opencensus-ext-requests>=0.7.6",
        "requests>=2.25.1",
        "twilio>=7.3.2",
        "azure-identity==1.7.1",
    ],
    author_email="",
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
)
