from django.views import View
from django.shortcuts import redirect, render
from common.models import (
    LinguisticLanguageModel,
    SkillsModel,
)


class BuildResumeView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(BuildResumeView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "resume/build-resume.html", context=self.context)


class ChooseTemplateView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        return super(ChooseTemplateView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "resume/choose-template.html", context=self.context)


class ResumeBuilderView(View):
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.context = {}
        self.context["is_authenticated"] = False
        if request.user.is_authenticated:
            self.context["is_authenticated"] = True
            self.context["role"] = request.user.role
        else:
            return redirect("login")
        return super(ResumeBuilderView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        self.context["linguistics"] = LinguisticLanguageModel.objects.all()
        self.context["skills"] = SkillsModel.objects.all()
        return render(request, "resume/resume-builder.html", context=self.context)
