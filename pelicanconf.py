#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gavin Carothers'
SITENAME = u'Garbage Collection'
SITEURL = ''

THEME = "/home/gavin/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "amelia"
DISPLAY_CATEGORIES_ON_MENU = False

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/gcarothers'),
          ('google-plus', 'https://www.google.com/+GavinCarothers'),)

GITHUB_USER = 'gcarothers'

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

PAGE_URL = ('{slug}.html')
PAGE_SAVE_AS = ('{slug}.html')