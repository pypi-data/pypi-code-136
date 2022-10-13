from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name = 'sdk_python_nacos',
    version = '0.0.2',
    author = 'jnan77',        
    author_email = 'jnan77@qq.com',
    url = 'https://pypi.org/project/sdk-python-nacos/',
    description = 'python min nacos client only get config',
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown"
)