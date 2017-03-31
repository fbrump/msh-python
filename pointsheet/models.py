from __future__ import unicode_literals

from django.db import models

class PointSheet(models.Model):
    """
    Description: This model keep all release for hours.
    """
    year = models.IntegerField()
    month = models.IntegerField()
    #person
    #manager
    #company
    #position

    class Meta:
        pass