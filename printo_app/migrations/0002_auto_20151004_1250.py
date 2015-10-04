# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-04 12:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='organization',
            name='employee',
            field=models.ManyToManyField(blank=True, related_name='org_employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
