from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import (
    CompanyModel
)
from .models import (
    JobLinguisticLanguageModel,
    JobModel,
    JobLocationModel,
    JobWeeklyOffModel,
    JobSkillModel,
    AppliedJobs,
    SavedJobs
)
from .serializers import (
    GetJobListSerializer,
    ApplyJobSerializer,
    SavedJobSerializer,
)
from common.models import (
    LocationModel,
)

class JobListView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        
        return super(JobListView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        page_no = request.GET.get("page", 1)
        jobs = JobModel.objects.all().order_by("-id")
        if request.user.is_authenticated:
            applied_jobs = list(AppliedJobs.objects.values_list("job", flat=True).filter(user=request.user.id))
            jobs = jobs.exclude(id__in=applied_jobs)

        # filters
        if request.GET.get("exp", "any") != "any":
            jobs = jobs.filter(experience__startswith=request.GET.get("exp"))
            self.context["exp"] = request.GET.get("exp", "any")
        if request.GET.get("search", None):
            jobs = jobs.filter(title__icontains=request.GET.get("search"))
            self.context["search"] = request.GET.get("search", "")
        if request.GET.get("location", None):
            locations = JobLocationModel.objects.values_list("job", flat=True).filter(location__location__icontains=request.GET.get("location"))
            jobs = jobs.filter(id__in=locations)
            self.context["location"] = request.GET.get("location", "")
        if request.GET.get("salary", "any") != "any":
            try:
                jobs = jobs.filter(package__gte=request.GET.get("salary"))
            except ValueError:
                pass
            self.context["salary"] = request.GET.get("salary", "any")
        if request.GET.get("type", "any") != "any":
            if request.GET.get("type") == "part":
                jobs = jobs.filter(part_time=True)
            if request.GET.get("type") == "full":
                jobs = jobs.filter(part_time=False)
            self.context["type"] = request.GET.get("type", "any")
        if request.GET.get("company", None):
            comp = CompanyModel.objects.values_list("id", flat=True).filter(name__icontains=request.GET.get("company").replace("-", " "))
            jobs = jobs.filter(company__in=comp)
            self.context["company"] = request.GET.get("company", "")
        self.context["companies"] = CompanyModel.objects.values("id", "name")
        self.context["locations"] = LocationModel.objects.all()

        paginator = Paginator(jobs, 4)
        page = paginator.page(page_no)
        self.context["paginator"] = page
        if page.object_list:
            self.context["hasobjects"] = True
        job_serializer = GetJobListSerializer(page, many=True)
        self.context["jobs"] = job_serializer.data
        return render(request, "jobs/job_list.html", context=self.context)


class CompanyListView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(CompanyListView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.GET.get("letter", None):
            self.context["companies"] = CompanyModel.objects.filter(name__startswith=request.GET.get("letter"))
            self.context["letter"] = request.GET.get("letter")
        elif request.GET.get("number", None):
            self.context["companies"] = CompanyModel.objects.filter(name__regex=r'^\d')    
            self.context["number"] = request.GET.get("number")
        elif request.GET.get("search", None):
            self.context["companies"] = CompanyModel.objects.filter(name__icontains=request.GET.get("search"))
            self.context["search"] = request.GET.get("search")
        else:
            self.context["companies"] = CompanyModel.objects.all()
        return render(request, "jobs/company-list.html", context=self.context)


class JobView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(JobView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        job = JobModel.objects.get(id=pk)
        job_serializer = GetJobListSerializer(job)
        self.context["job"] = job_serializer.data
        self.context["details"] = job
        skills = []
        for skill in job_serializer.data["skills"]:
            skills.append(skill.id)
        similar_job = list(JobSkillModel.objects.values_list("job", flat=True).filter(skill__in=skills))
        similar_jobs = JobModel.objects.filter(id__in=similar_job).exclude(id=pk)[:4]
        similar_serializer = GetJobListSerializer(similar_jobs, many=True)
        self.context["similar"] = similar_serializer.data
        locations = JobLocationModel.objects.filter(job=job.id)
        if locations:
            self.context["locations"] = locations
        else: 
            self.context["locations"] = [{"location": "Not Provided"}]
        laguage = JobLinguisticLanguageModel.objects.filter(job=job.id)
        if laguage:
            self.context["laguages"] = laguage
        else: 
            self.context["laguages"] = [{"laguage": "Not Provided"}]
        week = JobWeeklyOffModel.objects.filter(job=job.id)
        if week:
            self.context["weeks"] = week
        else: 
            self.context["weeks"] = [{"day": "Not Provided"}]
        return render(request, "jobs/job-view.html", context=self.context)


class ApplyJobView(APIView):

    def post(self, request):
        result = "error"
        if not request.user.is_authenticated:
            return Response({"result": "Not"})
        if request.user.role == "COMPANY":
            return Response({"result": "permi"})
        try:
            apply_serializer = ApplyJobSerializer(data={
                "job": request.data.get("job"),
                "user": request.user.id
            })
            if apply_serializer.is_valid():
                try:
                    job = AppliedJobs.objects.get(job=apply_serializer.validated_data["job"], user=apply_serializer.validated_data["user"])
                    result = "Already"
                except AppliedJobs.DoesNotExist:
                    apply_serializer.save()
                    result = "Done"
            else:
                pass
        except:
            pass
        return Response({"result": result})


class SavedJobView(APIView):

    def post(self, request):
        result = "error"
        if not request.user.is_authenticated:
            return Response({"result": "Not"})
        if request.user.role == "COMPANY":
            return Response({"result": "permi"})
        try:
            saved_serializer = SavedJobSerializer(data={
                "job": request.data.get("job"),
                "user": request.user.id
            })
            if saved_serializer.is_valid():
                try:
                    job = SavedJobs.objects.get(job=saved_serializer.validated_data["job"], user=saved_serializer.validated_data["user"])
                    result = "Already"
                except SavedJobs.DoesNotExist:
                    saved_serializer.save()
                    result = "Done"
            else:
                pass
        except:
            pass
        return Response({"result": result})
