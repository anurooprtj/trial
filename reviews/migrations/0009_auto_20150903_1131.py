# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20150901_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewimages',
            name='ReviewImage',
            field=models.ImageField(upload_to=reviews.models.img_path),
        ),
    ]
