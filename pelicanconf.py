#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'staggerlee011'
SITENAME = 'serialexperiments'
#SITEURL = 'https://blog.serialexperiments.co.uk/'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'

# Blogroll
LINKS = (('Home','/index.html'),
('About','/pages/about.html'),)

# Social widget
SOCIAL = (('Email','mailto:stebennettsjb@gmail.com'),
('GitHub','https://github.com/Staggerlee011'),
('LInkedin','https://www.linkedin.com/in/stephenjohnbennett/'),
)

DEFAULT_PAGINATION = 6

# voce settings
DISPLAY_CATEGORIES_ON_MENU = True
THEME = 'themes/voce'
USER_LOGO_URL = 'images/07.png'
DEFAULT_DATE_FORMAT = "%b %d, %Y"  
MANGLE_EMAILS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = [
    # ...
    'pelican_gist',
    # ...
]

STATIC_PATHS = [
    'images',
    'files',  # this
]

EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    #'files/robots.txt': {'path': 'robots.txt'},
}