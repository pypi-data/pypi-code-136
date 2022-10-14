from setuptools import find_packages, setup

setup(
    name="py3_slack_notify",
    packages=find_packages(include=["py_slack_notify"]),
    version="0.4.1",
    description="Python package for sending notification to Slack in thread with emoji",
    author="thaopn",
    url="https://github.com/ThaoPN/py_slack_notify",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    test_suite="",
)
