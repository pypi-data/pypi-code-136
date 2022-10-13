from setuptools import setup, find_packages

# Load the long_description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hte',
    version='0.0.21',
    author="Eirik Berger",
    author_email="eirik.berger@gmail.com",
    description="Extracting content from spesific address books",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
        'PyPDF2',
        'pdf2image',
        'pytesseract',
        'tesseract',
        'tqdm',
        'scikit-image',
        'opencv-python',
        'pytest-shutil',
        'pandas',
        'numpy',
        'pillow',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
