from django.contrib import admin
from .models import (
    JobModel,
    JobLocationModel,
    JobLinguisticLanguageModel,
    JobSkillModel,
)


admin.site.register(JobModel)
admin.site.register(JobLocationModel)
admin.site.register(JobLinguisticLanguageModel)
admin.site.register(JobSkillModel)