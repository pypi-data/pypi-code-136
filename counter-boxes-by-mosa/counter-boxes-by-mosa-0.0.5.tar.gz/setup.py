import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="counter-boxes-by-mosa",
    version="0.0.5",
    author="mo_mosa",
    author_email="mohamedmosa.work@gmail.com",
    description="this is for counting boxes from vidoes as a computer vision problem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m7mdmosa27/counter_boxes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)