from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="virtual_image_clara",
    version="0.0.1",
    author="Clara Guandalini",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/claraalcina/projeto-image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)