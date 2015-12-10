# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20150831_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantprofile',
            name='profilePicture',
            field=models.ImageField(upload_to=b'restaurantpics/restaurantimages', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='coverPicture',
            field=models.ImageField(upload_to=b'userpics/usercover', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(upload_to=b'userpics/userprofile', blank=True),
        ),
    ]
