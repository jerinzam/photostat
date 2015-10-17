# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printo_app', '0005_auto_20151005_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('orderNo', models.CharField(unique=True, blank=True, max_length=60)),
                ('customer', models.CharField(max_length=20)),
                ('orderDate', models.DateTimeField(null=True, auto_now_add=True)),
                ('qty', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('printType', models.IntegerField(default=1, choices=[(1, 'one-side'), (2, 'two-side')])),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_printed', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('document', models.ManyToManyField(to='printo_app.Document')),
                ('shop', models.ForeignKey(to='printo_app.Shop')),
            ],
        ),
    ]
