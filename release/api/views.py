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
	"""docstring for PointsheetList"""
	queryset = Release.objects.all()
	serializer_class = ReleaseSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		print('POST -- ReleaseList')
		print(request)
		return self.create(request, *args, **kwargs)

#@csrf_exempt
# def ReleaseList(request):
# 	"""
# 		List all code releases, or create a new release.

# 		Methods:
# 			GET -- Return all releases
# 			POST -- Insert new release
# 	"""
# 	if request.method == 'GET':
# 		release = Release.objects.all()
# 		serializer = ReleaseSerializer(release, many=True)
# 		return JsonResponse(serializer.data, safe=False)

# 	elif request.method == 'POST':
# 		print('POST -- method')
# 		print(request.data)
# 		data = JSONParser().parse(request)
# 		print('json data ---')
# 		print(data)
# 		serializer = ReleaseSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)


class ReleaseDetail(
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
	generics.GenericAPIView
	):
	queryset = Release.objects.all()
	serializer_class = ReleaseSerializer

	def get(self, request, *args, **kwargs):
		print('test')
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		print('PUT in ReleaseDetail')
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

# @csrf_exempt
# def ReleaseDetail(request, pk):
# 	"""
# 		Retrieve, update or delete a code snippet.

# 		Methods:
# 			GET -- Return one release
# 			PUT -- Update one release
# 			DELETE -- Delete one release
# 	"""
# 	try:
# 		release = Release.objects.get(id=pk)
# 	except Release.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = ReleaseSerializer(release)
# 		return JsonResponse(serializer.data)

# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(release, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data)
# 		return JsonResponse(serializer.errors, status=400)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return HttpResponse(status=204)
