from django.shortcuts import render
from django.views import View

from .models import (
    TestimonialModel,
    OurClientModel,
)


class HomeView(View):
    context = {}

    def get(self, request):
        
        # Testimonial data
        self.context["testimonials"] = TestimonialModel.objects.all()

        # Our Clients data
        self.context["clients"] = OurClientModel.objects.all()

        return render(request, "index.html", context=self.context)
