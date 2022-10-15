import versioneer
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='translator_json',
    packages=find_packages(include=['translator']),
    description='A translator for Json info',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Florent Simonnot',
    author_email='contact@gwanly.fr',
    url='https://gitlab.com/FlorentSimonnot1/translator',
    install_requires=REQUIREMENTS,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    use_scm_version=True,
    data_files=[('.', ['requirements.txt'])],
    entry_points={
        'console_scripts': [
            'json_translator=translator.translate_generator:json_translator'
        ]
    },
    include_package_data=True,
    project_urls={
        'Source': 'https://gitlab.com/FlorentSimonnot1/translator',
    }
)
