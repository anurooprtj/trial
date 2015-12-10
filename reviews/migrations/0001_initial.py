# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0003_auto_20150820_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewText', models.TextField(default=b'')),
                ('reviewRating', models.IntegerField(default=0)),
                ('reviewedOn', models.DateTimeField(auto_now=True)),
                ('likeCount', models.IntegerField(default=0)),
                ('reviewOn', models.ForeignKey(to='restaurants.Restaurant')),
                ('reviewedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('replyText', models.TextField(default=b'')),
                ('repliedOn', models.DateTimeField(auto_now=True)),
                ('repliedBy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('replyOn', models.ForeignKey(to='reviews.RestaurantReview')),
            ],
        ),
    ]
