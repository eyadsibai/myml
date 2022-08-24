"""Sphinx configuration."""
project = "MyML"
author = "Eyad Sibai"
copyright = "2022, Eyad Sibai"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
