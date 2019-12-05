from django.db import models
from aerobox_api.models import ProjectData
from django.contrib.auth.models import User
import hashlib
import os

def create_key():
    return hashlib.md5(os.urandom(32)).hexdigest()

class UserExtension(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)##ForeignKey==onetoone
    #user = models.ManyToManyField(UserExtension)
    u_name=models.CharField(max_length=100,default=1)
    personal_key=models.CharField(max_length=33,blank=True,default=create_key,unique=True)
    projectdata = models.ManyToManyField(ProjectData)
