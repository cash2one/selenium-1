# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0004_auto_20170724_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='clicktask',
            name='pv',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1),
        ),
    ]