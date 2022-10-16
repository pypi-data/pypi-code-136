from setuptools import setup
from pathlib import Path

def read(file_name):
	return (Path(__file__).parent / file_name).read_text()

setup(
	name='easy_geppy',
	version='0.1.1',
	description='EasyGeppy is an easy to use programming interface for Geppy',
	long_description=read('README.md'),
	long_description_content_type='text/markdown',
	url='https://github.com/edvieira/EasyGeppy',
	author='Eduardo Henrique Vieira dos Santos',
	author_email='edvieira@github.com',
	license='GPL-3.0 license',
	packages=[
		'easy_geppy',
		],
	install_requires=[
						'deap>=1.3.3',
						'dill>=0.3.5.1',
						'geppy>=0.1.3',
						'numpy',
						'pandas>=1.3.4',
						'sympy',
						'graphviz'
						],

	classifiers=[
		'Development Status :: 1 - Planning',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Programming Language :: Python :: 3',
	],
)
