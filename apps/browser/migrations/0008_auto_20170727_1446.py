# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-27 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0007_auto_20170725_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='clicktask',
            name='sectime',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clicktask',
            name='securl',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
