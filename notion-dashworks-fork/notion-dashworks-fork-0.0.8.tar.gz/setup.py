from xml.etree.ElementInclude import include
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements(fname):
    "Takes requirements from requirements.txt and returns a list."
    with open(fname) as fp:
        reqs = list()
        for lib in fp.read().split("\n"):
            # Ignore pypi flags and comments
            if not lib.startswith("-") or lib.startswith("#"):
                reqs.append(lib.strip())
        return reqs


install_requires = get_requirements("requirements.txt")

setuptools.setup(
    name="notion-dashworks-fork",
    version="0.0.8",
    author="Developers Dashworks",
    author_email="support@dashworks.ai",
    description="Unofficial Python API client for Notion.so forked for dashworks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dashworkstech/notion-dashworks",
    install_requires=install_requires,
    include_package_data=True,
    package_data={"notion": ["py.typed"]},
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
