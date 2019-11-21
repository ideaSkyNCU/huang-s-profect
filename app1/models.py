from django.db import models
from aerobox_api.models import AeroboxData, UserExtension


class ProjectData(models.Model):
    name = models.CharField(max_length=100,default=1)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)

    user = models.ManyToManyField(UserExtension)
    aerobox_data = models.ManyToManyField(AeroboxData)

'''
    def get_allinf(self):
        return {
	    "name":self.aerobox_data.aerobox.name,
	    "lon":self.aerobox_data.aerobox.lon,
	    "lat":self.aerobox_data.aerobox.lat,
	    "start_time":self.start_time,
            "end_time":self.end_time,

	    "host":list(h_id in self.host.all()),
            "aerobox_data":list(a_id in self.aerobox_data.all()),
	}
'''
