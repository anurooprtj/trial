from django.conf.urls import patterns,url
from . import views
urlpatterns = [
url(r'^(?P<rest_id>[0-9]+)/$',views.reviewadd,name='reviewadd'),
url(r'^(?P<review_id>[0-9]+)/(?P<rest_id>[0-9]+)/commentadd/$',views.commentadd,name='commentadd'),
url(r'^(?P<review_id>[0-9]+)/(?P<rest_id>[0-9]+)/reviewfull/$',views.reviewfull,name='reviewfull'),
url(r'^(?P<review_id>[0-9]+)/(?P<rev_userid>[0-9]+)/(?P<site_id>[0-9]+)/helikes/',views.helikes,name='helikes'),
url(r'^(?P<review_id>[0-9]+)/(?P<rev_userid>[0-9]+)/(?P<site_id>[0-9]+)/hedislikes/',views.hedislikes,name='hedislikes'),
url(r'^(?P<img_id>[0-9]+)/imgcommentadd/$',views.imgcommentadd,name='imgcommentadd'),
]