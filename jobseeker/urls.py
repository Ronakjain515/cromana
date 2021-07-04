from django.urls import path
from .views import (
    JobseekerDetailsView,
    AppliedJobsListView,
    SavedJobsListView,
)

urlpatterns = [
    path("jobseeker-details", JobseekerDetailsView.as_view(), name="jobseeker-details"),
    path("applied-jobs", AppliedJobsListView.as_view(), name="applied-jobs"),
    path("saved-jobs", SavedJobsListView.as_view(), name="saved-jobs"),
]