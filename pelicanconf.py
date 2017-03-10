#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'S\xe9bastien'
SITENAME = u"L'entreprise Lib\xe9r\xe9e"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Appearance
THEME = 'bulrush'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']
JINJA_ENVIRONMENT = {
    'extensions': ['webassets.ext.jinja2.AssetsExtension', 'jinja2.ext.with_'],
}



# Other settings
GITHUB_URL = 'https://github.com/smorele/entreprise-liberee'
TWITTER_USERNAME = 'smorele'