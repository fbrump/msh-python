# -*- coding: utf-8 -*-
# msh-python/login/views.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class LoginView(TemplateView):
    template_name = "login/login.html"
    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['current_Menu'] = 'release-menu'
        print('Context:')
        print(context['current_Menu'])
        return context
