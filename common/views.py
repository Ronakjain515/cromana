from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import (
    TestimonialModel,
    OurClientModel,
)
from users.models import CustomUser
from .serializer import LoginSerializer
from users.serializer import (
    RegisterCustomJobSeekerSerializer,
    RegisterJobSeekerSerializer,
)


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

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        return super(LoginView, self).dispatch(request, *args, **kwargs)

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
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        return super(RegisterJobSeekerView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "register/jobseeker.html")

    def post(self, request):
        custom_user_serializer = RegisterCustomJobSeekerSerializer(data=request.POST)

        if custom_user_serializer.is_valid():
            data = request.POST.copy()
            data["profilepic"] = request.FILES.get("profilepic")
            user_serializer = RegisterJobSeekerSerializer(data=data)

            if user_serializer.is_valid():
                custom_user_serializer.save()
                user_serializer.save(user=custom_user_serializer.instance)
                self.context["success"] = "You have Successfully Registered with us."
            else:
                self.context["error"] = user_serializer.errors
        else:
            self.context["error"] = custom_user_serializer.errors
        return render(request, "register/jobseeker.html", context=self.context)


class RegisterCompanyView(View):

    def get(self, request):
        return render(request, "register/company.html")

#     Gaurav
