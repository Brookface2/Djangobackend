from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('member', 'Member'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    def is_admin(self):
        return self.role == 'admin'

    def is_coach(self):
        return self.role == 'coach'

    def is_member(self):
        return self.role == 'member'