# -*- coding: utf-8 -*-
# msh-python/release/models.py

from __future__ import unicode_literals

from django.db import models

from pointsheet.models import Pointsheet

class Release(models.Model):
	"""
	Description: That class mapping release of system.

	Properties:
		date 			 		-- Date of release
		dayweek 		 		-- Day of week of release
		checkin 		 		-- Time of check-in job
		checkout_lunch 	 		-- Time of check-out to lunch
		checkin_lunch 	 		-- Time of check-in from lunch
		checkout 		 		-- Time of check-out job
		is_holiday 		 		-- Is holiday or not
		type_absence 	 		-- Type of absence, if exist
		checkin_absence  		-- Time of check-in to absence, if exist
		checkout_absence 		-- Time of check-out from absence, if exist
		justification_absence 	-- Description of justification of absence, if exist
		file_link 				-- File for link with document or something like this for justification absence, if existe
		pointsheet 				-- Pointsheet associated
	"""
	SUNDAY = 'SUN'
	MONDAY = 'MON'
	TUESDAY = 'TUE'
	WEDNESDAY = 'WED'
	THUSDAY = 'THU'
	FRIDAY = 'FRI'
	SATURDAY = 'SAT'
	DAY_OF_WEEK_CHOICES = (
		(SUNDAY, 'Sunday'),
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNESDAY, 'Wednesday'),
		(THUSDAY, 'Thusday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday'),
	)
	TYPE_ABSENCE_CHOICES = (
		('1', 'Medical appointment'),
		('2', 'Personal matters'),
		('3', 'Day off'),
	)
	date = models.DateField()
	dayweek = models.CharField(
		max_length=3,
		choices=DAY_OF_WEEK_CHOICES
	)
	checkin = models.TimeField()
	checkout_lunch = models.TimeField(null=True)
	checkin_lunch = models.TimeField(null=True)
	checkout = models.TimeField()
	is_holiday = models.BooleanField(default=False)
	type_absence = models.CharField(
		blank=True, 
		null=True,
		max_length=3,
		choices=TYPE_ABSENCE_CHOICES
	)
	checkin_absence = models.TimeField(null=True)
	checkout_absence = models.TimeField(null=True)
	justification_absence = models.TextField(null=True, max_length=5000)
	file_link = models.URLField(max_length=2000, null=True)
	# Relationsheep
	pointsheet = models.ForeignKey(Pointsheet, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('date', 'pointsheet')
		index_together = ['date', 'dayweek', 'pointsheet']
