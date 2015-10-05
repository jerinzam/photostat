# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printo_app', '0004_auto_20151004_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='orderCount',
        ),
        migrations.AddField(
            model_name='city',
            name='latitude',
            field=models.DecimalField(null=True, decimal_places=7, max_digits=11),
        ),
        migrations.AddField(
            model_name='city',
            name='longitude',
            field=models.DecimalField(null=True, decimal_places=7, max_digits=11),
        ),
        migrations.AddField(
            model_name='college',
            name='latitude',
            field=models.DecimalField(null=True, decimal_places=7, max_digits=11),
        ),
        migrations.AddField(
            model_name='college',
            name='longitude',
            field=models.DecimalField(null=True, decimal_places=7, max_digits=11),
        ),
        migrations.AddField(
            model_name='shop',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
