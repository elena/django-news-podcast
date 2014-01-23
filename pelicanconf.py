#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Django Community'
SITENAME = u'Django News Podcast'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Django', 'http://djangoproject.com/'),
          ('https://groups.google.com/forum/#!forum/django-developers', 'Django Developer List'),
          ('https://groups.google.com/forum/#!forum/django-announce', 'Django Announcements'),
          ('https://groups.google.com/forum/#!forum/django-updates', 'Django Updates'),
          ('Python.org', 'http://python.org/'),
)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 40

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs']

THEME = "theme"

OUTPUT_PATH = "."
