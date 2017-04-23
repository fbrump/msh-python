# -*- coding: utf-8 -*-
# msh-python/release/tests.py

from django.test import TestCase

import unittest
import datetime

from rest_framework.test import APIRequestFactory
from pointsheet.models import Pointsheet
from .models import Release
from .api.serializers import ReleaseSerializer

from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class ReleaseTest(unittest.TestCase):
	"""docstring for ReleaseTest"""
	def setUp(self):
		# print('>>>> SET UP')
		self.create_pointsheet_valid()
	def tearDown(self):
		# print('>>>> TEAR DOWN')
		self.delete_pointsheet_valid()
	## PRIVATES METHODS
	#@classmethod
	def create_pointsheet_valid(self):
		"""
		"""
		Pointsheet.objects.create(year=2016, month=12)
	#@classmethod
	def get_pointsheet_valid(self):
		"""
		"""
		return Pointsheet.objects.get(year=2016, month=12)
	#@classmethod
	def delete_pointsheet_valid(self):
		"""
		"""
		Pointsheet.objects.filter(year=2016, month=12).delete()

	def create_basic_release_normal(self, date, dayofweek, pointsheet):
		return Release.objects.create(
			date=date,
			dayweek=dayofweek,
			checkin= datetime.time(9, 0),
			checkout_lunch= datetime.time(12, 0),
			checkin_lunch= datetime.time(13, 0),
			checkout= datetime.time(18, 0),
			pointsheet=pointsheet
		)
	def create_basic_release_weeekend_work_without_lunch(self, date, dayofweek, pointsheet):
		return Release.objects.create(
			date=date,
			dayweek=dayofweek,
			checkin= datetime.time(9, 0),
			checkout= datetime.time(14, 0),
			pointsheet=pointsheet
		)
	def create_basic_release_weeekend_work(self, date, dayofweek, pointsheet):
		return Release.objects.create(
			date=date,
			dayweek=dayofweek,
			checkin= datetime.time(9, 0),
			checkout_lunch= datetime.time(12, 0),
			checkin_lunch= datetime.time(13, 0),
			checkout= datetime.time(16, 0),
			pointsheet=pointsheet
		)

	## PUBLICS TESTS
	def test_create_new_release(self):
		"""
			Description -- : Teste if create new release is correct or not
			Senario ------ : One pointsheet for one release
		"""
		# print('test_create_new_release')
		# Arrange
		
		pointsheet = self.get_pointsheet_valid()
		self.create_basic_release_normal(datetime.date(2016, 12, 01), Release.TUESDAY, pointsheet)
		#Act
		_count = len(Release.objects.all())
		
		#Assert
		self.assertEqual(_count, 1)

	def test_create_new_release_multiples(self):
		"""
			Description -- : Teste if create new release is correct or not when have multiples inserts and work on weekends
			Senario ------ : One pointsheet for multiples releases
		"""
		# print('test_create_new_release_multiples')
		# Arrange
		pointsheet = self.get_pointsheet_valid()
		
		self.create_basic_release_normal(datetime.date(2016, 12, 2), Release.WEDNESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 3), Release.FRIDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 6), Release.MONDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 7), Release.TUESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 8), Release.WEDNESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 9), Release.THUSDAY, pointsheet)
		#Act
		_count = len(Release.objects.all())
		_release = Release.objects.get(date=datetime.date(2016, 12, 3), dayweek=Release.FRIDAY, pointsheet=pointsheet)

		#Assert
		self.assertEqual(_count, 6)
		self.assertEqual(_release.dayweek, Release.FRIDAY)

	def test_create_new_release_multiples_with_weekend_work(self):
		"""
			Description -- : Teste if create new release is correct or not when have multiples inserts and work on weekends
			Senario ------ : One pointsheet for multiples releases (many differents)
		"""
		# print('test_create_new_release_multiples_with_weekend_work')
		# Arrange
		pointsheet = self.get_pointsheet_valid()

		self.create_basic_release_weeekend_work_without_lunch(datetime.date(2016, 12, 10), Release.SATURDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 12), Release.MONDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 13), Release.TUESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 14), Release.WEDNESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 15), Release.THUSDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 16), Release.FRIDAY, pointsheet)
		self.create_basic_release_weeekend_work(datetime.date(2016, 12, 17), Release.SATURDAY, pointsheet)
		self.create_basic_release_weeekend_work_without_lunch(datetime.date(2016, 12, 18), Release.SUNDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 19), Release.MONDAY, pointsheet)
		#Act
		_count = len(Release.objects.all())
		_release_date = Release.objects.get(date=datetime.date(2016, 12, 16))
		_count_release_dayweek = len(Release.objects.filter(dayweek=Release.SATURDAY))
		#Assert
		self.assertEqual(_count, 9)
		self.assertEqual(_release_date.dayweek, Release.FRIDAY)
		self.assertEqual(_count_release_dayweek, 2)

	def test_delete_one_release(self):
		"""
			Description -- : Teste if create new release is correct or not
			Senario ------ : One pointsheet for one release
		"""
		# print('test_delete_one_release')
		# Arrange
		pointsheet = self.get_pointsheet_valid()
		self.create_basic_release_weeekend_work_without_lunch(datetime.date(2016, 12, 10), Release.SATURDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 12), Release.MONDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 13), Release.TUESDAY, pointsheet)
		#Act
		Release.objects.get(date=datetime.date(2016, 12, 12)).delete()
		_count = len(Release.objects.all())
		#Assert
		self.assertEqual(_count, 2)

	def test_update_one_release(self):
		"""
			Description -- : Teste if create new release is correct or not
			Senario ------ : One pointsheet for one release
		"""
		# print('test_delete_one_release')
		# Arrange
		pointsheet = self.get_pointsheet_valid()
		self.create_basic_release_weeekend_work_without_lunch(datetime.date(2016, 12, 10), Release.SATURDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 12), Release.MONDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 13), Release.TUESDAY, pointsheet)
		#Act
		_release = Release.objects.get(date=datetime.date(2016, 12, 12))
		_release.date = datetime.date(2016, 12, 14)
		_release.save()
		_count = len(Release.objects.all())
		#Assert
		self.assertEqual(_count, 3)

