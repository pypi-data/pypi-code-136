from setuptools import setup, find_packages

setup(

    name='cleancourt',
    version='0.5.1',
    description='a library for cleaning court docket entries',
    author='Logan Pratico',
    author_email='praticol@lsc.gov',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        ],
    keywords="name standardization, plaintiff names, court data, name cleaning",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9, <4",
    install_requires=["sklearn", "loguru", "probablepeople", "rapidfuzz", "tqdm", "pandas", "sparse-dot-topn", "ftfy"],
    project_urls={
            

        },

        )
