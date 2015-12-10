# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20150820_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantCusines',
            field=json_field.fields.JSONField(default=b'{\n\t"americanCusine":False,\n\t"andhraCusine" :False,\n\t"arabianCusine": False,\n\t"asianCusine":False,\n\t"bakeryCusine":False,\n\t"bengaliCusine":False,\n\t"biriyaniCusine":False,\n\t"britishCusine":False,\n\t"cafeCusine":False,\n\t"chettinadCusine":False,\n\t"chineseCusine":False,\n\t"coffeeteaCusine":False,\n\t"fastfoodCusine":False,\n\t"continentalCusine":False,\n\t"dessertsCusine":False,\n\t"europeanCusine":False,\n\t"frenchCusine":False,\n\t"goanCusine":False,\n\t"gujarathiCusine":False,\n\t"healthyFoodCusine":False,\n\t"hyderabadiCusine":False,\n\t"italianCusine":False,\n\t"japaneseCusine":False,\n\t"juices":False,\n\t"kashmiriCusine":False,\n\t"keralaCusine":False,\n\t"lounge":False,\n\t"malabariCusine":False,\n\t"malaysianCusine":False,\n\t"mexicanCusine":False,\n\t"middleEastCusine":False,\n\t"mughlaiCusine":False,\n\t"multiCusine":False,\n\t"nepaleseCusine":False,\n\t"northIndianCusine":False,\n\t"otherCusines":False,\n\t"pakisthaniCusine":False,\n\t"pizza":False,\n\t"pub":False,\n\t"seaFoodCusine":False,\n\t"southIndianCusine":False,\n\t"spanishCusine":False,\n\t"streetFoodCusine":False, \n\t"thaiCusine" :False,\n   \t"tibetanCusine":False }', help_text='Enter a valid JSON object'),
        ),
    ]
