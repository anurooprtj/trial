# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='RestaurantCusines',
            field=json_field.fields.JSONField(default={b'Indian': True, b'Italian': False}, help_text='Enter a valid JSON object'),
        ),
    ]
