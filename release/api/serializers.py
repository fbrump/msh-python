# -*- coding: utf-8 -*-
# msh-python/pointsheet/api/release.py

from rest_framework import serializers
from release.models import Release


class ReleaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Release
        fields = '__all__'
	# id = serializers.IntegerField(read_only=True)
	# date = serializers.DateField(format="%Y-%m-%d") #%H:%M:%S
	# dayweek = serializers.ChoiceField(Release.DAY_OF_WEEK_CHOICES)
	# checkin = serializers.TimeField(format='%H:%M:%S')
	# def create(self, validated_data):
	# 	return Pointsheet.objects.create(**validated_data)
	# def update(self, instance, validated_data):
	# 	instance.year = validated_data.get('year', instance.year)
	# 	instance.month = validated_data.get('month', instance.month)
	# 	instance.save()
	# 	return instance()
    # class Meta:
    # 	model = Pointsheet
    # 	fields = ('id', 'year', 'month', )