# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0010_auto_20150907_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imgcomment', models.TextField(default=b'')),
                ('imgcommentOn', models.DateTimeField(auto_now_add=True)),
                ('commentBy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('commentOf', models.ForeignKey(to='reviews.ReviewImages')),
            ],
        ),
    ]
