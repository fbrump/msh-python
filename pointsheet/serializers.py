# -*- coding: utf-8 -*-
# msh-python/pointsheet/serializers.py

from rest_framework import serializers
from .models import Pointsheet

class PointsheetSerializer(serializers.Serializer):
    class Meta:
    	model = Pointsheet
    	fields = ('id', 'year', 'month', )