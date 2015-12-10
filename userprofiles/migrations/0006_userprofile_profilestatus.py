# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0005_auto_20150908_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profileStatus',
            field=models.CharField(default=b'', max_length=250),
        ),
    ]
