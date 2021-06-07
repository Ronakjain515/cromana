from rest_framework import serializers
import html2text

from .models import (
    JobModel,
    JobLocationModel,
    JobLinguisticLanguageModel,
    JobSkillModel,
    JobWeeklyOffModel
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

    def get_role_responsibility(self, instance):
        return html2text.html2text(instance.role_responsibility)[:100]
    
    def get_experience(self, instance):
        return instance.experience.replace("to", " to ")

    class Meta:
        model = JobModel
        fields = ["id", "title", "role_responsibility", "experience", "package"]