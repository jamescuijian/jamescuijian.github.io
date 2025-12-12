#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ========== 复用 pelicanconf.py 的大部分配置 ==========
AUTHOR = '鸡鼠三剑客'
SITENAME = "JamesCui"
# 🔥 关键修正 1：加上 https://
SITEURL = 'https://jamescuijian.github.io'

PATH = 'content'
TIMEZONE = 'Asia/Chongqing'
THEME = "mytheme"
DEFAULT_LANG = 'zh'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ("Homepage", "https://jamescuijian.github.io"),
    ("Categories", "https://jamescuijian.github.io/categories.html"),
    ("Tags", "https://jamescuijian.github.io/tags.html"),
    ("Archives", "https://jamescuijian.github.io/archives.html"),
    ("About", "https://jamescuijian.github.io/about.html"),
)

LINKS = (
    ('ChinaGeology', 'https://chinageology.com'),
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

SOCIAL = (('github','https://github.com/JamesCui'),)  # 🔥 也建议加 https

SHARE = (
    ('twitter', 'http://twitter.com/share', '?text=', '&url='),
    ('facebook', 'http://facebook.com/sharer.php', '?t=', '&u='),
    ('google-plus', 'http://plus.google.com/share', '?text=', '&url='),
)

DEFAULT_PAGINATION = 10

# 🔥 关键修正 2：必须设为 False！
RELATIVE_URLS = False

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ["neighbors", "related_posts", "tag_cloud"]

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

RELATED_POSTS_MAX = 10