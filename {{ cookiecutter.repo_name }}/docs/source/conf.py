# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Could be handled by cookiecutter
project = "{{ cookiecutter.project_name }}"  # fill it with your own project name
copyright = "{{ cookiecutter.year }}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"
# release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # write docs in Markdown
    "sphinx.ext.napoleon",  # parse Google and Numpy docstrings
    "sphinx.ext.autodoc",  # generate documentation from docstrings
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.autosummary",  # generate summary tables for modules/classes
    "autoapi.extension",
    "nbsphinx",  # convert Jupyter notebooks to Sphinx docs
]

autoapi_dirs = ["../../{{ cookiecutter.repo_name }}"]
autoapi_type = "python"

templates_path = ["_templates"]
exclude_patterns = [
    ".ipynb_checkpoints",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
