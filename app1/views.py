from django.shortcuts import render, redirect
from aerobox_api.models import ProjectData
from .models import UserExtension
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import hashlib

def monitor(request):
    print(request.GET)
    print(request.POST)

    is_ajax = False
    #if request.is_ajax():
    #    is_ajax = True
    test = {'test':'It is test!',
            'GET':'GET',
	    'array':[1, 2, 3, 4],
	    'b[]':request.GET.getlist('b[ssssssssss]'),
	    'brray':[99,88,77,66,55],
	    'is_ajax':is_ajax,
           }
    return JsonResponse(test)


def login(request):
    if request.method == "POST":
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user and user.is_active:
            auth.login(request, user)
            user_e, created = UserExtension.objects.get_or_create(user=user) #also: user_e, _
            user_e.personal_key = hashlib.md5(os.urandom(32)).hexdigest()
            user_e.save(update_fields=['personal_key'])#change p_k only
            return HttpResponseRedirect('/monitor')
        else:
            return HttpResponse("login didn't sucess!!")
    
    return render(request, 'login.html')

def home(request):
    print(request.GET)
    test=["home test :)"]
    return HttpResponse(test)

@login_required
def post_detail(request):
    username = request.user
    user = User.objects.get(username=username)
    u=UserExtension.objects.get(user=user)
    np={
        'name':u.user.username,
        'p_k':u.personal_key,
    }
    return JsonResponse(np)


@login_required
def projects_details(request,pk):
    compare_username = request.user
    user = User.objects.get(username=compare_username)
    u=UserExtension.objects.get(user=user)
    
    all_list={}
    pd_list={}
    ad_list={}
    p=0
    a=0
    if(UserExtension.objects.filter(personal_key=pk,user__username=compare_username).first()):#exists()
        for pd in u.projectdata.all():  ##pd=lot of projectdata
            for ad in pd.aerobox_data.all(): ##ad=lot of aerobox_data
                ad_list={
                         'pm':ad.pm,
                         'temp':ad.temp,
                         'rh':ad.rh,
                         'co2':ad.co2,
                         'time':ad.time,
                         'aerobox_name':ad.aerobox.aerobox_name,
                         'lon':ad.aerobox.lon,
                         'lat':ad.aerobox.lat,
                        }
                pd_list[str(a)]=ad_list
                a+=1
            all_list[str(p)]=pd_list
            p+=1

    return JsonResponse(all_list)


