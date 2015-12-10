from django.conf.urls import url
from dashboard import views

urlpatterns=[
url(r'^dashboardhome/$',views.dashboardHome,name="dashboardhome")
]