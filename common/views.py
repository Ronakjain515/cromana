from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import (
    TestimonialModel,
    OurClientModel,
)
from users.models import CustomUser
from .serializer import LoginSerializer


class HomeView(View):
    context = {}

    def get(self, request):
        
        # Testimonial data
        self.context["testimonials"] = TestimonialModel.objects.all()

        # Our Clients data
        self.context["clients"] = OurClientModel.objects.all()

        return render(request, "index.html", context=self.context)


class LoginView(View):
    context = {}

    def get(self, request):

        return render(request, "login.html")
    
    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        
        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data["email"], 
                                            password=serializer.validated_data["password"])
            if user:
                return redirect("home")
            else:
                self.context["error"] = "Invalid Credentials.."
        else:
            self.context["error"] = serializer.errors
        return render(request, "login.html", context=self.context)


class RegisterChooseView(View):

    def get(self, request):
        return render(request, "register/choose.html")


class RegisterJobSeekerView(View):

    def get(self, request):
        return render(request, "register/jobseeker.html")


class RegisterCompanyView(View):

    def get(self, request):
        return render(request, "register/company.html")
