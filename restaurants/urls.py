from django.conf.urls import patterns,url
from restaurants import views
urlpatterns = [

	url(r'^$',views.home, name = "home"),
	url(r'^viewgraph/sample/$',views.show_graph,name ="show_graph"),
	url(r'^viewrestaurant/(?P<restaurantId>[0-9]+)/$',views.viewRestaurant,name = "viewRestaurant"),
	url(r'filter/$',views.applyFilter,name = "applyFilter"),
	url(r'(?P<location>[\w\-]+)/$',views.byLocation,name = "byLocation"),
	
	



]