from django.contrib import admin
from .models import Aerobox, AeroboxData, ProjectData
from app1.models import UserExtension
# Register your models here.

admin.site.register(Aerobox)
admin.site.register(AeroboxData)
admin.site.register(ProjectData)
admin.site.register(UserExtension)
