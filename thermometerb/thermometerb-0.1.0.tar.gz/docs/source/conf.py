# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import datetime
import os
import subprocess
import sys

sys.path.insert(0, os.path.abspath("../../src/"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "thermometerb"
copyright = f"{datetime.date.today().year}, Bryan Crossland"
author = "Bryan Crossland"

# version = (
#     subprocess.check_output(
#         ["python3", "setup.py", "--version"],
#         cwd=os.path.join(os.path.dirname(__file__), os.pardir, os.pardir),
#     )
#     .decode()
#     .strip()
# )
#
# release = version
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.duration",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "myst_parser",
]

autodoc_typehints = "description"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
templates_path = ["_templates"]
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"

html_theme_options = {
    "github_user": "bacrossland",
    "github_repo": "thermometerb",
    "github_button": True,
    "extra_nav_links": {
        "View on github": "https://github.com/bacrossland/thermometerb",
    },
}

html_static_path = ["_static"]

add_module_names = False
