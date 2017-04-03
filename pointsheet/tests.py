# -*- coding: utf-8 -*-
# msh-python/pointsheet/tests.py

from .models import Pointsheet
from .serializers import PointsheetSerializer
from django.test import TestCase
import unittest

class TestPointsheet(unittest.TestCase):
	"""
	"""

	def test_insert_pointsheet(self):
		"""
		"""
		Pointsheet.objects.create(year=2017, month=01)
		_count = len(Pointsheet.objects.all())
		# Assert
		self.assertNotEqual(0, _count)

	def test_list_pointsheet(self):
		"""
		"""
		_list = Pointsheet.objects.all()
		_count = len(_list)
		# Assert
		self.assertNotEqual(0, _count)

if __name__ == '__main__':
	unittest.main()