from django.contrib import admin

from .models import (
    CustomUser, 
    JobSeekerModel,
    CompanyModel,
)

admin.site.register(CustomUser)
admin.site.register(JobSeekerModel)
admin.site.register(CompanyModel)
