from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.1"
DESCRIPTION = "Arabic Spell Checker And Corrector Using NLP"
LONG_DESCRIPTION = "Arabic Spell Checker And Corrector Using NLP"

# Setting up
setup(
    name="julan_nasser",
    version=VERSION,
    author="Julan_Nasser",
    author_email="Julan-Nasser@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=["nlp", "ar-nlp", "nlp-ar", "ar spell check", "ar spell corrector"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    package_data={'': ['./resources/*.pickle']},
)