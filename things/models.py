from django.db import models
#
class Thing(models.Model):
    thing_name = models.CharField(max_length=30, blank=False)
    thing_description = models.CharField(max_length=100, blank=False)
    thing_quantity = models.IntegerField(blank=False)
