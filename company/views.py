from django.views import View
from django.shortcuts import redirect, render


class CompanyDetailsView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if not request.user.is_authenticated:
            return redirect("home")
        return super(CompanyDetailsView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        print("doneas")
        return render(request, "company/companydetails.html")