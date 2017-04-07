# -*- coding: utf-8 -*-
# msh-python/release/models.py

from __future__ import unicode_literals

from django.db import models

from pointsheet.models import Pointsheet

class Release(models.Model):
    """
    Description: That class mapping release of system.

    Properties:
    	date 			 		--
    	dayweek 		 		--
    	checkin 		 		--
    	checkout_lunch 	 		--
    	checkin_lunch 	 		--
    	checkout 		 		--
    	is_holiday 		 		--
    	type_absence 	 		--
    	checkin_absence  		--
    	checkout_absence 		--
    	justification_absence 	--
    	file_link 				--
    	pointsheet 				--
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
		('3', 'Day off'),)
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
        index_together = ['date', 'day_of_week', 'pointsheet']