# -*- coding: utf-8 -*-
# msh-python/release/api/views.py

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from release.models import Release
from .serializers import ReleaseSerializer

@csrf_exempt
def ReleaseList(request):
	"""
		List all code releases, or create a new release.

		Methods:
			GET -- Return all releases
			POST -- Insert new release
	"""
	if request.method == 'GET':
		release = Release.objects.all()
		serializer = ReleaseSerializer(release, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ReleaseSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ReleaseDetail(request, pk):
	"""
		Retrieve, update or delete a code snippet.

		Methods:
			GET -- Return one release
			PUT -- Update one release
			DELETE -- Delete one release
	"""
	try:
		release = Release.objects.get(id=pk)
	except Release.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ReleaseSerializer(release)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(release, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)
