from rest_framework import serializers

from .models import CustomUser, JobSeekerModel


class RegisterCustomJobSeekerSerializer(serializers.ModelSerializer):
    """
    Serializer for Email Password for Job Seeker Register
    """
    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class RegisterJobSeekerSerializer(serializers.ModelSerializer):
    """
    Serializer for Job Seeker Register
    """
    class Meta:
        model = JobSeekerModel
        fields = ["profilepic", "firstname", "lastname", "mobileno", "gender"]
