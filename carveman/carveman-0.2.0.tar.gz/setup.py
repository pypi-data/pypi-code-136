from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="carveman",            
    version="0.2.0",
    author="5f0",
    url="https://github.com/5f0ne/carveman",
    description="File carving for pictures, documents and other files based on it's file signatures",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    package_data={

    },
    install_requires=[
       "hash_calc"
    ],
     entry_points={
        "console_scripts": [
            "carveman = carveman.__main__:main"
        ]
    }
)
