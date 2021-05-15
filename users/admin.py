from django.contrib import admin

from .models import CustomUser, JobSeekerModel

admin.site.register(CustomUser)
admin.site.register(JobSeekerModel)
