# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_reviewimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewimages',
            name='imageBy',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviewimages',
            name='imageofRest',
            field=models.OneToOneField(default=b'', to='restaurants.Restaurant'),
        ),
        migrations.AlterField(
            model_name='reviewimages',
            name='imageofRev',
            field=models.ForeignKey(default=b'', to='reviews.RestaurantReview'),
        ),
    ]
