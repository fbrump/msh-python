# -*- coding: utf-8 -*-
# msh-python/release/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class ReleaseView(TemplateView):
    template_name = "release/release.html"
    def get_context_data(self, **kwargs):
        context = super(ReleaseView, self).get_context_data(**kwargs)
        context['current_Menu'] = 'release-menu'
        print('Context:')
        print(context['current_Menu'])
        return context