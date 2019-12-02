from django.db import models
from django.contrib.auth.models import User
import hashlib
import os

#User = get_user_model()

def create_key():
    return hashlib.md5(os.urandom(32)).hexdigest()

class Aerobox(models.Model):
    name=models.CharField(max_length=100,default=1)
    lon=models.FloatField(blank=True)
    lat=models.FloatField(blank=True)

class AeroboxData(models.Model):
    name=models.CharField(max_length=100,default=1)
    
    pm=models.FloatField(blank=True)
    temp=models.FloatField(blank=True)
    rh=models.IntegerField(blank=True)
    co2=models.IntegerField(blank=True)
    time=models.DateTimeField(auto_now_add=True)
    aerobox=models.OneToOneField(Aerobox,on_delete=models.CASCADE)

class UserExtension(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ##ForeignKey==onetoone
    name=models.CharField(max_length=100,default=1)
    personal_key=models.CharField(max_length=33,blank=True,default=create_key,unique=True)

