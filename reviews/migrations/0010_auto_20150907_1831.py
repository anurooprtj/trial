# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0009_auto_20150903_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='likedby',
        ),
        migrations.AlterField(
            model_name='reviewimages',
            name='imageBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviewimages',
            name='imageofRest',
            field=models.ForeignKey(to='restaurants.Restaurant'),
        ),
        migrations.AlterField(
            model_name='reviewimages',
            name='imageofRev',
            field=models.ForeignKey(to='reviews.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='likes',
            name='likeOf',
            field=models.ForeignKey(to='reviews.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='likes',
            name='likedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
