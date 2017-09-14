# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170725_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('foget', '找回密码')], default='register', max_length=10, verbose_name='发送类型'),
        ),
    ]