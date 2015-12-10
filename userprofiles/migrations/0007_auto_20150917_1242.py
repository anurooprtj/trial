# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0006_userprofile_profilestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(default=b'userpics/unnamed.jpg', upload_to=b'userpics/userprofile', blank=True),
        ),
    ]
