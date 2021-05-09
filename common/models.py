from django.db import models


class TestimonialModel(models.Model):
    name        = models.CharField(max_length=50)
    designition = models.CharField(max_length=100)
    comment     = models.CharField(max_length=700)
    image       = models.ImageField(upload_to="testimonials")

    def __str__(self):
        return self.name
    

class OurClientModel(models.Model):
    name    = models.CharField(max_length=50)
    image   = models.ImageField(upload_to="clients")

    def __str__(self):
        return self.name