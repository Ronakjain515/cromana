from django.db import models
from django.utils import timezone
from users.models import CompanyModel
from common.models import (
    LocationModel,
    SkillsModel,
    LinguisticLanguageModel
)

class JobModel(models.Model):
    """
    Model for storing jobs data.
    """

    JobStatus = (
        ("DRAFT", "Draft"),
        ("PUBLISHED", "Published"),
        ("DONE_HIRING", "Done Hiring"),
    )


    company             = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    title               = models.CharField(max_length=100, null=True, blank=True)
    role_responsibility = models.CharField(max_length=2000, null=True, blank=False)
    requirements        = models.CharField(max_length=2000, null=True, blank=False)
    experience          = models.CharField(max_length=30, null=True, blank=False)
    shift_timing        = models.CharField(max_length=30, null=True, blank=False)
    package             = models.CharField(max_length=40, null=True, blank=False)
    joining_date        = models.CharField(max_length=30, null=True, blank=False)
    apply_last_date     = models.DateField(null=True, blank=False)
    part_time           = models.BooleanField(null=False, blank=False)
    no_of_opening       = models.IntegerField(null=True, blank=False)
    status              = models.CharField(max_length=15, null=True, blank=False, choices=JobStatus)
    created_at          = models.DateTimeField(default=timezone.now)
    updated_at          = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.title



class JobLocationModel(models.Model):
    job         = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    location    = models.ForeignKey(LocationModel, on_delete=models.CASCADE)


class JobSkillModel(models.Model):
    job     = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    skill   = models.ForeignKey(SkillsModel, on_delete=models.CASCADE)


class JobLinguisticLanguageModel(models.Model):
    job     = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    laguage = models.ForeignKey(LinguisticLanguageModel, on_delete=models.CASCADE)

