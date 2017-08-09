# -*- coding: utf-8 -*-
# msh-python/login/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^login/$', views.LoginView.as_view(), name='login_view'),
	]

urlpatterns = format_suffix_patterns(urlpatterns)