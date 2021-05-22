from django.urls import path
from .views import (
    CompanyDetailsView,
)


urlpatterns = [
    path("my-details", CompanyDetailsView.as_view(), name="company-my-details"),
]