from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="dash-addons",
    version="0.0.4",
    author="Jia-Yau Shiau",
    author_email="jiayau.shiau@gmail.com",
    description="Additional toolbox for Plotly Dash",
    url="https://github.com/Janus-Shiau/dash_addons",
    packages=setuptools.find_packages(),
    entry_points={},
    include_package_data=True,
    package_data={},
    python_requires=">=3.7",
    license="Apache Software License (Apache-2.0)",
    install_requires=["dash", "numpy", "Pillow"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
