# -*- coding: utf-8 -*-
# msh-python/release/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from . import views

urlpatterns = [
	# url(r'^api/releases/$', views.PointsheetList.as_view(), name='pointsheets'),
	# url(r'^api/releases/(?P<pk>[0-9]+)/$', views.PointsheetDetail.as_view(), name='pointsheets-detail'),
	url(r'^release/$', views.index),
	]

urlpatterns = format_suffix_patterns(urlpatterns)