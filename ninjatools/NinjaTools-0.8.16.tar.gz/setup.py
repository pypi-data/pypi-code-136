import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NinjaTools",
    version="0.8.16",
    author="Nikko Gonzales",
    author_email="nikkoxgonzales@gmail.com",
    description="Bunch of useful tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikkoxgonzales/ninja-tools",
    install_requires=[
        'pywin32>=303',
        'pyperclip>=1.8.2',
        'psutil>=5.9.0',
    ],
    extras_require={
        'image': [
            'opencv-python==4.5.5.62',
            'scikit-image>=0.19.2',
            'numpy>=1.22.3',
        ],

        'memory': [
            'Pymem>=1.8.5',
            'regex'
        ],

        'excel': [
            'openpyxl==3.0.10',
            'webcolors>=1.12'
        ],

        'all': [
            'opencv-python==4.5.5.62',
            'scikit-image>=0.19.2',
            'openpyxl==3.0.10',
            'webcolors>=1.12'
            'numpy>=1.22.3',
            'Pymem>=1.8.5',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.9'
)
