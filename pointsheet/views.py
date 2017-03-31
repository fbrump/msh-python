# -*- coding: utf-8 -*-
# msh-python/pointsheet/views.py

#from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics

from .models import Pointsheet
from .serializers import PointsheetSerializer

class PointsheetList(
	mixins.ListModelMixin,
	mixins.CreateModelMixin,
	generics.GenericAPIView
	):
	"""docstring for PointsheetList"""
	queryset = Pointsheet.objects.all()
	serializer_class = PointsheetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
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

def PointsheetView(request):
	return 'view-pointsheet'