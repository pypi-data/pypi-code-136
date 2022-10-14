import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monitor_utility",
    version="0.0.18",
    author="vSir",
    author_email="weiguo341@gmail.com",
    description="simple tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nevquit/monitor_utility",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'iWAN','iWAN_Request','pubkey2address','substrate-interface==1.1','websocket-client==0.58.0',"BalanceSpider","multicall==0.1.2","web3==5.28.0"
    ]
)