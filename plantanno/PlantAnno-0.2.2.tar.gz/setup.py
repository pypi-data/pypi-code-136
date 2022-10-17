# coding utf8
import setuptools
from plantanno.versions import get_versions

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="PlantAnno",
    version=get_versions(),
    author="Yuxing Xu",
    author_email="xuyuxing@mail.kib.ac.cn",
    description="An automated process for plant genome annotation",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/SouthernCD/PlantAnno",

    entry_points={
        "console_scripts": ["PlantAnno = plantanno.cli:main"]
    },    

    packages=setuptools.find_packages(),

    install_requires=[
        "toolbiox>=0.0.15",
        "interlap>=0.2.6",
        "bioseqtools>=0.2.0",
    ],

    python_requires='>=3.5',
)