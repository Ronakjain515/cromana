from django.contrib import admin

from .models import (
    TestimonialModel,
    OurClientModel,
    LinguisticLanguageModel,
    LocationModel,
    SkillsModel,
)


admin.site.register(TestimonialModel)
admin.site.register(OurClientModel)
admin.site.register(LinguisticLanguageModel)
admin.site.register(LocationModel)
admin.site.register(SkillsModel)

