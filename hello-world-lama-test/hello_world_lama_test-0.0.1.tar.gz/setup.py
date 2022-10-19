import setuptools

with open("README.md") as readme_file:
    README = readme_file.read()
    
setuptools.setup(
    name="hello_world_lama_test",
    version="0.0.1",
    author="Lama Alosaimi",
    description="test",
    long_description_content_type="text/markdown",
    long_description=README,
    packages=["hello_world_code"],
    license="MIT",
    keywords=['test'],
    url="https://gist.github.com/lamoboos223/e1b8e3638e3b5eddd01ae0bf2d1c8d73"
)