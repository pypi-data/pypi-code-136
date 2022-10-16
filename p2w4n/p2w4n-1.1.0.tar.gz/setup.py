from setuptools import setup, find_packages
import p2w4n

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (
    name="p2w4n",
    version=p2w4n.__version__,
    author="Learner Chen",
    author_email="learner.chen@icloud.com",
    description="Convert PDF/PPT(X) file word document readfy for import into Notion.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="NO-DISTRIBUTION",
    url="https://www.3thinking.cn/p2w4n/",
    # packages=find_packages(),
    packages=['p2w4n'],
    package_dir={'p2w4n': 'p2w4n'},
    entry_points={'console_scripts': ['p2w4n = p2w4n.__main__:main']},
    include_package_data=True,
    install_requires=[
        "PyMuPDF==1.20.2",
        "pywin32==304"        
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7"
    ]
)