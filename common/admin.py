from django.contrib import admin

from .models import (
    TestimonialModel,
    OurClientModel,
)


admin.site.register(TestimonialModel)
admin.site.register(OurClientModel)
