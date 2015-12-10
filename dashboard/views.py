from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def dashboardHome(request):
	return render(request,'dashboard/home.html')