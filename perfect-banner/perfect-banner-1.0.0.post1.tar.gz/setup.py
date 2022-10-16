from setuptools import setup
import banner

with open("README.md") as f:
    long_description = f.read()

#===========================================
# S E T U P | Create the setup
#===========================================

setup(
    name = "perfect-banner",
    version = banner.__version__,
    description = "Let text fit the screen",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = banner.__author__,
    keywords = [
        "ascii art",
        "art",
        "text",
        "string",
        "terminal"
    ],
    py_modules = ["banner"],
)