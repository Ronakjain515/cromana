from django.views import View
from django.shortcuts import redirect, render

from users.models import CompanyModel
from users.serializer import RegisterCompanySerializer
from common.models import (
    LocationModel,
    SkillsModel,
    LinguisticLanguageModel,
)
from jobs.serializers import (
    JobSerializer,
    JobSkillSerializer,
    JobLocationSerializer,
    JobWeeklyOffSerializer,
    JobLinguisticLanguageSerializer,
    GetJobListSerializer,
)
from jobs.models import (
    JobModel,
    JobWeeklyOffModel,
    JobSkillModel,
    JobLinguisticLanguageModel,
    JobLocationModel
)


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


class CreateNewJobView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if not (request.user.is_authenticated and request.user.role == "COMPANY"):
            return redirect("home")
        self.context["is_authenticated"] = True
        self.context["role"] = request.user.role
        return super(CreateNewJobView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        self.context["company"] = CompanyModel.objects.get(user=request.user)
        self.context["locations"] = LocationModel.objects.all()
        self.context["skills"] = SkillsModel.objects.all()
        self.context["linguistics"] = LinguisticLanguageModel.objects.all()
        return render(request, "company/createnewjob.html", context=self.context)
    
    def post(self, request):
        company = CompanyModel.objects.get(user=request.user)
        data = {
            "company": company.id,
            "title": request.POST.get("title"),
            "role_responsibility": request.POST.get("role_responsibility"),
            "requirements": request.POST.get("requirements"),
            "experience": request.POST.get("minexp") + "to" + request.POST.get("maxexp"),
            "shift_timing": request.POST.get("startoffice") + " to " + request.POST.get("endoffice"),
            "package": request.POST.get("package"),
            "apply_last_date": request.POST.get("applybefore"),
            "part_time": True if request.POST.get("parttime") else False,
            "no_of_opening": request.POST.get("no_of_opening"),
            "status": "DRAFT" if request.POST.get("draft") else "PUBLISHED",
            "gender": request.POST.get("gender")
        }
        # job data
        job_serializer = JobSerializer(data=data)
        if job_serializer.is_valid():
            job_serializer.save()
            
            # location data
            location_data = []
            for location in request.POST.getlist("locations"):
                location_data.append({
                    "job": job_serializer.data["id"],
                    "location": location
                })
            location_serializer = JobLocationSerializer(data=location_data, many=True)
            if location_serializer.is_valid():
                location_serializer.save()

                # language data
                language_data = []
                for language in request.POST.getlist("linguistic"):
                    language_data.append({
                        "job": job_serializer.data["id"],
                        "laguage": language
                    })
                language_serializer = JobLinguisticLanguageSerializer(data=language_data, many=True)
                if language_serializer.is_valid():
                    language_serializer.save()

                    # skills data
                    skill_data = []
                    for skill in request.POST.getlist("skills"):
                        skill_data.append({
                            "job": job_serializer.data["id"],
                            "skill": skill
                        })
                    skill_serializer = JobSkillSerializer(data=skill_data, many=True)
                    if skill_serializer.is_valid():
                        skill_serializer.save()

                        # week data
                        week_data = []
                        for week in request.POST.getlist("weekoff"):
                            week_data.append({
                                "job": job_serializer.data["id"],
                                "day": week
                            })
                        week_serializer = JobWeeklyOffSerializer(data=week_data, many=True)
                        if week_serializer.is_valid():
                            week_serializer.save()
                            self.context["success"] = "You have  successfully created new Job Post.."
                        else:
                            self.context["error"] = week_serializer.errors
                    else:
                        self.context["error"] = skill_serializer.errors
                else:
                    self.context["error"] = language_serializer.errors
            else:
                self.context["error"] = location_serializer.errors
        else:
            self.context["error"] = job_serializer.errors
        self.context["company"] = company
        self.context["locations"] = LocationModel.objects.all()
        self.context["skills"] = SkillsModel.objects.all()
        self.context["linguistics"] = LinguisticLanguageModel.objects.all()
        return render(request, "company/createnewjob.html", context=self.context)


class JobListView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if not (request.user.is_authenticated and request.user.role == "COMPANY"):
            return redirect("home")
        self.context["is_authenticated"] = True
        self.context["role"] = request.user.role
        return super(JobListView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        company = CompanyModel.objects.get(user=request.user)
        self.context["company"] = company
        jobs = JobModel.objects.filter(company=company)
        job_serializer = GetJobListSerializer(jobs, many=True)
        self.context["jobs"] = job_serializer.data
        return render(request, "company/job-list.html", context=self.context)
