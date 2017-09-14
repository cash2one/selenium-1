# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-19 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(error_messages={'unique': '用户名已存在'}, help_text='不允许有特殊字符', max_length=50, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机')),
                ('image', models.ImageField(default='media/default.jpg', upload_to='media/userprofile/%Y')),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户信息',
            },
        ),
    ]