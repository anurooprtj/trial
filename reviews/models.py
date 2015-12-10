from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant

class RestaurantReview(models.Model):
	reviewText = models.TextField(null=False,blank=False)
	reviewRating = models.IntegerField(blank=False,null=False,default = 3)
	reviewedBy  = models.ForeignKey(User)
	reviewOn = models.ForeignKey(Restaurant)
	reviewedOn = models.DateTimeField(auto_now_add = True)
	likeCount = models.IntegerField(default = 0)
	def __unicode__(self):
		return unicode(self.id)



class likes(models.Model):
	likedBy=models.ForeignKey(User)
	likeOf=models.ForeignKey(RestaurantReview)




class ReviewReply(models.Model):
	replyText =models.TextField(default = "")
	repliedBy = models.ForeignKey(User)
	replyOn = models.ForeignKey(RestaurantReview)
	repliedOn = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return unicode(self.id)


def img_path(instance,filename):
	name="pics"
	return 'reviewpics/'+str(instance.imageofRest.restaurantName)+str(instance.imageofRev.id)+str(instance.imageofRest.id)


class ReviewImages(models.Model):
	ReviewImage=models.ImageField(upload_to=img_path)
	imageofRev=models.ForeignKey(RestaurantReview)
	imageofRest=models.ForeignKey(Restaurant)
	imageBy=models.ForeignKey(User)

class ImgComments(models.Model):
	commentOf=models.ForeignKey(ReviewImages)
	commentBy=models.ForeignKey(User)
	imgcomment=models.TextField(default="")
	imgcommentOn=models.DateTimeField(auto_now=True)
