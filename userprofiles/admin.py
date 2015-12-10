from django.contrib import admin

from .models import UserProfile, RestaurantProfile, CheckInCounter

admin.site.register(UserProfile)
admin.site.register(RestaurantProfile)
admin.site.register(CheckInCounter)