from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='brainmaps',
    version='0.0.4',
    author_email="alex@harston.io",
    description="A command-line client to the BrainMaps platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexharston/brainmaps-cli",
    license="MIT",
    python_requires='>=3',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='brainmaps, brainmaps-api, atlas, anatomy',
    py_modules=['brainmaps-cli'],
    install_requires=[
        'Click',
        'numpy',
        'scipy',
        'requests',
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        brainmaps=brainmaps.client:cli
    ''' 
)

