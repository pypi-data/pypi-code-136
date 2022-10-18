# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pycocap import __version__ as ver

project = 'pyCOCAP'
copyright = '2022, Lennart Schüler'
author = 'Lennart Schüler'
version = ver
release = ver

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.imgmath",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",  # parameters look better than with numpydoc only
    "numpydoc",

]

# autosummaries from source-files
autosummary_generate = True
# dont show __init__ docstring
autoclass_content = "class"
# sort class members
autodoc_member_order = "groupwise"
# autodoc_member_order = 'bysource'

# Notes in boxes
napoleon_use_admonition_for_notes = True
# Attributes like parameters
# napoleon_use_ivar = True
# this is a nice class-doc layout
numpydoc_show_class_members = True
# class members have no separate file, so they are not in a toctree
numpydoc_class_members_toctree = False
# for the covmodels alot of classmembers show up...
# maybe switch off with:    :no-inherited-members:
numpydoc_show_inherited_class_members = True

templates_path = ['_templates']
exclude_patterns = []

master_doc = 'contents'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    "**": [
        "relations.html",  # needs 'show_related': True theme option to display
        "searchbox.html",
    ]
}

html_static_path = ['_static']

html_logo = 'pics/COCAP_logo.png'
html_favicon = 'pics/COCAP.ico'
