# -*- coding: utf-8 -*-
# msh-python/login/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
	]

urlpatterns = format_suffix_patterns(urlpatterns)