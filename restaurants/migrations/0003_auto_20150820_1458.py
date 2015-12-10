# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_restaurantcusines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='RestaurantCusines',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='restaurantCusines',
            field=json_field.fields.JSONField(default={b'arabianCusine': False, b'southIndianCusine': False, b'fastfoodCusine': False, b'gujarathiCusine': False, b'chettinadCusine': False, b'tibetanCusine': False, b'kashmiriCusine': False, b'hyderabadiCusine': False, b'americanCusine': False, b'bengaliCusine': False, b'asianCusine': False, b'spanishCusine': False, b'coffeeteaCusine': False, b'multiCusine': False, b'middleEastCusine': False, b'europeanCusine': False, b'mexicanCusine': False, b'cafeCusine': False, b'northIndianCusine': False, b'dessertsCusine': False, b'pakisthaniCusine': False, b'frenchCusine': False, b'continentalCusine': False, b'malabariCusine': False, b'keralaCusine': False, b'italianCusine': False, b'seaFoodCusine': False, b'lounge': False, b'streetFoodCusine': False, b'biriyaniCusine': False, b'healthyFoodCusine': False, b'juices': False, b'pizza': False, b'bakeryCusine': False, b'thaiCusine': False, b'mughlaiCusine': False, b'britishCusine': False, b'pub': False, b'otherCusines': False, b'chineseCusine': False, b'japaneseCusine': False, b'andhraCusine': False, b'nepaleseCusine': False, b'malaysianCusine': False, b'goanCusine': False}, help_text='Enter a valid JSON object'),
        ),
    ]
