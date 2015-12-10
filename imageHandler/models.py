from django.db import models
from restaurants.models import Restaurant
from reviews.models import RestaurantReview

class RestaurantImage(models.Model):
	restaurantImage = models.ImageField(upload_to = 'restaurantpics/restaurantimages')
	restaurantId = models.ForeignKey(Restaurant)
	def __unicode__(self):
		return self.id


class ReviewImage(models.Model):
	reviewImage = models.ImageField(upload_to = 'restaurantpics/reviews')
	reviewId = models.ForeignKey(RestaurantReview)
	def __unicode__(self):
		return self.id


