# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0014_auto_20181120_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientbill',
            name='include_timesheet',
            field=models.BooleanField(default=False, verbose_name='Include timesheet'),
        ),
    ]
