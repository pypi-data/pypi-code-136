import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
	name='LoupeTool',
	version='0.1.20',
	description='',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=setuptools.find_packages(),
	install_requaires=['pandas>=1.3.4', 'numpy>=1.21.3', 'sklearn>=0.0'],
	include_package_data=True,
)