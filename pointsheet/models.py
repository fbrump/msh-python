# -*- coding: utf-8 -*-
# msh-python/pointsheet/models.py

from __future__ import unicode_literals

from django.db import models

class Pointsheet(models.Model):
    """
    Description: This model keep all release for hours.
    """
    year = models.IntegerField()
    month = models.IntegerField()
    #person
    #manager
    #company
    #position

    #class Meta:
        #unique_together = ('year', 'month')
        #index_together = ['year', 'month', 'pointsheet']