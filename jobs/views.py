from django.shortcuts import render
from django.views import View


class JobListView(View):
    def get(self, request):
        return render(request, "jobs/job_list.html")
