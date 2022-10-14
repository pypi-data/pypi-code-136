import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amunpy",
    version="0.9.8",
    author="Grzegorz Kowal",
    author_email="grzegorz@amuncode.org",
    description="Python Interface for the AMUN code's snapshots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.amuncode.org/",
    project_urls={
        "Bug Tracker": "https://bitbucket.org/amunteam/amun-code/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['h5py', 'numpy', 'xxhash', 'lz4', 'zstandard'],
    extras_require={
        "interpolation": ['scipy'],
    }
)
