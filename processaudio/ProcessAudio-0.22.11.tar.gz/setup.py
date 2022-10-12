from setuptools import setup, find_packages

# from distutils.core import setup

try:
    with open('README.md') as f:
        long_description = f.read()
except Exception as e:
    long_description = ''
    print(e)

setup(
    name="ProcessAudio",
    packages=["ProcessAudio"],
    include_package_data=True,
    version="0.22.11",
    description="Procesamiento de audios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="William Rodriguez",
    author_email="wisrovi.rodriguez@gmail.com",
    license="GPLv3",
    url="https://github.com/wisrovi/ProcessAudio",
    download_url="https://github.com/wisrovi/ProcessAudio/releases/tag/V0.22.11",
    keywords=["encoding", "i18n", "xml"],
    install_requires=['librosa', 'matplotlib', "nlpaug", "scipy"],  # external packages as dependencies
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
