import setuptools

setuptools.setup(
    include_package_data=True,
    name="gnssanalysis",
    version="0.0.10",
    description="basic python module for gnss analysis",
    author="Geoscience Australia",
    author_email="GNSSAnalysis@ga.gov.au",
    packages=setuptools.find_packages(),
    install_requires=[
        "boto3",
        "click",
        "matplotlib",
        "numpy",
        "pandas",
        "plotext==4.2",
        "plotly",
        "pymongo",
        "pytest",
        "scipy",
        "tqdm",
        "unlzw",
    ],
    entry_points={
        "console_scripts": [
            "diffutil = gnssanalysis:gn_utils.diffutil",
            "snxmap = gnssanalysis:gn_utils.snxmap",
            "sp3merge = gnssanalysis:gn_utils.sp3merge",
            "log2snx = gnssanalysis:gn_utils.log2snx",
            "trace2mongo = gnssanalysis:gn_utils.trace2mongo",
        ]
    },
)
