import setuptools
with open(r'C:\Users\Finn\Desktop\Pypi\tempMailApi\pytempmailsapi\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='py-temp-mails-api',
	version='1.03',
	author='Fitrad3w',
	author_email='onigirisell@protonmail.com',
	description='pyTempMailsApi is a library that allows you to easily interact with the site https://temp-mail.org/',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/onigirisell/pyTempMailsApi',
	packages=['pytempmailsapi'],
	install_requires= ['grequests', 'requests'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)