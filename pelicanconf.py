#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = 'Michael Hanke & Alex Waite'
SITENAME = 'studyforrest.org'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

#
# Configure Pelican a bit
#
PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_javascript', 'tipue_search', 'sitemap']
SITEMAP = { 'format': 'xml' }

THEME = 'theme'
DIRECT_TEMPLATES = ['search'] # unset all templates; use these
STATIC_PATHS = ['img/']

#HEADERID_LINK_CHAR = '<i class="icon-link"></i>'

FEED_ALL_ATOM = None
AUTHOR_SAVE_AS = False

#
# Configure the site
#
STATIC_PATHS = ['img']
MENUITEMS = ( ('About', 'about.html'),
              ('Access', 'access.html'),
              ('Data', 'data.html'),
              ('Explore', 'explore.html'),
              ('Publications', 'publications.html'),
)
