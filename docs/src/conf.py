# Configuration file for the Sphinx documentation builder.
# documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html
# extensions: https://www.sphinx-doc.org/en/master/usage/extensions/


# Project information
project = 'fvr'
author = 'Daniel Weschke'
copyright = '%Y, Daniel Weschke'


# General configuration

extensions = []                       # will be appended below

## Options for internationalisation
language = 'en'

## Options for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'
source_suffix = '.rst'

## Options for templating
templates_path = ['_templates']       # relative to conf.py dir


# Builder options

## Options for HTML output
html_theme = 'furo'
html_theme_options = {}
html_static_path = ['_static']        # relative to conf.py dir
html_copy_source = False              # copy reST sources to html/sources/
html_show_sourcelink = False          # links to reST sources


# Domain options

## Options for the Python domain
add_module_names = False
modindex_common_prefix = ['fvr.']     # prefix ignored for sorting, used in `Module Index`
# python_display_short_literal_types = True
# python_use_unqualified_type_names = True


# built-in extension todo
# add directive `.. todo::` and `.. todolist::`
extensions.append('sphinx.ext.todo')
todo_include_todos = True


# built-in extension viewcode
# links to python package module files
extensions.append('sphinx.ext.viewcode')


# built-in extension autodoc
extensions.append('sphinx.ext.autodoc')
autodoc_typehints = 'description'     # show typehints in 'signature', 'description', 'both', 'none'
# autodoc_type_alias = {
#   'Callable': 'Callable',           # otherwise Callable -> collections.abc.Callable
#   'ArrayLike': 'ArrayLike',         # otherwise ArrayLike -> _SupportsArray[dtype[Any]] | ...
# }
autodoc_typehints_format = 'short'     # 'short': e.g. io.StringIO -> StringIO


# built-in extension apidoc
extensions.append('sphinx.ext.apidoc')
apidoc_modules = [
  # 'path': relative to conf.py dir
  # 'destination': relative to source dir
  {'path': '../../src', 'destination': './api'}
]
apidoc_max_depth = 4
apidoc_separate_modules = True        # doc for each module on an individual page
apidoc_module_first = True            # module doc before submodule doc


# built-in extension napoleon
# add docstring styles: Google and NumPy
extensions.append('sphinx.ext.napoleon')
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_keyword = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True
napoleon_custom_sections = None
