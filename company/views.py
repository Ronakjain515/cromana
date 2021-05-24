from django.views import View
from django.shortcuts import redirect, render

from users.models import CompanyModel
from users.serializer import RegisterCompanySerializer


class CompanyDetailsView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if not (request.user.is_authenticated and request.user.role == "COMPANY"):
            return redirect("home")
        self.context["is_authenticated"] = True
        self.context["role"] = request.user.role
        return super(CompanyDetailsView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        company = CompanyModel.objects.get(user=request.user)
        self.context["company"] = company
        self.context["email"] = request.user.email
        return render(request, "company/companydetails.html", context=self.context)

    def post(self, request):
        company = CompanyModel.objects.get(user=request.user)
        data = request.POST.copy()
        if data.get("image") == "":
            del data["image"]
        else:
            data["image"] = request.FILES.get("image")
        data["user"] = request.user
        company_serializer = RegisterCompanySerializer(company, data=data)
        if company_serializer.is_valid():
            company_serializer.save()
    
        self.context["company"] = company
        self.context["email"] = request.user.email
        return render(request, "company/companydetails.html", context=self.context)
