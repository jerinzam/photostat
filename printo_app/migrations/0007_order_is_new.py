# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printo_app', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
