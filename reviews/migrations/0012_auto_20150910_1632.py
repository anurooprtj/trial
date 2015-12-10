# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_imgcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgcomments',
            name='imgcommentOn',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
