# Configuration file for the Sphinx documentation builder.
# documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html
# extensions: https://www.sphinx-doc.org/en/master/usage/extensions/

# INFO: for sidebar api content, the modules.rst must be loaded? hidden?


# Project information
project = 'fvr'
author = 'Daniel Weschke'
copyright = '%Y, Daniel Weschke'
vesion = '25.12.22'
release = '25.12.22'


# General configuration
extensions = []                       # will be appended below

## Options for highlighting
# pygments_style = None                 # None: theme default, '' == 'sphinx'
# pygments_dark_style = 'fruity'        # '' == 'sphinx'

## Options for internationalisation
language = 'en'

## Options for markup
show_authors = False

## Options for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'
source_suffix = {'.rst': 'restructuredtext'}

## Options for templating
templates_path = ['_templates']       # relative to conf.py dir


# Builder options

## Options for HTML output
html_theme = 'furo'
html_theme_options = {
  "footer_icons": [
    {
      "name": "home",
      "url": "/",
      "html": """
      <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 576 512" height="200px" width="200px" xmlns="http://www.w3.org/2000/svg">
        <path d="M280.37 148.26L96 300.11V464a16 16 0 0 0 16 16l112.06-.29a16 16 0 0 0 15.92-16V368a16 16 0 0 1 16-16h64a16 16 0 0 1 16 16v95.64a16 16 0 0 0 16 16.05L464 480a16 16 0 0 0 16-16V300L295.67 148.26a12.19 12.19 0 0 0-15.3 0zM571.6 251.47L488 182.56V44.05a12 12 0 0 0-12-12h-56a12 12 0 0 0-12 12v72.61L318.47 43a48 48 0 0 0-61 0L4.34 251.47a12 12 0 0 0-1.6 16.9l25.5 31A12 12 0 0 0 45.15 301l235.22-193.74a12.19 12.19 0 0 1 15.3 0L530.9 301a12 12 0 0 0 16.9-1.6l25.5-31a12 12 0 0 0-1.7-16.93z"></path></svg>
      """,
      "class": "",
    },
    {
      "name": "git",
      "url": "https://gitea.weseng.de/daniel/fvr",
      "html": """
        <svg stroke="currentColor" fill="currentColor" stroke-width="0" role="img" viewBox="0 0 24 24" height="200px" width="200px" xmlns="http://www.w3.org/2000/svg">
          <path d="M4.209 4.603c-.247 0-.525.02-.84.088-.333.07-1.28.283-2.054 1.027C-.403 7.25.035 9.685.089 10.052c.065.446.263 1.687 1.21 2.768 1.749 2.141 5.513 2.092 5.513 2.092s.462 1.103 1.168 2.119c.955 1.263 1.936 2.248 2.89 2.367 2.406 0 7.212-.004 7.212-.004s.458.004 1.08-.394c.535-.324 1.013-.893 1.013-.893s.492-.527 1.18-1.73c.21-.37.385-.729.538-1.068 0 0 2.107-4.471 2.107-8.823-.042-1.318-.367-1.55-.443-1.627-.156-.156-.366-.153-.366-.153s-4.475.252-6.792.306c-.508.011-1.012.023-1.512.027v4.474l-.634-.301c0-1.39-.004-4.17-.004-4.17-1.107.016-3.405-.084-3.405-.084s-5.399-.27-5.987-.324c-.187-.011-.401-.032-.648-.032zm.354 1.832h.111s.271 2.269.6 3.597C5.549 11.147 6.22 13 6.22 13s-.996-.119-1.641-.348c-.99-.324-1.409-.714-1.409-.714s-.73-.511-1.096-1.52C1.444 8.73 2.021 7.7 2.021 7.7s.32-.859 1.47-1.145c.395-.106.863-.12 1.072-.12zm8.33 2.554c.26.003.509.127.509.127l.868.422-.529 1.075a.686.686 0 0 0-.614.359.685.685 0 0 0 .072.756l-.939 1.924a.69.69 0 0 0-.66.527.687.687 0 0 0 .347.763.686.686 0 0 0 .867-.206.688.688 0 0 0-.069-.882l.916-1.874a.667.667 0 0 0 .237-.02.657.657 0 0 0 .271-.137 8.826 8.826 0 0 1 1.016.512.761.761 0 0 1 .286.282c.073.21-.073.569-.073.569-.087.29-.702 1.55-.702 1.55a.692.692 0 0 0-.676.477.681.681 0 1 0 1.157-.252c.073-.141.141-.282.214-.431.19-.397.515-1.16.515-1.16.035-.066.218-.394.103-.814-.095-.435-.48-.638-.48-.638-.467-.301-1.116-.58-1.116-.58s0-.156-.042-.27a.688.688 0 0 0-.148-.241l.516-1.062 2.89 1.401s.48.218.583.619c.073.282-.019.534-.069.657-.24.587-2.1 4.317-2.1 4.317s-.232.554-.748.588a1.065 1.065 0 0 1-.393-.045l-.202-.08-4.31-2.1s-.417-.218-.49-.596c-.083-.31.104-.691.104-.691l2.073-4.272s.183-.37.466-.497a.855.855 0 0 1 .35-.077z"></path>
        </svg>
      """,
      "class": "",
    },
  ],
}
html_title = f'{project} {release} documentation'
html_static_path = ['_static']        # relative to conf.py dir
html_last_updated_fmt = '%b %d, %Y'
html_copy_source = False              # copy reST sources to html/sources/
html_show_sourcelink = False          # links to reST sources
html_file_suffix = '.html'            # extension for generated files
html_show_copyright = True            # show “© Copyright …” using `copyright'
html_show_search_summary = True
html_show_sphinx = True
html_scaled_image_link = True         # Link images that have been resized
                                      # per-image deactivation `:class: no-scaled-link'


