
import io
from setuptools import find_packages, setup

setup(
	name				= "ftcircuitsynthesis",
	version				= '0.0.1',
	description			= 'fault tolerant circuit synthesis for universal fault-tolerant quantum computing based on concatenated codes',
	author 				= 'Yongsoo Hwang',
	author_email 		= 'yhwang@etri.re.kr',
	install_requires 	= ['simplejson', 'icecream', 'qubitmapping', 'userproperty'],
	packages 			= find_packages(),
	zip_safe 			= False,
	python_requires 	= '>=3'
	)