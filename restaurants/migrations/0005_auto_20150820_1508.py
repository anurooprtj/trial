# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20150820_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantCusines',
            field=json_field.fields.JSONField(default=b'{\n\t"americanCusine":0,\n\t"andhraCusine" :0,\n\t"arabianCusine": 0,\n\t"asianCusine":0,\n\t"bakeryCusine":0,\n\t"bengaliCusine":0,\n\t"biriyaniCusine":0,\n\t"britishCusine":0,\n\t"cafeCusine":0,\n\t"chettinadCusine":0,\n\t"chineseCusine":0,\n\t"coffeeteaCusine":0,\n\t"fastfoodCusine":0,\n\t"continentalCusine":0,\n\t"dessertsCusine":0,\n\t"europeanCusine":0,\n\t"frenchCusine":0,\n\t"goanCusine":0,\n\t"gujarathiCusine":0,\n\t"healthyFoodCusine":0,\n\t"hyderabadiCusine":0,\n\t"italianCusine":0,\n\t"japaneseCusine":0,\n\t"juices":0,\n\t"kashmiriCusine":0,\n\t"keralaCusine":0,\n\t"lounge":0,\n\t"malabariCusine":0,\n\t"malaysianCusine":0,\n\t"mexicanCusine":0,\n\t"middleEastCusine":0,\n\t"mughlaiCusine":0,\n\t"multiCusine":0,\n\t"nepaleseCusine":0,\n\t"northIndianCusine":0,\n\t"otherCusines":0,\n\t"pakisthaniCusine":0,\n\t"pizza":0,\n\t"pub":0,\n\t"seaFoodCusine":0,\n\t"southIndianCusine":0,\n\t"spanishCusine":0,\n\t"streetFoodCusine":0, \n\t"thaiCusine" :0,\n   \t"tibetanCusine":0 }', help_text='Enter a valid JSON object'),
        ),
    ]
