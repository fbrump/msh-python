# -*- coding: utf-8 -*-
# msh-python/release/api/views.py

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import mixins
from rest_framework import generics

from release.models import Release
from .serializers import ReleaseSerializer

class ReleaseList(
	mixins.ListModelMixin,
	mixins.CreateModelMixin,
	generics.GenericAPIView
	):
	"""
		Release List -- View for API List
		Methods:
			GET -- Lista all itens
			POST -- insert new item
	"""
	queryset = Release.objects.all()
	serializer_class = ReleaseSerializer

	def get(self, request, *args, **kwargs):
		"""
			METHOD GET: Return all itens.
		"""
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		"""
			METHOD POST: Insert new item.
		"""
		print('POST -- ReleaseList')
		print(request)
		return self.create(request, *args, **kwargs)

class ReleaseDetail(
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
	generics.GenericAPIView
	):
	"""
		Release details -- View for work details
		Methods:
			GET -- Get one item
			PUT -- Update one item
			DELETE -- Remove one item
	"""
	queryset = Release.objects.all()
	serializer_class = ReleaseSerializer

	def get(self, request, *args, **kwargs):
		"""
			METHOD GET: Return one item.
		"""
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		"""
			METHOD PUT: Update one item.
		"""
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		"""
			METHOD DELETE: Remove one item from database.
		"""
		return self.destroy(request, *args, **kwargs)