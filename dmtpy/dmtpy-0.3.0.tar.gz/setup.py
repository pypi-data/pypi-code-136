from pathlib import Path
import shutil
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


# Remove build and dist folders
shutil.rmtree(Path("build"), ignore_errors=True)
shutil.rmtree(Path("dist"), ignore_errors=True)

setup(
    name="dmtpy",
    version="0.3.0",
    author="SINTEF Ocean",
    description="Python runtime library for SIMOS based DMT models",
    url="https://github.com/SINTEF/dmtpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests"]),
    install_requires=[
        "h5py",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
