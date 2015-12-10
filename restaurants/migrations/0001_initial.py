# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restaurantName', models.CharField(max_length=200)),
                ('restaurantContact', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('restaurantWebsite', models.URLField()),
                ('restaurantFBLink', models.URLField()),
                ('restaurantAddress', models.TextField(default=b'')),
                ('restaurantCity', models.CharField(max_length=100)),
                ('restaurantLocation', models.CharField(max_length=100)),
                ('restaurantMapLocation', location_field.models.plain.PlainLocationField(max_length=63)),
                ('openingTime', models.TimeField(null=True, blank=True)),
                ('closingTime', models.TimeField(null=True, blank=True)),
                ('hitCount', models.IntegerField(default=0)),
                ('checkInCount', models.IntegerField(default=0)),
            ],
        ),
    ]
