from setuptools import setup
from codecs import open
from os import path
import re
package_name = "yagamee"
root_dir = path.abspath(path.dirname(__file__))


def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, "requirements.txt")).readlines()]


with open(path.join(root_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(
        r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

setup(
    name=package_name,
    version=version,
    description="理系大学生のためのレポート作成支援ツール",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mya-Mya/yagamee",
    author="Mya-Mya",
    author_email="",
    license="MIT",
    keywords="matplotlib, graphing, report, report-making, university, science",
    packages=[package_name],
    install_requires=_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