class ReleaseSerializeTest(unittest.TestCase):
	def setUp(self):
		"""
			Method define enviroment for testing, executed behind method
		"""
		# print('>>>> SET UP - SERIALIZER')
		self.create_pointsheet_valid()
	def tearDown(self):
		"""
			Method clear enviroment for testing, executed after method
		"""
		# print('>>>> TEAR DOWN - SERIALIZER')
		self.delete_pointsheet_valid()
	def create_pointsheet_valid(self):
		"""
			Mehtod that create one pointsheet valid
		"""
		Pointsheet.objects.create(year=2017, month=02)
	def get_pointsheet_valid(self):
		"""
			Method that get one pointsheet valid
		"""
		return Pointsheet.objects.get(year=2017, month=02)
	def delete_pointsheet_valid(self):
		"""
			Method that deleted one pointsheet valid
		"""
		Pointsheet.objects.filter(year=2017, month=02).delete()
	def get_release_normaly(self):
		"""
			Method that get a release normaly day
			Keyword arguments:
		"""
		return {
			u'checkin_lunch': u'13:00', 
			u'checkin_absence': None, 
			u'type_absence': None, 
			u'dayweek': Release.WEDNESDAY, 
			u'file_link': None, 
			u'checkin': u'09:00:00', 
			u'checkout_lunch': None, 
			u'pointsheet': self.get_pointsheet_valid(), 
			u'is_holiday': False, 
			u'checkout_absence': None, 
			u'date': u'2017-02-01', 
			u'justification_absence': None, 
			u'checkout': u'18:00:00',
		}
	def get_release_is_holiday_off_work(self):
		"""
			Method that get a release for holiday when dont work (off)
		"""
		return {
			u'dayweek': Release.THUSDAY, 
			u'pointsheet': self.get_pointsheet_valid(), 
			u'checkin': u'09:00', 
			u'checkout': u'18:00',
			u'is_holiday': True, 
			u'date': u'2017-02-02'
		}

	def test_create_release_serialze(self):
		"""
			Description -- : Teste if create new release is correct or not
			Senario ------ : One pointsheet for one release
		"""
		# print('test_create_release_serialze')
		# Arrange
		factory = APIRequestFactory()
		_data = {
			u'checkin_lunch': u'13:00', 
			u'checkin_absence': u'', 
			u'type_absence': u'', 
			u'dayweek': u'', 
			u'file_link': u'', 
			u'checkin': u'09:00', 
			u'checkout_lunch': None, 
			u'pointsheet': u'', 
			u'is_holiday': u'', 
			u'checkout_absence': u'', 
			u'date': u'2017-02-01', 
			u'justification_absence': u'', 
			u'checkout': u'18:00'
		}
		#Act
		request = factory.post('/api/releases/', { 'data': _data, 'method': 'POST' }, format='json')
		
		#Assert
		self.assertFalse(len(Release.objects.all()), 0)
		self.assertIsNotNone(request)
	
	def test_serialize_insert_release_normaly(self):
		"""
			Unittest for testing one insert a normaly day serializer
		"""
		# print('test_serialize_insert_release_normaly')
		# Arrange
		data = self.get_release_normaly()
		serializer = ReleaseSerializer(data=data)
		serializer.is_valid()
		#Act
		serializer.create(serializer.data)
		_count = len(Release.objects.all())
		_item_added = Release.objects.get(pointsheet=self.get_pointsheet_valid(), date=data.get('date'), dayweek=data.get('dayweek'))
		#Assert
		self.assertTrue(_count, 1)
		self.assertIsNotNone(_item_added)
		self.assertEqual(_item_added.date, datetime.date(2017, 02, 01))
		self.assertTrue(_item_added.id > 0)

	def test_serialize_insert_release_holiday_off_without(self):
		"""
			Unittest for testing one insert a holiday without work
		"""
		# print('test_serialize_insert_release_holiday_off_without')
		# Arrange
		data = self.get_release_is_holiday_off_work()
		serializer = ReleaseSerializer(data=data)
		serializer.is_valid()
		#Act
		serializer.create(serializer.data)
		_count = len(Release.objects.all())
		_item_added = Release.objects.get(pointsheet=self.get_pointsheet_valid(), date=data.get('date'), dayweek=data.get('dayweek'))
		#Assert
		self.assertTrue(_count, 1)
		self.assertIsNotNone(_item_added)
		self.assertEqual(_item_added.date, datetime.date(2017, 02, 02))
		self.assertTrue(_item_added.id > 0)
