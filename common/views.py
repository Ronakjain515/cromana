from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import (
    TestimonialModel,
    OurClientModel,
)
from .serializer import LoginSerializer
from users.serializer import (
    RegisterCustomJobSeekerSerializer,
    RegisterJobSeekerSerializer,
    RegisterCompanySerializer,
)


class HomeView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(HomeView, self).dispatch(request, *args, **kwargs)

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
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "login.html", context=self.context)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        
        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data["email"], 
                                            password=serializer.validated_data["password"])
            if user:
                if user.status != "PENDING":
                    login(request, user)
                    return redirect("home")
                    
                else:
                    self.context["error"] = "Your Account is not Conformed by Admin."
            else:
                self.context["error"] = "Invalid Credentials.."
        else:
            self.context["error"] = serializer.errors
        return render(request, "login.html", context=self.context)


class RegisterChooseView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(RegisterChooseView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "register/choose.html", context=self.context)


class RegisterJobSeekerView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(RegisterJobSeekerView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "register/jobseeker.html", context=self.context)

    def post(self, request):
        custom_user_serializer = RegisterCustomJobSeekerSerializer(data=request.POST)

        if custom_user_serializer.is_valid():
            data = request.POST.copy()
            data["profilepic"] = request.FILES.get("profilepic")
            user_serializer = RegisterJobSeekerSerializer(data=data)

            if user_serializer.is_valid():
                custom_user_serializer.save(role="JOBSEEKER")
                user_serializer.save(user=custom_user_serializer.instance)
                self.context["success"] = "You have Successfully Registered with us."
            else:
                self.context["error"] = user_serializer.errors
        else:
            self.context["error"] = custom_user_serializer.errors
        return render(request, "register/jobseeker.html", context=self.context)


class RegisterCompanyView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(RegisterCompanyView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "register/company.html", context=self.context)

    def post(self, request):
        custom_user_serializer = RegisterCustomJobSeekerSerializer(data=request.POST)

        if custom_user_serializer.is_valid():
            data = request.POST.copy()
            data["image"] = request.FILES.get("image")
            user_serializer = RegisterCompanySerializer(data=data)

            if user_serializer.is_valid():
                custom_user_serializer.save(status="PENDING", role="COMPANY")
                user_serializer.save(user=custom_user_serializer.instance)
                self.context["success"] = "You have Successfully Registered with us."
            else:
                self.context["error"] = user_serializer.errors
        else:
            self.context["error"] = custom_user_serializer.errors
        return render(request, "register/company.html", context=self.context)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect("home")
