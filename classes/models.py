from django.db import models
from django.conf import settings

class GymClass(models.Model):  # Renamed from "Classes"
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='instructed_classes',
        limit_choices_to={'role': 'coach'}
    )
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} at {self.start_time}"
