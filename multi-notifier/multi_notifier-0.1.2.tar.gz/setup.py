import typing

import setuptools


def load_req() -> typing.List[str]:
	with open('requirements.txt') as f:
		return f.readlines()


setuptools.setup(
	name="multi_notifier",
	version="0.1.2",
	author="Seuling N.",
	description="notify multiple recipients on multiple protocols",
	long_description="notify multiple recipients on multiple protocols",
	packages=setuptools.find_packages(exclude=["tests*"]),
	install_requires=load_req(),
	python_requires=">=3.10",
	license="multi_notifier currently has no license model."
)
