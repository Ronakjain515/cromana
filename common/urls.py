from django.urls import path
from .views import (
    HomeView,
    LoginView,
    RegisterChooseView,
    RegisterJobSeekerView,
    RegisterCompanyView,
)


urlpatterns = [
    path('home', HomeView.as_view(), name="home"),
    path('login', LoginView.as_view(), name="login"),
    path('register/choose', RegisterChooseView.as_view(), name="register-choose"),
    path('register/jobseeker', RegisterJobSeekerView.as_view(), name="register-jobseeker"),
    path('register/company', RegisterCompanyView.as_view(), name="register-company"),
]
