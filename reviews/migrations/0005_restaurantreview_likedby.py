# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20150820_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantreview',
            name='likedby',
            field=models.BooleanField(default=False),
        ),
    ]
