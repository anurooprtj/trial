from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from phonenumber_field.modelfields import PhoneNumberField
class UserProfile(models.Model):
	userObject = models.OneToOneField(User)
	firstName = models.CharField(max_length = 100,blank = True)
	middleName = models.CharField(max_length = 100,blank = True)
	lastName = models.CharField(max_length =100,blank = True)
	phoneNumber = PhoneNumberField(blank = True) 
	profilePicture = models.ImageField(upload_to = 'userpics/userprofile',blank = True,)
	coverPicture = models.ImageField(upload_to = 'userpics/usercover',blank = True)
	followersCount = models.IntegerField(default = 0)
	follows = models.ManyToManyField('self',related_name= "follow", symmetrical = False,blank = True)
	userPoints = models.IntegerField(default  = 0)
	checkedInAt = models.ManyToManyField(Restaurant,related_name = 'checked_in_at',symmetrical = False,through = 'CheckInCounter')
	profileStatus = models.CharField(max_length = 250, default = "")
	def __unicode__(self):
		return unicode(self.id)
	
 
class RestaurantProfile(models.Model):
	userObject = models.OneToOneField(User)
	profilePicture = models.ImageField(upload_to = 'restaurantpics/restaurantimages',blank = True)
	restaurantObject = models.OneToOneField(Restaurant)
	def __unicode__(self):
		return unicode(self.userObject)



class CheckInCounter(models.Model):
	user = models.ForeignKey(UserProfile)
	restaurant = models.ForeignKey(Restaurant)
	checkInCount = models.IntegerField(default = 1)
	def __unicode__(self):
		return unicode(self.user)

