"""foodjoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('restaurants.urls',namespace="restaurants")),
    url(r'dashboard/',include('dashboard.urls',namespace="dashboard")),
    url(r'accounts/',include('allauth.urls')),
    url(r'restaurants/', include('restaurants.urls')),
    url(r'profiles/',include('userprofiles.urls',namespace="profiles")),
    url(r'reviews/',include('reviews.urls',namespace="reviews")),
    url(r'photos/',include('imageHandler.urls')),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


