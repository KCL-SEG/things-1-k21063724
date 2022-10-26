from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(unique=False, blank=False)
