# -*- coding: utf-8 -*-
# msh-python/release/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class ReleaseView(TemplateView):
    template_name = "release/release.html"