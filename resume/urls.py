from django.urls import path
from .views import (
    BuildResumeView,
    ChooseTemplateView,
    ResumeBuilderView,
)

urlpatterns = [
    path("build-resume", BuildResumeView.as_view(), name="build-resume"),
    path("choose-template", ChooseTemplateView.as_view(), name="choose-template"),
    path("resume-builder", ResumeBuilderView.as_view(), name="resume-builder"),
]
