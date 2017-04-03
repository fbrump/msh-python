# -*- coding: utf-8 -*-
# msh-python/pointsheet/serializers.py

from rest_framework import serializers
from .models import Pointsheet


class PointsheetSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	year = serializers.IntegerField()
	month = serializers.IntegerField()
	def create(self, validated_data):
		return Pointsheet.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.year = validated_data.get('year', instance.year)
		instance.month = validated_data.get('month', instance.month)
		instance.save()
		return instance()
    # class Meta:
    # 	model = Pointsheet
    # 	fields = ('id', 'year', 'month', )