# Domain options

## Options for the Python domain
add_module_names = False              # prefix module names to all objects (classes, methods)
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
autoclass_content = 'class'           # class, init, both (class + init under class)
autodoc_class_signature = 'separated' # mixed (args at class), separated (args at __init__)
autodoc_member_order = 'groupwise'    # alphabetical, groupwise, bysource
autodoc_default_options = {
  # 'special-members': '__iter__, __contains__, __getitem__, __setitem__, __pos__, __neg__, __add__, __iadd__, __sub__, __isub__, __mul__, __rmul__, __imul__, __matmul__, __imatmul__, __abs__, __lt__, __le__, __gt__, __ge__, __eq__, __ne__, __str__, __repr__'
  'special-members': '__init__, __iter__, __contains__, __getitem__, __setitem__, __pos__, __neg__, __add__, __iadd__, __sub__, __isub__, __mul__, __rmul__, __imul__, __matmul__, __imatmul__, __abs__, __lt__, __le__, __gt__, __ge__, __eq__, __ne__, __str__, __repr__'
}
autodoc_typehints = 'description'     # show typehints in 'signature', 'description', 'both', 'none'
# autodoc_type_alias = {
#   'Callable': 'Callable',           # otherwise Callable -> collections.abc.Callable
#   'ArrayLike': 'ArrayLike',         # otherwise ArrayLike -> _SupportsArray[dtype[Any]] | ...
# }
autodoc_typehints_format = 'short'    # 'short': e.g. io.StringIO -> StringIO


# built-in extension apidoc
extensions.append('sphinx.ext.apidoc')
apidoc_modules = [
  # 'path': relative to conf.py dir
  # 'destination': relative to source dir
  {'path': '../../src/fvr', 'destination': './api'}
]
apidoc_max_depth = 4
apidoc_separate_modules = True        # doc for each module on an individual page
apidoc_module_first = True            # module doc before submodule doc
apidoc_implicit_namespaces = True     # True: any folder is a packages, even w/o __init.py
apidoc_automodule_options = {
  'members', 'show-inheritance', 'undoc-members'
}


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
