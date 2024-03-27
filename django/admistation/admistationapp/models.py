from django.db import models

class post(models.Model):
    concept = models.CharField(max_length=75)
    description = models.CharField(max_length=75)
    title = models.CharField(max_length=65)
