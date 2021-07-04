from django.urls import path
from .views import (
    JobListView,
    CompanyListView,
    JobView,
    ApplyJobView,
    SavedJobView,
)

urlpatterns = [
    path('jobs-list', JobListView.as_view(), name="job-list"),
    path('company-list', CompanyListView.as_view(), name="company-list"),
    path('jobs/<int:pk>/', JobView.as_view(), name="job-view"),
    path('apply-job', ApplyJobView.as_view(), name="apply-job"),
    path('save-job', SavedJobView.as_view(), name="save-job"),
]