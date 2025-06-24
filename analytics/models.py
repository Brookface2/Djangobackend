from django.db import models
from django.conf import settings
from datetime import date

class FormReturnRate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    week_start = models.DateField()
    week_end = models.DateField()
    return_percentage = models.FloatField()
