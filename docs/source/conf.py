#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest.mock
import enum

# Mock Pythonista modules
sys.modules['console'] = unittest.mock.MagicMock()
sys.modules['editor'] = unittest.mock.MagicMock()
sys.modules['ui'] = unittest.mock.MagicMock()
sys.modules['objc_util'] = unittest.mock.MagicMock()
sys.modules['clipboard'] = unittest.mock.MagicMock()

# readthedocs.org doesn't support Python 3.6 yet
enum.IntFlag = enum.Enum

sys.path.insert(0, os.path.abspath('../..'))
import blackmamba  # noqa: E402


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'Black Mamba'

copyright = '2017, {}'.format(blackmamba.__author__)
author = blackmamba.__author__
version = blackmamba.__version__
release = blackmamba.__version__

language = None

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {'**': ['navigation.html', 'localtoc.html', 'relations.html']}


# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'BlackMambadoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'BlackMamba.tex', 'Black Mamba Documentation',
     'Robert Vojta', 'manual'),
]


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'blackmamba', 'Black Mamba Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'BlackMamba', 'Black Mamba Documentation',
     author, 'BlackMamba', 'One line description of project.',
     'Miscellaneous'),
]


intersphinx_mapping = {'https://docs.python.org/': None}
