from setuptools import setup
import codecs, os

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
     long_description = "\n" + fh.read()

setup(
    name='gquote',
    version='1.0.2',
    install_requires=['pillow', 'requests'],
    include_package_data=True,
    author="Justxd22",
    author_email="xdjust18@gmail.com",
    url="https://github.com/justxd22/gquote",
    readme = "README.md",
    license = "GPLV3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    description=("Generate Beautiful quote images"),
    long_description_content_type="text/markdown",
    long_description=long_description,
    zip_safe=True,
    python_requires=">=3.6",
    project_urls={"Github": "https://github.com/justxd22/gquote"},
    keywords=["quotes", "png", "images", "pillow", "generate"],
)
