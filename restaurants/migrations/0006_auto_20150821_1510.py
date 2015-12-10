# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20150820_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurantRating',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='voteCount',
            field=models.IntegerField(default=0),
        ),
    ]
