from django.urls import path
from .views import (
    JobListView,
)

urlpatterns = [
    path('jobs-list', JobListView.as_view(), name="job-list")
]