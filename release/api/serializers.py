# -*- coding: utf-8 -*-
# msh-python/pointsheet/api/release.py

from rest_framework import serializers
from release.models import Release
from pointsheet.models import Pointsheet
from pointsheet.serializers import PointsheetSerializer


class ReleaseSerializer(serializers.Serializer):
	"""
		Class that mapping serializer Release Model

		Properties:
			id --
			date --
			dayweek --
			checkin --
			checkout lunch --
			checkin lunch --
			checkout --
			is_holiday --
			pointsheet --
			
		Methods:
			create --
			update --
	"""
	id = serializers.IntegerField(read_only=True)
	date = serializers.DateField(format="%Y-%m-%d")
	dayweek = serializers.ChoiceField(Release.DAY_OF_WEEK_CHOICES)
	checkin = serializers.TimeField(format='%H:%M:%S')
	checkout_lunch = serializers.TimeField(format='%H:%M:%S')
	checkin_lunch = serializers.TimeField(format='%H:%M:%S')
	checkout = serializers.TimeField(format='%H:%M:%S')
	is_holiday = serializers.BooleanField(required=False)
	pointsheet = PointsheetSerializer(many=False)
	def create(self, validated_data):
		"""
			Method for insert new item on database
		"""
		_serializePointsheet = PointsheetSerializer(validated_data.pop('pointsheet'))
		_pointsheet = Pointsheet.objects.get(
			year=_serializePointsheet.data['year'],
			month=_serializePointsheet.data['month'])
		validated_data['pointsheet'] = _pointsheet
		return Release.objects.create(**validated_data)
	def update(self, instance, validated_data):
		"""
			Method for update one instance of the database Release
		"""
		instance.date = validated_date.get('date', instance.date)
		instance.dayweek = validated_data.get('dayweek', instance.dayweek)
		instance.checkin = validated_data.get('checkin', instance.checkin)
		instance.checkout_lunch = validated_data.get('checkout_lunch', instance.checkout_lunch)
		instance.checkin_lunch = validated_data.get('checkin_lunch', instance.checkin_lunch)
		instance.checkout = validated_data.get('checkout', instance.checkout)
		instance.is_holiday = validated_data.get('is_holiday', instance.is_holiday)
		instance.save()
		return instance()
	# class Meta:
	# 	model = Pointsheet
	# 	fields = ('id', 'year', 'month', )