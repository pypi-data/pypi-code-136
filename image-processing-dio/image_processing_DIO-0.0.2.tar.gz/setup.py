from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_DIO",
    version="0.0.2",
    author="my_name",
    author_email="santosunior@gmail.com",
    description="Package basic of processing image",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ernestojr-7/image-processing-DIO",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)