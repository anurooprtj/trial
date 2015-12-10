# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0006_auto_20150821_1510'),
        ('reviews', '0005_restaurantreview_likedby'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ReviewImage', models.ImageField(upload_to=b'reviewpics/')),
                ('imageBy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('imageofRest', models.OneToOneField(to='restaurants.Restaurant')),
                ('imageofRev', models.ForeignKey(to='reviews.RestaurantReview')),
            ],
        ),
    ]
