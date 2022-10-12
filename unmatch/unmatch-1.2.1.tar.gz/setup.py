# from setuptools import setup
#
# setup(name='unmatch',
#       version='1.0.0',
#       description='ungreat matching of strings module',
#       packages=['unmatch'],
#       author_email='ldr200@mail.ru',
#       zip_safe=False)


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unmatch", # Replace with your own username
    version="1.2.1",
    author="Fallen Nephalem",
    author_email="ldr200@mail.ru",
    description="ungreat matching of strings module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FallenNephalem/ungreat_matching",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='MIT',
    include_package_data=True,
    zip_safe=False
)
