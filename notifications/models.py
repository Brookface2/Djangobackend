from django.db import models
from django.conf import settings

class Notification(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    related_form = models.ForeignKey('forms.FormTemplate', on_delete=models.SET_NULL, null=True, blank=True)
