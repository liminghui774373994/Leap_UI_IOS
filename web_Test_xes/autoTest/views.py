from django.http import HttpResponse
from django.shortcuts import render
from . import  models
import json
import requests






def index(request):
    return render(request, 'autoTest/index.html')


# def returncoupon(request):
#
#     return render(request,'activity/successful.html')

def post_request(request):
    #userurl = "http://101.200.158.144/business/v1/teacher/login"
    userurl = request.POST.get('URL', '1')
    userData = request.POST.get('Body','1')
    #headers = {request.POST.get('Headers','1')}
    # userData = {
    # "email": "chenmengyi@100tal.com",
    # "password": "123456"}
    headers = {'Content-Type':'application/json','Host':'broadcast-qa.speiyou.cn'}
    rep = requests.post(userurl,data=json.dumps(userData),headers= headers)
    print(rep)
    return HttpResponse(str(rep.text))

def get_request(request):
    userurl = request.POST.get('URL', '1')
    userData = request.POST.get('Body', '1')
    headers = {'Content-Type': 'application/json'}
    rep = requests.get(userurl, data=json.dumps(userData), headers=headers)
    print(rep)
    return HttpResponse(str(rep))
