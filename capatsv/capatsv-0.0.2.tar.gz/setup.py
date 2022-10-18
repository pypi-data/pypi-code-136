from setuptools import setup, find_packages

setup(
	name='capatsv',
	version='0.0.2',
	description='Cellranger ATAC Peak Annotation, sourced from Cellranger ATAC v2.1.0',
	url='https://github.com/Teichlab/capatsv',
	packages=find_packages(),
	install_requires=['six', 'pybedtools'],
	entry_points = {
        "console_scripts": ['capatsv = capatsv.capatsv:main']
    },
	author='Krzysztof Polanski',
	author_email='kp9@sanger.ac.uk',
	license='MIT'
)
