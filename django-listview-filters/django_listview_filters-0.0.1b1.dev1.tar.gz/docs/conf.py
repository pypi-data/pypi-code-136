import os
import sys

from django import setup as django_setup
from django.conf import settings



# import __init__
# from __init__ import __version__

sys.path.insert(0, os.path.abspath("../"))
print("Path: {}".format(sys.path[0]))

from src.django_listview_filters.__init__ import __version__

settings.configure()

django_setup()

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Django ListView Filters"
copyright = "2022, Karl Wooster"
author = "Karl Wooster"
# release = "0.0.1b0.dev1"
version = __version__
print("Version: {}".format(version))
release = version

# rst_epilog = """
# .. |ProjectVersion| replace:: version...{version}
# """.format(version = version)

substitutions = [
    ('|ProjectVersion|', version),
]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "docs.custom-extensions.extensions",
    "sphinx.ext.autosectionlabel",
]

autosectionlabel_prefix_document = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
