import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Cryptem",
    version="0.0.3",
    author="emendir",
    description="Cryptographic applications library based on elliptic curve cryptography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ipfs.io/ipns/k2k4r8ld8q6344t8dop0rwuk8f3vhpo42un6zrnrffogaayr7xv59p83",

    project_urls={
        "Source Code on IPFS": "https://ipfs.io/ipns/k2k4r8ld8q6344t8dop0rwuk8f3vhpo42un6zrnrffogaayr7xv59p83",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # 'package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    py_modules=['Cryptem'],
    install_requires=['eciespy', 'coincurve', 'cryptography'],
)
