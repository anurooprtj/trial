# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20150902_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkincounter',
            old_name='resturant',
            new_name='restaurant',
        ),
    ]
