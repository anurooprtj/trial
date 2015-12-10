from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile,CheckInCounter
from restaurants.models import Restaurant


def viewUser(request,userName):
	contextDi = {}
	if request.user.is_active:
		currentUser=User.objects.get(username=request.user)
		currentuserprofileobject=UserProfile.objects.get(userObject=currentUser)
		contextDi['userprofileObject'] = currentuserprofileobject
	userObject = User.objects.get(username = userName)
	profileObject = UserProfile.objects.get(userObject = userObject)
	contextDi['profileObject'] = profileObject
	contextDi['recentCheckIns'] = profileObject.checkincounter_set.all()[:10]
	contextDi['reviews'] = userObject.restaurantreview_set.all()
	contextDi['favouriteSpots'] = profileObject.checkincounter_set.all()[:10]
	return render(request,'profile/profile.html',contextDi)


@login_required
def createProfile(request):
	if request.user:
		username = request.user
		userObject = User.objects.get(username = username)
		contextDi = {}
		if UserProfile.objects.filter(userObject = userObject).count():
			return HttpResponseRedirect('/restaurants/')

	if request.POST:
		username = request.user
		userObject = User.objects.get(username = username)
		contextDi = {}
		if UserProfile.objects.filter(userObject = userObject).count():
			return HttpResponseRedirect('/restaurants/')
		else:
			newProfile = UserProfile(userObject = userObject)
			newProfile.save()
			contextDi['profileObject'] = userObject
			return render(request,'profile/createProfile.html',contextDi)
	else:
		return render(request,'profile/createProfile.html')
			


@login_required
def saveBasic(request):
	if request.POST:
		contextDi = {}
		username = request.user
		userObject = User.objects.get(username = username)
		userProfileObject = UserProfile.objects.get(userObject = userObject)
		data = request.POST
		firstName = data['firstname']
		middleName = data['middlename']
		lastName = data['lastname']
		if request.FILES:
			profilePic = request.FILES['profilePic']
			userProfileObject.profilePicture = profilePic
		userProfileObject.middleName = middleName
		userProfileObject.lastName = lastName
		userProfileObject.firstName = firstName
		userProfileObject.save()
		contextDi['user'] = userObject
		contextDi['profile'] = userProfileObject
		return HttpResponseRedirect('/profiles/viewProfile/')

@login_required
def savePhone(request):
	if request.POST:
		contextDi = {}
		username =request.user
		userObject = User.objects.get(username = username)
		userProfileObject =  UserProfile.objects.get(userObject = userObject)
		data =request.POST
		phoneNumber = data['contact']
		userProfileObject(phoneNumber = phoneNumber)
		userProfileObject.save()
		return render(request,'profile/viewProfile.html',contextDi)


@login_required
def deleteProfile(request):
	if request.POST or None:
		username = request.user
		userObject = User.objects.get(username = username)
		userProfileObject = UserProfile.objects.get(userObject = userObject)
		userProfileObject.delete()
		userObject.delete()
		return render(request,'/restaurants/',)


@login_required
def viewProfile(request):
	contextDi = {}
	username = request.user
	userObject = User.objects.get(username = username)	
	if  UserProfile.objects.filter(userObject = userObject):
		contextDi['user'] = userObject 
		contextDi['profileObject'] = UserProfile.objects.get(userObject=userObject)
		profobj=UserProfile.objects.get(userObject=userObject)
		print profobj.middleName
		return render (request,'profile/viewProfile.html',contextDi)
	else:
	    contextDi['noprofile']='You havent created ur profile yet....'
	    return render(request,'profile/viewProfile.html',contextDi)	

@login_required
def addCheckin(request,restaurantId):
	username = request.user
	userObject = User.objects.get(username = username)
	userProfile = UserProfile.objects.get(userObject = userObject)
	restaurantObject=Restaurant.objects.get(id = restaurantId)
	if(CheckInCounter.objects.filter(user = userProfile).filter(restaurant = restaurantObject).count()):
		chechInObject = CheckInCounter.objects.filter(user = userProfile).get(restaurant = restaurantObject)
		chechInObject.checkInCount = chechInObject.checkInCount+1
		chechInObject.save()
	else:
		checkIn = CheckInCounter(user = userProfile,restaurant = restaurantObject)
		checkIn.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def followme(request,userprofile_id):
	username=request.user
	userObject=User.objects.get(username=username)
	following=UserProfile.objects.get(userObject=userObject)
	tofollow=UserProfile.objects.get(id=userprofile_id)
	if tofollow not in following.follows.all():
		addfollow=following.follows.add(tofollow)
		tofollow.followersCount+=1
		tofollow.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))	


@login_required
def unfollowhim(request,userprofile_id):
    username=request.user
    userObject=User.objects.get(username=username)
    userprofileobject=UserProfile.objects.get(userObject=userObject)
    toremoveuser=UserProfile.objects.get(id=userprofile_id)
    if toremoveuser in userprofileobject.follows.all():
    	userprofileobject.follows.remove(toremoveuser)
    	toremoveuser.followersCount-=1
    	toremoveuser.save()
    	userprofileobject.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))	



