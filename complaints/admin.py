from django.contrib import admin

from complaints.models import *

# Register your models here.
admin.site.register(state_master)
admin.site.register(district_master)
admin.site.register(police_station_master)
admin.site.register(crime_category_master)
admin.site.register(complaint_master)

