from django.shortcuts import render, redirect
from .models import ProjectData
from aerobox_api.models import AeroboxData, UserExtension #?????
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import os
import hashlib

def monitor(request):
    print(request.GET)
    print(request.POST)
    #for pro in post_detail:
        #return

    is_ajax = False
    if request.is_ajax():
        is_ajax = True
    test = {'GET':'GET',
	    'array':[1, 2, 3, 4],
	    #'a':request.GET['a'],
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
        user=auth.authenticate(username=username,password=password)##########
        if user and user.is_active:
            auth.login(request, user)
            user_e=UserExtension.objects.get(user=user)#user_e == userextension object
            user_e.p_k = hashlib.md5(os.urandom(32)).hexdigest()
            user_e.save(update_fields=['p_k'])#change p_k only
            return HttpResponseRedirect('/monitor')
        else:
            return HttpResponse("login didn't sucess!!")
    
    return render(request, 'login.html')

'''
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/monitor')
'''

def home(request):
    print(request.GET)
    test=[11,22,":)"]
    return HttpResponse(test)
#    post_list = Post.objects.all()
##    return render(request, 'home.html',{
##        'post_list':post_list,
##    })


@login_required
def post_detail(request):
    username = request.GET.get('username')
    user = User.objects.get(username=username)
    u=USERExtension.objects.get(user=user)
    np={
        'name':u.user.username,
        'p_k':u.p_k,
    }
    return JsonResponse(np)
'''
@login_required
def projects_details(request): #need p_k
    username = request.GET.get('username')
    user = User.object.get(username=username)
    u=USERExtension.objects.get(user=user)

    if(User.object.filter(pk=u.p_k,username=username)[0].exists):
        #for P in ProjectData?????????????????????
        if(ProjectData.user.name==u.user.username):
            ok_data={
                'name': ProjectData.name,
                'start_time': ProjectData.start_time,
                'end_time': ProjectData.end_time,
                'user':  ProjectData.user,  #????????
                'aerobox_data':  ProjectData.aerobox_data,#????????
            }
#==========>for "/projects/<id>/Get/"
#==========>return [project i]
        return JsonResponse(ok_data)
    return HttpResponse("you are not a valid user!!!")
'''

