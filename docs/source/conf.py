# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PDGrapher"
copyright = "2023, ggonzales"
author = "dmohorcic, ggonzales, davidzqhuang"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "myst_parser"]

# Autodoc settings
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
autodoc_member_order = "bysource"

# Napoleon settings
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
napoleon_numpy_docstring = False

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "nature"
html_static_path = ["_static"]
