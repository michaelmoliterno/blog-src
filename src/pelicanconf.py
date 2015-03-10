#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Moliterno'
SITENAME = u'Michael Moliterno'
SITEURL = ''


OUTPUT_PATH = 'output/blog'
# PAGE_URL = '../{slug}.html'
# PAGE_SAVE_AS = '../{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False



##PATH = 'content'
# This requires Pelican 3.3+
STATIC_PATHS = ['images','docs','d3']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# # Resources
LINKS = (('python', 'http://python.org/'),
         ('pandas', 'http://pandas.pydata.org/'),
         ('scikit learn', 'http://scikit-learn.org/stable/documentation.html'),
         ('d3.js', 'https://github.com/mbostock/d3/wiki'))


# Social widget
SOCIAL = (('GitHub', 'https://github.com/michaelmoliterno'),
          ('LinkedIn', 'https://www.linkedin.com/in/michaelmoliterno'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



# Added by michaelmoliterno
THEME = '../pelican-themes/bootstrap'


# # Where to look for plugins
# PLUGIN_PATH = ['./pelican-plugins']
# # Which plugins to enable
# PLUGINS = ['better_figures_and_images']

GITHUB_USERNAME = 'michaelmoliterno'

MENUITEMS = [# ('Portfolio', '/pages/portfolio.html'),
			('cv/résumé', 'https://michaelmoliterno.github.io/docs/Michael_Moliterno_CV.pdf')]

