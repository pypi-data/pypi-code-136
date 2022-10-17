from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Dio_package_house_rocket_project",
    version="0.0.1",
    author="Francisco Moriya",
    author_email="frmoriya@gmail.com",
    description="Real estate sales recomnendation project",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frmoriya/house-rocket-project.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
)