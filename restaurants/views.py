from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.template import Context, Template, RequestContext
from django.template.loader import get_template

from .models import Restaurant

import json
from django.db.models import Q

from reviews.models import RestaurantReview,likes
from django.contrib.auth.models import User
from django.db.models import Count
from math import sin,cos,sqrt,atan2,radians

from graphos.sources.simple import SimpleDataSource
from graphos.renderers import flot


def home(request):
	restaurants = Restaurant.objects.all()
	contexDi  = {}
	review = []
	for each in restaurants:
		restaurantreview = {}
		restaurantreview['restaurantObject'] = each
		restaurantreview['name'] = each.restaurantName

		restaurantreview['comment'] = each.restaurantreview_set.all()


		review.append(restaurantreview)


	contexDi['reviews'] = review
	
	return render(request,'restaurants/home.html',contexDi)


def viewRestaurant(request,restaurantId):
	contextDi = {}
	restaurant = Restaurant.objects.get(id = restaurantId)
	likeobjects=likes.objects.all()
	restaurantReviews = restaurant.restaurantreview_set.all()
	checkInCount = restaurant.checkincounter_set.count()
	contextDi['checkInCount'] = checkInCount
	address = [x.strip for x in restaurant.restaurantAddress.split(',')]
	contextDi['address'] = address
	contextDi['restaurantObject'] = restaurant
	contextDi['reviews'] = restaurantReviews
	print request.user.is_active
	if request.user.is_active:
		username=request.user
		userobj=User.objects.get(username=username)
		likedreviews=[]
		for each in likes.objects.filter(likedBy=userobj):
			likedreviews.append(each.likeOf)
		contextDi['likedreviews']=likedreviews		
	nearbyRestObjects=findNearby(restaurantId)
	topfoodiesid=find_topfoodies(restaurantId)
	topfoodies=[]
	for each in topfoodiesid:
		topfoodies.append(User.objects.get(pk=each))
	contextDi['topfoodies']=topfoodies
	contextDi['nearbyrestobj']=nearbyRestObjects
	return render(request,'restaurants/view.html',contextDi)



def byLocation(request,location):
	contextDi = {}
	location = str(location)
	restaurants = Restaurant.objects.filter(restaurantCity = location)
	review =[]
	for each in restaurants:
		restaurantreview = {}
		restaurantreview['restaurantObject'] = each 
		restaurantreview['name'] = each.restaurantName
		restaurantreview['comment'] = each.restaurantreview_set.all()[0]
		review.append(restaurantreview)

	contextDi['reviews'] = review
	contextDi['city'] = location
	return render(request,'restaurants/home.html',contextDi)




def applyFilter(request):
	contextDi = {}
	if request.GET.get('location'):
		location = request.GET['location']
		print location
		restaurants =Restaurant.objects.filter(restaurantCity= location)
	else:
		restaurants = Restaurant.objects.all()
		location = "Cochin"


	requiredRestaurants  = []
	if request.GET.get('cusineFilters'):
		array1 = json.loads(request.GET['cusineFilters'])
		for each in array1:
			for restaurant in restaurants.all():
				if getattr(restaurant,each):
					requiredRestaurants.append(restaurant)
					


	restaurants = list(set(requiredRestaurants))


	if request.GET.get('featureFilters'):
		array2 = json.loads(request.GET['featureFilters'])
		for each in array2:
			for restaurant in restaurants:
				if not getattr(restaurant,each):
					restaurants.remove(restaurant)


	
	review = []
	
	for each in restaurants:

		restaurantreview = {}
		restaurantreview['restaurantObject'] = each
		restaurantreview['name'] = each.restaurantName
		restaurantreview['comment'] = each.restaurantreview_set.all()[0]
		review.append(restaurantreview)

	contextDi['reviews'] = review
	contextDi['city'] = location
	
	
	print review
	data = {"city":location}
	return render(request,'restaurants/filter.html',contextDi)


