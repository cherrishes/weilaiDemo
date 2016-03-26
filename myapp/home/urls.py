# !/bash/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rdy'
"""
网站主页url配置
"""
from django.conf.urls import patterns, url
home_patterns = patterns(
    'myapp.home.views',
    url(r'^$', "login", name='first'),
    url(r'^login$', "login", name='login'),
    url(r'^logout$', "logout", name='logout'),
    url(r'^signup', "signup", name='signup'),
    url(r'^home$', "home", name='home'),
    url(r'^fun$', "fun", name='fun'),
    url(r'^week_list$', "week_list", name='week_list'),
    url(r'^chat$', "chat", name='chat'),
    url(r'^deal_plan$', "deal_plan", name='deal_plan'),


)