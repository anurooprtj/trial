# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20150820_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantreview',
            name='reviewRating',
            field=models.IntegerField(default=3),
        ),
    ]
