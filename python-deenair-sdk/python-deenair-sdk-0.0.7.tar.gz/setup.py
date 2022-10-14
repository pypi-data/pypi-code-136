from setuptools import setup, find_packages

setup(
    name='python-deenair-sdk',
    version="0.0.7",
    description="pythod-deenair-sdk. Base python library to interact with DeenAiR blockchain.",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    author="DeenAiR Labs",
    author_email="social@deenair.org",
    url="https://github.com/deenair-labs/python_deenair_sdk",
    install_requires=[
        'base58~=2.1.1',
        'requests~=2.28.1',
        'bip-utils',
        'mnemonic',
        'setuptools',
        'python-dateutil',
        'pynacl==1.5.0',
    ],
    python_requires=">=3.7, <4",
    py_modules=["python_deenair_sdk"],
    license="MIT",
    keywords="DeenAiR",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

                 ]

)
