from django.urls import path
from .views import (
    CompanyDetailsView,
    CreateNewJobView,
    JobListView,
    CompanyPublicView,
)


urlpatterns = [
    path("company-details", CompanyDetailsView.as_view(), name="company-company-details"),
    path("create-new-job", CreateNewJobView.as_view(), name="create-new-job"),
    path("job-list", JobListView.as_view(), name="company-job-list"),
    path("details/<int:pk>/", CompanyPublicView.as_view(), name="company-details"),
]