# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'dwssphinx'
copyright = '2024, K Clarke'
author = 'K Clarke'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.redoc'
]
redoc_uri = 'https://unpkg.com/redoc@2.1.3/bundles/redoc.standalone.js'

redoc = [
    {
        'name': 'Risk Profiler API',
        'page': 'api example',
        'spec': 'riskprofiler.yml',
        'embed': True,
        'opts': {
            'suppress-warnings': True
        }
    }
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
