from django.conf.urls import include, url
from django.contrib import admin
from app1.views import monitor, home, login, post_detail, projects_details#logout

urlpatterns = [
    #url(r'^admin/$', include(admin.site.urls)),
    url(r'^monitor/$',monitor),
    url(r'^$',home),
    url(r'^login/$',login),
    url(r'^projects/get/$', post_detail, name='post_detail'),
    url(r'^projects/aaa/get/$',projects_details,name='projects_details'),
]
'''
    url(r'^projects/(?P<pk>\d+)/get/$',projects_details,name='projects_details'),#project i 
'''
