import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="dicom_cnn",
    version="0.0.2",
    author="Pixilib",
    url="https://github.com/Pixilib/dicom_cnn",
    python_requires="~=3.9",
    description="Librairie to sort - process dicom to feed CNN models",
    packages=setuptools.find_packages(where='src'),    # List of all python modules to be installed
    install_requires=required,
    package_dir={"": "src"}
)