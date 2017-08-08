# -*- coding: utf-8 -*-
# msh-python/account/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	url(r'^account/$', views.Index, name='account'),
	]

urlpatterns = format_suffix_patterns(urlpatterns)