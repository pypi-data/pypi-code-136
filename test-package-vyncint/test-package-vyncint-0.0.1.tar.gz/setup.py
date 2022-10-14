import setuptools

with open("README.md", "r") as fh:
	description = fh.read()

setuptools.setup(
	name="test-package-vyncint",
	version="0.0.1",
	author="vyncint",
    author_email="vyncint@icloud.com",
	packages=["test_package_vyncint"],
	description="A sample test package",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://gitlab.com/vyncint/test-tackage-vyncint",
	license='MIT',
	python_requires='>=3.8',
	install_requires=[]
)
