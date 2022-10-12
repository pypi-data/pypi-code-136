from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path("__file__").parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="nlcor",
   # packages=find_packages(include='nlcor', exclude=['tests']),
    version="3.0.3",
    packages=find_packages(include=['nlcor' , 'nlcor.correlations' , 'nlcor.utilities' , 'nlcor.visualization'], exclude=['tests']),
    author="Chitta Ranjan, Devleena Banerjee,Vahab Najari",
    author_email="cranjan@processminer.com, dbanerjee@processminer.com",
    long_description=long_description,
    description="Nlcor uses a dynamic partitioning approach with adaptive segmentation for a more precise nonlinear correlation estimation.",
    long_description_content_type="text/markdown",
    url="https://github.com/ProcessMiner/nlcorpython",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite="tests",
    python_requires='>=3.6',
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
    ]
)
