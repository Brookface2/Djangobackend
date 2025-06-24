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

class Booking(models.Model):
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'member'}
    )
    gym_class = models.ForeignKey(
        GymClass,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ('member', 'gym_class')  # Prevent double-booking

    def __str__(self):
        return f"{self.member} booked {self.gym_class}"
