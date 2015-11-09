import sys
import os
import shlex

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]  

# -- General configuration ------------------------------------------------
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'RobinDeGuzmanCV'
copyright = u'2015, Robin F. De Guzman'
author = u'Robin'
version = '1.0'
release = '1.0'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sphinx = False
html_show_copyright = True
html_search_language = 'en'
htmlhelp_basename = 'RobinDeGuzmanHelp'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',

    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = './_static/id.jpg'
