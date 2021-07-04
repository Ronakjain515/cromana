from rest_framework import serializers
import html2text

from .models import (
    JobModel,
    JobLocationModel,
    JobLinguisticLanguageModel,
    JobSkillModel,
    JobWeeklyOffModel,
    AppliedJobs,
    SavedJobs,
)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = "__all__"


class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocationModel
        fields = "__all__"


class JobLinguisticLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLinguisticLanguageModel
        fields = "__all__"

class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkillModel
        fields = "__all__"

class JobWeeklyOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobWeeklyOffModel
        fields = "__all__"


class GetJobListSerializer(serializers.ModelSerializer):
    role_responsibility = serializers.SerializerMethodField("get_role_responsibility")
    experience = serializers.SerializerMethodField("get_experience")
    skills = serializers.SerializerMethodField("get_skills")
    company_name = serializers.CharField(source="company.name")
    location = serializers.SerializerMethodField("get_location")
    created_at = serializers.SerializerMethodField("get_created_at")

    def get_created_at(self, instance):
        return instance.created_at

    def get_location(self, instance):
        location = JobLocationModel.objects.filter(job=instance).first()
        if location:
            return location.location
        return "Not Provide"

    def get_skills(self, instance):
        return JobSkillModel.objects.filter(job=instance)

    def get_role_responsibility(self, instance):
        return html2text.html2text(instance.role_responsibility)[:100]
    
    def get_experience(self, instance):
        return instance.experience.replace("to", " to ")

    class Meta:
        model = JobModel
        fields = ["id", "title", "role_responsibility", "no_of_opening", "experience", "shift_timing", "created_at", "package", "location", "skills", "company_name"]


class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedJobs
        fields = "__all__"


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJobs
        fields = "__all__"
