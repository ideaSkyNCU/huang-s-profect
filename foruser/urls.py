"""foruser URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app1.views import monitor, home, login#logout, projects_details, post_detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^monitor/$',monitor),
    url(r'^$',home),
    url(r'^login/$',login),
'''
    url(r'^projects/(?P<pk>\d+)/get/$',projects_details,name='projects_details'),#project i 
    url(r'^projects/get/$', post_detail, name='post_detail'),#username+id'''
]