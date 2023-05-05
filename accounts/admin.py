from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(police_incharge)
admin.site.register(police_officer)
admin.site.site_header = "O.C.R.S Admin"
admin.site.site_title = "O.C.R.C Admin Portal"
admin.site.index_title = "Welcome to Online Crime Reporting System Admin Panel"