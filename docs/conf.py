# Configuració de Sphinx per al projecte de demo
import os
import sys

# Perquè autodoc trobi el codi de src/
sys.path.insert(0, os.path.abspath("../src"))

project = "Demo Read the Docs"
author = "César Alejandro Crespo Freire"
release = "1.0"
language = "ca"

extensions = [
    "sphinx.ext.autodoc",   # genera documentació a partir dels docstrings
    "sphinx.ext.napoleon",  # entén docstrings estil Google
]

html_theme = "sphinx_rtd_theme"
