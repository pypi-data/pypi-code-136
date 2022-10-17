from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="py_pixel_art_snake_package",
    version="0.0.1",
    author="Calins_e_Marcosvinisilv",
    author_email="caiolima2000@hotmail.com",
    description="Mode used to play snake game in python with pixel art",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Calima94/dio_snake_pkg_create.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
    package_data={
        # If any package contains *.txt or *.csv files, include them:
        '': ['*.ttf', '*.jpeg', '*.png', '*.csv', '*.mp3', '*jpg'],
    }
    ,
)
