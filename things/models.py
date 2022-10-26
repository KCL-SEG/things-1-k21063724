from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField(blank=False)
