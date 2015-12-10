from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField
from json_field import JSONField

class Restaurant(models.Model):
	restaurantName = models.CharField(max_length = 200)
	restaurantContact = PhoneNumberField()
	restaurantWebsite = models.URLField()
	restaurantFBLink = models.URLField()
	restaurantAddress = models.TextField(default = "")
	restaurantCity = models.CharField(max_length = 100)
	restaurantLocation  = models.CharField(max_length = 100)
	restaurantMapLocation = PlainLocationField(based_fields = [restaurantLocation],zoom = 13)
	openingTime = models.TimeField(null = True, blank = True, auto_now  = False, auto_now_add = False)
	closingTime = models.TimeField(null = True, blank = True, auto_now = False, auto_now_add = False)
	hitCount  = models.IntegerField(default = 0)
	checkInCount = models.IntegerField(default = 0)
	restaurantRating = models.DecimalField(decimal_places = 1,max_digits = 2)
	voteCount = models.IntegerField(default = 0)
	
	americanCusine = models.BooleanField(default = False)
	andhraCusine = models.BooleanField(default = False)
	arabianCusine = models.BooleanField(default = False)
	bakeryCusine = models.BooleanField(default = False)
	bengaliCusine = models.BooleanField(default = False)
	biriyaniCusine = models.BooleanField(default = False)
	britishCusine  = models.BooleanField(default = False)
	cafeCusine = models.BooleanField(default = False)
	chettinadCusine = models.BooleanField(default = False)
	chineseCusine = models.BooleanField(default = False)
	coffeeteaCusine = models.BooleanField(default = False)
	fastfoodCusine = models.BooleanField(default = False)
	continentalCusine = models.BooleanField(default = False)
	dessertsCusine = models.BooleanField(default = False)
	europeanCusine = models.BooleanField(default = False)
	frenchCusine = models.BooleanField(default = False)
	goanCusine = models.BooleanField(default = False)
	gujarathiCusine = models.BooleanField(default = False)
	healthyFoodCusine = models.BooleanField(default = False)
	hyderabadiCusine = models.BooleanField(default = False)
	italianCusine  = models.BooleanField(default = False)
	japaneseCusine = models.BooleanField(default = False)
	juices = models.BooleanField(default = False)
	kashmiriCusine = models.BooleanField(default = False)
	keralaCusine = models.BooleanField(default = False)
	lounge = models.BooleanField(default = False)
	malabariCusine = models.BooleanField(default = False)
	malaysianCusine = models.BooleanField(default = False)
	mexicanCusine = models.BooleanField(default = False)
	middleEastCusine = models.BooleanField(default = False)
	mughlaiCusine = models.BooleanField(default = False)
	multiCusine = models.BooleanField(default = False)
	nepaleseCusine = models.BooleanField(default = False)
	northIndianCusine = models.BooleanField(default = False)
	otherCusines = models.BooleanField(default = False)
	pakisthaniCusine = models.BooleanField(default = False)
	pizza = models.BooleanField(default = False)
	pub = models.BooleanField(default = False)
	seaFoodCusine = models.BooleanField(default = False)
	spanishCusine = models.BooleanField(default = False)
	streetFoodCusine = models.BooleanField(default = False)
	thaiCusine = models.BooleanField(default = False)
	tibetanCusine = models.BooleanField(default = False)


	restaurantCusines = JSONField(default="""{
	"americanCusine":0,
	"andhraCusine" :0,
	"arabianCusine": 0,
	"asianCusine":0,
	"bakeryCusine":0,
	"bengaliCusine":0,
	"biriyaniCusine":0,
	"britishCusine":0,
	"cafeCusine":0,
	"chettinadCusine":0,
	"chineseCusine":0,
	"coffeeteaCusine":0,
	"fastfoodCusine":0,
	"continentalCusine":0,
	"dessertsCusine":0,
	"europeanCusine":0,
	"frenchCusine":0,
	"goanCusine":0,
	"gujarathiCusine":0,
	"healthyFoodCusine":0,
	"hyderabadiCusine":0,
	"italianCusine":0,
	"japaneseCusine":0,
	"juices":0,
	"kashmiriCusine":0,
	"keralaCusine":0,
	"lounge":0,
	"malabariCusine":0,
	"malaysianCusine":0,
	"mexicanCusine":0,
	"middleEastCusine":0,
	"mughlaiCusine":0,
	"multiCusine":0,
	"nepaleseCusine":0,
	"northIndianCusine":0,
	"otherCusines":0,
	"pakisthaniCusine":0,
	"pizza":0,
	"pub":0,
	"seaFoodCusine":0,
	"southIndianCusine":0,
	"spanishCusine":0,
	"streetFoodCusine":0, 
	"thaiCusine" :0,
   	"tibetanCusine":0 }""")
	

	def __unicode__(self):
		return unicode(self.id)


