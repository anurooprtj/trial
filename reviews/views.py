
from django.shortcuts import render
from forms import ImageUploadForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Restaurant,RestaurantReview,ReviewReply,likes,ReviewImages,ImgComments
from django.core.urlresolvers import reverse
from restaurants.views import findNearby
from django.contrib.auth.decorators import login_required

@login_required
def reviewadd(request,rest_id):
	if request.method=='POST':
		username=request.user
		userobj=User.objects.get(username=username)
		restaurantobject=Restaurant.objects.get(pk=int(rest_id))
		reviewtext=request.POST['rtext']
		reviewrating=request.POST['rrating']
		add=RestaurantReview.objects.create(reviewText=reviewtext,reviewRating=reviewrating,reviewedBy=userobj,reviewOn=restaurantobject)
		for img in request.FILES.getlist('image'):
			imgadd=add.reviewimages_set.create(ReviewImage=img,imageofRev=add,imageofRest=restaurantobject,imageBy=userobj)			
        return HttpResponseRedirect('/restaurants/viewrestaurant/'+str(rest_id))


@login_required
def commentadd(request,review_id,rest_id):
    if request.method=='POST':
    	replytext=request.POST['rcomment']
        username=request.user
        userobj=User.objects.get(username=username)
        reviewobject=RestaurantReview.objects.get(pk=review_id)
        add=ReviewReply.objects.create(replyText=replytext,repliedBy=userobj,replyOn=reviewobject)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))        


def reviewfull(request,review_id,rest_id):
	reviewobj=RestaurantReview.objects.get(pk=review_id)
	contextDi={}
	contextDi['review']=reviewobj
	if request.user.is_active:
		username=request.user
		userobj=User.objects.get(username=username)
		likedreviews=[]
		for each in likes.objects.filter(likedBy=userobj):
			likedreviews.append(each.likeOf)
		contextDi['likedreviews']=likedreviews
	restaurantobj=Restaurant.objects.get(id=rest_id)
	address=[x.strip for x in restaurantobj.restaurantAddress.split(',')]
	contextDi['address']=address
	contextDi['restaurantObject']=restaurantobj
	nearbyrestobj=findNearby(rest_id)
	contextDi['nearbyrestobj']=nearbyrestobj
	return render(request,'review/reviewfull.html',contextDi) 



def login_redirecturl(request):
    return HttpResponse('done')	

@login_required
def helikes(request,review_id,rev_userid,site_id):
	username=request.user
	userobj=User.objects.get(username=username)
	revuserobj=User.objects.get(pk=rev_userid)
	reviewobj=RestaurantReview.objects.get(id=review_id,reviewedBy=revuserobj)
	restobj=reviewobj.reviewOn
	rest_id=restobj.id
	addflag=reviewobj.likes_set.create(likedBy=userobj,likeOf=reviewobj)
	reviewobj.likeCount+=1
	reviewobj.save()
	if str(site_id)=='1':
		return HttpResponseRedirect('/restaurants/viewrestaurant/'+str(rest_id))
	else:
	    return HttpResponseRedirect(reverse('reviews:reviewfull',args=(review_id,rest_id)))	


@login_required
def hedislikes(request,review_id,rev_userid,site_id):
	username=request.user
	userobj=User.objects.get(username=username)
	revuserobj=User.objects.get(pk=rev_userid)
	reviewobj=RestaurantReview.objects.get(id=review_id)
	likeobj=reviewobj.likes_set.filter(likeOf=reviewobj).get(likedBy=userobj)
	print likeobj
	likeobj.delete()
	reviewobj.likeCount-=1
	if reviewobj.likeCount < 0:
		reviewobj.likeCount=0
	reviewobj.save()
	restobj=reviewobj.reviewOn
	rest_id=str(restobj.id)
	if str(site_id)=='1':
		return HttpResponseRedirect('/restaurants/viewrestaurant/'+str(rest_id))
	else:
		return HttpResponseRedirect(reverse('reviews:reviewfull',args=(review_id,rest_id)))


@login_required
def imgcommentadd(request,img_id):
	username=request.user
	userobj=User.objects.get(username=username)
	imgobj=ReviewImages.objects.get(pk=img_id)
	comment=request.POST.get('imgcomment')
	addcomment=ImgComments.objects.create(commentOf=imgobj,commentBy=userobj,imgcomment=comment)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





