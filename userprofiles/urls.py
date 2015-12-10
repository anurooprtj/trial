from django.conf.urls import patterns,url
from userprofiles import views

urlpatterns = [
	url(r'^profile/(?P<userName>[\w\-]+)/$',views.viewUser,name = "viewProfile"),
	url(r'^createProfile/',views.createProfile,name = "createProfie"),
	url(r'^followher/(?P<userprofile_id>[0-9]+)/$',views.followme,name="followher"),
	url(r'^unfollowhim/(?P<userprofile_id>[0-9]+)/$',views.unfollowhim,name="unfollowhim"),
	url(r'^saveBasic/',views.saveBasic,name = "saveBasic"),
	url(r'^savePhone/',views.savePhone,name = "savePhone"),
	url(r'^delete/',views.deleteProfile,name = "deleteProfile"),
	url(r'^viewProfile/',views.viewProfile,name = "viewProfile"),
	url(r'(?P<restaurantId>[\w\-]+)/check-in/$',views.addCheckin,name= "checkIn"),

]