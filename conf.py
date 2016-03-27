import sys
import os
extensions = ['sphinx.ext.graphviz',]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Bugflow Docs'
copyright = u'2016, Chris Gough'
version = '0.0'
release = '0.0.0'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'BugflowDocsdoc'
latex_elements = {
}
latex_documents = [
  ('index', 'BugflowDocs.tex', u'Bugflow Docs Documentation',
   u'Chris Gough', 'manual'),
]
man_pages = [
    ('index', 'bugflowdocs', u'Bugflow Docs Documentation',
     [u'Chris Gough'], 1)
]
texinfo_documents = [
  ('index', 'BugflowDocs', u'Bugflow Docs Documentation',
   u'Chris Gough', 'BugflowDocs', 'One line description of project.',
   'Miscellaneous'),
]
