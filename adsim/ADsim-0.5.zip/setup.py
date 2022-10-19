from distutils.core import setup
from pathlib import Path

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name = "ADsim",
    version = "0.5",
    platforms = ["linux2", "win32"],
    description = "ADsim-module",
    long_description=long_description,
    install_requires=["ADwin",],
    maintainer = "Jaeger Computergesteuerte Messtechnik GmbH",
    author = "Markus Borchers",
    author_email = "info@ADwin.de",
    url = "https://www.adwin.de/us/produkte/adsim.html",
    license="Apache License, Version 2",
    py_modules=["ADsim"])
