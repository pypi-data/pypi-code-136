import pathlib

from setuptools import setup, find_packages

dir = pathlib.Path(__file__).parent.resolve()
version = "0.0.0.dev29"

long_description = (dir / "README.rst").read_text(encoding="utf-8")
requirements = [
    "numpy",
    "pandas",
    "nltk",
    "scipy",
    "smart_open",
    "tensorflow",
    "sklearn",
    "matplotlib",
    "statsmodels",
    "pythainlp",
    "pyspellchecker",
    "fairseq",
    "tensorboardX",
    "jupyter",
    "ipywidgets",
    "widgetsnbextension",
    "pandas-profiling",
    "xlrd",
    "gdown",
    "dill",
]

setup(
    name="doyle",
    version=version,
    description="doyle description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/62090500409/doyle",
    author="Thanaphit S.",
    author_email="thanaphit.su@mail.kmutt.ac.th",
    license="Unlicense",
    classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Framework :: IPython",
            "Framework :: Jupyter :: JupyterLab",
            "License :: OSI Approved :: The Unlicense (Unlicense)",
            "Natural Language :: English",
            "Natural Language :: Thai",
            "Programming Language :: Python :: 3.7"
        ],
    package_dir={"doyle": "doyle"},
    packages=find_packages(),
    include_package_data=True,
    package_data={"": [
        "statics/category_variable_conf_30-1500_viznet_dataset_threshold.bin", 
        "statics/fsign.json"
        ]},
    python_requires="==3.7",
    install_requires=requirements,
)
