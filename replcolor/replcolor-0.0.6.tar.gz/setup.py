import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read() # Your README.md file will be used as the long description!

setuptools.setup(
    name="replcolor", # Put your username here!
    version="0.0.6", # The version of your package!
    author="Nathan T", # Your name here!
    author_email="self@dreamclient.us", # Your e-mail here!
    description="rgb colors for replit", # A short description here!
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/@1gn/rcsrc", # Link your package website here! (most commonly a GitHub repo)
    packages=setuptools.find_packages(), # A list of all packages for Python to distribute!
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Enter meta data into the classifiers list!
    python_requires='>=3.6', # The version requirement for Python to run your package!
)
