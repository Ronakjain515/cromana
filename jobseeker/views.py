from django.views import View
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from users.models import (
    JobSeekerModel,
)
from users.serializer import (
    RegisterJobSeekerSerializer,
)
from jobs.serializers import (
    GetJobListSerializer
)
from jobs.models import (
    AppliedJobs,
    JobModel,
    SavedJobs,
)


class JobseekerDetailsView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if not (request.user.is_authenticated and request.user.role == "JOBSEEKER"):
            return redirect("home")
        self.context["is_authenticated"] = True
        self.context["role"] = request.user.role
        return super(JobseekerDetailsView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        user = JobSeekerModel.objects.get(user__id=request.user.id)
        self.context['user'] = user
        return render(request, "jobseeker/jobseekerdetails.html", context=self.context)

    def post(self, request):
        user = JobSeekerModel.objects.get(user__id=request.user.id)
        self.context['user'] = user
        data = request.POST.copy()
        if data.get("profilepic") == "":
            del data["profilepic"]
        else:
            data["profilepic"] = request.FILES.get("profilepic")
        data["user"] = request.user
        
        user_serializer = RegisterJobSeekerSerializer(user, data=data)
        if user_serializer.is_valid():
            user_serializer.save()
        else:
            self.context["error"] = user_serializer.errors

        return render(request, "jobseeker/jobseekerdetails.html", context=self.context)


class AppliedJobsListView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if not (request.user.is_authenticated and request.user.role == "JOBSEEKER"):
            return redirect("home")
        self.context["is_authenticated"] = True
        self.context["role"] = request.user.role
        return super(AppliedJobsListView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        user = JobSeekerModel.objects.get(user__id=request.user.id)
        self.context['user'] = user
        page_no = request.GET.get("page", 1)
        applied_jobs = list(AppliedJobs.objects.values_list("job", flat=True).filter(user=request.user.id))
        jobs = JobModel.objects.filter(id__in=applied_jobs)
        paginator = Paginator(jobs, 5)
        page = paginator.page(page_no)
        self.context["paginator"] = page
        if page.object_list:
            self.context["hasobjects"] = True
        job_serializer = GetJobListSerializer(page, many=True)
        self.context["jobs"] = job_serializer.data
        return render(request, "jobseeker/applied-jobs.html", context=self.context)


class SavedJobsListView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        if not (request.user.is_authenticated and request.user.role == "JOBSEEKER"):
            return redirect("home")
        self.context["is_authenticated"] = True
        self.context["role"] = request.user.role
        return super(SavedJobsListView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        user = JobSeekerModel.objects.get(user__id=request.user.id)
        self.context['user'] = user
        page_no = request.GET.get("page", 1)
        saved_jobs = list(SavedJobs.objects.values_list("job", flat=True).filter(user=request.user.id))
        jobs = JobModel.objects.filter(id__in=saved_jobs)
        paginator = Paginator(jobs, 5)
        page = paginator.page(page_no)
        self.context["paginator"] = page
        if page.object_list:
            self.context["hasobjects"] = True
        job_serializer = GetJobListSerializer(page, many=True)
        self.context["jobs"] = job_serializer.data
        return render(request, "jobseeker/saved-jobs.html", context=self.context)
