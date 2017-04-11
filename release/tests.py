# -*- coding: utf-8 -*-
# msh-python/release/tests.py

from django.test import TestCase

import unittest
import datetime

from pointsheet.models import Pointsheet
from .models import Release

class ReleaseTest(unittest.TestCase):
	"""docstring for ReleaseTest"""
	def create_pointsheet_valid(self):
		return Pointsheet.objects.create(year=2016, month=12)
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
	
	def test_create_new_release(self):
		"""
			Description -- : Teste if create new release is correct or not
			Senario ------ : One pointsheet for one release
		"""
		# Arrange
		pointsheet = self.create_pointsheet_valid()
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
		# Arrange
		pointsheet = self.create_pointsheet_valid()
		
		self.create_basic_release_normal(datetime.date(2016, 12, 2), Release.WEDNESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 3), Release.FRIDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 6), Release.MONDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 7), Release.TUESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 8), Release.WEDNESDAY, pointsheet)
		self.create_basic_release_normal(datetime.date(2016, 12, 9), Release.THUSDAY, pointsheet)
		#Act
		_count = len(Release.objects.all())
		_release = Release.objects.get(id=2)
		#Assert
		self.assertEqual(_count, 7)
		self.assertEqual(_release.dayweek, Release.WEDNESDAY)

	def test_create_new_release_multiples_with_weekend_work(self):
		"""
			Description -- : Teste if create new release is correct or not when have multiples inserts and work on weekends
			Senario ------ : One pointsheet for multiples releases (many differents)
		"""
		# Arrange
		pointsheet = self.create_pointsheet_valid()

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
		self.assertEqual(_count, 16)
		self.assertEqual(_release_date.dayweek, Release.FRIDAY)
		self.assertEqual(_count_release_dayweek, 2)