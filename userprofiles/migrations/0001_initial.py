# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20150820_1508'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckInCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkInCount', models.IntegerField(default=1)),
                ('resturant', models.ForeignKey(to='restaurants.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restaurantObject', models.OneToOneField(to='restaurants.Restaurant')),
                ('userObject', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profilePicture', models.ImageField(upload_to=b'userpics/userprofile')),
                ('coverPicture', models.ImageField(upload_to=b'userpics/usercover')),
                ('followersCount', models.IntegerField(default=0)),
                ('userPoints', models.IntegerField(default=0)),
                ('checkedInAt', models.ManyToManyField(related_name='checked_in_at', through='userprofiles.CheckInCounter', to='restaurants.Restaurant')),
                ('follows', models.ManyToManyField(related_name='follow', to='userprofiles.UserProfile')),
                ('userObject', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checkincounter',
            name='user',
            field=models.ForeignKey(to='userprofiles.UserProfile'),
        ),
    ]