def findNearby(restaurantId):
	restobj=Restaurant.objects.get(id=restaurantId)
	loc=restobj.restaurantMapLocation
	latlong=loc.split(',')
	latorg=float(latlong[0])
	lonorg=float(latlong[1])
	nearbyrest=[]
	otherobjects=Restaurant.objects.filter(~Q(id=restaurantId))
	for each in otherobjects:
		latlongtemp=each.restaurantMapLocation.split(',')
		lattemp=float(latlongtemp[0])
		lontemp=float(latlongtemp[1])
		R = 6373.0
		lat1 = radians(latorg)
		lon1 = radians(lonorg)
		lat2 = radians(lattemp)
		lon2 = radians(lontemp)
		dlon = lon2 - lon1
		dlat = lat2 - lat1
		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))
		distance=R*c
		if distance<5:
			nearbyrest.append(each)
	return nearbyrest

def find_topfoodies(restaurantId):
	restobj=Restaurant.objects.get(id=restaurantId)
	foodieobjects=RestaurantReview.objects.values('reviewedBy').filter(reviewOn=restobj).annotate(num_reviews=Count('reviewedBy')).order_by('-num_reviews')[:5]
	topfoodiesid=[]
	print foodieobjects
	for each in foodieobjects:
		topfoodiesid.append(each['reviewedBy'])
	return topfoodiesid


def show_graph(request):
    #create datapool and initialize chartobject
    '''true=True
    data1 =  [
        [2004, 50,200],
        [2005, 100,150],
        [2006, 150,100],
        [2007, 200,50]
    ]    
    data2 =  [
        [2004, 200],
        [2005, 150],
        [2006, 100],
        [2007, 50]
    ]
    dataset2=[{'data':data1},{'data':data2}
        ]
    dataset=[
    {
    "label":'data1',
    "data":data1,
    "yaxis":1,
    "color": "#FF0000",
    "points":{'symbol':'triangle','fillcolor':'#FF0001','show':'true'},
    "lines":{'show':'true'},
    },
    {
    "label":"data2",
    "data":data2,
    "yaxis":2,
    "color":'#0062FF',
    "points":{'symbol':'diamond','fillcolor':'#0162FF','show':'true'},
    "lines":{'show':'true'},
    }
    ]    
    print dataset2
    chart = flot.LineChart(SimpleDataSource(data=dataset),options={'xaxes':{'ticks':[]},'yaxes':[{'position': "left",
        'color': "black",
        'yaxis':1,
        "points":{'symbol':'diamond','fillcolor':'#0162F3','show':'true'},
        "lines":{'show':'true'},        
        'axisLabel': "Sin(x)",
        'axisLabelFontSizePixels': 12,
        'axisLabelFontFamily': 'Verdana, Arial',
        'axisLabelPadding': 3},

        { 'position': "right",           
        'color': "black",
        'yaxis':2,
        'axisLabel': "Cos(x)",
        'axisLabelFontSizePixels': 12,
        'axisLabelFontFamily': 'Verdana, Arial',
        'axisLabelPadding': 3}]})
    data=[
    [0, 0.995], [1, 0.98007], [2, 0.95534], [3, 0.92106], [4, 0.87758], [5, 0.82534], [6, 0.76484], [7, 0.69671], [8, 0.62161], [9, 0.5403], [10, 0.4536], [11, 0.36236], [12, 0.2675], [13, 0.16997], [14, 0.07074], [15, -0.0292], [16, -0.12884], [17, -0.2272], [18, -0.32329], [19, -0.41615], [20, -0.50485], [21, -0.5885], [22, -0.66628], [23, -0.73739], [24, -0.80114], [25, -0.85689], [26, -0.90407], [27, -0.94222], [28, -0.97096], [29, -0.98999], [30, -0.99914], [31, -0.99829], [32, -0.98748], [33, -0.9668], [34, -0.93646], [35, -0.89676], [36, -0.8481], [37, -0.79097], [38, -0.72593], [39, -0.65364], [40, -0.57482], [41, -0.49026], [42, -0.4008], [43, -0.30733], [44, -0.2108], [45, -0.11215], [46, -0.01239], [47, 0.0875], [48, 0.18651], [49, 0.28366], [50, 0.37798]]
    return render_to_response('restaurants/graph.html',{'chart':chart,'data':data})'''
    return HttpResponse('none')



