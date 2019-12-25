from django.db import models

class Aerobox(models.Model):
    aerobox_name=models.CharField(max_length=100,default=1)
    lon=models.FloatField(blank=True)
    lat=models.FloatField(blank=True)

class AeroboxData(models.Model):
    pm=models.FloatField(blank=True)
    temp=models.FloatField(blank=True)
    rh=models.IntegerField(blank=True)
    co2=models.IntegerField(blank=True)
    time=models.DateTimeField(auto_now_add=True)
    aerobox=models.OneToOneField(Aerobox,on_delete=models.CASCADE)

class ProjectData(models.Model):
    pj_name = models.CharField(max_length=100,default=1)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    aerobox_data = models.ManyToManyField(AeroboxData)

