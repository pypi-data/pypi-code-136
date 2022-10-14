from setuptools import setup

setup(
	name='easy_geppy',
	version='0.1.0',
	description='A example Python package',
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
						],

	classifiers=[
		'Development Status :: 1 - Planning',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.8',
	],
)
