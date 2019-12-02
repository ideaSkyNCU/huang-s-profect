from django.shortcuts import render, redirect
from .models import ProjectData, UserExtension
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
            user_e, created = UserExtension.objects.get_or_create(user=user)
            user_e.personal_key = hashlib.md5(os.urandom(32)).hexdigest()
            user_e.save(update_fields=['personal_key'])#change p_k only
            return HttpResponseRedirect('/monitor')
        else:
            #st="login didn't sucess"
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
#    return render(request, 'home.html',{
#        'post_list':post_list,
#    })


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

'''
@login_required
def projects_details(request): #need p_k
    username = request.GET.get('username')
    user = User.object.get(username=username)
    u=USERExtension.objects.get(user=user)

    if(request.method=="GET"):
        u=USERExtension.objects.get(personal_key=personal_key)
        p=u.projects.all()
    ok_data={
        
    }
#    post = Post.objects.get(pk=pk)
#==========>for "/projects/<id>/Get/"
#==========>return [project i]
    return JsonResponse(ok_data)

'''

