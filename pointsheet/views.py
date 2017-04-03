# -*- coding: utf-8 -*-
# msh-python/pointsheet/views.py

#from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from django.views.generic import TemplateView
from django.http import HttpResponse
import json

from .models import Pointsheet
from .serializers import PointsheetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

class PointsheetList(
	mixins.ListModelMixin,
	mixins.CreateModelMixin,
	generics.GenericAPIView
	):
	"""docstring for PointsheetList"""
	queryset = Pointsheet.objects.all()
	serializer_class = PointsheetSerializer

	def get(self, request, *args, **kwargs):
		print('Method GET from Pointsheet List')
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		print('Method POST from Pointsheet List')
		print(self)
		return self.create(request, *args, **kwargs)

class PointsheetDetail(
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
	generics.GenericAPIView
	):
	queryset = Pointsheet.objects.all()
	serializer_class = PointsheetSerializer

	def get(self, request, *args, **kwargs):
		print('test')
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

class PointsheetView(TemplateView):
    template_name = "pointsheet/pointsheet.html"