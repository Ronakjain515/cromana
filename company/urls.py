from django.urls import path
from .views import (
    CompanyDetailsView,
)


urlpatterns = [
    path("company-details", CompanyDetailsView.as_view(), name="company-company-details"),
]