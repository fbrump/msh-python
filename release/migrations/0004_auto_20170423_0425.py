# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-23 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0003_auto_20170414_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='pointsheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointsheet.Pointsheet'),
        ),
    ]
