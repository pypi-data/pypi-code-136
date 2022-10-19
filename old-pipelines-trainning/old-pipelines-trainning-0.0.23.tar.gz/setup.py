import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="old-pipelines-trainning",
    version="0.0.23",
    author="JuanMaTB",
    author_email="jm.torrado.borrachero@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
       'coloredlogs',
   ],
)