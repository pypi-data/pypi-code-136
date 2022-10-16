import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'numpy>=1.19.5',
    'tqdm==4.60.0',
    'jsonpickle==2.0.0'
]

setuptools.setup(
    name="jjy", # Replace with your own username
    version="0.0.3.5",
    author="jjy37777",
    author_email="jjy37777@naver.com",
    description="jjy ai framework",
    long_description=long_description,
    install_requires=install_requires,
    long_description_content_type="text/markdown",
    url="https://github.com/woduq1414/deep-learning-without-framework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# python setup.py sdist bdist_wheel


#python -m twine upload dist/*

