#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '鸡鼠三剑客'
SITENAME = "JamesCui"
SITEURL = 'jamescuijian.github.io'

PATH = 'content'
TIMEZONE = 'Asia/Chongqing'
THEME = "mytheme"
DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (("Homepage","https://jamescuijian.github.io"),
             ("Categories","https://jamescuijian.github.io/categories.html"),
             ("Tags","https://jamescuijian.github.io/tags.html"),
           ("Archives","https://jamescuijian.github.io/archives.html"),
             ("About","https://jamescuijian.github.io/about.html"),        
		 )

# Blogroll
LINKS = (('ChinaGeology', 'https://chinageology.com'),
        ('GeoPython', 'http://doc.geopython.com/'),
         ('Fan', 'https://fanzheng.org'),
        ('FlagPlus', 'http://o00o.site'),
        ('CosLi', 'http://blog.cosli.top'),        
        ('Akagi201', 'http://akagi201.org'),
        ('XuanWo', 'http://xuanwo.org/'),
        ('4Orange','https://blog.daftme.com'),
        ('River','http://blog.riverrun.xyz/'),
        ('LogCG Blog','https://www.logcg.com'),   
        ('GuoLao', 'http://guolao.me/'),
        )

# Social widget
SOCIAL = (('github','http://github.com/JamesCui'),
		)

SHARE = (('twitter', 'http://twitter.com/share', '?text=', '&amp;url='),
         ('facebook', 'http://facebook.com/sharer.php', '?t=', '&amp;u='),
         ('google-plus', 'http://plus.google.com/share', '?text=', '&amp;url='))


# DISQUS_SITENAME = ""

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ["neighbors","related_posts","tag_cloud", "related_posts"]
#sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.8,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
}
}
#相关文章
RELATED_POSTS_MAX = 10
