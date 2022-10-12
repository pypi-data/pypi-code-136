import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="TmpVar",
    version="0.0.1",
    author="Blockhead-yj",
    author_email="136271877@qq.com",
    description="create a temporary environment to run some code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blockhead-yj/TmpVar",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)
