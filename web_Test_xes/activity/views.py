from django.shortcuts import render
from . import  models






def index(request):
    return render(request, 'activity/index.html')


def returncoupon(request):

    return render(request,'activity/successful.html')
