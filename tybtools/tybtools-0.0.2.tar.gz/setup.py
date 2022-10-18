# @Author: Tang Yubin <tangyubin>
# @Date:   2022-06-19T11:59:03+08:00
# @Email:  tang-yu-bin@qq.com
# @Last modified by:   tangyubin
# @Last modified time: 2022-06-19T16:26:21+08:00
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tybtools",
    entry_points={"console_scripts": ["cv_tools=cv_tools:main"]},
    version="0.0.2",
    author="Tang Yubin",
    author_email="tang-yu-bin@qq.com",
    description="tools for cv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/aierwiki/easytrain",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)