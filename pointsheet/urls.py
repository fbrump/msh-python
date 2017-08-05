# -*- coding: utf-8 -*-
# msh-python/pointsheet/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^v1/api/pointsheets/$', views.PointsheetList.as_view(), name='pointsheets'),
	url(r'^v1/api/pointsheets/(?P<pk>[0-9]+)/$', views.PointsheetDetail.as_view(), name='pointsheets-detail'),
	url(r'^pointsheet/$', views.PointsheetView.as_view(), name='pointsheet'),
	]

urlpatterns = format_suffix_patterns(urlpatterns)