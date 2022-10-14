from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
requirements = ['mediapipe','ffmpeg-python==0.2.0','opencv-python==4.5.5.64','numpy']

__version__ = '1.0.2'

setup(
    name='Presage Physiology Preprocessing',
    version=__version__,
    packages=['presage_physiology_preprocessing'],
    author="Presage Technologies",
    author_email="support@presagetech.com",
    description="A Python helper package used for preprocessing video before sending it to Presage Technologies Physiology API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'presage_physiology_preprocessing': 'presage_physiology_preprocessing'},
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    url="https://physiology.presagetech.com/",
    project_urls={
        "Bug Tracker": "https://github.com/Presage-Security/presage_physiology_preprocessing/issues",
    },
)
